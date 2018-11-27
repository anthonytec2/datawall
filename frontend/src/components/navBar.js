import React, { Component } from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
class MyNavBar extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <React.Fragment>
        <Navbar style={{ margin: 0, padding: 0 }}>
          <Navbar.Header>
            <Navbar.Brand>
              <a href="#home">Datawall</a>
            </Navbar.Brand>
          </Navbar.Header>
          <Nav>
            <NavItem eventKey={1} href="#">
              About
            </NavItem>
            <NavItem eventKey={2} href="#">
              Careers
            </NavItem>
          </Nav>
        </Navbar>
      </React.Fragment>
    );
  }
}

export default MyNavBar;