import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

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
    return (
      <div>
        <p>{this.state.contractName}</p>
        <p>{this.state.contractStatus}</p>
        <p>{this.state.contractContent}</p>
        <Button onClick = {() => this.props.onDetailSelected(this.state.contractName)}>Detail</Button>
      </div>
    );
  }
}

export default ContractListItem;