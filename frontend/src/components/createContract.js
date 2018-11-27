import React, { Component } from 'react';
import { FormGroup, FormControl, ControlLabel, Panel, Button } from 'react-bootstrap';

class CreateContract extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contractName:"",
      contractDesc:"",
      modelAddress:"",
      companies:"",
      rules:""
    }
  }
  onNameChange = (e) => {
    this.setState({ contractName: e.target.value });
  }
  onDescChange = (e) => {
    this.setState({ contractDesc: e.target.value });
  }
  onAddressChange = (e) => {
    this.setState({ modelAddress: e.target.value });
  }
  onCompanyListChange = (e) => {
    this.setState({ companies: e.target.value });
  }
  render() {
    const sharpStyle = {
      "borderRadius":0,
      "fontSize": "20px"
    };
    console.log("[createContract] ", this.props.companyName);
    return (
      <div style = {{marginTop:"20px"}}>
          <Panel style={sharpStyle}>
            <Panel.Heading>
              {"Citi"}
            </Panel.Heading>
            <Panel.Body>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Contract Name
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.contractName}
                    placeholder=""
                    onChange={this.onNameChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Contract Description
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.contractDesc}
                    placeholder="Contract usage, model introduction, etc."
                    onChange={this.onDescChange}
                  />
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Model Repo
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.modelAddress}
                    placeholder="URL of the repo where user can see model"
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
                    Companies
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.companies}
                    placeholder="List of companies required for this contract"
                    onChange={this.onCompanyListChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Pricing Rules
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.rules}
                    placeholder="Tell users how they are going to be charged"
                    onChange={this.onCompanyListChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
              <form>
                <FormGroup
                  controlId="formControlsTextarea"
                >
                  <ControlLabel>
                    Companies
                  </ControlLabel>
                  <FormControl
                    componentClass="textarea"
                    type="text"
                    value={this.state.companies}
                    placeholder="List of companies required for this contract"
                    onChange={this.onCompanyListChange}
                  />
                  <FormControl.Feedback />  
                </FormGroup>
              </form>
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

export default CreateContract;
