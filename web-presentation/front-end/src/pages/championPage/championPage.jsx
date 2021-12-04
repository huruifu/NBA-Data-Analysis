import React, { Component } from "react";
import Carousel from "react-bootstrap/Carousel";

import "./championPage.css";

class ChampionPage extends Component {
  state = {
    index: 0,
    championImg: "/mac/champion.png",
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
        <Carousel.Item>
          <img
            className="d-block img-format"
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
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    );
  }
}

export default ChampionPage;
