-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 24, 2022 at 07:11 AM
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
  `profit` varchar(200) NOT NULL,
  `productName` varchar(200) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`sno`, `name`, `number`, `email`, `address`, `paymentMethod`, `total`, `productId`, `productPrice`, `profit`, `productName`, `date`, `status`) VALUES
(32, 'Ali Murtuza', '01862816218', 'alimurtuza@gmail.com', 'halisohor', 'Bikash', '50100', '31', '50000', '', 'Heritage', '2022-01-28 18:50:13.464986', '1'),
(33, 'Ali Murtuza', '01862816218', 'alimurtuza@gmail.com', 'halisohor', 'cash on delivery', '3200', '32', '3100', '', 'White One Piece Toilet Seat', '2022-01-28 18:50:57.227135', '0'),
(34, 'Ali Murtuza', '01862816218', 'alimurtuza@gmail.com', 'halisohor', 'Bikash', '5100', '33', '5000', '', 'wall showpice', '2022-01-28 18:51:22.428446', '0'),
(35, 'Ali Murtuza', '01862816218', 'alimurtuza@gmail.com', 'halisohor', 'Bikash', '27240', '25', '27140', '', 'Eden', '2022-01-28 19:00:07.406375', '0'),
(36, 'mizan', '01862856218', 'mizan@gmail.com', 'bnnbn', 'cash on delivery', '3425', '28', '3325', '166.25', 'Venus', '2022-03-24 00:50:57.865721', '0');

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
(25, 'Eden', 'Wooden Double Bed I BDH-358-3-1-20', '27140', 'bed.jpg', 'Furniture', 300, '250', '2022-01-26 01:04:00.110480', 3),
(26, 'wall sticker', 'wall best sticker', '1200', 'wall.jpg', 'Wall decoration', 250, '0', '2022-01-26 01:07:08.529924', 3),
(27, 'ardunio', 'best ardunio', '750tk', 'Arduino.jpg', 'Electronics', 0, '0', '2022-01-26 01:09:27.395508', 3),
(28, 'Venus', 'Showcase | SCH-103-1-1-20\r\n', '3325', 'sch-103-1-1-20.jpg', 'Furniture', 500, '112.9', '2022-01-26 16:01:27.038015', 1),
(29, 'wall decoration light', 'House exterior wall lights Ideas | Wall Lighting Design Ideas | Wall Decoration lights', '5000', 'maxresdefault.jpg', 'Electronics', 250, '0', '2022-01-26 16:03:33.366544', 1),
(30, 'Hand Painting', 'man-made hand Painting', '2000', '8304b93b9685370df93cc882de6b6964.jpg', 'Painting', 600, '29.2', '2022-01-26 16:05:01.940515', 1),
(31, 'Heritage', 'Wooden Dining Set | TDH-333 & CFD-333(6 PCS)', '50000', '3.jpg', 'Furniture', 0, '0', '2022-01-26 17:57:49.833101', 2),
(32, 'White One Piece Toilet Seat', 'Contact seller to get latest images & best quotes', '3100', 'untitled-1-500x500.jpg', 'SanitarySystems', 0, '40', '2022-01-26 18:00:02.683709', 2),
(33, 'wall showpice', '\r\n\r\nHandcrafted and Out of Best Wall Hanging Showpiece - Live Enhanced\r\n', '5000', 'hanging-show-piece-5.jpg', 'Wall decoration', 220, '0', '2022-01-26 18:02:14.902165', 2),
(35, 'xzmznxmz', 'zx xz x ', 'zx zxzxzxz', 'bed.jpg', 'Furniture', 0, '0', '2022-03-23 23:48:25.669983', 8);

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

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`sno`, `name`, `email`, `number`, `comment`, `date`, `productId`) VALUES
(24, 'Ali Murtuza', 'alimurtuza@gmail.com', '01862816218', 'good product\r\n', '2022-01-28 18:57:33.313903', 25),
(25, 'Ali Murtuza', 'alimurtuza@gmail.com', '01862816218', 'good product', '2022-02-05 15:22:36.731518', 28),
(26, 'Ali Murtuza', 'alimurtuza@gmail.com', '01862816218', '', '2022-02-05 19:47:03.331418', 30);

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
(3, 'shop3', 'shopLogo.png', '12345', '2021-11-19 20:49:26.000000'),
(7, 'shop4', 'shopLogo.png', '12345', '2022-02-27 21:52:23.609302'),
(8, 'shop1', 'shopLogo.png', '12345678', '2022-03-23 23:12:47.860329');

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
(14, 'Ali Murtuza', 'alimurtuza@gmail.com', '01862816218', 'Chittagong', 'Chittagong', 'halisohor', '12345', '2022-01-26 18:46:17.435748', 'Screenshot from 2021-12-16 19-35-34.png'),
(15, 'mizan', 'mizan@gmail.com', '01862856218', 'Chittagong', 'Chittagong', 'Halisohor', '12345678', '2022-02-27 21:43:49.904207', 'userLogo.png');

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
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `shops`
--
ALTER TABLE `shops`
  MODIFY `shopId` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
