import React, { Component } from "react";
import Spinner from "react-bootstrap/Spinner";
import BootstrapTable from "react-bootstrap-table-next";
import paginationFactory from "react-bootstrap-table2-paginator";

import Card from "react-bootstrap/Card";

import { getDatabase, ref, onValue, value } from "firebase/database";
import "./teamRankingSummaryPage.css";

class TeamRankingSummaryPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      rawTeamImg: "/etlImages/team.png",
      cleanTeamImg: "/etlImages/team_ranking.png",
      columns: [
        { dataField: "YEAR", text: "Season", sort: true },
        { dataField: "TEAM", text: "Team", sort: true },
        { dataField: "TEAM_ID", text: "Team ID" },
        { dataField: "CONFERENCE", text: "CONFERENCE", sort: true },
        { dataField: "G", text: "total games" },
        { dataField: "W", text: "Win Games", sort: true },
        { dataField: "L", text: "lose Games", sort: true },
        { dataField: "HOME_RECORD", text: "Home Record", sort: true },
        { dataField: "ROAD_RECORD", text: "Road Record", sort: true },
        { dataField: "W_PCT", text: "Wining Pct" },
        { dataField: "STANDINGSDATE", text: "STANDINGSDATE" },
      ],
    };
  }

  getData = () => {
    let db = getDatabase();
    let rankingRef = ref(db, "team-ranking");
    onValue(rankingRef, (snapshot) => {
      let data = snapshot.val();
      // console.log(data);
      this.setState({ data: data, loading: false });
    });
    console.log(this.state);
  };

  componentDidMount = () => {
    this.getData();
  };

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
    //       <Card.Title>raw team ranking data</Card.Title>
    //       <Card.Text>
    //         <img className="img-format" src={this.state.rawTeamImg} />
    //         <Card className="text-center">
    //           <Card.Header>After ETL</Card.Header>
    //           <Card.Body>
    //             <Card.Title>clean team ranking data</Card.Title>
    //             <Card.Text>
    //               <img
    //                 className="img-format"
    //                 src={this.state.cleanTeamImg}
    //               />
    //             </Card.Text>
    //           </Card.Body>
    //         </Card>
    //       </Card.Text>
    //     </Card.Body>
    //   </Card>
    // );
  }
}

export default TeamRankingSummaryPage;
