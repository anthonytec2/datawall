import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

class SideBar extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div>
        <p>This is the side bar</p>
        <Button> button1 </Button>
        <Button> button2 </Button>
      </div>
    );
  }
}

export default SideBar;
