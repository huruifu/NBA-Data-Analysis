import React, { Component } from "react";

import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class AvgAstModal extends React.Component {
  state = {
    age: 0,
    count: 0,
    height: 0,
    weight: 0,
    avgAst: 0,
    nextSeasonAge: 0,
    nextSeasonHeight: 0,
    nextSeasonWeight: 0,
    player_position_index: 0,
    status_index: 0,
  };

  predict = () => {
    let predictValue =
      this.state.age * 0.5495510867660398 +
      this.state.count * 0.001951171228582191 +
      this.state.height * 0.06066350111162505 +
      this.state.weight * -0.023107691576517563 +
      this.state.avgAst * 0.8706604491917964 +
      this.state.nextSeasonAge * -0.5801353991084546 +
      this.state.nextSeasonHeight * -0.06718100228160792 +
      this.state.nextSeasonWeight * 0.027171368759090632 +
      this.getStatusWeight() +
      this.getPositionWeight();
    return predictValue.toFixed(2);
  };

  getStatusWeight = () => {
    switch (this.state.status_index) {
      case 0:
        return -0.22447935543034217;
      case 1:
        return -0.22393625141922494;
      case 2:
        return -0.3586709904292356;
      case 3:
        return -0.32869834825058164;
      case 4:
        return -0.2878710191775542;
      default:
        return 0;
    }
  };

  getPositionWeight = () => {
    switch (this.state.player_position_index) {
      case 0:
        return 0.5686275766604322;
      case 1:
        return 0.3441569835032559;
      case 2:
        return 0.3366598783632808;
      case 3:
        return 0.32985764466270145;
      case 4:
        return 0.3762355310363787;
      case 5:
        return 0.637300472252502;
      case 6:
        return 0.20202205506379087;
      case 7:
        return 0.4480135488161109;
      case 8:
        return 0.40041474503684094;
      case 9:
        return 0.9019250757155337;
      case 10:
        return -0.1751013560058243;
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
          The predict average assists in next season is{" "}
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
              <Form.Group as={Col} controlId="formGridEmail">
                <Form.Label>age</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter last season age"
                  // value={this.state.count}
                  onChange={(e) => this.setState({ age: e.target.value })}
                />
              </Form.Group>

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

            <Row className="mb-3">
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
            </Row>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridAddress2">
                <Form.Label>next season height</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter Height next season"
                  onChange={(e) =>
                    this.setState({ nextSeasonHeight: e.target.value })
                  }
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridAddress1">
                <Form.Label>next season weight</Form.Label>
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
                <Form.Label>avg Ast</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Enter avg ast"
                  onChange={(e) => this.setState({ avgAst: e.target.value })}
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

export default AvgAstModal;
