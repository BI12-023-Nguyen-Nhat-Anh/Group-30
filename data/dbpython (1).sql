-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2023 at 04:54 PM
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
-- Database: `dbpython`
--

-- --------------------------------------------------------

--
-- Table structure for table `billingandpayments`
--

CREATE TABLE `billingandpayments` (
  `ID` varchar(20) NOT NULL,
  `CustomerID` varchar(20) DEFAULT NULL,
  `BillingDate` date DEFAULT NULL,
  `DueDate` date DEFAULT NULL,
  `BillingAmount` decimal(10,2) DEFAULT NULL,
  `LateFee` decimal(10,2) DEFAULT NULL,
  `TotalBill` decimal(10,2) DEFAULT NULL,
  `PaymentDate` date DEFAULT NULL,
  `PaymentAmount` decimal(10,2) DEFAULT NULL,
  `Status` enum('paid','overdue') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ID` varchar(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `ResidentialAddress` varchar(100) DEFAULT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `AccountBalance` decimal(10,2) DEFAULT 0.00,
  `TaxCode` varchar(20) NOT NULL,
  `Type` enum('Household','Manufacturing_industries','Administrative_offices','Business') NOT NULL,
  `Status` enum('Online','Offline') NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ID`, `Name`, `Address`, `ResidentialAddress`, `PhoneNumber`, `Email`, `AccountBalance`, `TaxCode`, `Type`, `Status`, `Password`) VALUES
('CA001203008874', 'Tran Thi B', '75 Dinh Tien Hoang, Hoan Kiem, Ha Noi', '', '555-345-6789', 'tranthib@example.com', '2500.00', '0107011013', 'Administrative_offices', 'Online', 'TTB@9012'),
('CA001203008878', 'Do Thi F', '17 Tran Phu, Hoan Kiem, Ha Noi', '', '555-789-0123', 'dothif@example.com', '700.00', '0107011017', 'Administrative_offices', 'Offline', 'DTF@5678'),
('CB001203008875', 'Pham Van C', '20 Hang Bong, Hoan Kiem, Ha Noi', '', '555-456-7890', 'phamvanc@example.com', '100000.00', '0107011014', 'Business', 'Online', 'PVC@3456'),
('CH001203008872', 'Le Thu Phuong', '19 Hoang Quoc Viet, Cau Giay, Ha Noi', '', '555-123-4567', 'someone@example.com', '500.00', '0107011011', 'Household', 'Online', 'LTP@1234'),
('CH001203008876', 'Le Thi D', '16 Kim Ma, Ba Dinh, Ha Noi', '', '555-567-8901', 'lethid@example.com', '300.00', '0107011015', 'Household', 'Offline', 'LTD@6789'),
('CM001203008873', 'Nguyen Van A', '72 Tran Duy Hung, Cau Giay, Ha Noi', '', '555-234-5678', 'nguyenvana@example.com', '12000.00', '0107011012', 'Manufacturing_industries', 'Offline', 'NVA@5678'),
('CM001203008877', 'Phan Van E', '35 Tran Thai Tong, Cau Giay, Ha Noi', '', '555-678-9012', 'phanvane@example.com', '24000.00', '0107011016', 'Manufacturing_industries', 'Online', 'PVE@1234');

-- --------------------------------------------------------

--
-- Table structure for table `electricityconsumption`
--

CREATE TABLE `electricityconsumption` (
  `ID` varchar(20) NOT NULL,
  `CustomerID` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  `ConsumptionAmount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `meterreading`
--

CREATE TABLE `meterreading` (
  `ID` varchar(20) NOT NULL,
  `CustomerID` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  `ReadingAmount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billingandpayments`
--
ALTER TABLE `billingandpayments`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `electricityconsumption`
--
ALTER TABLE `electricityconsumption`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Indexes for table `meterreading`
--
ALTER TABLE `meterreading`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `billingandpayments`
--
ALTER TABLE `billingandpayments`
  ADD CONSTRAINT `billingandpayments_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`);

--
-- Constraints for table `electricityconsumption`
--
ALTER TABLE `electricityconsumption`
  ADD CONSTRAINT `electricityconsumption_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`);

--
-- Constraints for table `meterreading`
--
ALTER TABLE `meterreading`
  ADD CONSTRAINT `meterreading_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
