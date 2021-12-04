import React, { Component } from "react";

import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class AvgPtsModal extends Component {
  state = {
    // age: 0,
    count: 0,
    // height: 0,
    // weight: 0,
    avgPts: 0,
    nextSeasonAge: 0,
    nextSeasonHeight: 0,
    nextSeasonWeight: 0,
    player_position_index: 0,
    status_index: 0,
  };

  predict = () => {
    let predictValue =
      // this.state.count * (-0.009854868617951875) +
      this.state.avgPts * 0.8930098970551869 +
      this.state.nextSeasonAge * (-0.17777944357606432) +
      this.state.nextSeasonHeight * (-0.007365458313683309) +
      this.state.nextSeasonWeight * (-0.010669228655380534) +
      this.getStatusWeight() +
      this.getPositionWeight() + 9.178426229863547;
    return predictValue.toFixed(2);
  };

  getStatusWeight = () => {
    switch (this.state.status_index) {
      case 0:
        return -0.12910361164272233;
      case 1:
        return -0.1997729325661938;
      case 2:
        return -0.3777806362715741;
      case 3:
        return -0.24900335804547918;
      case 4:
        return -0.1726787816961902;
      default:
        return 0;
    }
  };

  getPositionWeight = () => {
    switch (this.state.player_position_index) {
      case 0:
        return 0.04498625222458093;
      case 1:
        return 0.17615736699869508;
      case 2:
        return 0.0;
      case 3:
        return -0.03163195454244776;
      case 4:
        return -0.08278047708654358;
      case 5:
        return 1.2473647410697641;
      case 6:
        return 0.0;
      case 7:
        return -0.32172274719936794;
      case 8:
        return 0.0;
      case 9:
        return 0.0;
      case 10:
        return 0.12433720509686712;
      default:
        return 0;
    }
  };

  onClickPredict = () => {
    let predictValue = this.predict();
    this.setState({ predictValue });
  };

  handleClose = () => {
    let state = this.state;
    delete state.predictValue;
    this.setState(state);
  };

  renderResults = () => {
    if (this.state.predictValue) {
      return (
        <Alert variant="primary" onClose={this.handleClose} dismissible>
          The predict average scores in next season is{" "}
          {this.state.predictValue}
        </Alert>
      );
    } else return null;
  };

  render() {
    return (
      <Modal
        backdrop="static"
        show={this.props.value}
        onHide={this.props.onHandleClose}
      >
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Row className="mb-3">
              {/* <Form.Group as={Col} controlId="formGridEmail">
                <Form.Label>age</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter last season age"
                  // value={this.state.count}
                  onChange={(e) => this.setState({ age: e.target.value })}
                />
              </Form.Group> */}

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>nextSeasonAge</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter next season age"
                  onChange={(e) =>
                    this.setState({ nextSeasonAge: e.target.value })
                  }
                />
              </Form.Group>
            </Row>

            {/* <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridAddress2">
                <Form.Label>height</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter Height"
                  onChange={(e) => this.setState({ height: e.target.value })}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridAddress1">
                <Form.Label>weight</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter weight"
                  onChange={(e) => this.setState({ weight: e.target.value })}
                />
              </Form.Group>
            </Row> */}

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridAddress2">
                <Form.Label>next season height (cm)</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter Height next season"
                  onChange={(e) =>
                    this.setState({ nextSeasonHeight: e.target.value })
                  }
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridAddress1">
                <Form.Label>next season weight (lb)</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter weight next season"
                  onChange={(e) =>
                    this.setState({ nextSeasonWeight: e.target.value })
                  }
                />
              </Form.Group>
            </Row>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridAddress2">
                <Form.Label>number of injuries</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter number of injuries"
                  onChange={(e) => this.setState({ count: e.target.value })}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridAddress1">
                <Form.Label>average points</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter avg pts"
                  onChange={(e) => this.setState({ avgPts: e.target.value })}
                />
              </Form.Group>
            </Row>

            <Row className="mb-3">
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
                </Form.Select>
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState2">
                <Form.Label>player injury status</Form.Label>
                <Form.Select
                  defaultValue="Choose..."
                  onChange={(e) =>
                    this.setState({ status_index: e.target.value })
                  }
                >
                  <option>Choose...</option>
                  <option value={0}>DTD</option>
                  <option value={1}>do not rest</option>
                  <option value={2}>out for season</option>
                  <option value={3}>out indefinitely</option>
                  <option value={4}>DNP</option>
                </Form.Select>
              </Form.Group>
            </Row>
          </Form>
          {this.renderResults()}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={this.props.onHandleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={this.onClickPredict}>
            Submit
          </Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default AvgPtsModal;
