import React, { Component } from "react";

import Card from "react-bootstrap/Card";
import "./playerStatSummaryPage.css";

class PlayerStatSummaryPage extends Component {
    state = {
        gameDetailImg: "/etlImages/gameDetails.png",
        gameImg: "/etlImages/game.png",
        playerStatImg1: "/etlImages/player_stat1.png",
        playerStatImg2: "/etlImages/player_stat2.png",
        playerStatImg3: "/etlImages/player_stat3.png",
    }
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw game data</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.gameImg} />
            <Card className="text-center">
              {/* <Card.Header>After ETL</Card.Header> */}
              <Card.Body>
                <Card.Title>raw game detail data</Card.Title>
                <Card.Text>
                  <img className="img-format" src={this.state.gameDetailImg} />
                </Card.Text>
              </Card.Body>
            </Card>
            <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>player stat summary</Card.Title>
                <Card.Text>
                  <img className="img-format" src={this.state.playerStatImg1} />
                  <img className="img-format" src={this.state.playerStatImg2} />
                  <img className="img-format" src={this.state.playerStatImg3} />
                </Card.Text>
              </Card.Body>
            </Card>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default PlayerStatSummaryPage;
