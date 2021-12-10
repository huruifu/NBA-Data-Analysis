# ETL Process:

* spark-submit data_etl/injuries_etl.py data/NBA/injuries_2010-2020.csv outputs (running file: data_etl/injuries_etl.py, input: data/NBA/injuries_2010-2020.csv, output: outputs, performing Injury Dataset ETL Process)

* spark-submit data_etl/player_etl.py data/NBA/2017-Player-Info.csv data/NBA/2018-2019-Player-Info.csv data/NBA/2019-2020-Player-Info.csv data/NBA/2020-2021-Player-Info.csv data/NBA/all_seasons.csv data/NBA/all_seasons.csv data/NBA/players.csv outputs (running file: data_etl/player_etl.py, inputs: data/NBA/2017-Player-Info.csv data/NBA/2018-2019-Player-Info.csv data/NBA/2019-2020-Player-Info.csv data/NBA/2020-2021-Player-Info.csv data/NBA/all_seasons.csv data/NBA/all_seasons.csv data/NBA/players.csv, output: outputs, performing player general info ETL Process)

* spark-submit data_etl/team_summary_etl.py data/nba/games.csv data/etl_team_summary_output
(Running file: data_etl/team_summary_etl.py , Input: data/nba/games.csv, output:data/etl_team_summary_output, get team’s yearly stats)

* spark-submit data_etl/nba_salary_etl.py data/nba/salary_1985to2018.csv data/nba/players_for_salary.csv data/etl_player_summary_output_noTeam data/clean_data/player_info.csv data/nba/injuries_2010-2020.csv data/clean_data/salary_etl
(Running file:data_etl/nba_salary_etl.py, Input:data/nba/salary_1985to2018.csv data/nba/players_for_salary.csv data/etl_player_summary_output_noTeam data/clean_data/player_info.csv data/nba/injuries_2010-2020.csv, Output: data/clean_data/salary_etl, ETL: salary data)

* spark-submit data_etl/team_ranking_etl.py data/nba/ranking.csv data/clean_data/etl_team_rank_output
(running file: data_etl/team_ranking_etl.py , Input: data/nba/ranking.csv, output:data/clean_data/etl_team_rank_output, performing the team ranking Dataset ETL process)



# Data Analytics:

## Age & Injury On Player's stat

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

* spark-submit data_etl/nba_etl_player_summary.py data/nba/games.csv data/nba/games_details.csv data/etl_player_summary_output data/etl_player_summary_output_noTeam data/etl_player_summary_justRegular
(Running file:data_etl/nba_etl_player_summary.py, Input: data/nba/games.csv data/nba/games_details.csv, Output: data/etl_player_summary_output data/etl_player_summary_output_noTeam data/etl_player_summary_justRegular, ETL: get player's scores, game durations and play times by year and team)

* spark-submit data_etl/team_ranking_etl.py data/nba/ranking.csv data/clean_data/etl_team_rank_output
(running file: data_etl/team_ranking_etl.py , Input: data/nba/ranking.csv, output:data/clean_data/etl_team_rank_output, performing the team ranking Dataset ETL process)




## MVP, ALL NBA Team and Champion 

* spark-submit data_analytics/model/mvp_analysis.py data/etl_player_summary_justRegular data/clean_data/player_info.csv data/etl_team_summary_output data/clean_data/etl_team_rank_output
(Running file: data_analytics/model/mvp_analysis.py , Input: data/etl_player_summary_justRegular, data/clean_data/player_info.csv, data/etl_team_summary_output, data/clean_data/etl_team_rank_output, Analyze the most influential factor in the selection of MVP)

* spark-submit data_analytics/model/all_nba_team_analysis.py data/etl_player_summary_justRegular data/clean_data/player_info.csv data/etl_team_summary_output data/clean_data/etl_team_rank_output
(Running file: data_analytics/model/mvp_analysis.py , Input: data/etl_player_summary_justRegulardata/clean_data/player_info.csv, data/etl_team_summary_output, data/clean_data/etl_team_rank_output, Analyze the most influential factor in the selection of all nba team)

* spark-submit data_analytics/model/champion_analysis.py data/etl_team_summary_output data/clean_data/etl_team_rank_output
(Running file: data_analytics/model/mvp_analysis.py , Input: data/etl_team_summary_output, data/clean_data/etl_team_rank_output, Find the key feature of championship based on the team regular season performance)

## Salary Analytics

* spark-submit data_analytics/nba_salary_analysis.py data/clean_data/salary_etl
(Running file:data_analytics/nba_salary_analysis.py, Input:data/clean_data/salary_etl, Analyze and predict on salary)

## Data Analytics on exploring new player's model players

* spark-submit data_analytics/newplayer_prepare.py data/clean_data/player_info.csv data/etl_player_summary_output data/input_summary
(running file: data_analytics/newplayer_prepare.py , Input: data/clean_data/player_info.csv, Output: data/etl_player_summary_output data/input_summary, joining the information of player’s physical conditions and the information of player’s NBA performance prepared for further analysis)

* python data_analytics/new_player_analysis.py data/etl_player_summary_output data/input_summary data/new_players & top_100 players/players.txt "Orlando Johnson" data_analytics/new_player_output
(running file: data_analytics/new_player_analysis.py, Input: data/etl_player_summary_output data/input_summary; data/new_players_&_top_100_players/players.txt; and an new player name from list data/new_players_&_top_100_players/new_players.txt eg: "Orlando Johnson", Output:data_analytics/new_player_output, generate several different plot within dictionary new_player_output and also print the professional names who are closest to the new player we put in using different input groups)



# Web Application

In order to run the web application on the local computers, there are following steps needed to do.

* If you do not have node or npm, download node and npm.

* Go to web-presentation/front-end folder.

* In you terminal or windows console, run npm install.

* npm start

These four steps will able to run the web application.
