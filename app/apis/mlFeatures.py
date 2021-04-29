def engineer_ml_dataset_features():
    """
        This function prepares training dataset and
        testing dataset
        
        Features applicable for the ML classification is engineered 
        primarily in SQL keeping the project purpose of database system 
        in mind. 
        
        The heavy lifting of this ML program is choosing right dataset and 
        normalizing them to suitable features. This is done via SQL and as 
        DB tables
        
        Training dataset: Baseline of the ML model is coming from the 
         table ml_team_stats. This table is the built from set of 3 intermediate tables all of them with
         very high cardinality > 50k records
         
         Prediction dataset: This is the variable dataset driven by users selection fantasy team from the
         front end      
         
    """
    
    query_team_baseline = " select * from ml_team_stats"
    
    query_fant_team_field_stat = """
                                    select  fantasyteamid,teamname, 
                                           avg(po_per_game) as po_per_game,
                                           avg(a_per_game) as a_per_game, 
                                           avg(e_per_game) as e_per_game, -- lots of 0s
                                           avg(dp_per_game) as dp_per_game
                                    from  (select   fts.fantasyteamid,fts.teamname, 
                                                    bss.playerid,bss.yearid,
                                                           sum(g) as g, sum(po) as po, 
                                                           sum(a) as a, 
                                                           sum(e) as e, 
                                                           sum(dp) as dp,
                                                           sum(po) / sum(g) as po_per_game,
                                                           sum(a) / sum(g) as a_per_game, 
                                                           sum(e) / sum(g) as  e_per_game, 
                                                           sum(dp) / sum(g) as  dp_per_game
                                             from (select ft.fantasyteamid,ft.teamname, 
                                                          ftp.playerid 
                                                   from fantasy_team ft,
                                                        fantasy_team_players ftp
                                                    where ft.fantasyteamid = ftp.fantasyteamid and 
                                                          ft.fantasyteamid = %(fantasy_team_id)s

                                                         ) fts,
                                                        fielding_season_stat bss
                                             where fts.playerid = bss.playerid
                                             group by fts.fantasyteamid,fts.teamname, 
                                                      bss.playerid,bss.yearid
                                            ) cte_team_stats
                                    group by  fantasyteamid,teamname ;


                                    """

    query_fant_team_batting_stat = """

                    select  fantasyteamid,teamname, 
                               avg(r_per_game) as r_per_game,
                               avg(ab_per_game) as ab_per_game, 
                               avg(h_per_game) as h_per_game,
                               avg(b2_per_game) as b2_per_game, 
                               avg(b3_per_game) as b3_per_game, 
                               avg(hr_per_game) as hr_per_game,
                               avg(rbi_per_game) as rbi_per_game,
                               avg(sb_per_game) as sb_per_game, 
                               avg(cs_per_game) as cs_per_game,
                               avg(bb_per_game) as bb_per_game,
                               avg(so_per_game) as so_per_game, 
                               avg(hbp_per_game) as hbp_per_game
                    from (
                                      select   fts.fantasyteamid,fts.teamname, 
                                               bss.playerid,bss.year,fts.pos,
                                               g,
                                               batting_r / g as r_per_game, 
                                               ab/g as ab_per_game, batting_h/g as h_per_game,
                                               b2/g as b2_per_game, b3/g as b3_per_game, 
                                               batting_hr/g as hr_per_game,
                                               rbi/g as rbi_per_game,
                                               sb/g as sb_per_game, 
                                               cs/g as cs_per_game,
                                               batting_bb / g as bb_per_game,
                                               batting_so/g as so_per_game, 
                                              cast(hbp as unsigned)/g as hbp_per_game 
                                        from  (select ft.fantasyteamid,ft.teamname, 
                                                          ftp.playerid,pp.pos 
                                                    from fantasy_team ft,
                                                         fantasy_team_players ftp,
                                                         vw_players_position pp
                                                    where ft.fantasyteamid = ftp.fantasyteamid and 
                                                          ft.fantasyteamid = %(fantasy_team_id)s and 
                                                          ftp.playerid = pp.playerid and
                                                          pp.pos <> 'p'
                                                   ) fts,
                                             batting_season_stat bss
                                        where fts.playerid = bss.playerid
                                             ) cte_team_stats
                        group by  fantasyteamid,teamname ;


                    """
    query_fant_team_pitching_stat = """

            select  fantasyteamid,teamname, 
                   avg(pitching_h_per_game) as pitching_h_per_game,
                   avg(er_per_game) as er_per_game, 
                   avg(pitching_hr_per_game) as pitching_hr_per_game,
                   avg(pitching_bb_per_game) as pitching_bb_per_game, 
                   avg(pitching_so_per_game) as pitching_so_per_game, 
                   avg(era_per_game) as era_per_game,
                   avg(ibb_per_game) as ibb_per_game,
                   avg(pitching_r_per_game) as pitching_r_per_game
            from (
                          select   fts.fantasyteamid,fts.teamname, 
                                   bss.playerid,bss.year,fts.pos,
                                   g,
                                  pitching_h / g as pitching_h_per_game,
                                  er/g as er_per_game, 
                                  pitching_hr / g as pitching_hr_per_game,
                                  pitching_bb / g as pitching_bb_per_game,
                                  pitching_so / g as pitching_so_per_game,
                                  era/g as era_per_game, 
                                  ibb / g as ibb_per_game,
                                  pitching_r /  g as pitching_r_per_game

                            from (select ft.fantasyteamid,ft.teamname, 
                                              ftp.playerid,pp.pos 
                                        from fantasy_team ft,
                                             fantasy_team_players ftp,
                                             vw_players_position pp
                                        where ft.fantasyteamid = ftp.fantasyteamid and 
                                              ft.fantasyteamid = %(fantasy_team_id)s and 
                                              ftp.playerid = pp.playerid and
                                              pp.pos = 'p'
                                       ) fts,
                                 pitching_season_stat bss
                            where fts.playerid = bss.playerid
                                 )cte_team_stats
            group by  fantasyteamid,teamname ;

        """
    
    return query_team_baseline, query_fant_team_field_stat, query_fant_team_batting_stat, query_fant_team_pitching_stat 

