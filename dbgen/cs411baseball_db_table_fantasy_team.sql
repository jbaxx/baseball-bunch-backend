
-- --------------------------------------------------------

USE cs411baseball_db;

--
-- Table structure for table `fantasy_team`
--


DROP TABLE IF EXISTS `fantasy_team`;
CREATE TABLE IF NOT EXISTS `fantasy_team` (
  `fantasyteamid` mediumint(9) NOT NULL AUTO_INCREMENT,
  `teamname` varchar(50) NOT NULL,
  `userid` mediumint(9) NOT NULL,
  PRIMARY KEY (`fantasyteamid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
