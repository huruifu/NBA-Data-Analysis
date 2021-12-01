import React, { Component } from "react";
import Accordion from "react-bootstrap/Accordion";
import Image from "react-bootstrap/Image";
import Button from 'react-bootstrap/Button';
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import AvgPtsModal from "../modal/avgPtsModal";
import AvgAstModal from "../modal/avgAstModal";

class AgeInjuryPlayer extends Component {
  state = {
    avgPtsShow: false,
    avgAstShow: false,
    playerMostInjuryImgPath: "/images/player_most_injury.png",
    teamMostInjuryImgPath: "/images/team_most_injury.png",
    codeSnippetPath: "/images/code_snippet.png",
    avgPtsModelImgPath: "/images/trueVsActualAvgPts.png",
    avgAstModelImgPath: "/images/PredVsActualAvgAst.png",
    correlationImgPath: "/images/correlation.png",
    avgAstCorrImgPath: "/images/avgAstCorr.png",
    injuryTypeImgs: [
      {
        imgPath: "/images/c_injury_type.png",
        description: "injury type in position C",
      },
      {
        imgPath: "/images/f_injury_type.png",
        description: "injury type in position F",
      },
      {
        imgPath: "/images/g_injury_type.png",
        description: "injury type in position G",
      },
      {
        imgPath: "/images/pf_injury_type.png",
        description: "injury type in position PF",
      },
      {
        imgPath: "/images/pg_injury_type.png",
        description: "injury type in position PG",
      },
      {
        imgPath: "/images/sf_injury_type.png",
        description: "injury type in position SF",
      },
      {
        imgPath: "/images/sg_injury_type.png",
        description: "injury type in position SG",
      },
    ],
  };

  handleAvgPtsShow = () => {
    this.setState({avgPtsShow: true});
  }

  handleAvgPtsClose =() => {
    this.setState({avgPtsShow: false})
  }

  handleAvgAstShow = () => {
    this.setState({avgAstShow: true});
  }

  handleAvgAstClose =() => {
    this.setState({avgAstShow: false})
  }

  render() {
    return (
      <Accordion flush>
        <Accordion.Item eventKey="0">
          <Accordion.Header>Top Players get injury</Accordion.Header>
          <Accordion.Body>
            {/* <Image src={this.state.playerMostInjuryImgPath} fluid /> */}
            <img className="img-format" src={this.state.playerMostInjuryImgPath} />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>
            Top Teams who have the highest injury events
          </Accordion.Header>
          <Accordion.Body>
            {/* <Image src={this.state.teamMostInjuryImgPath} fluid /> */}
            <img className="img-format" src={this.state.teamMostInjuryImgPath} />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Injury Type</Accordion.Header>
          <Accordion.Body>
            <Row xs={1} md={2} className="g-4">
              {this.state.injuryTypeImgs.map((imgObj) => (
                <Col>
                  <Card>
                    {/* <Card.Img variant="top" src={imgObj.imgPath} /> */}
                    <img className="img-format" src={imgObj.imgPath} />
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
          <Accordion.Header>Feature Correlation</Accordion.Header>
          <Accordion.Body>
          {/* <Image src={this.state.correlationImgPath} fluid /> */}
          <img className="img-format" src={this.state.correlationImgPath} />
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="4">
          <Accordion.Header>
            Predicting players' avg stat in next season
          </Accordion.Header>
          <Accordion.Body>
          <Image src={this.state.avgPtsModelImgPath} fluid />
            <Button variant="primary" onClick={this.handleAvgPtsShow}>
              Launch demo
            </Button>
            <AvgPtsModal value={this.state.avgPtsShow} onHandleClose={this.handleAvgPtsClose}/>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="5">
          <Accordion.Header>
            Predicting players' avg ast in next season
          </Accordion.Header>
          <Accordion.Body>
          {/* <Image src={this.state.avgAstCorrImgPath} fluid />
          <Image src={this.state.avgAstModelImgPath} fluid /> */}
          <img className="img-format" src={this.state.avgAstCorrImgPath} />
          <img className="img-format" src={this.state.avgAstModelImgPath} />
            <Button variant="primary" onClick={this.handleAvgAstShow}>
              Launch demo
            </Button>
            <AvgAstModal value={this.state.avgAstShow} onHandleClose={this.handleAvgAstClose}/>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    );
  }
}

export default AgeInjuryPlayer;
