import React, { Component } from "react";
import Card from "react-bootstrap/Card";

import "./playerInfoSummaryPage.css";

class PlayerInfoSummaryPage extends Component {
  state = {
    allSeasonImg: "/etlImages/allSeason.png",
    playerBefore2017Img: "/etlImages/playerBefore2017.png",
    player2018Img: "/etlImages/player_2018.png",
    player2019Img: "/etlImages/player_2019.png",
    player2020Img: "/etlImages/player_2020.png",
    playerInfoImg: "/etlImages/playerInfo.png",
  };
  render() {
    return (
      <Card className="text-center">
        <Card.Header>Before ETL</Card.Header>
        <Card.Body>
          <Card.Title>raw player info data</Card.Title>
          <Card.Text>
            <img className="img-format" src={this.state.playerBefore2017Img} />
            <img className="img-format" src={this.state.player2018Img} />
            <img className="img-format" src={this.state.player2019Img} />
            <img className="img-format" src={this.state.player2020Img} />
            <Card className="text-center">
              {/* <Card.Header>After ETL</Card.Header> */}
              <Card.Body>
                <Card.Title>raw all season data</Card.Title>
                <Card.Text>
                  <img className="img-format" src={this.state.allSeasonImg} />
                  <Card className="text-center">
              <Card.Header>After ETL</Card.Header>
              <Card.Body>
                <Card.Title>clean player info</Card.Title>
                <Card.Text>
                  <img className="img-format" src={this.state.playerInfoImg} />
                </Card.Text>
              </Card.Body>
            </Card>
                </Card.Text>
              </Card.Body>
            </Card>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default PlayerInfoSummaryPage;
