import React, { Component } from "react";
import Image from "react-bootstrap/Image";

import "./homePage.css";


class HomePage extends React.Component {
  state = {
    backgroundImgPath: "/images/background.jpg"
  };

  render() {
    return (
      <div className="container">
        <Image src={this.state.backgroundImgPath} fluid/>
        <div class="centered">Centered</div>
      </div>
    );
  }
}

export default HomePage;
