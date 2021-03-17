-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 16, 2021 at 09:59 PM
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
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
CREATE TABLE IF NOT EXISTS `players` (
`playerID`     varchar(9) DEFAULT NULL,
`birthYear`    varchar(9) DEFAULT NULL,
`birthMonth`   varchar(10) DEFAULT NULL,
`birthDay`     varchar(8) DEFAULT NULL,
`birthCountry` varchar(14) DEFAULT NULL,
`birthState`   varchar(22) DEFAULT NULL,
`birthCity`    varchar(26) DEFAULT NULL,
`deathYear`    varchar(9) DEFAULT NULL,
`deathMonth`   varchar(10) DEFAULT NULL,
`deathDay`     varchar(8) DEFAULT NULL,
`deathCountry` varchar(14) DEFAULT NULL,
`deathState`   varchar(20) DEFAULT NULL,
`deathCity`    varchar(26) DEFAULT NULL,
`nameFirst`    varchar(14) DEFAULT NULL,
`nameLast`     varchar(14) DEFAULT NULL,
`nameGiven`    varchar(43) DEFAULT NULL,
`weight`       varchar(6) DEFAULT NULL,
`height`       varchar(6) DEFAULT NULL,
`bats`         varchar(4) DEFAULT NULL,
`throws`       varchar(6) DEFAULT NULL,
`debut`        varchar(10) DEFAULT NULL,
`finalGame`    varchar(10) DEFAULT NULL,
`retroID`      varchar(8) DEFAULT NULL,
`bbrefID`      varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`playerID`, `birthYear`, `birthMonth`, `birthDay`, `birthCountry`, `birthState`, `birthCity`, `deathYear`, `deathMonth`, `deathDay`, `deathCountry`, `deathState`, `deathCity`, `nameFirst`, `nameLast`, `nameGiven`, `weight`, `height`, `bats`, `throws`, `debut`, `finalGame`, `retroID`, `bbrefID`) VALUES
('washbge01', '1914', '10', '6', 'USA', 'ME', 'Solon', '1979', '1', '5', 'USA', 'LA', 'Baton Rouge', 'George', 'Washburn', 'George Edward', '175', '73', 'L', 'R', '1941-05-04', '1941-05-04', 'washg103', 'washbge01'),
('washbgr01', '1946', '12', '3', 'USA', 'IL', 'Coal City', '', '', '', '', '', '', 'Greg', 'Washburn', 'Gregory James', '190', '72', 'R', 'R', '1969-06-07', '1969-09-21', 'washg101', 'washbgr01'),
('washbja01', '1974', '8', '13', 'USA', 'WI', 'La Crosse', '', '', '', '', '', '', 'Jarrod', 'Washburn', 'Jarrod Michael', '190', '73', 'L', 'L', '1998-06-02', '2009-09-15', 'washj001', 'washbja01'),
('washbli01', '1874', '6', '16', 'USA', 'NH', 'Lynn', '1940', '3', '22', 'USA', 'NY', 'Malone', 'Libe', 'Washburn', 'Libeus', '180', '70', 'B', 'L', '1902-05-30', '1903-07-17', 'washl102', 'washbli01'),
('washbra01', '1938', '5', '31', 'USA', 'WA', 'Pasco', '', '', '', '', '', '', 'Ray', 'Washburn', 'Ray Clark', '205', '73', 'R', 'R', '1961-09-20', '1970-10-01', 'washr101', 'washbra01'),
('washebu01', '1882', '10', '11', 'USA', 'OH', 'Akron', '1955', '12', '8', 'USA', 'OH', 'Akron', 'Buck', 'Washer', 'William', '175', '70', 'R', 'R', '1905-04-25', '1905-04-25', 'washb101', 'washebu01'),
('washicl01', '1954', '8', '31', 'USA', 'CA', 'Los Angeles', '2020', '6', '10', 'USA', 'CA', 'Orinda', 'Claudell', 'Washington', 'Claudell', '190', '72', 'L', 'L', '1974-07-05', '1990-06-18', 'washc001', 'washicl01'),
('washida01', '1990', '11', '20', 'USA', 'CA', 'San Diego', '', '', '', '', '', '', 'David', 'Washington', 'David Edward', '260', '77', 'L', 'L', '2017-06-14', '2017-06-19', 'washd001', 'washida01'),
('washige01', '1907', '6', '4', 'USA', 'TX', 'Linden', '1985', '2', '17', 'USA', 'TX', 'Linden', 'George', 'Washington', 'Sloan Vernon', '190', '71', 'L', 'R', '1935-04-17', '1936-06-16', 'washg102', 'washige01'),
('washihe01', '1951', '11', '16', 'USA', 'MS', 'Belzonia', '', '', '', '', '', '', 'Herb', 'Washington', 'Herbert Lee', '170', '72', 'R', 'R', '1974-04-04', '1975-05-04', 'washh101', 'washihe01'),
('washila01', '1953', '9', '7', 'USA', 'CA', 'Long Beach', '', '', '', '', '', '', 'LaRue', 'Washington', 'LaRue', '170', '72', 'R', 'R', '1978-09-07', '1979-09-30', 'washl101', 'washila01'),
('washiri01', '1978', '5', '30', 'USA', 'GA', 'Milledgeville', '', '', '', '', '', '', 'Rico', 'Washington', 'Enrico Aliceno', '195', '69', 'L', 'R', '2008-04-01', '2008-04-20', 'washr002', 'washiri01'),
('washiro01', '1952', '4', '29', 'USA', 'LA', 'New Orleans', '', '', '', '', '', '', 'Ron', 'Washington', 'Ronald', '155', '71', 'R', 'R', '1977-09-10', '1989-07-07', 'washr001', 'washiro01'),
('washiul01', '1953', '10', '27', 'USA', 'OK', 'Stringtown', '', '', '', '', '', '', 'U. L.', 'Washington', 'U. L.', '175', '71', 'B', 'R', '1977-09-06', '1987-10-04', 'washu001', 'washiu_01'),
('wasinma01', '1961', '8', '4', 'USA', 'CA', 'Monterey', '', '', '', '', '', '', 'Mark', 'Wasinger', 'Mark Thomas', '165', '72', 'R', 'R', '1986-05-27', '1988-04-21', 'wasim001', 'wasinma01'),
('waslega01', '1941', '7', '21', 'USA', 'CT', 'Meriden', '', '', '', '', '', '', 'Gary', 'Waslewski', 'Gary Lee', '190', '76', 'R', 'R', '1967-06-11', '1972-09-28', 'waslg101', 'waslega01'),
('wasseeh01', '1980', '12', '6', 'USA', 'AL', 'Sylacauga', '', '', '', '', '', '', 'Ehren', 'Wassermann', 'Ehren Josef', '190', '72', 'B', 'R', '2007-07-20', '2008-09-26', 'wasse001', 'wasseeh01'),
('waszgbj01', '1970', '8', '24', 'USA', 'NE', 'Omaha', '', '', '', '', '', '', 'B. J.', 'Waszgis', 'Robert Michael', '215', '74', 'R', 'R', '2000-07-29', '2000-10-01', 'waszb001', 'waszgb.01'),
('waterch01', '1980', '8', '17', 'USA', 'FL', 'Lakeland', '', '', '', '', '', '', 'Chris', 'Waters', 'Christopher Myron', '170', '72', 'L', 'L', '2008-08-05', '2009-10-01', 'watec001', 'waterch01'),
('waterfr01', '1845', '', '', 'USA', 'NY', 'New York', '1899', '12', '16', 'USA', 'OH', 'Cincinnati', 'Fred', 'Waterman', 'Frederick A.', '148', '67', '', '', '1871-05-05', '1875-09-23', 'watef102', 'waterfr01'),
('waterfr02', '1927', '2', '2', 'USA', 'MS', 'Benton', '1989', '8', '28', 'USA', 'FL', 'Pensacola', 'Fred', 'Waters', 'Fred Warren', '185', '71', 'L', 'L', '1955-09-20', '1956-09-23', 'watef101', 'waterfr02'),
('waterst01', '1952', '4', '6', 'USA', 'IL', 'Carbondale', '2017', '5', '19', 'USA', 'IL', 'Marion', 'Steve', 'Waterbury', 'Steven Craig', '190', '77', 'R', 'R', '1976-09-14', '1976-09-27', 'wates101', 'waterst01'),
('wathadu01', '1973', '8', '22', 'USA', 'FL', 'Jacksonville', '', '', '', '', '', '', 'Dusty', 'Wathan', 'Dustin James', '215', '76', 'R', 'R', '2002-09-24', '2002-09-29', 'wathd001', 'wathadu01'),
('wathajo01', '1949', '10', '4', 'USA', 'IA', 'Cedar Rapids', '', '', '', '', '', '', 'John', 'Wathan', 'John David', '205', '74', 'R', 'R', '1976-05-26', '1985-10-06', 'wathj001', 'wathajo01'),
('watkibi01', '1858', '5', '5', 'CAN', 'ON', 'Brantford', '1937', '6', '9', 'USA', 'MI', 'Port Huron', 'Bill', 'Watkins', 'William Henry', '156', '70', 'R', '', '1884-08-01', '1884-10-13', 'watkb101', 'watkibi01'),
('watkibo01', '1948', '3', '12', 'USA', 'CA', 'San Francisco', '', '', '', '', '', '', 'Bob', 'Watkins', 'Robert Cecil', '170', '73', 'R', 'R', '1969-09-06', '1969-09-26', 'watkb102', 'watkibo01'),
('watkida01', '1944', '3', '15', 'USA', 'KY', 'Owensboro', '', '', '', '', '', '', 'Dave', 'Watkins', 'David Roger', '185', '70', 'R', 'R', '1969-04-09', '1969-10-02', 'watkd101', 'watkida01'),
('watkied01', '1877', '6', '21', 'USA', 'PA', 'Philadelphia', '1933', '3', '29', 'USA', 'AZ', 'Kelvin', 'Ed', 'Watkins', 'James Edward', '', '', '', '', '1902-09-06', '1902-09-06', 'watke101', 'watkied01'),
('watkige01', '1900', '6', '4', 'USA', 'TX', 'Freestone County', '1970', '6', '1', 'USA', 'TX', 'Austin', 'George', 'Watkins', 'George Archibald', '175', '72', 'L', 'R', '1930-04-15', '1936-09-27', 'watkg101', 'watkige01'),
('watkiha99', '1869', '6', '14', 'USA', 'NY', 'Seneca Falls', '1949', '4', '29', 'United Kingdom', 'London', 'Harrow', 'Harvey', 'Watkins', 'Harvey Lennox', '', '', '', '', '', '', 'watkh801', 'watkiha99'),
('watkilo01', '1989', '8', '29', 'USA', 'KS', 'Wichita', '', '', '', '', '', '', 'Logan', 'Watkins', 'Vincent Logan', '195', '71', 'L', 'R', '2013-08-04', '2014-09-28', 'watkl001', 'watkilo01'),
('watkipa01', '1972', '9', '2', 'USA', 'NC', 'Raleigh', '', '', '', '', '', '', 'Pat', 'Watkins', 'William Patrick', '185', '74', 'R', 'R', '1997-09-09', '1999-05-01', 'watkp001', 'watkipa01'),
('watkisc01', '1970', '5', '15', 'USA', 'OK', 'Tulsa', '', '', '', '', '', '', 'Scott', 'Watkins', 'Scott Allen', '180', '75', 'L', 'L', '1995-08-01', '1995-09-30', 'watks001', 'watkisc01'),
('watkist01', '1978', '7', '19', 'USA', 'TX', 'Lubbock', '', '', '', '', '', '', 'Steve', 'Watkins', 'Stephen Douglas', '190', '76', 'R', 'R', '2004-08-21', '2004-10-02', 'watks002', 'watkist01'),
('watkito01', '1980', '6', '18', 'USA', 'FL', 'Fort Myers', '', '', '', '', '', '', 'Tommy', 'Watkins', 'Thomas Gray', '200', '70', 'R', 'R', '2007-08-10', '2007-08-22', 'watkt001', 'watkito01'),
('watline01', '1922', '12', '25', 'USA', 'NC', 'Yanceyville', '2019', '12', '29', 'USA', 'NC', 'Yanceyville', 'Neal', 'Watlington', 'Julius Neal', '195', '72', 'L', 'R', '1953-07-12', '1953-09-17', 'watln101', 'watline01'),
('watsoal01', '1970', '11', '18', 'USA', 'NY', 'Jamaica', '', '', '', '', '', '', 'Allen', 'Watson', 'Allen Kenneth', '195', '75', 'L', 'L', '1993-07-08', '2000-08-10', 'watsa001', 'watsoal01'),
('watsoar01', '1884', '1', '11', 'USA', 'IN', 'Jeffersonville', '1950', '5', '9', 'USA', 'NY', 'Buffalo', 'Art', 'Watson', 'Arthur Stanhope', '175', '70', 'L', 'R', '1914-05-19', '1915-08-07', 'watsa101', 'watsoar01'),
('watsobo01', '1946', '4', '10', 'USA', 'CA', 'Los Angeles', '2020', '5', '14', 'USA', 'TX', 'Houston', 'Bob', 'Watson', 'Robert Jose', '201', '72', 'R', 'R', '1966-09-09', '1984-09-30', 'watsb001', 'watsobo01'),
('watsobr01', '1981', '9', '30', 'USA', 'CA', 'Los Angeles', '', '', '', '', '', '', 'Brandon', 'Watson', 'Brandon Eric', '170', '73', 'L', 'R', '2005-08-09', '2007-06-25', 'watsb002', 'watsobr01'),
('watsodo01', '1885', '1', '30', 'USA', 'OH', 'Carroll County', '1949', '12', '30', 'USA', 'CA', 'San Diego', 'Doc', 'Watson', 'Charles John', '170', '72', 'L', 'L', '1913-09-03', '1915-09-21', 'watsd101', 'watsodo01'),
('watsojo01', '1908', '1', '16', 'USA', 'VA', 'Tazewell', '1965', '4', '29', 'USA', 'WV', 'Huntington', 'Johnny', 'Watson', 'John Thomas', '175', '72', 'L', 'R', '1930-09-26', '1930-09-28', 'watsj101', 'watsojo01'),
('watsoma01', '1974', '1', '23', 'USA', 'GA', 'Atlanta', '', '', '', '', '', '', 'Mark', 'Watson', 'Mark Bradford', '215', '76', 'R', 'L', '2000-05-19', '2003-08-21', 'watsm001', 'watsoma03'),
('watsoma02', '1978', '9', '5', 'USA', 'PA', 'Lancaster', '', '', '', '', '', '', 'Matt', 'Watson', 'Matthew Kyle', '205', '71', 'L', 'R', '2003-09-12', '2010-08-07', 'watsm002', 'watsoma02'),
('watsomi01', '1890', '1', '10', 'USA', 'GA', 'Flovilla', '1962', '4', '10', 'USA', 'AR', 'Pine Bluff', 'Milt', 'Watson', 'Milton Robert', '180', '73', 'R', 'R', '1916-07-26', '1919-06-16', 'watsm102', 'watsomi01'),
('watsomo01', '1865', '1', '27', 'USA', 'OH', 'Middleport', '1898', '11', '23', 'USA', 'OH', 'Middleport', 'Mother', 'Watson', 'Walter L.', '145', '69', '', '', '1887-05-19', '1887-05-27', 'watsm101', 'watsomo01'),
('watsomu01', '1896', '10', '15', 'USA', 'LA', 'Arizona', '1949', '8', '25', 'USA', 'LA', 'Shreveport', 'Mule', 'Watson', 'John Reaves', '185', '73', 'R', 'R', '1918-07-04', '1924-09-18', 'watsm103', 'watsomu01'),
('watsoto01', '1985', '5', '30', 'USA', 'IA', 'Sioux City', '', '', '', '', '', '', 'Tony', 'Watson', 'Anthony Michael', '224', '75', 'L', 'L', '2011-06-08', '2020-09-26', 'watst001', 'watsoto01'),
('wattal01', '1899', '12', '12', 'USA', 'PA', 'Philadelphia', '1968', '3', '15', 'USA', 'VA', 'Norfolk', 'Allie', 'Watt', 'Albert Bailey', '154', '68', 'R', 'R', '1920-10-03', '1920-10-03', 'watta101', 'wattal01'),
('watted01', '1941', '4', '4', 'USA', 'IA', 'Lamoni', '', '', '', '', '', '', 'Eddie', 'Watt', 'Eddie Dean', '183', '70', 'R', 'R', '1966-04-12', '1975-06-14', 'watte101', 'watted01'),
('wattfr01', '1902', '12', '15', 'USA', 'DC', 'Washington', '1956', '8', '31', 'USA', 'DC', 'Washington', 'Frank', 'Watt', 'Frank Marion', '205', '73', 'R', 'R', '1931-04-14', '1931-09-27', 'wattf101', 'wattfr01'),
('watwojo01', '1905', '8', '17', 'USA', 'AL', 'Alexander City', '1980', '3', '1', 'USA', 'AL', 'Goodwater', 'Johnny', 'Watwood', 'John Clifford', '186', '73', 'L', 'L', '1929-04-16', '1939-05-29', 'watwj101', 'watwojo01'),
('waughji01', '1933', '11', '25', 'USA', 'OH', 'Lancaster', '2010', '2', '16', 'USA', 'SC', 'Rock Hill', 'Jim', 'Waugh', 'James Elden', '185', '75', 'R', 'R', '1952-04-19', '1953-09-26', 'waugj101', 'waughji01'),
('waybo01', '1906', '4', '2', 'USA', 'PA', 'Emlenton', '1974', '6', '20', 'USA', 'PA', 'Pittsburgh', 'Bob', 'Way', 'Robert Clinton', '168', '70', 'R', 'R', '1927-04-12', '1927-05-15', 'way-b101', 'waybo01'),
('wayenfr01', '1898', '8', '27', 'USA', 'KS', 'Franklin', '1975', '4', '16', 'USA', 'OH', 'Zanesville', 'Frank', 'Wayenberg', 'Frank', '172', '72', 'R', 'R', '1924-08-25', '1924-08-28', 'wayef101', 'wayenfr01'),
('waynega01', '1962', '11', '30', 'USA', 'MI', 'Dearborn', '', '', '', '', '', '', 'Gary', 'Wayne', 'Gary Anthony', '185', '75', 'L', 'L', '1989-04-07', '1994-06-03', 'wayng001', 'waynega01'),
('wayneju01', '1979', '4', '16', 'USA', 'HI', 'Honolulu', '', '', '', '', '', '', 'Justin', 'Wayne', 'Justin Morgan', '200', '75', 'R', 'R', '2002-09-03', '2004-07-25', 'waynj001', 'wayneju01'),
('weafeke01', '1913', '2', '6', 'USA', 'MA', 'Woburn', '2005', '6', '4', 'USA', 'NY', 'Guilderland', 'Ken', 'Weafer', 'Kenneth Albert', '183', '72', 'R', 'R', '1936-05-29', '1936-05-29', 'weafk101', 'weafeke01'),
('weathda01', '1969', '9', '25', 'USA', 'TN', 'Lawrenceburg', '', '', '', '', '', '', 'David', 'Weathers', 'John David', '205', '75', 'R', 'R', '1991-08-02', '2009-10-03', 'weatd001', 'weathda01'),
('weathro01', '1915', '2', '25', 'USA', 'TX', 'Warren', '1991', '1', '19', 'USA', 'TX', 'Woodville', 'Roy', 'Weatherly', 'Cyril Roy', '170', '66', 'L', 'R', '1936-06-27', '1950-10-01', 'weatr101', 'weathro01'),
('weathry01', '1999', '12', '17', 'USA', 'TN', 'Loretto', '', '', '', '', '', '', 'Ryan', 'Weathers', 'Ryan', '230', '73', 'R', 'L', '', '', 'weatr001', 'weathry01'),
('weavear01', '1879', '4', '7', 'USA', 'KS', 'Wichita', '1917', '3', '23', 'USA', 'CO', 'Denver', 'Art', 'Weaver', 'Arthur Coggshall', '160', '73', '', 'R', '1902-09-14', '1908-09-07', 'weava101', 'weavear01'),
('weavebu01', '1890', '8', '18', 'USA', 'PA', 'Pottstown', '1956', '1', '31', 'USA', 'IL', 'Chicago', 'Buck', 'Weaver', 'George Daniel', '170', '71', 'B', 'R', '1912-04-11', '1920-09-27', 'weavb101', 'weavebu01'),
('weaveea99', '1930', '8', '14', 'USA', 'MO', 'St. Louis', '2013', '1', '19', 'At Sea', 'Caribbean Sea', '', 'Earl', 'Weaver', 'Earl Sidney', '180', '67', 'R', 'R', '', '', 'weave801', 'weaveea99'),
('weaveer01', '1973', '8', '4', 'USA', 'IL', 'Springfield', '', '', '', '', '', '', 'Eric', 'Weaver', 'James Eric', '230', '77', 'R', 'R', '1998-05-30', '2000-08-17', 'weave001', 'weaveer01'),
('weavefa01', '1865', '3', '23', 'USA', 'WV', 'Parkersburg', '1943', '1', '23', 'USA', 'OH', 'Akron', 'Farmer', 'Weaver', 'William B.', '170', '70', 'B', '', '1888-09-16', '1894-09-29', 'weavf102', 'weavefa01'),
('weavefl01', '1941', '5', '12', 'USA', 'TX', 'Ben Franklin', '2008', '11', '17', 'USA', 'TX', 'Powderly', 'Floyd', 'Weaver', 'David Floyd', '195', '76', 'R', 'R', '1962-09-30', '1971-09-26', 'weavf101', 'weavefl01'),
('weaveha01', '1892', '2', '26', 'USA', 'PA', 'Clarendon', '1983', '5', '30', 'USA', 'NY', 'Rochester', 'Harry', 'Weaver', 'Harry Abraham', '160', '71', 'R', 'R', '1915-09-18', '1919-05-04', 'weavh101', 'weaveha01'),
('weaveje01', '1976', '8', '22', 'USA', 'CA', 'Northridge', '', '', '', '', '', '', 'Jeff', 'Weaver', 'Jeffrey Charles', '200', '77', 'R', 'R', '1999-04-14', '2010-09-29', 'weavj002', 'weaveje01'),
('weaveje02', '1982', '10', '4', 'USA', 'CA', 'Northridge', '', '', '', '', '', '', 'Jered', 'Weaver', 'Jered David', '210', '79', 'R', 'R', '2006-05-27', '2017-05-19', 'weavj003', 'weaveje02'),
('weaveji01', '1903', '11', '25', 'USA', 'TN', 'Obion County', '1983', '12', '12', 'USA', 'FL', 'Lakeland', 'Jim', 'Weaver', 'James Dement', '230', '78', 'R', 'R', '1928-08-27', '1939-05-08', 'weavj101', 'weaveji01'),
('weaveji02', '1939', '2', '19', 'USA', 'PA', 'Lancaster', '', '', '', '', '', '', 'Jim', 'Weaver', 'James Brian', '178', '72', 'L', 'L', '1967-08-13', '1968-06-29', 'weavj102', 'weaveji02'),
('weaveji03', '1959', '10', '10', 'USA', 'NY', 'Kingston', '', '', '', '', '', '', 'Jim', 'Weaver', 'James Francis', '190', '75', 'L', 'L', '1985-04-10', '1989-09-30', 'weavj001', 'weaveji03'),
('weavelu01', '1993', '8', '21', 'USA', 'FL', 'DeLand', '', '', '', '', '', '', 'Luke', 'Weaver', 'Luke Allen', '185', '74', 'R', 'R', '2016-08-13', '2020-09-26', 'weavl001', 'weavelu01'),
('weavemo01', '1906', '6', '15', 'USA', 'NC', 'Helton', '1994', '6', '14', 'USA', 'FL', 'Orlando', 'Monte', 'Weaver', 'Montie Morton', '170', '72', 'L', 'R', '1931-09-20', '1939-07-04', 'weavm101', 'weavemo01'),
('weaveor01', '1886', '6', '4', 'USA', 'KY', 'Newport', '1970', '11', '28', 'USA', 'LA', 'New Orleans', 'Orlie', 'Weaver', 'Orville Forest', '180', '72', 'R', 'R', '1910-09-14', '1911-10-09', 'weavo101', 'weaveor01'),
('weavero01', '1954', '10', '6', 'USA', 'NY', 'Amsterdam', '', '', '', '', '', '', 'Roger', 'Weaver', 'Roger Edward', '190', '75', 'R', 'R', '1980-06-06', '1980-10-04', 'weavr101', 'weavero01'),
('weavesa01', '1855', '7', '20', 'USA', 'PA', 'Philadelphia', '1914', '2', '1', 'USA', 'PA', 'Philadelphia', 'Sam', 'Weaver', 'Samuel H.', '175', '70', 'R', 'R', '1875-10-25', '1886-05-29', 'weavs101', 'weavesa01'),
('webbbi01', '1895', '6', '25', 'USA', 'IL', 'Chicago', '1943', '1', '12', 'USA', 'IL', 'Chicago', 'Bill', 'Webb', 'William Joseph', '161', '70', 'R', 'R', '1917-09-17', '1917-10-01', 'webbb101', 'webbbi01'),
('webbbi02', '1913', '12', '12', 'USA', 'GA', 'Atlanta', '1994', '6', '1', 'USA', 'GA', 'Austell', 'Bill', 'Webb', 'Willie Fred', '180', '74', 'R', 'R', '1943-05-15', '1943-05-15', 'webbb102', 'webbbi02'),
('webbbr01', '1979', '5', '9', 'USA', 'KY', 'Ashland', '', '', '', '', '', '', 'Brandon', 'Webb', 'Brandon Tyler', '230', '75', 'R', 'R', '2003-04-22', '2009-04-06', 'webbb001', 'webbbr01'),
('webbda01', '1989', '8', '18', 'USA', 'KY', 'Paducah', '2017', '10', '14', 'USA', 'TN', 'Waverly', 'Daniel', 'Webb', 'Robert Wyatt McDaniel', '215', '75', 'R', 'R', '2013-09-04', '2016-04-28', 'webbd001', 'webbda01'),
('webbea01', '1897', '9', '17', 'USA', 'TN', 'White County', '1965', '5', '23', 'USA', 'TN', 'Jamestown', 'Earl', 'Webb', 'William Earl', '185', '73', 'L', 'R', '1925-08-13', '1933-10-01', 'webbe101', 'webbea01'),
('webbele01', '1915', '5', '6', 'USA', 'CA', 'Kelseyville', '1986', '11', '13', 'USA', 'CA', 'Santa Maria', 'Les', 'Webber', 'Lester Elmer', '185', '72', 'R', 'R', '1942-05-17', '1948-04-26', 'webbl102', 'webbele01'),
('webbha01', '1950', '5', '21', 'USA', 'NY', 'Copiague', '', '', '', '', '', '', 'Hank', 'Webb', 'Henry Gaylon Matthew', '175', '75', 'R', 'R', '1972-09-05', '1977-10-02', 'webbh101', 'webbha01'),
('webbja01', '1993', '8', '15', 'USA', 'CA', 'Riverside', '', '', '', '', '', '', 'Jacob', 'Webb', 'Jacob Lawrence', '210', '74', 'R', 'R', '2019-04-16', '2020-09-26', 'webbj002', 'webbja01'),
('webbjo01', '1979', '5', '23', 'USA', 'FL', 'Pensacola', '', '', '', '', '', '', 'John', 'Webb', 'John Floyd', '220', '75', 'R', 'R', '2004-08-02', '2005-04-20', 'webbj001', 'webbjo01'),
('webble01', '1885', '3', '1', 'USA', 'OH', 'Mount Gilead', '1958', '1', '12', 'USA', 'OH', 'Circleville', 'Lefty', 'Webb', 'Cleon Earl', '165', '71', 'B', 'L', '1910-05-23', '1910-08-05', 'webbl101', 'webble01'),
('webblo01', '1996', '11', '18', 'USA', 'CA', 'Rocklin', '', '', '', '', '', '', 'Logan', 'Webb', 'Logan T.', '220', '73', 'R', 'R', '2019-08-17', '2020-09-27', 'webbl001', 'webblo01'),
('webbre01', '1924', '9', '25', 'USA', 'DC', 'Washington', '1996', '2', '7', 'USA', 'MD', 'Hyattsville', 'Red', 'Webb', 'Samuel Henry', '175', '72', 'L', 'R', '1948-09-15', '1949-07-22', 'webbr101', 'webbre01'),
('webbry01', '1986', '2', '5', 'USA', 'FL', 'Clearwater', '', '', '', '', '', '', 'Ryan', 'Webb', 'Ryan Christopher', '245', '78', 'R', 'R', '2009-07-08', '2016-06-26', 'webbr001', 'webbry01'),
('webbsk01', '1909', '11', '4', 'USA', 'MS', 'Meridian', '1986', '7', '8', 'USA', 'MS', 'Meridian', 'Skeeter', 'Webb', 'James Laverne', '150', '69', 'R', 'R', '1932-07-20', '1948-08-31', 'webbs101', 'webbsk01'),
('webbty01', '1990', '7', '20', 'USA', 'VA', 'Nassawadox', '', '', '', '', '', '', 'Tyler', 'Webb', 'Jon Tyler', '240', '77', 'L', 'L', '2017-06-24', '2020-09-26', 'webbt001', 'webbty01'),
('weberbe01', '1969', '11', '17', 'USA', 'TX', 'Port Arthur', '', '', '', '', '', '', 'Ben', 'Weber', 'Benjamin Edward', '185', '76', 'R', 'R', '2000-04-03', '2005-05-08', 'webeb001', 'weberbe01'),
('weberch01', '1868', '10', '22', 'USA', 'OH', 'Cincinnati', '1914', '6', '13', 'USA', 'TX', 'Beaumont', 'Charlie', 'Weber', 'Charles P.', '', '', '', 'R', '1898-07-30', '1898-07-30', 'webec101', 'weberch01'),
('weberha01', '1862', '2', '12', 'USA', 'NY', '', '1926', '12', '22', 'USA', 'IN', 'Indianapolis', 'Harry', 'Weber', 'Henry J.', '', '', '', '', '1884-07-22', '1884-07-31', 'webeh101', 'weberha01'),
('weberjo01', '1862', '2', '15', 'CAN', 'ON', 'Hamilton', '1921', '12', '15', 'CAN', 'ON', 'Wentworth', 'Joe', 'Weber', 'Joseph Edward', '167', '69', 'R', '', '1884-05-30', '1884-06-05', 'webej101', 'weberjo01'),
('weberne01', '1972', '12', '6', 'USA', 'CA', 'Newport Beach', '', '', '', '', '', '', 'Neil', 'Weber', 'Neil Aaron', '215', '77', 'L', 'L', '1998-09-11', '1998-09-27', 'weben001', 'webbene01'),
('weberry01', '1990', '8', '12', 'USA', 'FL', 'St. Petersburg', '', '', '', '', '', '', 'Ryan', 'Weber', 'James Ryan', '175', '73', 'R', 'R', '2015-09-08', '2020-09-27', 'weber001', 'weberry01'),
('weberth01', '1984', '9', '28', 'USA', 'NE', 'Seward', '', '', '', '', '', '', 'Thad', 'Weber', 'Thad G.', '205', '74', 'R', 'R', '2012-04-22', '2013-08-20', 'webet001', 'weberth01');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
