import React, { Component } from "react";

import Carousel from "react-bootstrap/Carousel";

import "./salaryPage.css";

class SalaryPage extends Component {
  state = {
    index: 0,
    salary_boxplot_byyear: "/salaryImages/salary_boxplot_byyear.png",
    salary_correlation: "/salaryImages/salary_correlation.png",
    salary_histogram: "/salaryImages/salary_histogram.png",
    salary_predictions: "/salaryImages/salary_predictions.png",
  };

  handleSelect = (selectedIndex, e) => {
    this.setState({ index: selectedIndex });
  };

  render() {
    return (
      <Carousel
        variant="dark"
        activeIndex={this.index}
        onSelect={this.handleSelect}
        interval={null}
      >
        <Carousel.Item>
          <img
            className="d-block img-format"
            src={this.state.salary_boxplot_byyear}
            width="50"
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption>
            <h3>First slide label</h3>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block img-format"
            src={this.state.salary_histogram}
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption >
            <h3>Second slide label</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block img-format"
            src={this.state.salary_correlation}
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption>
            <h3>Third slide label</h3>
            <p>
              Praesent commodo cursus magna, vel scelerisque nisl consectetur.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block img-format"
            src={this.state.salary_predictions}
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption>
            <h3>Fourth slide label</h3>
            <p>
              Praesent commodo cursus magna, vel scelerisque nisl consectetur.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    );
  }
}

export default SalaryPage;
