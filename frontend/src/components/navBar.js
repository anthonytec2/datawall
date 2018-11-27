import React, { Component } from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
class MyNavBar extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <React.Fragment>
        <Navbar style={{margin: 0, paddingBottom: 0, paddingTop: 0}}>
          <Navbar.Header>
            <Navbar.Brand>
            <img
              style={{width: 200, height: 80}}
              src={require('./datawall_blue.png')} />
            </Navbar.Brand>
          </Navbar.Header>
          <Nav>
            <NavItem style={{paddingTop:0}} eventKey={1} href="#"a>
              <h1 style={{margin:0, textAlign: "center"}}> About </h1>
            </NavItem>
            <NavItem style={{paddingTop:0}} eventKey={2} href="#">
              <h1 style={{margin:0, textAlign: "center"}}> Career </h1>
            </NavItem>
          </Nav>
        </Navbar>
      </React.Fragment>
    );
  }
}

export default MyNavBar;