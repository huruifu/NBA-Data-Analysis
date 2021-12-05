import React, { Component } from "react";
import Carousel from "react-bootstrap/Carousel";

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
            <h3>Salary boxplot by year</h3>
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
            <h3>Salary Histogram</h3>
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
            <h3>Salary Correlation</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block img-format"
            src={this.state.salary_featureImportance}
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption>
            <h3>Using tree model, salary feature Importance</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block img-format_v2"
            src={this.state.salary_predictions}
            alt="First slide"
          />
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>
          <Carousel.Caption>
            <h3>Prediction Vs Actual Value</h3>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    );
  }
}

export default SalaryPage;
