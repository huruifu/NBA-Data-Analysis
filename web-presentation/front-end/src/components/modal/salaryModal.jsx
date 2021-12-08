import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class SalaryPredictionModal extends Component {
  state = {
    season: 0, // 0
    avgFgm: 0, // 1
    avgFga: 0, // 2
    avgFg3m: 0, // 3
    avgFg3a: 0, // 4
    avgFtm: 0, // 5
    avgFta: 0, // 6
    avgOreb: 0, // 7
    avgDreb: 0, // 8
    avgReb: 0, // 9
    avgAst: 0, // 10
    avgStl: 0, // 11
    avgBlk: 0, // 12
    avgTo: 0, // 13
    avgPf: 0, // 14
    avgPts: 0, // 15
    avgPm: 0, // 16

    sumFgm: 0, // 17
    sumFga: 0, // 18
    sumFg3m: 0, // 19
    sumFg3a: 0, // 20
    sumFtm: 0, // 21
    sumFta: 0, // 22
    sumOreb: 0, // 23
    sumDreb: 0, // 24
    sumReb: 0, // 25
    sumAst: 0, // 26
    sumStl: 0, // 27
    sumBlk: 0, // 28
    sumTo: 0, // 29
    sumPf: 0, // 30
    sumPts: 0, // 31
    sumPm: 0, // 32
    sumIfminutes: 0, // 33
    avgSeconds: 0, // 34
    sumSeconds: 0, // 35

    age: 0, // 36
    playerHeight: 0, // 37
    playerWeight: 0, // 38
    injuries: 0, // 39
  };

  predict =() => {
      let value0 = this.treeZero();
      let value1 = this.treeOne();
      let value2 = this.treeTwo();
      let value3 = this.treeThree();
      let predictVal = (((value0 + value1 + value2 + value3) / 3)).toFixed(2);
      return predictVal;
  }

  treeZero =() => {
      if (this.state.avgFgm <= 4.3293297290802) {
          if (this.state.avgSeconds <= 1387.2916870117188) {
              return 2400957.4036109494;
          }
          else {
              return 5572791.827027027;
          }
      }
      else {
          if (this.state.avgPts <= 18.107650756835938) {
              return 8772213.052083334;
          }
          else {
              return 1.4503244575757576E7;
          }
      }
  }

  treeOne =() => {
      if (this.state.sumFgm <= 305.5) {
          if (this.state.avgPts <= 9.05041217803955) {
              return 2589478.0593080726;
          }
          else {
              return 6485838.012383901;
          }
      }
      else {
          if (this.state.avgSeconds <= 1685.2750244140625) {
              return 5754362.948905109;
          }
          else {
              return 1.0409896063953489E7;
          }
      }
  }

  treeTwo =() => {
      if (this.state.avgFgm <= 4.905505895614624) {
          if (this.state.sumSeconds <= 63867.0) {
              return 2087445.1692183723;
          }
          else {
              return 4862079.808703536;
          }
      }
      else {
          if (this.state.age <= 25.25) {
              return 6396012.757281553;
          }
          else {
              return 1.4952690413489737E7;
          }
      }
  }

  treeThree =() => {
      if (this.state.avgFgm <= 4.055598497390747) {
          if (this.state.sumPf <= 93.5) {
              return 1891391.9981651376;
          }
          else {
              return 4052995.1195426197;
          }
      }
      else {
          if (this.state.avgSeconds <= 1878.9026489257812) {
              return 7899501.603174604;
          }
          else {
              return 1.2807812695384616E7;
          }
      }
  }

  isButtonEnabled =() => {
    let state = this.state;
    return Object.keys(state).every(key => state[key] != null);
  }

  onClickPredict =() => {
    let predictVal = this.predict();
    this.setState({predictVal});
  }

  renderResults = () => {
    if (this.state.predictVal) {
      return (
        <Alert variant="primary" onClose={this.handleCloseAlert} dismissible>
          The predict yearly salary is{" "}
          {this.state.predictVal}
        </Alert>
      );
    } else return null;
  };

  handleCloseAlert = () => {
    let state = this.state;
    delete state.predictVal;
    Object.keys(state).forEach(key => {
        state[key] = 0;
    });
    this.setState(state);
  };

  render() {
    return (
      <div>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="season">
              <Form.Label>Season</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter next season age"
                onChange={(e) => this.setState({ season: e.target.value })}
              />
            </Form.Group>

            <Form.Group as={Col} controlId="sumIfminutes">
              <Form.Label>Total Games played</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) =>
                  this.setState({ sumIfminutes: e.target.value })
                }
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFgm">
              <Form.Label>Average Field Goal Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFgm: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFgm">
              <Form.Label>Sum Field Goal Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFgm: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFga">
              <Form.Label>Average Field Goal Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFga: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFga">
              <Form.Label>Sum Field Goal Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFga: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFg3m">
              <Form.Label>Average 3 point Field Goal Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFg3m: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFg3m">
              <Form.Label>Sum Field Goal Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFg3m: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFg3a">
              <Form.Label>Average 3 point Field Goal Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFg3a: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFg3a">
              <Form.Label>Sum Field Goal Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFg3a: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFtm">
              <Form.Label>Average Free Throw Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFtm: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFtm">
              <Form.Label>Sum Free Throw Made</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFtm: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgFta">
              <Form.Label>Average Free Throw Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgFta: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumFta">
              <Form.Label>Sum Free Throw Attempt</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumFta: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgOreb">
              <Form.Label>Average Offensive Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgOreb: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumOreb">
              <Form.Label>Sum Offensive Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumOreb: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgDreb">
              <Form.Label>Average defensive Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgDreb: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumDreb">
              <Form.Label>Sum Defensive Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumDreb: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgReb">
              <Form.Label>Average Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgReb: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumReb">
              <Form.Label>Sum Rebound</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumReb: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgAst">
              <Form.Label>Average Assist</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgAst: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumAst">
              <Form.Label>Sum Assist</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumAst: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgStl">
              <Form.Label>Average Steal</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgStl: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumStl">
              <Form.Label>Sum Steal</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumStl: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgBlk">
              <Form.Label>Average Block</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgBlk: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumBlk">
              <Form.Label>Sum Block</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumBlk: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgTo">
              <Form.Label>Average Turn Over</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgTo: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumTo">
              <Form.Label>Sum Turn Over</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumTo: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgPf">
              <Form.Label>Average Personal Fouls</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgPf: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumPf">
              <Form.Label>Sum Personal Fouls</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumPf: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgPts">
              <Form.Label>Average Points</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgPts: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumPts">
              <Form.Label>Sum Points</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumPts: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgPm">
              <Form.Label>Box Plus Minus</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgPm: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumPm">
              <Form.Label>Plus Minus</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumPm: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="avgSeconds">
              <Form.Label>Average Seconds in a game</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) => this.setState({ avgSeconds: e.target.value })}
              />
            </Form.Group>
            <Form.Group as={Col} controlId="sumSeconds">
              <Form.Label>Total Seconds played</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) => this.setState({ sumSeconds: e.target.value })}
              />
            </Form.Group>
          </Row>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="height">
              <Form.Label>height (cm)</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter Height next season"
                onChange={(e) =>
                  this.setState({ playerHeight: e.target.value })
                }
              />
            </Form.Group>

            <Form.Group as={Col} controlId="weight">
              <Form.Label>weight (lb)</Form.Label>
              <Form.Control
                type="number"
                //   placeholder="Enter weight next season"
                onChange={(e) =>
                  this.setState({ playerWeight: e.target.value })
                }
              />
            </Form.Group>
          </Row>
        </Form>
        {this.renderResults()}
        <Button style={{marginLeft: "93%"}} variant="primary" onClick={this.onClickPredict} disabled={!this.isButtonEnabled}>
          Submit
        </Button>
      </div>
    );
  }
}

export default SalaryPredictionModal;
