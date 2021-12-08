import React, { Component } from "react";
import Spinner from "react-bootstrap/Spinner";
import BootstrapTable from "react-bootstrap-table-next";
import paginationFactory from "react-bootstrap-table2-paginator";
import Card from "react-bootstrap/Card";

import { getDatabase, ref, onValue, value } from "firebase/database";
import "./playerInfoSummaryPage.css";

class PlayerInfoSummaryPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      allSeasonImg: "/etlImages/allSeason.png",
      playerBefore2017Img: "/etlImages/playerBefore2017.png",
      player2018Img: "/etlImages/player_2018.png",
      player2019Img: "/etlImages/player_2019.png",
      player2020Img: "/etlImages/player_2020.png",
      playerInfoImg: "/etlImages/playerInfo.png",
      columns: [
        { dataField: "season", text: "season" },
        { dataField: "team_abbreviation", text: "team" },
        { dataField: "PLAYER_ID", text: "PLAYER_ID" },
        { dataField: "player_name", text: "player name" },
        { dataField: "age", text: "age" },
        { dataField: "draft_number", text: "draft_number" },
        { dataField: "draft_round", text: "draft_round" },
        { dataField: "draft_year", text: "draft_year" },
        { dataField: "player_height", text: "player_height" },
        { dataField: "player_position", text: "player_position" },
        { dataField: "player_weight", text: "player_weight" },
      ],
    }
  }

  getData = () => {
    let db = getDatabase();
    let playerSummaryRef = ref(db, "player-summary");
    onValue(playerSummaryRef, (snapshot) => {
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
    //       <Card.Title>raw player info data</Card.Title>
    //       <Card.Text>
    //         <img className="img-format" src={this.state.playerBefore2017Img} />
    //         <img className="img-format" src={this.state.player2018Img} />
    //         <img className="img-format" src={this.state.player2019Img} />
    //         <img className="img-format" src={this.state.player2020Img} />
    //         <Card className="text-center">
    //           {/* <Card.Header>After ETL</Card.Header> */}
    //           <Card.Body>
    //             <Card.Title>raw all season data</Card.Title>
    //             <Card.Text>
    //               <img className="img-format" src={this.state.allSeasonImg} />
    //               <Card className="text-center">
    //           <Card.Header>After ETL</Card.Header>
    //           <Card.Body>
    //             <Card.Title>clean player info</Card.Title>
    //             <Card.Text>
    //               <img className="img-format" src={this.state.playerInfoImg} />
    //             </Card.Text>
    //           </Card.Body>
    //         </Card>
    //             </Card.Text>
    //           </Card.Body>
    //         </Card>
    //       </Card.Text>
    //     </Card.Body>
    //   </Card>
    // );
  }
}

export default PlayerInfoSummaryPage;
