-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 06, 2021 at 08:48 PM
-- Server version: 10.3.28-MariaDB
-- PHP Version: 7.3.6

USE cs411baseball_db;

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

-- --------------------------------------------------------

--
-- Structure for view `vw_players_position`
--

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_players_position`  AS  select `players_position`.`playerid` AS `playerid`,`players_position`.`pos` AS `pos`,`players_position`.`gs` AS `gs`,`players_position`.`gs_rank` AS `gs_rank`,`players_position`.`gs_row_rnk` AS `gs_row_rnk` from `players_position` where `players_position`.`gs_row_rnk` = 1 ;

--
-- VIEW  `vw_players_position`
-- Data: None
--

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
