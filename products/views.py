from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from djongo.database import DatabaseError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from django.db.models import Q


@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        query = request.query_params.get('keyword', '')
        page = request.query_params.get('page', 1)
        page_size = 10

        try:
            # Build the query
            product_query = Q(product_title__icontains=query)
            products = Product.objects.filter(product_query).order_by('_id')

            # # Optimize the query
            # products = products.select_related('related_field_1', 'related_field_2').prefetch_related(
            # 'related_objects')

            # Paginate the results
            paginator = Paginator(products, page_size)
            try:
                page = int(page)
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)  # return the last page

            # Serialize the data
            serializer = ProductSerializer(products, many=True)

            # Cache the results (optional)
            cache_key = f'product_list:{query}:{page}'.replace(' ', '_')
            cache_timeout = 60 * 5  # 5 minutes
            cached_data = cache.get(cache_key)
            if cached_data is not None:
                return Response(cached_data, status=status.HTTP_200_OK)
            else:
                data = {'products': serializer.data, 'page': page, 'pages': paginator.num_pages}
                cache.set(cache_key, data, cache_timeout)
                return Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            # Handle the case where the queried object does not exist
            error_message = 'Product not found.'
            return Response({'error': error_message}, status=status.HTTP_404_NOT_FOUND)

        except DatabaseError:
            error_message = 'An error occurred while retrieving the product list.'
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Handle the case where the request method is not GET
    return Response({'error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
