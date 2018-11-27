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
            <img
              style={{width: 245, height: 125}}
              src={require('./datawall_black.png')} />
            </Navbar.Brand>
          </Navbar.Header>
          <Nav>
            <NavItem eventKey={1} href="#"a>
              <h1 style={{textAlign: "center"}}> About </h1>
            </NavItem>
            <NavItem eventKey={2} href="#">
              <h1 style={{textAlign: "center"}}> Career </h1>
            </NavItem>
          </Nav>
        </Navbar>
      </React.Fragment>
    );
  }
}

export default MyNavBar;