import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { Form } from 'react-bootstrap';
import { Navbar } from 'react-bootstrap';

class ContractDetail extends Component {
  constructor(props){
    super(props);
    console.log("[ContractDetail] ", props.contractInfo);
    this.state = {
      contractInfo:props.contractInfo,
      membership:props.membership,
      queryText:""
    }
  }
  onQueryChange = () => {
    console.log("query changes");
  }
  onSubmit = () => {
    console.log("submit");
  }
  render() {
    let companyList = this.state.contractInfo.companies.map(
      (companyName, i) => {
        return <p key = {i}>{companyName}</p>
      }
    );
    return (
      <div>
        <p>Contract Name: {this.state.contractInfo.name} </p>
        <p>Description: {this.state.contractInfo.description} </p>
        <p>Pricing Rules: {this.state.contractInfo.pricing}</p>
        <p>Status: {this.state.contractInfo.pricing}</p>
        <p>Content: {this.state.contractInfo.content}</p>
        {companyList}
        <Button> Join </Button>    

        <p>Current Price: Ask pricing server</p>  
        <p>Payment History: Ask pricing server if membership</p>

      <form onSubmit={this.handleSubmit}>
        <label>
          <input 
            type="text" value={this.state.queryText} 
            onChange={this.onQueryChange} />
        </label>
        <input type="submit" value="Query" />
      </form>
      </div>
    );
  }
}

export default ContractDetail;