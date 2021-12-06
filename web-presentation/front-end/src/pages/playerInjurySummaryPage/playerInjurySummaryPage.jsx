import React, { Component } from "react";
import Card from "react-bootstrap/Card";
import Table from "react-bootstrap/Table";
import Spinner from "react-bootstrap/Spinner";
import BootstrapTable from "react-bootstrap-table-next";
import paginationFactory from "react-bootstrap-table2-paginator";

import "./playerInjurySummaryPage.css";
import { database } from "../../initFirebase";
import { getDatabase, ref, onValue, value } from "firebase/database";

class PlayerInjurySummaryPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      cleanInjuryImg: "/etlImages/clean_injuries.png",
      rawInjuryImg: "/etlImages/injury.png",
      columns: [
        { dataField: "Team", text: "Team" },
        { dataField: "Relinquished", text: "Relinquished" },
        { dataField: "injury_name", text: "Injury Name" },
        { dataField: "status", text: "Status" },
        { dataField: "Date", text: "Date" },
        { dataField: "month", text: "Month" },
        { dataField: "year", text: "Year" },
        { dataField: "played_season", text: "Season" },
      ],
    };
    // let db = getDatabase();
    // let injuryRef = ref(db, "injury");
    // onValue(injuryRef, (snapshot) => {
    //   let data = snapshot.val();
    //   // console.log(data);
    //   this.setState({ data: data, loading: false });
    // });
    // console.log(this.state);
  }

  getData = () => {
    let db = getDatabase();
    let injuryRef = ref(db, "injury");
    onValue(injuryRef, (snapshot) => {
      let data = snapshot.val();
      // console.log(data);
      this.setState({ data: data, loading: false });
    });
    console.log(this.state);
  };

  componentDidMount =() => {
    this.getData()
  }

  render() {
    return this.state.loading ? (
      <div>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    ) : (
      <BootstrapTable
        keyField="name"
        data={this.state.data}
        columns={this.state.columns}
        pagination={paginationFactory()}
      ></BootstrapTable>
      // <Table striped bordered hover>
      //   <thead>
      //     <tr>
      //       <th>#</th>
      //       <th>Team</th>
      //       <th>Relinquished</th>
      //       <th>Injury Name</th>
      //       <th>Status</th>
      //       <th>Date</th>
      //       <th>Month</th>
      //       <th>Year</th>
      //       <th>Season</th>
      //     </tr>
      //   </thead>
      //   <tbody>
      //     {this.state.data.map((obj, i) => (
      //       <tr>
      //         <td>{i}</td>
      //         <td>{obj["Team"]}</td>
      //         <td>{obj["Relinquished"]}</td>
      //         <td>{obj["injury_name"]}</td>
      //         <td>{obj["status"]}</td>
      //         <td>{obj["Date"]}</td>
      //         <td>{obj["month"]}</td>
      //         <td>{obj["year"]}</td>
      //         <td>{obj["played_season"]}</td>
      //       </tr>
      //     ))}
      //   </tbody>
      // </Table>
      // <Card className="text-center">
      //   <Card.Header>Before ETL</Card.Header>
      //   <Card.Body>
      //     <Card.Title>raw injury data</Card.Title>
      //     <Card.Text>
      //       <img className="img-format" src={this.state.rawInjuryImg} />
      //       <Card className="text-center">
      //         <Card.Header>After ETL</Card.Header>
      //         <Card.Body>
      //           <Card.Title>clean injury data</Card.Title>
      //           <Card.Text>
      //             <img className="img-format" src={this.state.cleanInjuryImg} />
      //           </Card.Text>
      //         </Card.Body>
      //       </Card>
      //     </Card.Text>
      //   </Card.Body>
      // </Card>
    );
  }
}

export default PlayerInjurySummaryPage;
