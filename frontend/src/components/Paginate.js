import React from "react";
import {Pagination} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";
import {useLocation} from "react-router-dom";

function Paginate({pages, page, keyword = ''}) {

    let location = useLocation()
    let redirect = location.pathname

    if (keyword) {
        keyword = keyword.split('?keyword=')[1].split('&')[0]
    }


    return (pages > 1 && (
            <Pagination>
                {/*<Pagination.First> </Pagination.First>*/}
                {[...Array(pages).keys()].map((x) => (
                    <LinkContainer
                        key={x + 1}
                        to={{
                            pathname: redirect,
                            search: `?keyword=${keyword}&page=${x + 1}`,
                        }}
                    >
                        <Pagination.Item active={x === page}>{x + 1}</Pagination.Item>
                    </LinkContainer>
                ))}
            </Pagination>
        )
    )
}

export default Paginate