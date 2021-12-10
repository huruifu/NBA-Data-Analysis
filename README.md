# NBA Data Analytics

As NBA Team managers, there are a lot of things needed to be concerned. They need to keep the teams' salary cap, and also maintain teams' competitiveness. In addition, they need to explore young players' potential. The goal of this project is to use Big Data tools to manage different kinds of NBA dataset and perform data analytics in order to explore information and prediction models that are useful to NBA Team managers. 

In the project, four topics will be analysed. These four topics are important to team managers since exploring these four topics can help team managers to keep the teams' salary cap, maintain teams' competitiveness and also find potential young players.

* It is known that age and injuries can affect players’ ability, but it is not clear how exactly age and injuries influence players’ ability. We will use the dataset about the NBA players injury history and NBA game details data in the last 10 years to get models about how players’ age and all kinds of injury affect players’ average points, steals, rebounds, assists.

* Using last 10 years NBA teams and players data to explore models that can predict champion, MVP, ALL-NBA Teams.

* Using Machine Learning algorithm to explore the new young players' potential, and find the future model players to them.

* Finding models that can predict players' salary.

The dataset used in this project come from following sources.

* https://www.kaggle.com/nathanlauga/nba-games

* https://www.kaggle.com/buyuknacar/active-nba-players-10-year-injury-history

* https://www.basketball-reference.com/contracts/players.html

* https://www.nbastuffer.com/player-stats/

* https://data.world/datadavis/nba-salaries/workspace/file?filename=salaries_1985to2018.csv

* https://www.si.com/nba/2020/12/14/top-100-nba-players-2021-daily-cover


Inside folder data_etl, there are files about performing etl in order to get clean data.

After performing etl process, the cleaned dataset will be stored in Firebase, which is a nosql database hosted by Google.

Inside folder data_analytics, there are files about performing data analytics on the four topics this project focuses on.

A detail description on how to run all codes in the project is in RUNNING.md

A web application is also designed to present the results of the project. The web application is implemented by using React libray, and connect to the Firebase which stores the cleaned dataset.

In order to run the web application on the local computers, there are following steps needed to do.

* If you do not have node or npm, download node and npm.

* Go to web-presentation/front-end folder.

* In you terminal or windows console, run npm install.

* npm start

These four steps will able to run the web application.







