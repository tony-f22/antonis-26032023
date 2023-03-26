import React from "react";
import { Spinner } from "react-bootstrap";

function Loader() {
    return (
        <Spinner
            animation="border"
            role="status"
            style={{
                height: '100px',
                width: '100px',
                margin: '100px',
                display: '100px',
            }}
        >
            <span className="sr-only">Loading...</span>

        </Spinner>
    )

}

export default Loader