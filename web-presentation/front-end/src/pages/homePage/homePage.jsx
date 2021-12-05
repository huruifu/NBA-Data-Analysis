import React, { Component } from "react";

import "./homePage.css";

class HomePage extends Component {
  state = {
    backgroundImgPath: "/images/background.jpg",
  };

  render() {
    return (
      // <div className="container">
      //   <img className="background-image" src={this.state.backgroundImgPath} />
      //   <div class="centered">Centered</div>
      // </div>
      <div style={{
         backgroundImage: "url(/images/background.jpg)",
         backgroundPosition: 'top',
         minHeight: '50%',
         height: '100vh',
         position: 'relative',
         display: 'block'
         }}>
      </div>
    );
  }
}

export default HomePage;
