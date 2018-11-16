import React, { Component } from 'react';
<<<<<<< HEAD
import { Navbar } from 'react-bootstrap';

class NavBar extends Component {
=======
import { Navbar, Nav, NavItem } from 'react-bootstrap';
class MyNavBar extends Component {
>>>>>>> 3b1944d66c1a02a183b471ccc5bc8da35f0e60e4
  constructor(props){
    super(props);
  }
  render() {
    return (
      <React.Fragment>
        <Navbar style = {{margin: 0, padding: 0}}>
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
              Career
            </NavItem>
          </Nav>
        </Navbar>
      </React.Fragment>
    );
  }
}

export default MyNavBar;