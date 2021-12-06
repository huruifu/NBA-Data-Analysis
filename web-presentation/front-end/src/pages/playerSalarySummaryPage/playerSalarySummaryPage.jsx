import React, { Component } from "react";
import Spinner from "react-bootstrap/Spinner";
import BootstrapTable from "react-bootstrap-table-next";
import paginationFactory from "react-bootstrap-table2-paginator";
import Card from "react-bootstrap/Card";

import { getDatabase, ref, onValue, value } from "firebase/database";
import "./playerSalarySummaryPage.css";

class PlayerSalarySummary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      cleanSalaryImg: "/etlImages/clean_salary.png",
        rawSalaryImg: "/etlImages/salary.png",
        playerRawImg: "/etlImages/player_raw.png" ,
      columns: [
        { dataField: "season", text: "season", sort: true },
        { dataField: "PLAYER_NAME", text: "PLAYER_NAME", sort: true },
        { dataField: "PLAYER_ID", text: "PLAYER_ID" },
        { dataField: "salary", text: "salary", sort: true },
        { dataField: "avg(AST)", text: "avg(AST)" },
        { dataField: "avg(BLK)", text: "avg(BLK)" },
        { dataField: "avg(DREB)", text: "avg(DREB)" },
        { dataField: "avg(FG3A)", text: "avg(FG3A)" },
        { dataField: "avg(FG3M)", text: "avg(FG3M)" },
        { dataField: "avg(FGA)", text: "avg(FGA)" },
        { dataField: "avg(FGM)", text: "avg(FGM)" },
        { dataField: "avg(FTA)", text: "avg(FTA)" },
        { dataField: "avg(FTM)", text: "avg(FTM)" },
        { dataField: "avg(OREB)", text: "avg(OREB)" },
        { dataField: "avg(PF)", text: "avg(PF)" },
        { dataField: "avg(PLUS_MINUS)", text: "avg(PLUS_MINUS)" },
        { dataField: "avg(PTS)", text: "avg(PTS)" },
        { dataField: "avg(REB)", text: "avg(REB)" },
        { dataField: "avg(seconds)", text: "avg(seconds)" },
        { dataField: "avg(STL)", text: "avg(STL)" },
        { dataField: "avg(TO)", text: "avg(TO)" },

        { dataField: "sum(AST)", text: "sum(AST)" },
        { dataField: "sum(BLK)", text: "sum(BLK)" },
        { dataField: "sum(DREB)", text: "sum(DREB)" },
        { dataField: "sum(FG3A)", text: "sum(FG3A)" },
        { dataField: "sum(FG3M)", text: "sum(FG3M)" },
        { dataField: "sum(FGA)", text: "sum(FGA)" },
        { dataField: "sum(FGM)", text: "sum(FGM)" },
        { dataField: "sum(FTA)", text: "sum(FTA)" },
        { dataField: "sum(FTM)", text: "sum(FTM)" },
        { dataField: "sum(ifminute)", text: "sum(ifminute)" },
        { dataField: "sum(OREB)", text: "sum(OREB)" },
        { dataField: "sum(PF)", text: "sum(PF)" },
        { dataField: "sum(PLUS_MINUS)", text: "sum(PLUS_MINUS)" },
        { dataField: "sum(PTS)", text: "sum(PTS)" },
        { dataField: "sum(REB)", text: "sum(REB)" },
        { dataField: "sum(seconds)", text: "sum(seconds)" },
        { dataField: "sum(STL)", text: "sum(STL)" },
        { dataField: "sum(TO)", text: "sum(TO)" },
        { dataField: "injuries", text: "injuries" },
        { dataField: "player_height", text: "player height" },
        { dataField: "player_weight", text: "player_weight" },
      ],
    };
  }

  getData = () => {
    let db = getDatabase();
    let salaryRef = ref(db, "salary");
    onValue(salaryRef, (snapshot) => {
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
    );
    // return (
    //   <Card className="text-center">
    //     <Card.Header>Before ETL</Card.Header>
    //     <Card.Body>
    //       <Card.Title>raw salary data</Card.Title>
    //       <Card.Text>
    //         <img className="img-format" src={this.state.rawSalaryImg} />
    //         <Card className="text-center">
    //           {/* <Card.Header>After ETL</Card.Header> */}
    //           <Card.Body>
    //             <Card.Title>raw player data</Card.Title>
    //             <Card.Text>
    //               <img
    //                 className="img-format"
    //                 src={this.state.playerRawImg}
    //               />
    //             </Card.Text>
    //             <Card className="text-center">
    //           <Card.Header>After ETL</Card.Header>
    //           <Card.Body>
    //             <Card.Title>clean salary data</Card.Title>
    //             <Card.Text>
    //               <img
    //                 className="img-format"
    //                 src={this.state.cleanSalaryImg}
    //               />
    //             </Card.Text>
    //           </Card.Body>
    //         </Card>
    //           </Card.Body>
    //         </Card>
    //       </Card.Text>
    //     </Card.Body>
    //   </Card>
    // );
  }
}

export default PlayerSalarySummary;
