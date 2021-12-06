import React, { Component } from "react";
import Spinner from "react-bootstrap/Spinner";
import BootstrapTable from "react-bootstrap-table-next";
import paginationFactory from "react-bootstrap-table2-paginator";

import Card from "react-bootstrap/Card";

import { getDatabase, ref, onValue, value } from "firebase/database";
import "./teamAbilitySummaryPage.css";

class TeamAbilitySummaryPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      imgPaths: [
        { path: "/etlImages/game.png", description: "raw game data" },
        {
          path: "/etlImages/teamAbility.png",
          description: "after etl, team ability data",
        },
      ],
      gameImgPath: "/etlImages/game.png",
      teamAbilityImgPath: "/etlImages/teamAbility.png",
      columns: [
        { dataField: "year", text: "Season", sort: true },
        { dataField: "TEAM_ID", text: "TEAM_ID",  },
        { dataField: "avg_AST_away", text: "avg_AST_away", sort: true },
        { dataField: "avg_AST_home", text: "avg_AST_home", sort: true },
        { dataField: "avg_PTS_away", text: "avg_PTS_away", sort: true },
        { dataField: "avg_PTS_home", text: "avg_PTS_home", sort: true },
        { dataField: "avg_REB_away", text: "avg_REB_away", sort: true },
        { dataField: "avg_REB_home", text: "avg_REB_home", sort: true },
      ],
    };
  }

  getData = () => {
    let db = getDatabase();
    let abilityRef = ref(db, "team-ability");
    onValue(abilityRef, (snapshot) => {
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
    //       <Card.Title>raw data from game.csv</Card.Title>
    //       <Card.Text>
    //         <img className="img-format" src={this.state.gameImgPath} />
    //         <Card className="text-center">
    //           <Card.Header>After ETL</Card.Header>
    //           <Card.Body>
    //             <Card.Title>Team Ability Summary</Card.Title>
    //             <Card.Text>
    //               <img className="img-format" src={this.state.teamAbilityImgPath} />
    //             </Card.Text>
    //           </Card.Body>
    //         </Card>
    //       </Card.Text>
    //     </Card.Body>
    //   </Card>
    // );
  }
}

export default TeamAbilitySummaryPage;
