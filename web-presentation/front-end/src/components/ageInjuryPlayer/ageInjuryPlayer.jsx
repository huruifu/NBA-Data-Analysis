import React, { Component } from "react";
import Accordion from "react-bootstrap/Accordion";
import Button from 'react-bootstrap/Button';
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import AvgPtsModal from "../modal/avgPtsModal";
import AvgAstModal from "../modal/avgAstModal";
import AvgStlModal from "../modal/avgStlModal";
import AvgBlkModal from "../modal/avgBlkModal";

class AgeInjuryPlayer extends Component {
  state = {
    avgPtsShow: false,
    avgAstShow: false,
    avgStlShow: false,
    avgBlkShow: false,
    playerMostInjuryImgPath: "/images/player_most_injury.png",
    teamMostInjuryImgPath: "/images/team_most_injury.png",
    correlationImgPath: "/images/correlation.png",
    avgAstCorrImgPath: "/images/avgAstCorr.png",
    corrImgs: [
      {imgPath: "/images/correlation.png", description: "feature correlation"},
      {imgPath: "/images/avgAstCorr.png", description: "feature selection"},
    ],
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
    scoreImgs: [
      {imgPath: "/images/ageScore.png", description: "age and avg score scatter plot"},
      {imgPath: "/images/countScore.png", description: "number of injury and avg score scatter plot"},
      {imgPath: "/images/heightScore.png", description: "height and avg score scatter plot"},
      {imgPath: "/images/weightScore.png", description: "weight and avg score scatter plot"},

      {imgPath: "/images/countResidualScore.png", description: "injury residual plot"},
      {imgPath: "/images/logCountResidualScore.png", description: "log injury residual plot"},
      {imgPath: "/images/ageResidualScore.png", description: "age residual plot"},
      {imgPath: "/images/heightResidualScore.png", description: "height residual plot"},
      {imgPath: "/images/weightResidualScore.png", description: "weight residual plot"},
      {imgPath: "/images/scoreResidualScore.png", description: "average score last season residual plot"},

      {imgPath: "/images/trueVsActualAvgPts.png", description: "validation prediction plot"}
    ],
    assistImgs: [
      {imgPath: "/images/ageAssist.png", description: "age and avg assist scatter plot"},
      {imgPath: "/images/countAssist.png", description: "number of injury and avg assist scatter plot"},
      {imgPath: "/images/heightAssist.png", description: "height and avg assist scatter plot"},
      {imgPath: "/images/weightAssist.png", description: "weight and avg assist scatter plot"},

      {imgPath: "/images/countResidualAssist.png", description: "injury residual plot"},
      {imgPath: "/images/logCountResidualAssist.png", description: "log injury residual plot"},
      {imgPath: "/images/ageResidualAssist.png", description: "age residual plot"},
      {imgPath: "/images/heightResidualAssist.png", description: "height residual plot"},
      {imgPath: "/images/weightResidualAssist.png", description: "weight residual plot"},
      {imgPath: "/images/assistResidualAssist.png", description: "average assist last season residual plot"},

      {imgPath: "/images/PredVsActualAvgAst.png", description: "validation prediction plot"}
    ],
    stlImgs: [
      {imgPath: "/images/ageSteal.png", description: "age and avg steal scatter plot"},
      {imgPath: "/images/countSteal.png", description: "number of injury and avg steal scatter plot"},
      {imgPath: "/images/heightSteal.png", description: "height and avg steal scatter plot"},
      {imgPath: "/images/weightSteal.png", description: "weight and avg steal scatter plot"},

      {imgPath: "/images/countResidualSteal.png", description: "injury residual plot"},
      {imgPath: "/images/logCountResidualSteal.png", description: "log injury residual plot"},
      {imgPath: "/images/ageResidualSteal.png", description: "age residual plot"},
      {imgPath: "/images/heightResidualSteal.png", description: "height residual plot"},
      {imgPath: "/images/weightResidualSteal.png", description: "weight residual plot"},
      {imgPath: "/images/stealResidualSteal.png", description: "average steal last season residual plot"},

      {imgPath: "/images/trueVsActualSteal.png", description: "validation prediction plot"}
    ],
    blkImgs: [
      {imgPath: "/images/ageBlk.png", description: "age and avg block scatter plot"},
      {imgPath: "/images/countBlk.png", description: "number of injury and avg block scatter plot"},
      {imgPath: "/images/heightBlk.png", description: "height and avg block scatter plot"},
      {imgPath: "/images/weightBlk.png", description: "weight and avg block scatter plot"},

      {imgPath: "/images/countResidualBlk.png", description: "injury residual plot"},
      {imgPath: "/images/logCountResidualBlk.png", description: "log injury residual plot"},
      {imgPath: "/images/ageResidualBlk.png", description: "age residual plot"},
      {imgPath: "/images/heightResidualBlk.png", description: "height residual plot"},
      {imgPath: "/images/weightResidualBlk.png", description: "weight residual plot"},
      {imgPath: "/images/blkResidualBlk.png", description: "average block last season residual plot"},

      {imgPath: "/images/trueVsActualBlk.png", description: "validation prediction plot"},
    ],
    drebImgs: [
      {imgPath: "/images/ageDreb.png", description: "age and avg defensive rebound scatter plot"},
      {imgPath: "/images/countDreb.png", description: "number of injury and avg defensive rebound scatter plot"},
      {imgPath: "/images/heightDreb.png", description: "height and avg defensive rebound scatter plot"},
      {imgPath: "/images/weightDreb.png", description: "weight and avg defensive rebound scatter plot"},

      // {imgPath: "/images/countResidualDreb.png", description: "injury residual plot"},
      // {imgPath: "/images/logCountResidualDreb.png", description: "log injury residual plot"},
      // {imgPath: "/images/ageResidualDreb.png", description: "age residual plot"},
      // {imgPath: "/images/heightResidualDreb.png", description: "height residual plot"},
      // {imgPath: "/images/weightResidualDreb.png", description: "weight residual plot"},
      // {imgPath: "/images/drebResidualDreb.png", description: "average deffensive rebound last season residual plot"},

      {imgPath: "/images/drebImportanceFeature.png", description: "feature importance plot"},

      {imgPath: "/images/trueVsActualDreb.png", description: "validation prediction plot"},
    ],
    orebImgs: [
      {imgPath: "/images/ageOreb.png", description: "age and avg offensive rebound scatter plot"},
      {imgPath: "/images/countOreb.png", description: "number of injury and avg offensive rebound scatter plot"},
      {imgPath: "/images/heightOreb.png", description: "height and avg offensive rebound scatter plot"},
      {imgPath: "/images/weightOreb.png", description: "weight and avg offensive rebound scatter plot"},

      // {imgPath: "/images/countResidualOreb.png", description: "injury residual plot"},
      // {imgPath: "/images/logCountResidualOreb.png", description: "log injury residual plot"},
      // {imgPath: "/images/ageResidualOreb.png", description: "age residual plot"},
      // {imgPath: "/images/heightResidualOreb.png", description: "height residual plot"},
      // {imgPath: "/images/weightResidualOreb.png", description: "weight residual plot"},
      // {imgPath: "/images/orebResidualOreb.png", description: "average offensive rebound last season residual plot"},

      {imgPath: "/images/orebFeatureImportance.png", description: "feature importance plot"},

      {imgPath: "/images/trueVsActualOreb.png", description: "validation prediction plot"},
    ]
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

  handleAvgStlShow = () => {
    this.setState({avgStlShow: true});
  }

  handleAvgStlClose =() => {
    this.setState({avgStlShow: false})
  }

  handleAvgBlkShow = () => {
    this.setState({avgBlkShow: true});
  }

  handleAvgBlkClose =() => {
    this.setState({avgBlkShow: false})
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
          <Row xs={1} md={2} className="g-4">
              {this.state.corrImgs.map((imgObj) => (
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
        <Accordion.Item eventKey="4">
          <Accordion.Header>
            Predicting players' avg score in next season
          </Accordion.Header>
          <Accordion.Body>
          {/* <Image src={this.state.avgPtsModelImgPath} fluid /> */}
          <Row xs={1} md={2} className="g-4">
              {this.state.scoreImgs.map((imgObj) => (
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
          {/* <img className="img-format" src={this.state.avgAstCorrImgPath} />
          <img className="img-format" src={this.state.avgAstModelImgPath} /> */}
          <Row xs={1} md={2} className="g-4">
              {this.state.assistImgs.map((imgObj) => (
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
            <Button variant="primary" onClick={this.handleAvgAstShow}>
              Launch demo
            </Button>
            <AvgAstModal value={this.state.avgAstShow} onHandleClose={this.handleAvgAstClose}/>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="6">
          <Accordion.Header>
            Predicting players' avg stl in next season
          </Accordion.Header>
          <Accordion.Body>
          <Row xs={1} md={2} className="g-4">
              {this.state.stlImgs.map((imgObj) => (
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
            <Button variant="primary" onClick={this.handleAvgStlShow}>
              Launch demo
            </Button>
            <AvgStlModal value={this.state.avgStlShow} onHandleClose={this.handleAvgStlClose}/>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="7">
          <Accordion.Header>
            Predicting players' avg block in next season
          </Accordion.Header>
          <Accordion.Body>
          <Row xs={1} md={2} className="g-4">
              {this.state.blkImgs.map((imgObj) => (
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
            <Button variant="primary" onClick={this.handleAvgBlkShow}>
              Launch demo
            </Button>
            <AvgBlkModal value={this.state.avgBlkShow} onHandleClose={this.handleAvgBlkClose}/>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="8">
          <Accordion.Header>
            Predicting players' defensive rebound in next season
          </Accordion.Header>
          <Accordion.Body>
          <Row xs={1} md={2} className="g-4">
              {this.state.drebImgs.map((imgObj) => (
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
        <Accordion.Item eventKey="9">
          <Accordion.Header>
            Predicting players' offensive rebound in next season
          </Accordion.Header>
          <Accordion.Body>
          <Row xs={1} md={2} className="g-4">
              {this.state.orebImgs.map((imgObj) => (
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
      </Accordion>
    );
  }
}

export default AgeInjuryPlayer;
