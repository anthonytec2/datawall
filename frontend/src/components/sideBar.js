import React, { Component } from 'react';
import { Button, ButtonGroup } from 'react-bootstrap';

class SideBar extends Component {
  constructor(props){
    super(props);
  }

  render() {
    const buttonStyle = {
      "borderRadius":0,
      "fontSize":"30px"
    }
    return (
      <React.Fragment>
        <ButtonGroup vertical style = {{width:"100%", marginTop: "20px"}}>
          <Button bsSize={"large"} bsStyle={"primary"} style={buttonStyle} onClick = {() => this.props.onContentSelected("MyContract")}>
                    My Contract
            </Button>
            <Button bsSize={"large"} bsStyle={"primary"} style={buttonStyle} onClick = {() => this.props.onContentSelected("Explore")}>
                  Explore
            </Button>
            <Button bsSize={"large"} bsStyle={"primary"} style={buttonStyle} onClick = {() => this.props.onContentSelected("Create")}>
                  Create Contract
            </Button>
            <Button bsSize={"large"} bsStyle={"primary"} style={buttonStyle} onClick = {() => this.props.onContentSelected("Settings")}>
                  Settings
            </Button>
            <Button bsSize={"large"} bsStyle={"primary"} style={buttonStyle} onClick = {() => this.props.onContentSelected("Dashboard")}>
                  Dashboard
            </Button>
        </ButtonGroup>
      </React.Fragment>
    );
  }
}

export default SideBar;
