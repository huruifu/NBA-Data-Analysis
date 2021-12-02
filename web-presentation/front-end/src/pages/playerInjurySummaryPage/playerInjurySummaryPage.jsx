import React, { Component } from "react";
import Card from "react-bootstrap/Card";

import "./playerInjurySummaryPage.css";

class PlayerInjurySummaryPage extends Component {
    state = {
        cleanInjuryImg: "/etlImages/clean_injuries.png",
        rawInjuryImg: "/etlImages/injury.png"
    }
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw injury data</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.rawInjuryImg} />
            <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>clean injury data</Card.Title>
                <Card.Text>
                  <img
                    className="img-format"
                    src={this.state.cleanInjuryImg}
                  />
                </Card.Text>
              </Card.Body>
            </Card>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default PlayerInjurySummaryPage;
