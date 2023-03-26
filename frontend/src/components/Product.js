import React from "react";
import {Card} from "react-bootstrap";

function Product({product}) {

    const jsonStr = product.image_urls.replace(/'/g, '"');
    const arr = JSON.parse(jsonStr);


    return (
        <Card className="my-3 p-3 rounded">

            <Card.Img src={arr[0]}/>

            <Card.Body>

                <Card.Title as="div">
                    <strong>{product.product_title}</strong>
                </Card.Title>

                <Card.Text as="div">
                    <div className="my-3">
                        {product.product_description.slice(0, 100)}...
                    </div>
                </Card.Text>

                <Card.Text as="h3">
                    <div className="my-3">
                        € {(product.price - (product.price * product.discount)).toFixed(2).toString().replace('.', ',')}
                        {/*<span className="discount">{(product.discount * 100).toFixed(0)}% off</span>*/}
                    </div>
                </Card.Text>

            </Card.Body>

        </Card>
    )
}

export default Product