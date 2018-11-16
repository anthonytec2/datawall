import React, { Component } from 'react';
import ContractListItem from './contractListItem'
import SideBar from './sideBar.js'

class ContractList extends Component {
  constructor(props){
    super(props);
    this.state = {
        contracts:props.contracts
    }
  }
  render() {
    const contractList = this.state.contracts.map(((contract, i) => {
      return (
        <ContractListItem 
          contractName = {contract.name}
          contractDescription = {contract.description}
          key = {i}/>
      );
    }));
    return (
      <div>
        {contractList}
      </div>
    );
  }
}

export default ContractList;
