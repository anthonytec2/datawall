import React, { Component } from 'react';
import { FormGroup, FormControl, ControlLabel, Panel, Button } from 'react-bootstrap';

class ContributeContract extends Component {
  constructor (props) {
    super(props);
    this.state = {
      bucketAddress: "",
      bucketKey: ""
    }
  }
  onAddressChange = (e) => {
    this.setState({ bucektAddress: e.target.value });
  }
  onKeyChange = (e) => {
    this.setState({ bucektKey: e.target.value });
  }
  onSubmitBucket = () => {
    console.log("bucket submitted ", this.state.bucketKey, this.state.bucketAddress);
  }
  render() {
    const sharpStyle = {
      "borderRadius":0,
      "fontSize": "20px"
    };
    console.log(this.props.contractName);
    return (
        <div style = {{marginTop:"20px"}}>
          <Panel style={sharpStyle}>
            <Panel.Heading>
              {this.props.companyName}
            </Panel.Heading>
            <Panel.Body>
              <div>
                {this.props.contractName}
                <p>Data Format: ["amount_local_currency:int", "old_balance_orig:int",
                    "new_balance_orig:int"]</p>
              </div>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Bucket address
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.queryText}
                    placeholder="Enter bucket address"
                    onChange={this.onAddressChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Bucket key
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.queryText}
                    placeholder="Enter bucket key"
                    onChange={this.onKeyChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
              <Button style = {sharpStyle} onClick={this.onSubmitBucket}>Submit data</Button>
            </Panel.Body>
          </Panel>
      </div>
    );
  }
}

export default ContributeContract;