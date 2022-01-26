-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 26, 2022 at 01:55 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `InteriorShop`
--

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `sno` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `number` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `paymentMethod` varchar(200) NOT NULL,
  `total` varchar(200) DEFAULT NULL,
  `productId` varchar(200) DEFAULT NULL,
  `productPrice` varchar(200) DEFAULT NULL,
  `productName` varchar(200) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Id` int(11) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_description` varchar(1000) NOT NULL,
  `product_price` varchar(200) NOT NULL,
  `product_image` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `sold` int(200) DEFAULT NULL,
  `rating` varchar(200) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `shopId` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Id`, `product_name`, `product_description`, `product_price`, `product_image`, `category`, `sold`, `rating`, `date`, `shopId`) VALUES
(25, 'Eden', 'Wooden Double Bed I BDH-358-3-1-20', '27140', 'bed.jpg', 'Furniture', 300, '0', '2022-01-26 01:04:00.110480', 3),
(26, 'wall sticker', 'wall best sticker', '1200', 'wall.jpg', 'Wall decoration', 250, '0', '2022-01-26 01:07:08.529924', 3),
(27, 'ardunio', 'best ardunio', '750tk', 'Arduino.jpg', 'Electronics', 0, '0', '2022-01-26 01:09:27.395508', 3),
(28, 'Venus', 'Showcase | SCH-103-1-1-20\r\n', '3325', 'sch-103-1-1-20.jpg', 'Furniture', 500, '0', '2022-01-26 16:01:27.038015', 1),
(29, 'wall decoration light', 'House exterior wall lights Ideas | Wall Lighting Design Ideas | Wall Decoration lights', '5000', 'maxresdefault.jpg', 'Electronics', 250, '0', '2022-01-26 16:03:33.366544', 1),
(30, 'Hand Painting', 'man-made hand Painting', '2000', '8304b93b9685370df93cc882de6b6964.jpg', 'Painting', 600, '0', '2022-01-26 16:05:01.940515', 1),
(31, 'Heritage', 'Wooden Dining Set | TDH-333 & CFD-333(6 PCS)', '50000', '3.jpg', 'Furniture', 0, '0', '2022-01-26 17:57:49.833101', 2),
(32, 'White One Piece Toilet Seat', 'Contact seller to get latest images & best quotes', '3100', 'untitled-1-500x500.jpg', 'SanitarySystems', 0, '0', '2022-01-26 18:00:02.683709', 2),
(33, 'wall showpice', '\r\n\r\nHandcrafted and Out of Best Wall Hanging Showpiece - Live Enhanced\r\n', '5000', 'hanging-show-piece-5.jpg', 'Wall decoration', 220, '0', '2022-01-26 18:02:14.902165', 2);

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `sno` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `number` varchar(200) NOT NULL,
  `comment` varchar(1000) NOT NULL,
  `date` datetime(6) NOT NULL,
  `productId` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shops`
--

CREATE TABLE `shops` (
  `shopId` int(200) NOT NULL,
  `shopName` varchar(500) NOT NULL,
  `shopImage` varchar(200) NOT NULL DEFAULT 'shopLogo.png',
  `password` varchar(8) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shops`
--

INSERT INTO `shops` (`shopId`, `shopName`, `shopImage`, `password`, `date`) VALUES
(1, 'shop1', 'shopLogo.png', '12345', '2021-11-17 22:00:22.000134'),
(2, 'shop2', 'shopLogo.png', '12345', '2021-11-18 20:49:26.000000'),
(3, 'shop3', 'shopLogo.png', '12345', '2021-11-19 20:49:26.000000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `division` varchar(200) NOT NULL,
  `district` varchar(200) NOT NULL,
  `area` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'userLogo.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `name`, `email`, `phone`, `division`, `district`, `area`, `password`, `date`, `image`) VALUES
(14, 'Mizan', 'dekbovideo@gmail.com', '01862856218', 'Chittagong', 'Chittagong', 'Marium Nagar,Rangunia', '12345', '2022-01-26 18:46:17.435748', 'userLogo.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `test` (`shopId`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`sno`),
  ADD KEY `productId` (`productId`);

--
-- Indexes for table `shops`
--
ALTER TABLE `shops`
  ADD PRIMARY KEY (`shopId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `shops`
--
ALTER TABLE `shops`
  MODIFY `shopId` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
