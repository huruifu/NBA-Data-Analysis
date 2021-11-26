import React, { Component } from "react";
import Accordion from "react-bootstrap/Accordion";
import Image from "react-bootstrap/Image";
import Card from "react-bootstrap/Card";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

class AgeInjuryPlayer extends React.Component {
  state = {
    playerMostInjuryImgPath: "/images/player_most_injury.png",
    teamMostInjuryImgPath: "/images/team_most_injury.png",
    codeSnippetPath: "/images/code_snippet.png",
    injuryTypeImgs: [
      { imgPath: "/images/c_injury_type.png", description: "injury type in position C" },
      { imgPath: "/images/f_injury_type.png", description: "injury type in position F" },
      { imgPath: "/images/g_injury_type.png", description: "injury type in position G" },
      { imgPath: "/images/pf_injury_type.png", description: "injury type in position PF" },
      { imgPath: "/images/pg_injury_type.png", description: "injury type in position PG" },
      { imgPath: "/images/sf_injury_type.png", description: "injury type in position SF" },
      { imgPath: "/images/sg_injury_type.png", description: "injury type in position SG" }
    ]
  };
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
          <Accordion.Header>
            Top Teams who have the highest injury events
          </Accordion.Header>
          <Accordion.Body>
            <Image src={this.state.teamMostInjuryImgPath} fluid />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Injury Type</Accordion.Header>
          <Accordion.Body>
            <Row xs={1} md={2} className="g-4">
              {this.state.injuryTypeImgs.map(imgObj => (
                <Col>
                  <Card>
                    <Card.Img variant="top" src={imgObj.imgPath} />
                    <Card.Body>
                      <Card.Title>{imgObj.description}</Card.Title>
                    </Card.Body>
                  </Card>
                </Col>
              ))}
            </Row>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="3">
          <Accordion.Header>
            Predicting players' stat in next season
          </Accordion.Header>
          <Accordion.Body>
            <Image src={this.state.codeSnippetPath} fluid />
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    );
  }
}

export default AgeInjuryPlayer;
