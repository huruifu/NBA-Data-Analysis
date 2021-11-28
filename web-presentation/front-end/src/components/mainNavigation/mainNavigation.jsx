import React, { Component } from "react";

import Container from 'react-bootstrap/Container'
import Navbar from 'react-bootstrap/Navbar'
import Nav from "react-bootstrap/Nav";

class MainNavigation extends Component {
  render() {
    return (
        <div>
        <Navbar bg="dark" expand="sm" variant="dark" fixed="top">
        <Container>
        <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/injury-age">Injury & Age</Nav.Link>
        </Nav>
        </Container>
      </Navbar>
      </div>
    );
  }
}

export default MainNavigation;
