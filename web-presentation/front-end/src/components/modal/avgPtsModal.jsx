import React, { Component } from "react";

import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class AvgPtsModal extends Component {
  state = {
    count: 0,
    height: 0,
    player_position_index: 0,
    avgPts: 0,
    nextSeasonAge: 0,
    nextSeasonWeight: 0,
  };

  predict = () => {
    console.log(this);
    let valueZero = this.treeZero();
    let valueOne = this.treeOne();
    let valueTwo = this.treeTwo();
    let valueThree = this.treeThree();
    let valueFour = this.treeFour();
    let predictAvgPts = (
      (valueZero + valueOne + valueTwo + valueThree + valueFour) /
      5
    ).toFixed(2);
    return predictAvgPts;
  };

  treeZero = () => {
    if (this.state.height <= 204.47000122070312) {
      if (this.state.avgPts <= 11.568016251050715) {
        if (this.state.nextSeasonWeight <= 99.56344223022461) {
          return 8.416734595597179;
        } else {
          return 6.826565880677082;
        }
      } else {
        if (this.state.avgPts <= 19.627857142857142) {
          return 14.804182705618071;
        } else {
          return 22.702957546364853;
        }
      }
    } else {
      if (this.state.count <= 11.5) {
        if (this.state.avgPts <= 10.605318699873365) {
          return 6.52009226262389;
        } else {
          return 14.6604129740276;
        }
      } else {
        if (this.state.nextSeasonAge <= 25.5) {
          return 21.421981330924417;
        } else {
          return 10.520023003980697;
        }
      }
    }
  };

  treeOne = () => {
    if (this.state.avgPts <= 13.3762077294686) {
      if (this.state.avgPts <= 9.434780219780219) {
        if ([2, 3, 4, 6, 11, 12].includes(this.state.player_position_index)) {
          return 6.233183718616151;
        } else {
          return 7.551003015688908;
        }
      } else {
        if (this.state.nextSeasonAge <= 23.5) {
          return 13.770355612349064;
        } else {
          return 10.840542530764298;
        }
      }
    } else {
      if (this.state.avgPts <= 22.894670846394984) {
        if ([1, 2, 3, 7].includes(this.state.player_position_index)) {
          return 15.913021452199985;
        } else {
          return 17.281744092728218;
        }
      } else {
        if (this.state.height <= 207.01000213623047) {
          return 25.961610477518715;
        } else {
          return 22.67831941211233;
        }
      }
    }
  };

  treeTwo = () => {
    if ([2, 3, 6, 9, 11, 12].includes(this.state.player_position_index)) {
      if (this.state.nextSeasonWeight <= 113.17120361328125) {
        if (this.state.nextSeasonWeight <= 100.01703643798828) {
          return 12.853566421956868;
        } else {
          return 8.046007891812852;
        }
      } else {
        if (this.state.count <= 2.5) {
          return 8.821087218828866;
        } else {
          return 12.85075647983338;
        }
      }
    } else {
      if (this.state.nextSeasonWeight <= 108.40848922729492) {
        if (this.state.avgPts <= 11.568016251050715) {
          return 8.119689050468544;
        } else {
          return 15.720193136978212;
        }
      } else {
        if (this.state.avgPts <= 18.720093656875267) {
          return 14.711603222849424;
        } else {
          return 28.158296296296292;
        }
      }
    }
  };

  treeThree = () => {
    if (this.state.avgPts <= 14.311290322580646) {
      if (this.state.avgPts <= 9.434780219780219) {
        if (this.state.nextSeasonWeight <= 100.92422103881836) {
          return 7.097160659711361;
        } else {
          return 6.029266823633394;
        }
      } else {
        if (this.state.avgPts <= 11.018518518518519) {
          return 10.2878147531935;
        } else {
          return 12.070690593046473;
        }
      }
    } else {
      if (this.state.avgPts <= 19.627857142857142) {
        if ([7, 9, 13].includes(this.state.player_position_index)) {
          return 11.689838556505224;
        } else {
          return 15.995133261868968;
        }
      } else {
        if (this.state.height <= 212.09000396728516) {
          return 23.764639148842235;
        } else {
          return 18.612051649928276;
        }
      }
    }
  };

  treeFour = () => {
    if (this.state.avgPts <= 11.018518518518519) {
      if (this.state.nextSeasonAge <= 31.5) {
        if ([1, 3, 5, 6, 7, 12].includes(this.state.player_position_index)) {
          return 6.969887231716011;
        } else {
          return 8.503847865187339;
        }
      } else {
        if (this.state.avgPts <= 4.1300675675675675) {
          return 2.2145779416511124;
        } else {
          return 7.189100028419758;
        }
      }
    } else {
      if (this.state.avgPts <= 19.627857142857142) {
        if (this.state.nextSeasonAge <= 31.5) {
          return 15.075402686011383;
        } else {
          return 13.554298503831413;
        }
      } else {
        if (this.state.nextSeasonWeight <= 113.62479782104492) {
          return 24.2322568646708;
        } else {
          return 18.275287356321844;
        }
      }
    }
  };

  onClickPredict = () => {
    // console.log(this.state.count);
    // console.log(this.state.height);
    // console.log(this.state.player_position_index);
    // console.log(this.state.avgPts);
    // console.log(this.state.nextSeasonAge);
    // console.log(this.state.nextSeasonWeight);
    let predictValue = this.predict();
    // console.log(predictValue);
    this.setState({ predictValue });
  };

  handleClose =() => {
    let state = this.state;
    delete state.predictValue;
    this.setState(state)
  }

  renderResults = () => {
    if (this.state.predictValue) {
      return (
        <Alert variant="primary" onClose={this.handleClose} dismissible>
          The predict average points in next season is{" "}
          {this.state.predictValue}
        </Alert>
      );
    }
    else return null;
  };

  render() {
    return (
      <Modal backdrop="static" show={this.props.value} onHide={this.props.onHandleClose}>
        {/* <Modal.Header closeButton>
          <Modal.Title>Demo of predicting next season avg points</Modal.Title>
        </Modal.Header> */}
        <Modal.Body>
          <Form>
            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridEmail">
                <Form.Label>number of injury in last season</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter num injury last season"
                  // value={this.state.count}
                  onChange={(e) => this.setState({ count: e.target.value })}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>last season height</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter height"
                  // value={this.state.height}
                  onChange={(e) => this.setState({ height: e.target.value })}
                />
              </Form.Group>
            </Row>

            <Form.Group className="mb-3" controlId="formGridAddress1">
              <Form.Label>avg points in last season</Form.Label>
              <Form.Control
                placeholder="Enter avg pts"
                // value={this.state.avgPts}
                onChange={(e) => this.setState({ avgPts: e.target.value })}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress2">
              <Form.Label>age in next Season</Form.Label>
              <Form.Control
                placeholder="Enter age in next season"
                // value={this.state.nextSeasonAge}
                onChange={(e) =>
                  this.setState({ nextSeasonAge: e.target.value })
                }
              />
            </Form.Group>

            <Row className="mb-3">
              <Form.Group className="mb-3" controlId="formGridLabel">
                <Form.Label>weight in next season</Form.Label>
                <Form.Control
                  placeholder="Enter weight in next season"
                  // value={this.state.nextSeasonWeight}
                  onChange={(e) =>
                    this.setState({ nextSeasonWeight: e.target.value })
                  }
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>player position</Form.Label>
                <Form.Select
                  defaultValue="Choose..."
                  onChange={(e) =>
                    this.setState({ player_position_index: e.target.value })
                  }
                >
                  <option>Choose...</option>
                  <option value={0}>PG</option>
                  <option value={1}>SG</option>
                  <option value={2}>PF</option>
                  <option value={3}>C</option>
                  <option value={4}>SF</option>
                  <option value={5}>G</option>
                  <option value={6}>F</option>
                  <option value={7}>G-F</option>
                  <option value={8}>F-G</option>
                  <option value={9}>SF-SG</option>
                  <option value={10}>C-PF</option>
                  <option value={11}>F-C</option>
                  <option value={12}>PF-C</option>
                  <option value={13}>SG-PF</option>
                </Form.Select>
              </Form.Group>
            </Row>
          </Form>
          {this.renderResults()}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" type="submit" onClick={this.onClickPredict}>
            Submit
          </Button>
          <Button variant="secondary" onClick={this.props.onHandleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default AvgPtsModal;
