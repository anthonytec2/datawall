import React, { Component } from 'react';
import ContractList from './components/contractList'
import SideBar from './components/sideBar';
import NavBar from  './components/navBar';

class App extends Component {
  constructor(props){
    // This is the contract and company dictionary used for test only
    const contracts = [
      {
        "name":"contract1",
        "description": "we will sell all your data",
        "company":[
          "jpm", "citi"
        ],
        "rules": "rule1"
      },
      {
        "name":"contract2",
        "description":"your data will sell us all",
        "company":[
          "boa", "capitalone"
        ],
        "rules": "rule2"
      },
      {
        "name":"contract3",
        "description":"use malicious data",
        "company":[
          "boa", "capitalone", "citi"
        ],
        "rules": "rule1"
      }
    ]
    // end of testing contract
    super(props);
    this.state = {contracts:contracts}; //it is an array
  }
  render() {
    return (
      <div>
        <div>
          <NavBar />
        </div>
        <div  class="grid-container">
          <div>
            <SideBar />
          </div>
          <div>
            <p>hello this is the homepage</p>
            <ContractList contracts = {this.state.contracts}/>
          </div>
        </div>
      </div>
    );
  }
}

export default App;