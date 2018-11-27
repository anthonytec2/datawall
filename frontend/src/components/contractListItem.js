import React, { Component } from 'react';
import { Button, Panel } from 'react-bootstrap';

class ContractListItem extends Component {
  constructor(props){
    super(props);
    this.state = {
      contractName: props.contractInfo.name,
      contractStatus: props.contractInfo.status,
      companyList: props.contractInfo.companies,
      contractContent: props.contractInfo.content
    }
  }
  render() {
    const sharpStyle = {
      "borderRadius":0,
      "fontSize":"20px"
    };
    let bsStyle = "warning";
    if (this.state.contractStatus === "ready") {
      bsStyle = "primary";
    }
    return (
      <Panel style={sharpStyle} bsStyle={bsStyle}>
        <Panel.Heading>
          {this.state.contractName}
        </Panel.Heading>
        <Panel.Body>
          <div>
            Description:{this.state.contractContent}
          </div>
          <div>
            Status:{this.state.contractStatus}
          </div>
          <Button style={sharpStyle} float={"right"} onClick = {() => this.props.onDetailSelected(this.state.contractName)}>Detail</Button>
        </Panel.Body>
      </Panel>
    );
  }
}

export default ContractListItem;