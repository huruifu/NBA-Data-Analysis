import React, { Component } from "react";
import Carousel from "react-bootstrap/Carousel";
import Tab from "react-bootstrap/Tab";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Nav from "react-bootstrap/Nav";

import SalaryPredictionModal from "../../components/modal/salaryModal";
import "./salaryPage.css";

class SalaryPage extends Component {
  state = {
    index: 0,
    salary_boxplot_byyear: "/salaryImages/salary_boxplot_byyear.png",
    salary_correlation: "/salaryImages/salary_correlation.png",
    salary_histogram: "/salaryImages/salary_histogram.png",
    salary_featureImportance: "/salaryImages/salary_featureImportance.png",
    salary_predictions: "/salaryImages/salary_predictions.png",
  };

  handleSelect = (selectedIndex, e) => {
    this.setState({ index: selectedIndex });
  };

  render() {
    return (
      <Tab.Container id="left-tabs-example" defaultActiveKey="first">
        <Row>
          <Col sm={3}>
            <Nav variant="pills" className="flex-column">
              <Nav.Item>
                <Nav.Link eventKey="first">Salary boplot</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="second">Salary Histogram</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="third">Correlation Plot</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="fourth">Feature Importance Plot</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="fifth">Prediction Vs Actual Value Plot</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="sixth">Demo</Nav.Link>
              </Nav.Item>
            </Nav>
          </Col>
          <Col sm={9}>
            <Tab.Content>
              <Tab.Pane eventKey="first">
                <Card>
                  <img
                    className="d-block img-format"
                    src={this.state.salary_boxplot_byyear}
                    width="50"
                  />
                  <Card.Body>
                    <Card.Title style={{textAlign: "center"}}>Salary boxplot by year</Card.Title>
                  </Card.Body>
                </Card>
              </Tab.Pane>
              <Tab.Pane eventKey="second">
                <Card>
                  <img
                    className="d-block img-format"
                    src={this.state.salary_histogram}
                    width="50"
                  />
                  <Card.Body>
                    <Card.Title style={{textAlign: "center"}}>Salary Histogram</Card.Title>
                  </Card.Body>
                </Card>
              </Tab.Pane>
              <Tab.Pane eventKey="third">
                <Card>
                  <img
                    className="d-block img-format"
                    src={this.state.salary_correlation}
                    width="50"
                  />
                  <Card.Body>
                    <Card.Title style={{textAlign: "center"}}>Salary Correlation</Card.Title>
                  </Card.Body>
                </Card>
              </Tab.Pane>
              <Tab.Pane eventKey="fourth">
                <Card>
                  <img
                    className="d-block img-format_v3"
                    src={this.state.salary_featureImportance}
                    width="50"
                  />
                  <Card.Body>
                    <Card.Title style={{textAlign: "center"}}>Feature Importance in Random Forest Model</Card.Title>
                  </Card.Body>
                </Card>
              </Tab.Pane>
              <Tab.Pane eventKey="fifth">
                <Card>
                  <img
                    className="d-block img-format"
                    src={this.state.salary_predictions}
                    width="100"
                  />
                  <Card.Body>
                    <Card.Title style={{textAlign: "center"}}>Prediction Vs Actual Value</Card.Title>
                  </Card.Body>
                </Card>
              </Tab.Pane>
              <Tab.Pane eventKey="sixth">
                <SalaryPredictionModal />
              </Tab.Pane>
            </Tab.Content>
          </Col>
        </Row>
      </Tab.Container>

      // <Carousel
      //   variant="dark"
      //   activeIndex={this.index}
      //   onSelect={this.handleSelect}
      //   interval={null}
      // >
      //   <Carousel.Item>
      //     <img
      //       className="d-block img-format"
      //       src={this.state.salary_boxplot_byyear}
      //       width="50"
      //       alt="First slide"
      //     />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <Carousel.Caption>
      //       <h3>Salary boxplot by year</h3>
      //     </Carousel.Caption>
      //   </Carousel.Item>
      //   <Carousel.Item>
      //     <img
      //       className="d-block img-format"
      //       src={this.state.salary_histogram}
      //       alt="First slide"
      //     />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <Carousel.Caption>
      //       <h3>Salary Histogram</h3>
      //     </Carousel.Caption>
      //   </Carousel.Item>
      //   <Carousel.Item>
      //     <img
      //       className="d-block img-format"
      //       src={this.state.salary_correlation}
      //       alt="First slide"
      //     />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <Carousel.Caption>
      //       <h3>Salary Correlation</h3>
      //     </Carousel.Caption>
      //   </Carousel.Item>
      //   <Carousel.Item>
      //     <img
      //       className="d-block img-format"
      //       src={this.state.salary_featureImportance}
      //       alt="First slide"
      //     />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br/>
      //     <Carousel.Caption>
      //       <h3>Using tree model, salary feature Importance</h3>
      //     </Carousel.Caption>
      //   </Carousel.Item>
      //   <Carousel.Item>
      //     <img
      //       className="d-block img-format_v2"
      //       src={this.state.salary_predictions}
      //       alt="First slide"
      //     />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <br />
      //     <Carousel.Caption>
      //       <h3>Prediction Vs Actual Value</h3>
      //     </Carousel.Caption>
      //   </Carousel.Item>
      // </Carousel>
    );
  }
}

export default SalaryPage;
