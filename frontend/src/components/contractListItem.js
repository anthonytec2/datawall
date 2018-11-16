import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

class ContractListItem extends Component {
  constructor(props){
    super(props);
    this.state = {
      contractName: props.contractName,
      contractInfo: props.description,
      companyList: props.company
    }
  }
  render() {
    const companyTag = this.state.companyTag.map((company, i) => {
      return (
        <Button text = {company} key = {i} />
      );
    });
    return (
      <div>
        <p>{this.state.contractName}</p>
        <p>{this.state.description}</p>
        
        <Button>Detail</Button>
      </div>
    );
  }
}

export default ContractListItem;