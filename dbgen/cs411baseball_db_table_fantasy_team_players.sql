
-- --------------------------------------------------------

USE cs411baseball_db;

--
-- Table structure for table `fantasy_team_players`
--

DROP TABLE IF EXISTS `fantasy_team_players`;
CREATE TABLE IF NOT EXISTS `fantasy_team_players` (
  `fantasyteamid` mediumint(9) DEFAULT NULL,
  `playerid` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
