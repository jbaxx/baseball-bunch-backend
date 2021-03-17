-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 16, 2021 at 09:58 PM
-- Server version: 10.3.28-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs411baseball_db`
--

USE fantasy;

-- --------------------------------------------------------

--
-- Table structure for table `teams_franchises`
--

DROP TABLE IF EXISTS `teams_franchises`;
CREATE TABLE IF NOT EXISTS `teams_franchises` (
`franchID`   varchar(8) DEFAULT NULL,
`franchName` varchar(33) DEFAULT NULL,
`active`     varchar(6) DEFAULT NULL,
`NAassoc`    varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `teams_franchises`
--

INSERT INTO `teams_franchises` (`franchID`, `franchName`, `active`, `NAassoc`) VALUES
('ALT', 'Altoona Mountain City', 'N', ''),
('ANA', 'Los Angeles Angels of Anaheim', 'Y', ''),
('ARI', 'Arizona Diamondbacks', 'Y', ''),
('ATH', 'Philadelphia Athletics', 'N', 'PNA'),
('ATL', 'Atlanta Braves', 'Y', 'BNA'),
('BAL', 'Baltimore Orioles', 'Y', ''),
('BFB', 'Buffalo Bisons', 'N', ''),
('BFL', 'Buffalo Bisons', 'N', ''),
('BLC', 'Baltimore Canaries', 'NA', ''),
('BLO', 'Baltimore Orioles', 'N', ''),
('BLT', 'Baltimore Terrapins', 'N', ''),
('BLU', 'Baltimore Monumentals', 'N', ''),
('BNA', 'Boston Red Stockings', 'NA', 'ATL'),
('BOS', 'Boston Red Sox', 'Y', ''),
('BRA', 'Brooklyn Atlantics', 'NA', ''),
('BRD', 'Boston Reds', 'N', ''),
('BRG', 'Brooklyn Gladiators', 'N', ''),
('BRS', 'Boston Reds', 'N', ''),
('BTT', 'Brooklyn Tip-Tops', 'N', ''),
('BUF', 'Buffalo Bisons', 'N', ''),
('BWW', 'Brooklyn Ward\'s Wonders', 'N', ''),
('CBK', 'Columbus Buckeyes', 'N', ''),
('CBL', 'Cleveland Blues', 'N', ''),
('CEN', 'Philadelphia Centennials', 'NA', ''),
('CFC', 'Cleveland Forest Citys', 'NA', ''),
('CHC', 'Chicago Cubs', 'Y', 'CNA'),
('CHH', 'Chicago Whales', 'N', ''),
('CHP', 'Chicago Pirates', 'N', ''),
('CHW', 'Chicago White Sox', 'Y', ''),
('CIN', 'Cincinnati Reds', 'Y', ''),
('CKK', 'Cincinnati Kelly\'s Killers', 'N', ''),
('CLE', 'Cleveland Indians', 'Y', ''),
('CLI', 'Cleveland Infants', 'N', ''),
('CLS', 'Columbus Solons', 'N', ''),
('CLV', 'Cleveland Spiders', 'N', ''),
('CNA', 'Chicago White Stockings', 'NA', 'CHC'),
('CNR', 'Cincinnati Reds', 'N', ''),
('COL', 'Colorado Rockies', 'Y', ''),
('COR', 'Cincinnati Outlaw Reds', 'N', ''),
('CPI', 'Chicago/Pittsburgh (Union League)', 'N', ''),
('DET', 'Detroit Tigers', 'Y', ''),
('DTN', 'Detroit Wolverines', 'N', ''),
('ECK', 'Brooklyn Eckfords', 'NA', ''),
('FLA', 'Florida Marlins', 'Y', ''),
('HAR', 'Hartford Dark Blues', 'N', 'HNA'),
('HNA', 'Hartford Dark Blues', 'NA', 'HAR'),
('HOU', 'Houston Astros', 'Y', ''),
('IBL', 'Indianapolis Blues', 'N', ''),
('IHO', 'Indianapolis Hoosiers', 'N', ''),
('IND', 'Indianapolis Hoosiers', 'N', ''),
('KCC', 'Kansas City Cowboys', 'N', ''),
('KCN', 'Kansas City Cowboys', 'N', ''),
('KCP', 'Kansas City Packers', 'N', ''),
('KCR', 'Kansas City Royals', 'Y', ''),
('KCU', 'Kansas City Cowboys', 'N', ''),
('KEK', 'Fort Wayne Kekiongas', 'NA', ''),
('LAD', 'Los Angeles Dodgers', 'Y', ''),
('LGR', 'Louisville Grays', 'N', ''),
('LOU', 'Louisville Colonels', 'N', ''),
('MAN', 'Middletown Mansfields', 'NA', ''),
('MAR', 'Baltimore Marylands', 'NA', ''),
('MIL', 'Milwaukee Brewers', 'Y', ''),
('MIN', 'Minnesota Twins', 'Y', ''),
('MLA', 'Milwaukee Brewers', 'N', ''),
('MLG', 'Milwaukee Grays', 'N', ''),
('MLU', 'Milwaukee Brewers', 'N', ''),
('NAT', 'Washington Nationals', 'NA', ''),
('NEW', 'Newark Pepper', 'N', ''),
('NHV', 'New Haven Elm Citys', 'NA', ''),
('NNA', 'New York Mutuals', 'NA', 'NYU'),
('NYI', 'New York Giants', 'N', ''),
('NYM', 'New York Mets', 'Y', ''),
('NYP', 'New York Metropolitans', 'N', ''),
('NYU', 'New York Mutuals', 'N', 'NNA'),
('NYY', 'New York Yankees', 'Y', ''),
('OAK', 'Oakland Athletics', 'Y', ''),
('OLY', 'Washington Olympics', 'NA', ''),
('PBB', 'Pittsburgh Burghers', 'N', ''),
('PBS', 'Pittsburgh Rebels', 'N', ''),
('PHA', 'Philadelphia Athletics', 'N', ''),
('PHI', 'Philadelphia Phillies', 'Y', ''),
('PHK', 'Philadelphia Keystones', 'N', ''),
('PHQ', 'Philadelphia Athletics', 'N', ''),
('PIT', 'Pittsburgh Pirates', 'Y', ''),
('PNA', 'Philadelphia Athletics', 'NA', 'ATH'),
('PRO', 'Providence Grays', 'N', ''),
('PWS', 'Philadelphia White Stockings', 'NA', ''),
('RES', 'Elizabeth Resolutes', 'NA', ''),
('RIC', 'Richmond Virginians', 'N', ''),
('ROC', 'Rochester Broncos', 'N', ''),
('ROK', 'Rockford Forest Citys', 'NA', ''),
('SBS', 'St. Louis Brown Stockings', 'N', 'SNA'),
('SDP', 'San Diego Padres', 'Y', ''),
('SEA', 'Seattle Mariners', 'Y', ''),
('SFG', 'San Francisco Giants', 'Y', ''),
('SLI', 'St. Louis Terriers', 'N', ''),
('SLM', 'St. Louis Maroons', 'N', ''),
('SLR', 'St. Louis Red Stockings', 'NA', ''),
('SNA', 'St. Louis Brown Stockings', 'NA', 'SBS'),
('STL', 'St. Louis Cardinals', 'Y', ''),
('STP', 'St. Paul Apostles', 'N', ''),
('SYR', 'Syracuse Stars', 'N', ''),
('SYS', 'Syracuse Stars', 'N', ''),
('TBD', 'Tampa Bay Rays', 'Y', ''),
('TEX', 'Texas Rangers', 'Y', ''),
('TLM', 'Toledo Maumees', 'N', ''),
('TOL', 'Toledo Blue Stockings', 'N', ''),
('TOR', 'Toronto Blue Jays', 'Y', ''),
('TRO', 'Troy Haymakers', 'NA', ''),
('TRT', 'Troy Trojans', 'N', ''),
('WAS', 'Washington Senators', 'N', ''),
('WBL', 'Washington Blue Legs', 'NA', ''),
('WES', 'Keokuk Westerns', 'NA', ''),
('WIL', 'Wilmington Quicksteps', 'N', ''),
('WNA', 'Washington Nationals', 'N', ''),
('WNL', 'Washington Nationals', 'N', ''),
('WNT', 'Washington Nationals', 'NA', ''),
('WOR', 'Worcester Ruby Legs', 'N', ''),
('WSN', 'Washington Nationals', 'Y', ''),
('WST', 'Washington Statesmen', 'N', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
