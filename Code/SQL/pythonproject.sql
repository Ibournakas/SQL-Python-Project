-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Jun 26, 2022 at 01:57 PM
-- Server version: 10.8.3-MariaDB-1:10.8.3+maria~jammy
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `month_to_tons`
--

CREATE TABLE `month_to_tons` (
  `month` int(11) NOT NULL,
  `tons` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `month_to_tons`
--

INSERT INTO `month_to_tons` (`month`, `tons`) VALUES
(12, 56179),
(5, 15374),
(6, 15028),
(7, 14839),
(1, 14697);

-- --------------------------------------------------------

--
-- Table structure for table `type_to_tons`
--

CREATE TABLE `type_to_tons` (
  `type` varchar(100) NOT NULL,
  `tons` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `type_to_tons`
--

INSERT INTO `type_to_tons` (`type`, `tons`) VALUES
('Curb Recycling', 170338),
('Recycled Tires', 3222),
('Misc. Recycling', 41428);

-- --------------------------------------------------------

--
-- Table structure for table `year_to_tons`
--

CREATE TABLE `year_to_tons` (
  `year` int(11) NOT NULL,
  `tons` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `year_to_tons`
--

INSERT INTO `year_to_tons` (`year`, `tons`) VALUES
(2022, 2343),
(2021, 23708),
(2020, 23885),
(2019, 22189),
(2018, 22452),
(2017, 22032),
(2016, 20938),
(2015, 20381),
(2014, 19793),
(2013, 14504),
(2012, 13534),
(2011, 9229);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
