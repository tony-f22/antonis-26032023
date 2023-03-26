import React, {useState} from "react";
import {Button, Form} from "react-bootstrap";
import {useLocation, useNavigate} from "react-router-dom";

function SearchBox() {

    const [keyword, setKeyword] = useState('')

    let navigate = useNavigate()
    let location = useLocation()
    let redirect = location.pathname

    const handleInputChange = (event) => {
        setKeyword(event.target.value);
    };

    const submitHandler = (e) => {
        e.preventDefault()
        // console.log(redirect)

        if (keyword) {
            navigate(redirect + `?keyword=${keyword}&page=1`)
        } else {
            navigate(redirect)
        }
    }

    return (
        <div>
            <Form onSubmit={submitHandler} className='d-flex'>
                <Form.Control
                    type="text"
                    name="q"
                    onChange={handleInputChange}
                    className="mr-sm-2 ml-sm-5"
                >
                </Form.Control>

                <Button
                    type="submit"
                    variant="outline-success"
                    className="p-2"
                >
                    Search
                </Button>
            </Form>
        </div>
    )
}

export default SearchBox