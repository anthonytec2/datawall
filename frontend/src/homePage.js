import React, { Component } from 'react';
import axios from './axios';
import ContractList from './components/contractList';
import SideBar from './components/sideBar';
import CreateContract from './components/createContract';
import SettingsPage from './components/settingsPage';
import ContractDetail from './components/contractDetail';
import NavBar from './components/navBar';
import ContributeContract from './components/contributeContract';
import { Grid, Row, Col } from "react-bootstrap";
class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // MyContract, Explore, Settings, Create, MyDetail, ExploreDetail
      contentState: undefined,
      myContracts: undefined,
      globalContracts: undefined,
      contractDetail: undefined,
      contributeContract: undefined
    }
  }
  componentDidMount() {
    let myContracts = undefined;
    let globalContracts = undefined;
    axios.get(`company/jpm/contracts`)
      .then(res => {
        myContracts = res.data.contracts;
        // console.log(myContracts);
        axios.get(`contract/all`)
          .then(res => {
            globalContracts = res.data.contracts;
            this.setState({ myContracts: myContracts, globalContracts: globalContracts });
          });
      });
  }
  onContentChange = (content) => {
    console.log("switching to content " + content);
    this.setState({ contentState: content });
  }

  onDetailSelected = (contractName) => {
    console.log("detail selected", contractName);
    var selectedContract = undefined;
    for (var i = 0; i < this.state.globalContracts.length; i++) {
      if (contractName === this.state.globalContracts[i].name) {
        selectedContract = this.state.globalContracts[i];
        break;
      }
    }
    console.log("found contract: ", selectedContract);
    if (this.state.contentState === "MyContract") {
      this.setState({ contentState: "MyDetail", contractDetail: selectedContract });
    } else if (this.state.contentState == "Explore") {
      this.setState({ contentState: "ExploreDetail", contractDetail: selectedContract })
    }
  }
  onDashboardSelected = () => {
    console.log("dashboard selected");
    this.setState({ contentState: "Dashboard" });
  }
  onContributeSelected = (contractName) => {
    console.log("contributed selected for ", contractName);
    this.setState({
      contentState: "Contribute",
      contributeContract: contractName
    });
  }
  render() {
    let displayContent = undefined;
    console.log("[render] current content is ", this.state.contentState);
    if (this.state.contentState === "MyContract") {
      displayContent = <ContractList
        contracts={this.state.myContracts}
        onDetailSelected={this.onDetailSelected}
      />;
    } else if (this.state.contentState === "Explore") {
      console.log(this.state.globalContracts);
      displayContent = <ContractList
        contracts={this.state.globalContracts}
        onDetailSelected={this.onDetailSelected}
      />;
      // displayContent = <p>This is display</p>
    } else if (this.state.contentState === "Create") {
      displayContent = <CreateContract />;
    } else if (this.state.contentState === "Settings") {
      displayContent = <SettingsPage />;
    } else if (this.state.contentState === "MyDetail") {
      console.log("showing details of ", this.state.contractDetail);
      displayContent = <ContractDetail
        membership={true}
        contractInfo={this.state.contractDetail}
        onContributeSelected={this.onContributeSelected}
      />
    } else if (this.state.contentState === "ExploreDetail") {
      console.log("showing details of ", this.state.contractDetail);
      displayContent = <ContractDetail
        membership={false}
        contractInfo={this.state.contractDetail}
        onContributeSelected={this.onContributeSelected}
      />
    } else if (this.state.contentState === "Contribute") {
      console.log("on contribute page, contract name is ", this.state.contributeContract);
      displayContent = <ContributeContract
        companyName={"Citi"}
        contractName={this.state.contributeContract}
      />
    } else if (this.state.contentState === "Dashboard") {
      displayContent = <div>
        <iframe src="http://35.243.211.120/dashboards/0e016fd8-0953-45ce-a334-3180aee8ccc5" height="600px" width="100%"></iframe>
      </div>
    } else {
      displayContent = undefined;
    }
    console.log(displayContent);
    return (
<<<<<<< HEAD
      <Grid style = {{padding: 0, margin: 0, width : "100%", height: "100%", fontSize:"3em"}}>
        <Row className="show-grid">
         <NavBar/>
        </Row>  
        <Row className="show-grid" style = {{height: "100%"}}>
=======
      <Grid style={{ padding: 0, margin: 0, width: "100%", height: "100%" }}>
        <Row className="show-grid">
          <NavBar />
        </Row>
        <Row className="show-grid" style={{ height: "100%" }}>
>>>>>>> bd078c91b80a750174025783843b86dbc620c759
          <Col xs={6} lg={3}>
            <SideBar onContentSelected={this.onContentChange} />
          </Col>
          <Col xs={6} lg={9}>
            <div>
              {displayContent}
            </div>
          </Col>
        </Row>
      </Grid>
    );
  }
}

export default HomePage;
