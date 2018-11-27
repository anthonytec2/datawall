import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import { FormGroup, FormControl, ControlLabel, Panel } from 'react-bootstrap';
import axios from 'axios';

class ContractDetail extends Component {
  constructor(props){
    super(props);
    console.log("[ContractDetail] ", props.contractInfo);
    this.state = {
      contractInfo:props.contractInfo,
      membership:props.membership,
      queryText:"",
      userName:"citi",
      currentPrice:props.contractInfo.initialPrice,
      queryResult:undefined
    };
  }
  componentDidMount() {
    axios.get(`http://35.243.211.120:5000/cost_user/` + this.state.userName)
    .then(res => {
        const data = res.data.cost;
        if (data !== undefined) {
          this.setState({currentPrice:data});
        }
    });
  }
  onSubmitQuery = () => {
    console.log(this.state.queryText);
    const params = {
      "User":"citi",
      "Data":[1,2,3,4,5,6,7]
    }
    // mock up thing here
    this.setState({queryResult:0});
    axios.post(`http://35.243.211.120:5000/inf`,params)
    .then(function (response) {
      console.log(response.data[0]);
      // this.setState({queryResult:response.data[0]});
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  handleChange = (e) => {
    this.setState({ queryText: e.target.value });
  }
  render() {
    const sharpStyle = {
      "borderRadius":0,
      "fontSize": "30px"
    };
    const tagStyle = {
      "borderRadius":0,
      "margin": "5px",
      "fontSize": "30px"
    };
    let companyList = this.state.contractInfo.companies.map(
      (companyName, i) => {
        return <Button bsStyle={"primary"} style={tagStyle} key = {i}>{companyName}</Button>
      }
    );
    let currentPricePerQuery = this.state.currentPrice;
    if (currentPricePerQuery === undefined) {
      currentPricePerQuery = this.state.contractInfo.initialPrice;
    }
    let queryResultDisplay = undefined;
    if (this.state.queryResult !== undefined) {
      queryResultDisplay = <p>query result: {this.state.queryResult}</p>;
    }
    return (
      <div style = {{marginTop:"20px"}}>
        <Panel style={sharpStyle}>
          <Panel.Heading>
            <p>Contract Name: {this.state.contractInfo.name} </p>
          </Panel.Heading>
          <Panel.Body>
            <div>
              <p>Description: {this.state.contractInfo.content} </p>
              <p>Pricing Rules: {"$2 base price"}</p>
              <p>Status: {this.state.contractInfo.status}</p>
              <p><a href = {"https://github.com/anthonytec2/datawall/tree/master/model_training"}>Training Scripts</a></p>
              <p>Input data format: ["amount_local_currency:int", "old_balance_orig:int",
                  "new_balance_orig:int"]</p>
              <p>Companies:</p>
              {companyList}
            </div>
          </Panel.Body>
        </Panel>
        <Panel style={sharpStyle}>
          <Panel.Heading>
            <p>Your status</p>
          </Panel.Heading>
          <Panel.Body>
            <div>
              <p>Current Price Per Query: {this.state.currentPrice}</p>  
            </div>
            <Button style={sharpStyle} 
                    onClick = {() => this.props.onContributeSelected(this.state.contractInfo.name)}
                    > Contribute </Button> 
          </Panel.Body>
        </Panel>
        <Panel style={sharpStyle}>
          <Panel.Heading>
            <p>Send a Query</p>
          </Panel.Heading>
          <Panel.Body>
          <form>
            <FormGroup
              controlId="formControlsTextarea"
            >
              <ControlLabel></ControlLabel>
              <FormControl
                componentClass="textarea"
                type="text"
                value={this.state.queryText}
                placeholder="Enter query"
                onChange={this.handleChange}
              />
              <FormControl.Feedback />  
            </FormGroup>
          </form>
          <Button style = {sharpStyle} onClick={this.onSubmitQuery}>Submit Query</Button>
          {queryResultDisplay}
          </Panel.Body>
        </Panel>
      </div>
    );
  }
}

export default ContractDetail;