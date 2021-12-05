import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

import "./App.css";

// import components
import MainNavigation from "./components/mainNavigation/mainNavigation";

// import pages
import HomePage from "./pages/homePage/homePage";
import AgeInjuryPlayerPage from "./pages/ageInjuryPlayerPage/ageInjuryPlayerPage";
import SalaryPage from "./pages/salaryPage/salaryPage";
import NewPlayerPage from "./pages/newPlayerPage/newPlayerPage";
import MVPAllNBATeamPage from "./pages/mvpAllNBATeamPage/mvpAllNBATeamPage";
import ChampionPage from "./pages/championPage/championPage";
import TeamAbilitySummaryPage from "./pages/teamAbilitySummaryPage/teamAbilitySummaryPage";
import TeamRankingSummaryPage from "./pages/teamRankingSummaryPage/teamRankingSummaryPage";
import PlayerSalarySummary from "./pages/playerSalarySummaryPage/playerSalarySummaryPage";
import PlayerInjurySummaryPage from "./pages/playerInjurySummaryPage/playerInjurySummaryPage";
import PlayerStatSummaryPage from "./pages/playerStatSummaryPage/playerStatSummaryPage";
import PlayerInfoSummaryPage from "./pages/playerInfoSummaryPage/playerInfoSummaryPage";

class App extends Component {
  render() {
    return (
      <div>
        <MainNavigation />
        <div className="componentPosition">
        <Switch>
          <Route path="/" exact={true}>
            <HomePage />
          </Route>
          <Route path="/etl/team-ability">
            <TeamAbilitySummaryPage />
          </Route>
          <Route path="/etl/team-ranking">
            <TeamRankingSummaryPage />
          </Route>
          <Route path="/etl/salary">
            <PlayerSalarySummary />
          </Route>
          <Route path="/etl/injury">
            <PlayerInjurySummaryPage />
          </Route>
          <Route path="/etl/player-stat-summary">
            <PlayerStatSummaryPage />
          </Route>
          <Route path="/etl/player-info-summary">
            <PlayerInfoSummaryPage />
          </Route>
          <Route path="/new-player">
            <NewPlayerPage />
          </Route>
          <Route path="/mvp-nba-all-team">
            <MVPAllNBATeamPage />
          </Route>
          <Route path="/champion">
            <ChampionPage />
          </Route>
          <Route path="/injury-age">
            <AgeInjuryPlayerPage />
          </Route>
          <Route path="/salary">
            <SalaryPage />
          </Route>
        </Switch>
        </div>
      </div>
    );
  }
}

export default App;
