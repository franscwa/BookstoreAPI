-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 01, 2023 at 03:17 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `publication_year` int(11) DEFAULT NULL,
  `rating` float NOT NULL,
  `copies_sold` int(11) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `publisher` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `title`, `author`, `genre`, `publication_year`, `rating`, `copies_sold`, `price`, `publisher`) VALUES
(1, 'The House of the Spirits', 'Isabel Allende', 'magical realism', 1982, 3, 100, '9', 'Harper Collins'),
(2, 'The Handmaids Tale', 'Margaret Atwood', 'science fiction', 1985, 4, 70, '9', 'Harper Collins'),
(3, 'In Mad Love and War', 'Joy Harjo', 'poetry', 1990, 5, 90, '12', 'Simon & Schuster'),
(4, 'Invisible Man', 'Ralph Ellison', 'fiction', 1952, 4, 80, '13', 'Simon & Schuster'),
(5, 'Howl and Other Poems', 'Allen Ginsberg', 'poetry', 1956, 2, 40, '14', 'Macmillan'),
(6, 'Bodega Dreams', 'Ernesto Quiñonez', 'fiction', 2000, 2, 44, '15', 'Macmillan'),
(7, 'Things Fall Apart', 'Chinua Achebe', 'historical fiction', 1958, 4, 66, '16', 'Macmillan'),
(8, 'The Three-Body Problem', 'Liu Cixin', 'science fiction', 2008, 3, 32, '17', 'Hachette'),
(9, 'A Wizard of Earthsea', 'Ursula K. Le Guin', 'fantasy', 1968, 2, 40, '18', 'Hachette'),
(10, 'The Stone Sky', 'N. K. Jemisin', 'fantasy', 2017, 4, 40, '19', 'Penguin Random House'),
(11, 'The Hobbit', 'J.R.R. Tolkien', 'fantasy', 1937, 1, 10, '20', 'Penguin Random House'),
(12, 'Unaccustomed Earth', 'Jhumpa Lahiri', 'fiction', 2008, 3, 54, '21', 'Penguin Random House');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
