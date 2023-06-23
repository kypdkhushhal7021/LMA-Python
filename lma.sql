-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2023 at 12:25 PM
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
-- Database: `lma`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `classification` varchar(500) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `classification`, `description`, `image`) VALUES
(1, 'Guitar', 'String instrument', 'The guitar is a fretted musical instrument that typically has six strings.\n It is usually held flat against the players body and played by strumming or plucking the strings with \nthe dominant hand', 'Guitar.png'),
(2, 'Piano', 'Simple chordophone', 'The piano is a keyboard instrument that produces sound when pressed on the keys. Most modern pianos have a row of 88 black and white keys: 52 white keys for the notes of the C major scale (C, D, E, F, G, A and B) and 36 shorter black keys raised above the white keys and set further back, for sharps and flats.', 'Piano.jpg'),
(3, 'dholakh', 'single hand', 'khjdg', 'dholakh.jpg'),
(4, 'Flute', 'single hand', 'khjdg', 'flute.png'),
(5, 'Horn', 'single hand', 'khjdg', 'horn.jpg'),
(6, 'Harmonium', 'single hand', 'khjdg', 'sm.jpg'),
(7, 'String', 'single hand', 'khjdg', 'str.jpg'),
(8, 'Tan', 'single hand', 'khjdg', 'tan.jpg'),
(9, 'Tabla', 'single hand', 'khjdg', 'tabla.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `name`) VALUES
('dfg', 'gfh', 'gfh'),
('e@ghjkf.c', 'hjdf', 'kjhde'),
('k@g.com', 'k', 'khushhal'),
('kypd@g.com', 'k', 'kypd'),
('lma@gmail.com', 'lma', 'lma'),
('r@g.com', 'r', 'rohini'),
('Ramya', 'Ramapriya', 'F'),
('rt', 'iu', 'iujh');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
