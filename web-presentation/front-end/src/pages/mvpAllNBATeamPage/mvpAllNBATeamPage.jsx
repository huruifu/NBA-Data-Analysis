import React, { Component } from "react";

import Accordion from "react-bootstrap/Accordion";

import "./mvpAllNBATeamPage.css";

class MVPAllNBATeamPage extends Component {
  state = {
    mvpFeatureImg: "/mac/mvp_feature.png",
    allnbaImg: "/mac/allnba.png",
  };

  render() {
    return (
      <Accordion>
        <Accordion.Item eventKey="0">
          <Accordion.Header>MVP</Accordion.Header>
          <Accordion.Body>
            <img className="img-format" src={this.state.mvpFeatureImg} />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>All NBA Team</Accordion.Header>
          <Accordion.Body>
          <img className="img-format" src={this.state.allnbaImg} />
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    );
  }
}

export default MVPAllNBATeamPage;
