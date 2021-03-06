-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 16, 2021 at 10:00 PM
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
-- Table structure for table `pitching`
--

DROP TABLE IF EXISTS `pitching`;
CREATE TABLE IF NOT EXISTS `pitching` (
`playerID`varchar(9) DEFAULT NULL,
`yearID`  varchar(6) DEFAULT NULL,
`stint`   varchar(5) DEFAULT NULL,
`teamID`  varchar(6) DEFAULT NULL,
`lgID`    varchar(4) DEFAULT NULL,
`W`       varchar(2) DEFAULT NULL,
`L`       varchar(2) DEFAULT NULL,
`G`       varchar(3) DEFAULT NULL,
`GS`      varchar(2) DEFAULT NULL,
`CG`      varchar(2) DEFAULT NULL,
`SHO`     varchar(3) DEFAULT NULL,
`SV`      varchar(2) DEFAULT NULL,
`IPouts`  varchar(6) DEFAULT NULL,
`H`       varchar(3) DEFAULT NULL,
`ER`      varchar(3) DEFAULT NULL,
`HR`      varchar(2) DEFAULT NULL,
`BB`      varchar(3) DEFAULT NULL,
`SO`      varchar(3) DEFAULT NULL,
`BAOpp`   varchar(5) DEFAULT NULL,
`ERA`     varchar(10) DEFAULT NULL,
`IBB`     varchar(3) DEFAULT NULL,
`WP`      varchar(2) DEFAULT NULL,
`HBP`     varchar(3) DEFAULT NULL,
`BK`      varchar(2) DEFAULT NULL,
`BFP`     varchar(4) DEFAULT NULL,
`GF`      varchar(2) DEFAULT NULL,
`R`       varchar(3) DEFAULT NULL,
`SH`      varchar(2) DEFAULT NULL,
`SF`      varchar(2) DEFAULT NULL,
`GIDP`    varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pitching`
--

INSERT INTO `pitching` (`playerID`, `yearID`, `stint`, `teamID`, `lgID`, `W`, `L`, `G`, `GS`, `CG`, `SHO`, `SV`, `IPouts`, `H`, `ER`, `HR`, `BB`, `SO`, `BAOpp`, `ERA`, `IBB`, `WP`, `HBP`, `BK`, `BFP`, `GF`, `R`, `SH`, `SF`, `GIDP`) VALUES
('gavigsa01', '2019', '1', 'TOR', 'AL', '4', '2', '52', '0', '0', '0', '0', '287', '85', '49', '18', '22', '88', '0.235', '4.61', '0', '0', '4', '1', '392', '9', '51', '1', '3', '4'),
('gearrco01', '2019', '1', 'SEA', 'AL', '0', '2', '48', '2', '0', '0', '0', '124', '38', '18', '3', '21', '39', '0.247', '3.92', '1', '4', '4', '0', '180', '3', '18', '0', '1', '9'),
('gearrco01', '2019', '2', 'NYA', 'AL', '1', '1', '18', '0', '0', '0', '0', '42', '17', '7', '2', '4', '8', '0.298', '4.50', '0', '0', '0', '1', '61', '5', '7', '0', '0', '2'),
('germado01', '2019', '1', 'NYA', 'AL', '18', '4', '27', '24', '0', '0', '0', '429', '125', '64', '30', '39', '153', '0.228', '4.03', '0', '5', '5', '0', '594', '0', '69', '1', '1', '6'),
('gibauia01', '2019', '1', 'TBA', 'AL', '0', '0', '1', '0', '0', '0', '0', '6', '1', '2', '0', '2', '2', '0.167', '9.00', '0', '0', '0', '0', '9', '1', '2', '0', '1', '0'),
('gibauia01', '2019', '2', 'TEX', 'AL', '1', '1', '9', '0', '0', '0', '0', '37', '11', '7', '1', '8', '14', '0.244', '5.11', '1', '1', '1', '0', '55', '0', '7', '0', '1', '0'),
('gibsoky01', '2019', '1', 'MIN', 'AL', '13', '7', '34', '29', '0', '0', '0', '480', '175', '86', '23', '56', '160', '0.275', '4.84', '0', '8', '7', '0', '706', '0', '99', '3', '2', '17'),
('gileske01', '2019', '1', 'TOR', 'AL', '2', '3', '53', '0', '0', '0', '23', '159', '36', '11', '5', '17', '83', '0.188', '1.87', '1', '2', '0', '0', '208', '44', '11', '0', '0', '1'),
('gilmase01', '2019', '1', 'BAL', 'AL', '0', '1', '1', '1', '0', '0', '0', '7', '7', '5', '2', '2', '1', '0.500', '19.29', '0', '0', '0', '0', '16', '0', '5', '0', '0', '0'),
('ginkeke01', '2019', '1', 'ARI', 'NL', '3', '0', '25', '0', '0', '0', '2', '73', '15', '4', '2', '9', '28', '0.174', '1.48', '0', '2', '0', '0', '96', '4', '7', '0', '0', '1'),
('giolilu01', '2019', '1', 'CHA', 'AL', '14', '9', '29', '29', '3', '2', '0', '530', '131', '67', '24', '57', '228', '0.205', '3.41', '1', '6', '4', '0', '705', '0', '69', '1', '3', '13'),
('givenmy01', '2019', '1', 'BAL', 'AL', '2', '6', '58', '0', '0', '0', '11', '189', '49', '32', '13', '26', '86', '0.213', '4.57', '1', '5', '2', '0', '260', '33', '35', '0', '2', '3'),
('glasnty01', '2019', '1', 'TBA', 'AL', '6', '1', '12', '12', '0', '0', '0', '182', '40', '12', '4', '14', '76', '0.186', '1.78', '0', '2', '0', '0', '230', '0', '13', '0', '1', '5'),
('godleza01', '2019', '1', 'ARI', 'NL', '3', '5', '27', '9', '0', '0', '2', '228', '81', '54', '12', '35', '58', '0.276', '6.39', '2', '3', '4', '1', '338', '9', '55', '3', '2', '9'),
('godleza01', '2019', '2', 'TOR', 'AL', '1', '0', '6', '0', '0', '0', '0', '48', '15', '7', '2', '7', '12', '0.246', '3.94', '0', '0', '1', '0', '69', '1', '7', '0', '0', '1'),
('gomezje01', '2019', '1', 'TEX', 'AL', '1', '0', '16', '0', '0', '0', '0', '46', '23', '14', '2', '6', '10', '0.359', '8.22', '0', '2', '1', '0', '73', '6', '15', '0', '2', '4'),
('gonsoto01', '2019', '1', 'LAN', 'NL', '4', '2', '11', '6', '0', '0', '1', '120', '26', '13', '4', '15', '37', '0.178', '2.93', '0', '2', '1', '0', '163', '1', '15', '0', '1', '0'),
('gonzach01', '2019', '1', 'COL', 'NL', '2', '6', '14', '12', '0', '0', '0', '189', '59', '37', '11', '33', '46', '0.246', '5.29', '0', '1', '1', '0', '278', '0', '39', '3', '1', '6'),
('gonzagi01', '2019', '1', 'MIL', 'NL', '3', '2', '19', '17', '0', '0', '0', '262', '76', '34', '9', '37', '78', '0.234', '3.50', '0', '5', '0', '0', '366', '0', '36', '4', '0', '7'),
('gonzama02', '2019', '1', 'SEA', 'AL', '16', '13', '34', '34', '0', '0', '0', '609', '210', '90', '23', '56', '147', '0.264', '3.99', '1', '2', '6', '1', '866', '0', '106', '1', '9', '22'),
('goodyni01', '2019', '1', 'CLE', 'AL', '3', '2', '39', '0', '0', '0', '0', '122', '30', '16', '7', '22', '50', '0.201', '3.54', '1', '0', '0', '0', '173', '6', '18', '0', '2', '1'),
('gordoal01', '2019', '1', 'KCA', 'AL', '0', '0', '2', '0', '0', '0', '0', '7', '8', '5', '1', '2', '0', '0.571', '19.29', '0', '0', '0', '0', '17', '1', '5', '0', '1', '0'),
('gotttr01', '2019', '1', 'SFN', 'NL', '7', '0', '50', '0', '0', '0', '1', '158', '41', '26', '4', '17', '57', '0.216', '4.44', '0', '1', '2', '0', '214', '6', '26', '1', '4', '1'),
('gracema02', '2019', '1', 'WAS', 'NL', '1', '2', '51', '1', '0', '0', '0', '140', '61', '33', '11', '10', '35', '0.319', '6.36', '0', '1', '2', '0', '206', '12', '34', '1', '2', '8'),
('gratebr01', '2019', '1', 'MIN', 'AL', '1', '1', '10', '0', '0', '0', '0', '29', '10', '5', '1', '2', '10', '0.278', '4.66', '1', '2', '1', '0', '40', '4', '5', '0', '1', '1'),
('grayjo02', '2019', '1', 'COL', 'NL', '11', '8', '26', '25', '0', '0', '0', '450', '147', '64', '19', '56', '150', '0.259', '3.84', '4', '7', '4', '0', '637', '1', '70', '7', '3', '16'),
('grayso01', '2019', '1', 'CIN', 'NL', '11', '8', '31', '31', '0', '0', '0', '526', '122', '56', '17', '68', '205', '0.196', '2.87', '1', '7', '7', '1', '708', '0', '59', '6', '5', '13'),
('greench03', '2019', '1', 'NYA', 'AL', '4', '4', '54', '15', '0', '0', '2', '207', '66', '32', '10', '19', '98', '0.247', '4.17', '0', '2', '6', '0', '295', '10', '35', '0', '3', '2'),
('greensh02', '2019', '1', 'DET', 'AL', '0', '2', '38', '0', '0', '0', '22', '114', '21', '5', '5', '12', '43', '0.153', '1.18', '1', '0', '1', '0', '151', '32', '11', '1', '0', '1'),
('greensh02', '2019', '2', 'ATL', 'NL', '0', '1', '27', '0', '0', '0', '1', '74', '25', '11', '3', '5', '21', '0.269', '4.01', '0', '0', '2', '0', '101', '5', '11', '0', '1', '1'),
('gregelu01', '2019', '1', 'SLN', 'NL', '0', '0', '6', '0', '0', '0', '0', '17', '11', '5', '0', '1', '2', '0.423', '7.94', '0', '0', '0', '0', '27', '3', '5', '0', '0', '1'),
('greinza01', '2019', '1', 'ARI', 'NL', '10', '4', '23', '23', '0', '0', '0', '438', '117', '47', '15', '21', '135', '0.220', '2.90', '2', '1', '3', '0', '562', '0', '48', '4', '3', '12'),
('greinza01', '2019', '2', 'HOU', 'AL', '8', '1', '10', '10', '0', '0', '0', '188', '58', '21', '6', '9', '52', '0.246', '3.02', '0', '1', '1', '1', '248', '0', '25', '1', '1', '10'),
('grotzza01', '2019', '1', 'SEA', 'AL', '1', '0', '14', '0', '0', '0', '0', '52', '14', '8', '0', '8', '18', '0.222', '4.15', '1', '6', '1', '0', '73', '4', '9', '0', '1', '1'),
('gsellro01', '2019', '1', 'NYN', 'NL', '2', '3', '52', '0', '0', '0', '1', '191', '64', '33', '7', '23', '60', '0.261', '4.66', '2', '4', '6', '0', '277', '9', '36', '1', '2', '7'),
('guduare01', '2019', '1', 'HOU', 'AL', '1', '0', '7', '0', '0', '0', '0', '16', '8', '7', '3', '4', '6', '0.364', '11.81', '0', '0', '0', '0', '27', '3', '7', '0', '1', '0'),
('guerrde01', '2019', '1', 'MIL', 'NL', '0', '0', '1', '0', '0', '0', '0', '2', '4', '4', '1', '0', '0', '0.800', '54.00', '0', '0', '0', '0', '6', '0', '4', '0', '1', '0'),
('guerrja01', '2019', '1', 'TOR', 'AL', '0', '0', '11', '0', '0', '0', '1', '42', '12', '6', '1', '5', '15', '0.231', '3.86', '1', '0', '1', '0', '59', '6', '6', '1', '0', '1'),
('guerrja01', '2019', '2', 'WAS', 'NL', '3', '1', '40', '0', '0', '0', '1', '161', '55', '29', '9', '12', '42', '0.256', '4.86', '2', '3', '0', '0', '228', '15', '30', '0', '1', '1'),
('guerrja02', '2019', '1', 'SDN', 'NL', '0', '0', '8', '0', '0', '0', '0', '26', '7', '5', '3', '3', '6', '0.219', '5.19', '0', '0', '0', '0', '36', '1', '5', '0', '1', '0'),
('guerrju02', '2019', '1', 'MIL', 'NL', '9', '5', '72', '0', '0', '0', '3', '251', '58', '33', '11', '36', '77', '0.194', '3.55', '2', '5', '4', '0', '344', '11', '35', '3', '2', '5'),
('guerrta01', '2019', '1', 'MIA', 'NL', '1', '2', '52', '0', '0', '0', '0', '138', '42', '32', '7', '36', '43', '0.246', '6.26', '0', '9', '6', '0', '216', '10', '34', '0', '3', '6'),
('guerrta02', '2019', '1', 'TEX', 'AL', '0', '0', '20', '0', '0', '0', '0', '79', '26', '17', '3', '22', '27', '0.263', '5.81', '0', '2', '2', '0', '123', '5', '19', '0', '0', '5'),
('guilbta01', '2019', '1', 'SEA', 'AL', '0', '0', '17', '0', '0', '0', '0', '37', '10', '5', '2', '3', '7', '0.213', '3.65', '1', '0', '1', '0', '51', '1', '6', '0', '0', '2'),
('gustaja01', '2019', '1', 'SFN', 'NL', '0', '0', '23', '0', '0', '0', '1', '73', '18', '8', '1', '9', '14', '0.209', '2.96', '0', '0', '0', '0', '99', '4', '11', '1', '3', '3'),
('gyorkje01', '2019', '1', 'SLN', 'NL', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0.000', '0.00', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0'),
('haderjo01', '2019', '1', 'MIL', 'NL', '3', '5', '61', '0', '0', '0', '37', '227', '41', '22', '15', '20', '138', '0.155', '2.62', '2', '0', '4', '0', '289', '46', '24', '0', '0', '2'),
('hahnje01', '2019', '1', 'KCA', 'AL', '0', '1', '6', '0', '0', '0', '0', '14', '7', '7', '1', '6', '7', '0.333', '13.50', '1', '0', '0', '0', '27', '2', '7', '0', '0', '0'),
('haleda02', '2019', '1', 'NYA', 'AL', '3', '0', '20', '0', '0', '0', '2', '113', '39', '13', '2', '7', '23', '0.264', '3.11', '1', '2', '1', '0', '157', '10', '13', '0', '1', '3'),
('hallma02', '2019', '1', 'DET', 'AL', '0', '1', '16', '0', '0', '0', '0', '70', '28', '20', '4', '15', '27', '0.289', '7.71', '1', '1', '1', '0', '113', '7', '20', '0', '0', '1'),
('hamelco01', '2019', '1', 'CHN', 'NL', '7', '7', '27', '27', '0', '0', '0', '425', '141', '60', '17', '56', '143', '0.260', '3.81', '1', '1', '7', '0', '617', '0', '64', '4', '6', '13'),
('hammejd01', '2019', '1', 'PHI', 'NL', '1', '0', '20', '0', '0', '0', '0', '57', '15', '8', '2', '12', '13', '0.217', '3.79', '0', '1', '0', '0', '81', '7', '8', '0', '0', '2'),
('handbr01', '2019', '1', 'CLE', 'AL', '6', '4', '60', '0', '0', '0', '34', '172', '53', '21', '6', '18', '84', '0.242', '3.30', '5', '0', '4', '0', '242', '54', '21', '1', '0', '4'),
('happja01', '2019', '1', 'NYA', 'AL', '12', '8', '31', '30', '0', '0', '0', '484', '160', '88', '34', '49', '140', '0.258', '4.91', '1', '3', '5', '0', '678', '0', '88', '0', '2', '17'),
('hardybl01', '2019', '1', 'DET', 'AL', '1', '1', '39', '0', '0', '0', '0', '133', '38', '22', '10', '13', '29', '0.232', '4.47', '0', '3', '0', '0', '182', '3', '24', '1', '4', '1'),
('harpery01', '2019', '1', 'MIN', 'AL', '4', '2', '61', '0', '0', '0', '1', '163', '54', '23', '7', '10', '50', '0.257', '3.81', '0', '5', '1', '0', '225', '7', '25', '0', '3', '2'),
('harriwi02', '2019', '1', 'HOU', 'AL', '4', '1', '68', '0', '0', '0', '4', '180', '42', '10', '6', '14', '62', '0.196', '1.50', '0', '3', '0', '0', '229', '10', '14', '1', '0', '7'),
('hartdo01', '2019', '1', 'MIL', 'NL', '0', '0', '4', '0', '0', '0', '0', '20', '4', '0', '0', '4', '3', '0.182', '0.00', '1', '0', '0', '0', '26', '2', '0', '0', '0', '1'),
('hartdo01', '2019', '2', 'NYN', 'NL', '0', '0', '1', '0', '0', '0', '0', '3', '0', '0', '0', '0', '0', '0.000', '0.00', '0', '0', '0', '0', '3', '0', '0', '0', '0', '0'),
('hartlge01', '2019', '1', 'PIT', 'NL', '0', '1', '29', '0', '0', '0', '0', '105', '52', '35', '8', '18', '38', '0.351', '9.00', '0', '5', '0', '1', '171', '10', '35', '1', '4', '0'),
('harvehu01', '2019', '1', 'BAL', 'AL', '1', '0', '7', '0', '0', '0', '0', '19', '3', '1', '1', '4', '11', '0.136', '1.42', '0', '0', '0', '0', '26', '1', '1', '0', '0', '0'),
('harvejo01', '2019', '1', 'NYA', 'AL', '1', '0', '9', '0', '0', '0', '0', '30', '11', '5', '1', '7', '11', '0.282', '4.50', '0', '0', '1', '0', '48', '4', '6', '0', '1', '2'),
('harvejo01', '2019', '2', 'COL', 'NL', '0', '0', '9', '0', '0', '0', '0', '24', '7', '5', '2', '6', '6', '0.241', '5.63', '0', '0', '1', '0', '36', '3', '5', '0', '0', '1'),
('harvema01', '2019', '1', 'LAA', 'AL', '3', '5', '12', '12', '0', '0', '0', '179', '63', '47', '13', '29', '39', '0.275', '7.09', '0', '3', '3', '0', '266', '0', '48', '1', '4', '5'),
('heanean01', '2019', '1', 'LAA', 'AL', '4', '6', '18', '18', '0', '0', '0', '286', '93', '52', '20', '30', '118', '0.251', '4.91', '1', '4', '7', '0', '409', '0', '53', '0', '2', '5'),
('hearnta01', '2019', '1', 'TEX', 'AL', '0', '1', '1', '1', '0', '0', '0', '1', '3', '4', '0', '4', '0', '0.750', '108.00', '0', '0', '0', '0', '8', '0', '5', '0', '0', '0'),
('hellebe01', '2019', '1', 'NYA', 'AL', '0', '0', '6', '0', '0', '0', '0', '22', '6', '1', '1', '3', '9', '0.250', '1.23', '1', '0', '0', '0', '28', '1', '1', '1', '0', '2'),
('hellije01', '2019', '1', 'WAS', 'NL', '2', '3', '9', '8', '0', '0', '0', '117', '47', '27', '9', '20', '30', '0.294', '6.23', '1', '1', '1', '0', '183', '1', '31', '1', '1', '4'),
('helslry01', '2019', '1', 'SLN', 'NL', '2', '0', '24', '0', '0', '0', '0', '110', '34', '12', '5', '12', '32', '0.245', '2.95', '2', '2', '0', '1', '153', '4', '13', '1', '1', '2'),
('hembrhe01', '2019', '1', 'BOS', 'AL', '1', '0', '45', '0', '0', '0', '2', '119', '34', '17', '7', '18', '46', '0.224', '3.86', '2', '2', '3', '0', '173', '14', '20', '0', '0', '0'),
('hendrky01', '2019', '1', 'CHN', 'NL', '11', '10', '30', '30', '1', '1', '0', '531', '168', '68', '19', '32', '150', '0.249', '3.46', '1', '1', '9', '0', '730', '0', '78', '8', '5', '6'),
('hendrli01', '2019', '1', 'OAK', 'AL', '4', '4', '75', '2', '0', '0', '25', '255', '61', '17', '5', '21', '124', '0.201', '1.80', '5', '7', '2', '0', '332', '41', '18', '2', '3', '5'),
('hergeji01', '2019', '1', 'CIN', 'NL', '0', '0', '5', '0', '0', '0', '0', '19', '8', '3', '2', '3', '0', '0.348', '4.26', '0', '0', '0', '0', '26', '4', '3', '0', '0', '1'),
('hernada01', '2019', '1', 'CIN', 'NL', '2', '5', '47', '0', '0', '0', '2', '128', '53', '38', '7', '20', '53', '0.306', '8.02', '3', '1', '1', '0', '198', '8', '39', '1', '3', '3'),
('hernada02', '2019', '1', 'BOS', 'AL', '0', '1', '29', '1', '0', '0', '0', '91', '27', '15', '1', '26', '57', '0.231', '4.45', '1', '4', '3', '0', '147', '2', '18', '1', '0', '1'),
('hernael01', '2019', '1', 'MIA', 'NL', '3', '5', '21', '15', '0', '0', '0', '247', '76', '46', '20', '26', '85', '0.242', '5.03', '1', '2', '9', '1', '353', '1', '49', '3', '1', '4'),
('hernafe02', '2019', '1', 'SEA', 'AL', '1', '8', '15', '15', '0', '0', '0', '215', '85', '51', '17', '25', '57', '0.291', '6.40', '0', '5', '6', '0', '325', '0', '58', '1', '1', '9'),
('hernajo02', '2019', '1', 'TEX', 'AL', '2', '1', '9', '2', '0', '0', '0', '50', '14', '8', '3', '13', '19', '0.219', '4.32', '0', '1', '0', '0', '78', '1', '10', '0', '1', '1'),
('herreke01', '2019', '1', 'CHA', 'AL', '3', '3', '57', '0', '0', '0', '1', '154', '60', '35', '8', '23', '53', '0.288', '6.14', '6', '8', '1', '2', '235', '16', '36', '1', '2', '1'),
('hessda01', '2019', '1', 'BAL', 'AL', '1', '10', '23', '14', '0', '0', '0', '240', '94', '63', '28', '30', '68', '0.287', '7.09', '0', '1', '2', '0', '365', '5', '73', '3', '3', '5'),
('hicksjo03', '2019', '1', 'SLN', 'NL', '2', '2', '29', '0', '0', '0', '14', '86', '16', '10', '2', '11', '31', '0.163', '3.14', '0', '2', '1', '0', '110', '21', '10', '0', '0', '3'),
('hildetr01', '2019', '1', 'MIN', 'AL', '2', '2', '22', '0', '0', '0', '1', '49', '30', '19', '2', '7', '15', '0.395', '10.47', '0', '1', '3', '0', '88', '5', '19', '0', '2', '0'),
('hillri01', '2019', '1', 'LAN', 'NL', '4', '1', '13', '13', '0', '0', '0', '176', '48', '16', '10', '18', '72', '0.223', '2.45', '2', '0', '4', '0', '242', '0', '20', '4', '1', '5'),
('hillti01', '2019', '1', 'KCA', 'AL', '2', '0', '46', '0', '0', '0', '1', '119', '31', '16', '4', '13', '39', '0.217', '3.63', '2', '0', '4', '0', '161', '4', '17', '1', '0', '6'),
('hiranyo01', '2019', '1', 'ARI', 'NL', '5', '5', '62', '0', '0', '0', '1', '159', '51', '28', '7', '22', '61', '0.249', '4.75', '2', '2', '3', '0', '233', '11', '31', '1', '2', '4'),
('hoffmje02', '2019', '1', 'COL', 'NL', '2', '6', '15', '15', '0', '0', '0', '210', '77', '51', '21', '34', '68', '0.283', '6.56', '3', '2', '4', '0', '315', '0', '51', '3', '2', '6'),
('holadbr01', '2019', '1', 'MIA', 'NL', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0.000', '0.00', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0'),
('holdejo02', '2019', '1', 'NYA', 'AL', '5', '2', '34', '1', '0', '0', '0', '124', '43', '29', '8', '11', '46', '0.256', '6.31', '1', '0', '2', '0', '181', '8', '32', '0', '0', '1'),
('hollade01', '2019', '1', 'SFN', 'NL', '2', '4', '31', '7', '1', '0', '0', '206', '68', '45', '17', '35', '71', '0.261', '5.90', '2', '0', '4', '0', '308', '10', '49', '6', '2', '4'),
('hollade01', '2019', '2', 'CHN', 'NL', '0', '1', '20', '1', '0', '0', '0', '47', '14', '12', '3', '10', '11', '0.246', '6.89', '0', '1', '0', '0', '68', '9', '12', '1', '0', '2'),
('hollagr01', '2019', '1', 'ARI', 'NL', '1', '2', '40', '0', '0', '0', '17', '107', '25', '18', '5', '24', '41', '0.198', '4.54', '2', '6', '0', '0', '152', '27', '18', '0', '2', '3'),
('holmecl01', '2019', '1', 'PIT', 'NL', '1', '2', '35', '0', '0', '0', '0', '150', '45', '31', '5', '36', '56', '0.232', '5.58', '1', '4', '9', '0', '240', '10', '36', '0', '0', '4'),
('housead01', '2019', '1', 'MIL', 'NL', '6', '7', '35', '18', '0', '0', '0', '334', '101', '46', '14', '37', '117', '0.244', '3.72', '2', '2', '5', '0', '462', '7', '49', '3', '3', '10'),
('howarsa01', '2019', '1', 'COL', 'NL', '2', '0', '20', '0', '0', '0', '0', '57', '21', '14', '5', '10', '23', '0.276', '6.63', '0', '2', '3', '0', '91', '3', '16', '2', '0', '1'),
('hoytja01', '2019', '1', 'CLE', 'AL', '0', '0', '8', '0', '0', '0', '0', '25', '6', '2', '2', '2', '10', '0.200', '2.16', '0', '0', '0', '0', '32', '2', '2', '0', '0', '0'),
('huangwe01', '2019', '1', 'TEX', 'AL', '0', '0', '4', '0', '0', '0', '0', '17', '8', '2', '0', '5', '2', '0.308', '3.18', '0', '3', '1', '0', '32', '1', '5', '0', '0', '0'),
('hudsoda01', '2019', '1', 'TOR', 'AL', '6', '3', '45', '1', '0', '0', '2', '144', '38', '16', '5', '23', '48', '0.215', '3.00', '0', '1', '3', '0', '207', '11', '18', '1', '3', '2'),
('hudsoda01', '2019', '2', 'WAS', 'NL', '3', '0', '24', '0', '0', '0', '6', '75', '18', '4', '3', '4', '23', '0.200', '1.44', '2', '1', '1', '0', '97', '14', '7', '0', '2', '1'),
('hudsoda02', '2019', '1', 'SLN', 'NL', '16', '7', '33', '32', '0', '0', '1', '524', '160', '65', '22', '86', '136', '0.245', '3.35', '8', '5', '9', '0', '757', '1', '80', '3', '7', '20'),
('hugheja02', '2019', '1', 'CIN', 'NL', '3', '4', '47', '0', '0', '0', '1', '145', '41', '22', '6', '19', '34', '0.236', '4.10', '0', '0', '2', '0', '199', '12', '27', '3', '1', '7');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
