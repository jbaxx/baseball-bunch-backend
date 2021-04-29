#!/bin/bash

echo cs411baseball_db_database.sql
mysql -u $USER_NAME -p < cs411baseball_db_database.sql
echo cs411baseball_db_table_batting_season_stat.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_batting_season_stat.sql
echo cs411baseball_db_table_fantasy_team.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_fantasy_team.sql
echo cs411baseball_db_table_fantasy_team_players.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_fantasy_team_players.sql
echo cs411baseball_db_table_pitching_season_stat.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_pitching_season_stat.sql
echo cs411baseball_db_table_players.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_players.sql
echo cs411baseball_db_table_teams.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_teams.sql
echo cs411baseball_db_table_teams_franchises.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_teams_franchises.sql
echo cs411baseball_db_table_teams_half.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_teams_half.sql
echo cs411baseball_db_table_users.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_users.sql
echo cs411baseball_db_table_users.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_users.sql
echo cs411baseball_db_table_players_position.sql
mysql -u $USER_NAME -p < cs411baseball_db_table_players_position.sql
echo cs411baseball_db_view_vw_players_position.sql
mysql -u $USER_NAME -p < cs411baseball_db_view_vw_players_position.sql
echo ml_team_batting_stats.sql
mysql -u $USER_NAME -p < ml_team_batting_stats.sql
echo ml_team_fielding_stats.sql
mysql -u $USER_NAME -p < ml_team_fielding_stats.sql
echo ml_team_pitching_stats.sql
mysql -u $USER_NAME -p < ml_team_pitching_stats.sql
echo ml_team_stats.sql
mysql -u $USER_NAME -p < ml_team_stats.sql
echo ml_teamfranch.sql
mysql -u $USER_NAME -p < ml_teamfranch.sql
echo ml_teams.sql
mysql -u $USER_NAME -p < ml_teams.sql
echo fielding_season_stat.sql
mysql -u $USER_NAME -p < fielding_season_stat.sql
