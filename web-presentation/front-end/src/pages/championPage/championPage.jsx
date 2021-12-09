import React, { Component } from "react";
import Carousel from "react-bootstrap/Carousel";

import "./championPage.css";

class ChampionPage extends Component {
  state = {
    index: 0,
    championImg: "/mac/champion.jpeg",
    featureImportanceImg: "/mac/champion-fi.jpeg",
    // correlation: "/mac/coorelation.jpeg"
    championAndTeamRank: "mac/championAndTeamRank.jpeg"
  };

  handleSelect = (selectedIndex, e) => {
    this.setState({ index: selectedIndex });
  };

  render() {
    return (
      <Carousel
        variant="dark"
        activeIndex={this.index}
        onSelect={this.handleSelect}
        interval={null}
      >
        <Carousel.Item eventKey="0">
          <img
            className="d-block img-format-v2"
            src={this.state.championAndTeamRank}
            width="50"
            alt="First slide"
          />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <Carousel.Caption>
            <h3>Probability plot of championship and regular season ranking</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item eventKey="1">
          <img
            className="d-block img-format-v2"
            src={this.state.championImg}
            width="50"
            alt="First slide"
          />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <Carousel.Caption>
            <h3>Model Feature Importance</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item eventKey="2">
          <img
            className="d-block img-format"
            src={this.state.featureImportanceImg}
            width="50"
            alt="First slide"
          />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <Carousel.Caption>
            <h3>Model Feature Importance</h3>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    );
  }
}

export default ChampionPage;
