import React, { Component } from "react";
import Accordion from "react-bootstrap/Accordion";
import Image from 'react-bootstrap/Image'


class AgeInjuryPlayer extends React.Component {
    state = {
        playerMostInjuryImgPath: "/images/player_most_injury.png",
        teamMostInjuryImgPath: "/images/team_most_injury.png",
        codeSnippetPath: "/images/code_snippet.png"
    }
  render() {
    return (
      <Accordion flush>
        <Accordion.Item eventKey="0">
          <Accordion.Header>Top Players get injury</Accordion.Header>
          <Accordion.Body>
          <Image src={this.state.playerMostInjuryImgPath} fluid />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>Top Teams who have the highest injury events</Accordion.Header>
          <Accordion.Body>
          <Image src={this.state.teamMostInjuryImgPath} fluid />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Injury Type</Accordion.Header>
          <Accordion.Body>
          
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="3">
          <Accordion.Header>Predicting players' stat in next season</Accordion.Header>
          <Accordion.Body>
          <Image src={this.state.codeSnippetPath} fluid />
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    );
  }
}

export default AgeInjuryPlayer;
