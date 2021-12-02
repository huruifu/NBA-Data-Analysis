import React, { Component } from "react";

import Card from "react-bootstrap/Card";

import "./teamRankingSummaryPage.css";

class TeamRankingSummaryPage extends Component {
    state = {
        rawTeamImg: "/etlImages/team.png",
        cleanTeamImg: "/etlImages/team_ranking.png"
    };
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw team ranking data</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.rawTeamImg} />
            <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>clean team ranking data</Card.Title>
                <Card.Text>
                  <img
                    className="img-format"
                    src={this.state.cleanTeamImg}
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

export default TeamRankingSummaryPage;
