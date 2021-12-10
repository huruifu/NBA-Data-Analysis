# ETL Process:

* spark-submit data_etl/injuries_etl.py data/NBA/injuries_2010-2020.csv outputs (running file: data_etl/injuries_etl.py, input: data/NBA/injuries_2010-2020.csv, output: outputs, performing Injury Dataset ETL Process)

* spark-submit data_etl/player_etl.py data/NBA/2017-Player-Info.csv data/NBA/2018-2019-Player-Info.csv data/NBA/2019-2020-Player-Info.csv data/NBA/2020-2021-Player-Info.csv data/NBA/all_seasons.csv data/NBA/all_seasons.csv data/NBA/players.csv outputs (running file: data_etl/player_etl.py, inputs: data/NBA/2017-Player-Info.csv data/NBA/2018-2019-Player-Info.csv data/NBA/2019-2020-Player-Info.csv data/NBA/2020-2021-Player-Info.csv data/NBA/all_seasons.csv data/NBA/all_seasons.csv data/NBA/players.csv, output: outputs, performing player general info ETL Process)


# Data Analytics:

* spark-submit data_analytics/injuries/most_injury_player.py data/clean_data/clean_injuries.csv (running file: data_analytics/injuries/most_injury_player.py, input: data/clean_data/clean_injuries.csv, plotting graph about players who get injury most)

* spark-submit data_analytics/injuries/most_injury_team.py data/clean_data/clean_injuries.csv (running file: data_analytics/injuries/most_injury_team.py, input: data/clean_data/clean_injuries.csv, plotting graph about teams which suffer the most injury events)

* spark-submit data_analytics/injuries/injuries_player_info_stat_join.py data/clean_data/clean_injuries.csv data/etl_player_summary_justRegular data/clean_data/player_info.csv outputs (running file: data_analytics/injuries/injuries_player_info_stat_join.py, inputs: data/clean_data/clean_injuries.csv data/etl_player_summary_justRegular data/clean_data/player_info.csv, output: outputs, joining three dataset together to generate dataset that needed to make analysis on age and injury)

* spark-submit data_analytics/injuries/injuries_types.py data/clean_data/clean_injuries.csv data/clean_data/player_info.csv (running file: data_analytics/injuries/injuries_types.py, inputs: data/clean_data/clean_injuries.csv data/clean_data/player_info.csv, generating plots about the frequency types of each injury type in each player positions)

* spark-submit data_analytics/injuries/nextSeasonAvgPtsModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgPtsModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average points, and save the model)

* spark-submit data_analytics/injuries/nextSeasonAvgStlModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgStlModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average steals, and save the model)

* spark-submit data_analytics/injuries/nextSeasonAvgAstModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgAstModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average assists, and save the model)

* spark-submit data_analytics/injuries/nextSeasonAvgBlkModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgBlkModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average blocks, and save the model)

* spark-submit data_analytics/injuries/nextSeasonAvgDrebModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgDrebModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average defensive rebounds, and save the model)

* spark-submit data_analytics/injuries/nextSeasonAvgOrebModel.py data_analytics/injuries/dataset/player.csv outputs (running file: data_analytics/injuries/nextSeasonAvgOrebModel.py input: data_analytics/injuries/dataset/player.csv output: outputs, training model to predict next season average ofensive rebounds, and save the model)




# Web Application

In order to run the web application on the local computers, there are following steps needed to do.

* If you do not have node or npm, download node and npm.

* Go to web-presentation/front-end folder.

* In you terminal or windows console, run npm install.

* npm start

These four steps will able to run the web application.
