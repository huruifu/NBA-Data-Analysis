import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

import "./App.css";

// import components
import MainNavigation from "./components/mainNavigation/mainNavigation";

// import pages
import HomePage from "./pages/homePage/homePage";
import AgeInjuryPlayerPage from "./pages/ageInjuryPlayerPage/ageInjuryPlayerPage";
import SalaryPage from "./pages/salaryPage/salaryPage";
import TeamAbilitySummaryPage from "./pages/teamAbilitySummaryPage/teamAbilitySummaryPage";

class App extends React.Component {
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
