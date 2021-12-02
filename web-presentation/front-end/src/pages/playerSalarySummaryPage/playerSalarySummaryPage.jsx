import React, { Component } from "react";

import Card from "react-bootstrap/Card";

import "./playerSalarySummaryPage.css";

class PlayerSalarySummary extends Component {
    state = {
        cleanSalaryImg: "/etlImages/clean_salary.png",
        rawSalaryImg: "/etlImages/salary.png",
        playerRawImg: "/etlImages/player_raw.png" 
    }
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw salary data</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.rawSalaryImg} />
            <Card className="text-center">
              {/* <Card.Header>After ETL</Card.Header> */}
              <Card.Body>
                <Card.Title>raw player data</Card.Title>
                <Card.Text>
                  <img
                    className="img-format"
                    src={this.state.playerRawImg}
                  />
                </Card.Text>
                <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>clean salary data</Card.Title>
                <Card.Text>
                  <img
                    className="img-format"
                    src={this.state.cleanSalaryImg}
                  />
                </Card.Text>
              </Card.Body>
            </Card>
              </Card.Body>
            </Card>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default PlayerSalarySummary;
