import React, { Component } from 'react';
import { Navbar } from 'react-bootstrap';

class NavBar extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div>
        <Navbar>
          <Navbar.Header>
            <Navbar.Brand>
              <a href="#home">dataWall</a>
            </Navbar.Brand>
          </Navbar.Header>
          <Nav>
            <NavItem eventKey={1} href="#">
              About
            </NavItem>
            <NavItem eventKey={2} href="#">
              FAQ
            </NavItem>
            <NavItem eventKey={3} href="#">
              Investor Something
            </NavItem>
            <NavItem eventKey={4} href="#">
              Something that starts with a C
            </NavItem>
            <NavItem eventKey={5} href="#">
              We're Hiring!
            </NavItem>
          </Nav>
        </Navbar>
      </div>
    );
  }
}

export default NavBar;
