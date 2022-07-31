-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2022 at 11:00 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `messmenu`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminid` varchar(30) COLLATE utf8_bin NOT NULL,
  `adminpass` varchar(30) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminid`, `adminpass`) VALUES
('admin@gmail.com', 'admin@123');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cid` int(11) NOT NULL,
  `cname` varchar(30) COLLATE utf8_bin NOT NULL,
  `cemail` varchar(30) COLLATE utf8_bin NOT NULL,
  `cmobile` varchar(10) COLLATE utf8_bin NOT NULL,
  `caddress` varchar(50) COLLATE utf8_bin NOT NULL,
  `cpass` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cid`, `cname`, `cemail`, `cmobile`, `caddress`, `cpass`) VALUES
(1, 'shubham', 'shu@gmail.com', '8888528529', 'pune', '123456'),
(4, 'Onkar Kulkarni', 'onkar@gmail.com', '7350765566', 'Pune', '12345'),
(5, 'Shripad Kulkarni', 'shripad@gmail.com', '7350636655', 'SIMCA', 'Shri@12345');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `mno` int(11) NOT NULL,
  `messemail` varchar(30) COLLATE utf8_bin NOT NULL,
  `items` varchar(200) COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`mno`, `messemail`, `items`, `price`) VALUES
(22, 'chinta@gmail.com', 'Chapati,Chole Bhaji,Mataki Bhaji,Rice,Dal,Papad,Gulab jamun,', 60),
(23, 'gharchiathvan@gmail.com', 'Puri,Chole Bhaji,Kopta Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Jilebi,', 60),
(24, 'rohini@gmail.com', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 50),
(25, 'umaya@gmail.com', 'Chapati,Batata Bhaji,Paneer Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Basundi,', 80);

-- --------------------------------------------------------

--
-- Table structure for table `mess`
--

CREATE TABLE `mess` (
  `messid` int(11) NOT NULL,
  `messname` varchar(50) COLLATE utf8_bin NOT NULL,
  `ownername` varchar(30) COLLATE utf8_bin NOT NULL,
  `messemail` varchar(30) COLLATE utf8_bin NOT NULL,
  `messmobile` varchar(10) COLLATE utf8_bin NOT NULL,
  `messpassword` varchar(20) COLLATE utf8_bin NOT NULL,
  `messaddress` text COLLATE utf8_bin NOT NULL,
  `messphoto` varchar(30) COLLATE utf8_bin NOT NULL,
  `messlocation` varchar(25) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `mess`
--

INSERT INTO `mess` (`messid`, `messname`, `ownername`, `messemail`, `messmobile`, `messpassword`, `messaddress`, `messphoto`, `messlocation`) VALUES
(5, 'Chintamani', 'Chintaman', 'chinta@gmail.com', '8574635241', 'Zxcvbnm@123', 'Sinhgad College , Pune', '9.jpg', '18.4651194,73.8353216'),
(6, 'Gharchi Athavan', 'S. K. Patil', 'gharchiathvan@gmail.com', '9874563214', 'Asdfghjkl@123', 'Sinhgad Institute of Management, Pune', '5.jpg', '18.4651194,73.8353216'),
(7, 'Rohini Mess', 'Aaji', 'rohini@gmail.com', '9876543210', 'Qwerty@123', 'Stanza Living , Pune', '4.jpg', '18.4651194,73.8353216'),
(8, 'Umaya Mess', 'Gujarati', 'umaya@gmail.com', '9876543210', 'Umaya@123', 'Sinhgad Institute of Management, Pune', 'umaya mess.jpeg', '18.4651194,73.8353216');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `oid` int(11) NOT NULL,
  `odate` varchar(30) COLLATE utf8_bin NOT NULL,
  `otime` varchar(10) COLLATE utf8_bin NOT NULL,
  `nooftiffeen` int(11) NOT NULL,
  `oprice` int(11) NOT NULL,
  `cname` varchar(30) COLLATE utf8_bin NOT NULL,
  `cemail` varchar(30) COLLATE utf8_bin NOT NULL,
  `mobile` varchar(10) COLLATE utf8_bin NOT NULL,
  `messemail` varchar(30) COLLATE utf8_bin NOT NULL,
  `messname` varchar(50) COLLATE utf8_bin NOT NULL,
  `menu` varchar(200) COLLATE utf8_bin NOT NULL,
  `address` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`oid`, `odate`, `otime`, `nooftiffeen`, `oprice`, `cname`, `cemail`, `mobile`, `messemail`, `messname`, `menu`, `address`) VALUES
(1, '0000-00-00', '04:29:00', 4, 320, 'shubham', 'onkar@gmail.com', '7350636655', 'umaya@gmail.com', 'Umaya Mess', 'Chapati,Batata Bhaji,Paneer Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Basundi,', 'siom'),
(2, '0000-00-00', '04:30:00', 4, 320, 'shubham', 'onkar@gmail.com', '7350636655', 'umaya@gmail.com', 'Umaya Mess', 'Chapati,Batata Bhaji,Paneer Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Basundi,', 'siom'),
(3, 'Sat,30 Jul', '04:58 PM', 8, 400, 'shubham', 'shu@gmail.com', '2589654512', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra), Tal.- Karmala'),
(4, 'Sat,30 Jul', '05:38 PM', 4, 240, 'Onkar Kulkarni', 'onkar@gmail.com', '9458426532', 'gharchiathvan@gmail.com', 'Gharchi Athavan', 'Puri,Chole Bhaji,Kopta Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Jilebi,', 'narhe'),
(5, 'Sat,30 Jul', '05:46 PM', 4, 240, 'Onkar Kulkarni', 'onkar@gmail.com', '9458426532', 'gharchiathvan@gmail.com', 'Gharchi Athavan', 'Puri,Chole Bhaji,Kopta Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Jilebi,', 'narhe'),
(6, 'Sun,31 Jul', '10:42 AM', 4, 240, 'Shripad Kulkarni', 'shripad@gmail.com', '7350636655', 'gharchiathvan@gmail.com', 'Gharchi Athavan', 'Puri,Chole Bhaji,Kopta Bhaji,Masala Rice,Papad,Koshimbir,Lonche,Jilebi,', 'SIMCA'),
(7, 'Sun,31 Jul', '11:12 AM', 4, 200, 'shubham', 'shripad@gmail.com', '7350636655', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra)'),
(8, 'Sun,31 Jul', '12:29 PM', 1, 50, 'shubham', 'shripad@gmail.com', '7350636655', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra), Tal.- Karmala, D'),
(9, 'Sun,31 Jul', '12:30 PM', 3, 150, 'shubham', 'shripad@gmail.com', '2589654512', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra), Tal.- Karmala, D'),
(10, 'Sun,31 Jul', '12:42 PM', 9, 450, 'shubham', 'shripad@gmail.com', '7350636655', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra), Tal.- Karmala,'),
(11, 'Sun,31 Jul', '12:53 PM', 1, 50, 'shubham', 'shripad@gmail.com', '7350636655', 'rohini@gmail.com', 'Rohini Mess', 'Chapati,Bengan Bharata,Mataki Bhaji,Rice,Dal,Koshimbir,Lonche,Fruit Salad,', 'At.- Khatgoan, Post.- Takali(Ra), Tal.- Karmala, D');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`mno`);

--
-- Indexes for table `mess`
--
ALTER TABLE `mess`
  ADD PRIMARY KEY (`messid`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`oid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `mno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `mess`
--
ALTER TABLE `mess`
  MODIFY `messid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
