import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { Form } from 'react-bootstrap';
import { Navbar } from 'react-bootstrap';

class ContractDetail extends Component {
  constructor(props){
    super(props);
  }
  render() {
    
    return (
      <div>
        <p>Contract Name: {props.contractName} </p>
        <p>Description: {props.description} </p>
        <p>Pricing Rules: {props.Pricing}</p>

        <Button> Join </Button>    

        <p>Current Price: {props.Current}</p>  
        <p>Payment History: {props.Payment}</p>

        <Form>
        <FormGroup
          controlId="formBasicText"
          validationState={this.getValidationState()}
        >
          <ControlLabel>Query Box</ControlLabel>
          <FormControl
            type="text"
            value={this.state.value}
            placeholder="What would you like to know?"
            onChange={this.handleChange}
          />
          <FormControl.Feedback />
          <HelpBlock>Input whatever you want, Grandpa</HelpBlock>
        </FormGroup>
        </Form>

        <Button> Query </Button>
      </div>
    );
  }
}

export default ContractDetail;