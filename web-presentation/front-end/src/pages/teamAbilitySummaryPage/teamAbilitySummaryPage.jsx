import React, { Component } from "react";

import Card from "react-bootstrap/Card";

import "./teamAbilitySummaryPage.css";

class TeamAbilitySummaryPage extends Component {
  state = {
    imgPaths: [
      { path: "/etlImages/game.png", description: "raw game data" },
      {
        path: "/etlImages/teamAbility.png",
        description: "after etl, team ability data",
      },
    ],
    gameImgPath: "/etlImages/game.png",
    teamAbilityImgPath: "/etlImages/teamAbility.png",
  };
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw data from game.csv</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.gameImgPath} />
            <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>Team Ability Summary</Card.Title>
                <Card.Text>
                  <img className="img-format" src={this.state.teamAbilityImgPath} />
                </Card.Text>
              </Card.Body>
            </Card>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default TeamAbilitySummaryPage;
