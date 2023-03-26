import React from "react";
import {Container, Navbar} from "react-bootstrap";
import SearchBox from "./SearchBox";

function Header() {

    return (
        <header>
            <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
                <Container>
                    <Navbar.Brand href="/">Intelistyle</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <SearchBox/>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    )
}

export default Header