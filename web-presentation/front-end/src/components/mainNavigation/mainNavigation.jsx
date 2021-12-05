import React, { Component } from "react";

import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from "react-bootstrap/Nav";
import NavDropdown from 'react-bootstrap/NavDropdown';

class MainNavigation extends Component {
  render() {
    return (
        <div>
        <Navbar bg="dark" expand="sm" variant="dark" fixed="top">
        <Container>
        <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <NavDropdown title="ETL" id="navbarScrollingDropdown">
          <NavDropdown.Item href="/etl/player-stat-summary">Player Stat Summary</NavDropdown.Item>
          <NavDropdown.Item href="/etl/player-info-summary">Player Info Summary</NavDropdown.Item>
          <NavDropdown.Item href="/etl/injury">Player Injury Summary</NavDropdown.Item>
          <NavDropdown.Item href="/etl/salary">Player Salary Summary</NavDropdown.Item>
          <NavDropdown.Item href="/etl/team-ability">Team Ability Summary</NavDropdown.Item>
          <NavDropdown.Item href="/etl/team-ranking">Team Ranking Summary</NavDropdown.Item>
        </NavDropdown>
          <Nav.Link href="/new-player">New Player Analytics</Nav.Link>
          <Nav.Link href="mvp-nba-all-team">MVP & All NBA Team</Nav.Link>
          <Nav.Link href="/champion">Champion</Nav.Link>
          <Nav.Link href="/injury-age">Injury & Age</Nav.Link>
          <Nav.Link href="/salary">Player Salary</Nav.Link>
        </Nav>
        </Container>
      </Navbar>
      </div>
    );
  }
}

export default MainNavigation;
