-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 14, 2021 at 10:06 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

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
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Id` int(11) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_description` varchar(1000) NOT NULL,
  `product_price` varchar(200) NOT NULL,
  `product_image` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `sold` int(200) NOT NULL,
  `rating` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Id`, `product_name`, `product_description`, `product_price`, `product_image`, `category`, `sold`, `rating`, `date`) VALUES
(1, 'aufers ® Oscar Food Grade Salt/Pepper/Pickle Set with Stand for Kitchen/Dining/Transparent/Wooden Design_Plastic 4 Piece Salt & Pepper Set (Plastic)', 'Buy the Original Herostyle Budget Friendly Sofa from Furny\r\nPerfectly practical and strikingly stylish, the Herostyle 3 seater sofa is the must have for every modern home. This sofa is crafted from good-quality solid wood which makes it durable and ensures that you enjoy those comfy moments on it for years to come. This sofa has a fixed seat which means you won’t have to worry about dust settling in or losing small items in the fold. You can arrange the back cushions as you want. Also Lifestyle sectional sofa saves plenty of space, so you can walk around freely.', '10000', 'product1.jpg', 'furniture', 200, '13', '2021-09-01 06:19:16.000000'),
(2, 'Furny Herostyle 3 Seater Fabric Sofa Set (Grey-Black)', '4 Door Wardrobe with a drawer and multiple shelves for organising clothes and storage\r\nProduct Dimensions:- Length: 150 cm (59.05 inches); Width: 45 cm (17.72 inches); Height: 183 cm (72.05 inches)\r\nManufactured using premium-quality engineered wood which offers sturdiness and durability\r\nContemporary design and long-lasting, smooth walnut finish gives a classy look\r\nSpaciously designed 4-door wardrobe for ample spacing, includes multiple shelves, hanging storage and a lockable drawer for efficient organisation\r\nDoor action tested thoroughly for over 10,000 cycles and drawer action of up to 5,000 cycles to ensure longevity\r\nConsists of a lockable drawer for storing your valuables, personal items, documents and more\r\nHigher load-bearing capacity of up to 95kg for large compartments and 45kg for the drawer\r\nRust-resistant hardware; 15 mm thick board adds to the robustness of the structure\r\nTested for stability with a tip-over test to prevent toppling over and assured safety\r\nSmooth edges', '155000', 'product.jpg', 'furniture', 500, '21', '2021-09-02 00:27:16.000000'),
(3, 'GODREJ INTERIO Squadro Engineered Wood Matte Finish 4-Door Wardrobe with Mirror (Cinnamon)', 'Dimensions W x H x D (cm) 180 x 201.3 x 59.9 / Primary Material: Particle Board/ Delivery Condition: Knock Down, Free Assembly Provided\r\nCompact Design:A no-frills affair, this wardrobe is compact in its structure, making it an ideal piece for apartments as well as bigger homes.\r\nPolished Cinnamon Finish:The cinnamon shade and polished look fuse together to create a sleek unit, that is sure to pair well with the rest of your furnishings.\r\nParticle Board Construct:The material of a wardrobe plays an important role. The particle board make is lightweight, which makes it easy to move around, especially when you want to change the layout of your room.\r\nWarranty:1 Year ,Contact on 1800 - 267 1122, and our contact center will log a service call.', '140000', 'product3.jpg', 'furniture', 17, '22', '2021-09-02 00:32:48.000000'),
(4, 'Nilkamal Freedom Mini Medium Plastic Cabinet Brown', 'Product Dimensions: (W x D x H) 59.5 x 35.5 x 123 cm\r\nPrimary Material: Plastic; Color: Weather Brown, Style: Contemporary ; It is divided into multiple separate compartments in a neat pattern so that various items can be sorted according to their usage and are easy to be found\r\nAssembly Required: The product requires basic assembly and comes with assembly instructions\r\nNumber of Shelves: 4; Can be used anywhere in house; Multipurpose corner cabinet , Care & Instructions : Wipe with clean dry cloth, Locking Facility - Yes\r\nWarranty: 1 year warranty on manufacturing defects', '10000', 'product4.jpg', 'furniture', 500, '21', '2021-09-03 00:35:59.000000'),
(5, 'HomeTown Chester Plus Fabric Two Seater Sofa in Beige Color', 'Product Dimension: Depth 880 mm, Width 1410 mm, Height 850 mm\r\nProduct Colour: Beige\r\nAssembly If Required, Would be provided by Seller without any cost. Seller will get in touch for assembly post product delivery.', '28000', 'product5.jpg', 'furniture', 22, '70', '2021-09-04 00:48:36.000000'),
(6, 'HomeTown Paddington Plus Fabric Two Sofa in Brown Color', 'Product Dimension: Depth 825 mm, Width 1409 mm, Height 870 mm\r\nProduct Colour: Brown\r\nAssembly If Required, Would be provided by Seller without any cost. Seller will get in touch for assembly post product delivery.', '20000', 'product6.jpg', 'furniture', 24, '100', '2021-09-04 00:50:28.000000'),
(7, 'WebelKart Pair of Kissing Duck Showpiece - 29 cm (Aluminium, Golden )', 'Best For Home Decor', '5000', 'product7.jpg', 'showpics', 400, '200', '2021-09-05 00:52:09.000000'),
(8, '\r\nNilkamal Gem Plastic Cabinet with Mirror (Ivory), Standard (GEMMCABINETIVR)', 'Primary Material: Plastic\r\nColor: Ivory, Style: Modern, Pack Content: Single Pack\r\nAssembly Required: Product requires assembly and comes with assembly instructions\r\nWarranty: 6 months spare part replacement warranty\r\nProvides versatile storage solution for small miscellaneous items. Care & Instructions : Wipe with clean dry cloth', '250000', 'product8.jpg', 'showpics', 300, '31', '2021-09-05 00:54:19.000000'),
(9, 'Wolpin Kitchen Wall Stickers Wood Wallpaper DIY PVC Shelf Liner, Furniture, Almirah, Table Top, Wardrobe, Kitchen Cupboard Decal, Mahogany Brown', 'WOOD FURNITURE SHELF LINER, MULTI-USE: This wood self-adhesive furniture wallpaper is ideal to decorate or upgrade renovate old furniture, fridge/refrigerator, kitchen cabinets, drawers, bed, office table, wardrobe, desk, door, laminate or decorate even the walls of bedroom, living room, hall, study, office, restaurants, glass etc. Can be applied on smooth putty wall and tiles as well.\r\nMATERIAL: PVC Vinyl ROLL SIZE: Large Size in cms: 45 x 300 cm [Need 7 Rolls to cover a 10 ft by 10 ft Wall Size.]\r\nSAFE & REMOVABLE: This wood decorative stickers wall paper is Removable, Waterproof, Heat resistant, Oil-resistant, Re-positionable and Eco-friendly. Wolpin wood wall decal is made with high quality eco and durable PVC film material. Accent the furniture in your house with this natural wood sicker. Our wallpaper will last for years without fading.\r\nJUST PEEL & STICK: Quick & easy to apply! This wall paper can be applied to any smooth, clean and dry Surface. There are gridlines on the back f', '350 ', 'product9.jpg', 'showpics', 1400, '32', '2021-09-05 00:56:16.000000'),
(10, 'Wolpin Wall Stickers Marble Wallpaper Furniture Kitchen, Cabinets, Almirah, Tabletop, Plastic Table, Wooden Table, Wardrobe, Renovation PVC DIY Self Adhesive, Pearl White', 'HOME DECOR, MULTI-USE: This decorative marble self-adhesive pvc wallpaper is ideal to decorate or renovate kitchen counter tops, cupboard, shelf liner, furniture, dining table, centre table, home/office desk, side tables, almirah, fridge, drawers, lamination, wall of bedroom, living room, hall, kitchen, bathroom, kids room, play room, nursery, study, office, restaurants, etc.\r\nMATERIAL: PVC Vinyl ROLL SIZE: Large Size in cms: 60 x 300 cm [Need 6 Rolls to cover a 10 ft by 10 ft Wall Size.]\r\nSAFE FOR WALLS: This matte marble decorative stickers contact paper is Removable, Waterproof, Heat resistant, Oil-resistant, Re-positionable and Eco-friendly. Wolpin marble effect wall decal is made with High quality Eco and durable PVC material. Accent the wall, kitchen, furniture and bathroom in your home with this bright, lively wallpaper.\r\nJUST PEEL & STICK: Easy to apply! This wall paper can be applied to any smooth, clean and dry Surface. There are gridlines on the back for easy measurement and', '350', 'product10.jpg', 'showpics', 300, '150', '2021-09-06 00:56:16.000000');

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
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `name`, `email`, `phone`, `division`, `district`, `area`, `password`, `date`) VALUES
(1, 'Abdullah Al Mizan', 'abdullahalmizan644@gmail.com', '01862856218', 'Chittagong', 'Rangunia', 'Marium Nagar,Rangunia', '54321', '2021-09-28 22:26:04.926741'),
(2, 'esha123', 'esha@gmail.com', '01862856218', 'Chittagong', 'Rangunia', 'Marium Nagar,Rangunia', '54321', '2021-09-28 22:27:58.042724'),
(4, 'Ali', 'ali@gmail.com', '01862856218', 'Chittagong', 'Chittagong', 'Halisohor', '12345678', '2021-10-07 22:41:05.940095');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
