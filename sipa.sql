-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 11, 2017 at 10:15 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sipa`
--

-- --------------------------------------------------------

--
-- Table structure for table `gejala`
--

CREATE TABLE `gejala` (
  `kode_g` varchar(30) NOT NULL,
  `gejala` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `gejala`
--

INSERT INTO `gejala` (`kode_g`, `gejala`) VALUES
('G001', 'Kelopak mata merah'),
('G002', 'Kelopak Mata Membengkak'),
('G003', 'Mata Terasa Sakit dan Gatal '),
('G004', 'Kotoran mata lengket dan bergantungan pada bulu mata'),
('G005', 'Rasa menjanggal dan sakit pada mata'),
('G006', 'Nyeri bila ditekan'),
('G007', 'Benjolan pada kelopak mata dalam beberapa minggu '),
('G008', 'Tidak nyeri pada saat ditekan '),
('G009', 'Terdapat sedikit kotoran pada mata'),
('G010', 'Mata merah'),
('G011', 'Mata sedikit gatal dan nyeri'),
('G012', 'Tenggorakan sakit dan demam'),
('G013', 'Mata gatal'),
('G014', 'Mata membengkak dan sakit'),
('G015', 'Mata berair'),
('G016', 'Mata terasa silau'),
('G017', 'Mata merasa kelilipan'),
('G018', 'Mata nyeri'),
('G019', 'Penglihatan menurun'),
('G020', 'Terasa sakit ringan hingga berat '),
('G021', 'Mata kotor'),
('G022', 'Rasa sakit berat'),
('G023', 'Mata bengkak susah dibuka');

-- --------------------------------------------------------

--
-- Table structure for table `penyakit`
--

CREATE TABLE `penyakit` (
  `kode_p` varchar(30) NOT NULL,
  `nama` varchar(45) NOT NULL,
  `penyebab` varchar(200) NOT NULL,
  `pengobatan` text NOT NULL,
  `pencegahan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `penyakit`
--

INSERT INTO `penyakit` (`kode_p`, `nama`, `penyebab`, `pengobatan`, `pencegahan`) VALUES
('P01', 'Blefaritis', 'Di sebebkan alergi debu, asap, bahan kimia, dan di sebabkan oleh bakteri stafilikok, streptococcus alpha atau beta hemolyticus', '-Kompres dengan garam fisiologis\r\n-Pemberian antibiotika', '-menjaga kebersihan daerah sekitar \r\n mata dan tangan bila hendak menyentuh \r\n mata.'),
('P02', 'Hordeolum', 'Di sebabkan oelh peradangan superatif kelenjar pada kelopak mata', '-Kompres dengan air hangat\r\n-Berikan antibiotika salep\r\n-Berikan antibiotika sistemik\r\n-Berikan anti nyeri', '-menjaga kebersihan daerah sekitar \r\n mata dan tangan bila hendak menyentuh \r\n mata.\r\n-Menghindari factor-faktor yang \r\n pencetus alergi.'),
('P03', 'Kalazion', 'Di sebabkan oleh peradangan granulomatosis kronis kelenjar meibom yang tersumbat', 'Di berikan insisi', '-menjaga kebersihan daerah sekitar \r\n mata dan tangan bila hendak menyentuh \r\n mata.'),
('P04', 'Konjungtivis Viral', 'Di sebabkan radang konjungtiva yang di sebabkan virus', '-Dengan diberikan sistomatik dan \r\n antibiotika', '-Menjaga kondisi tubuh (kebersihan)\r\n-Menjaga kontak dengan orang yang \r\n sakit mata'),
('P05', 'Konjungtivis Alergi', 'Di sebabkan konjungtiva akibat reaksi alergi terhadap non infeksi', '-Dengan memberikan anti alergi topical \r\n dan sistematik. ', '-menjaga kebersihan daerah sekitar \r\n mata dan tangan bila hendak menyentuh \r\n mata.\r\n-Menghindari faktor yang pencetus \r\n alergi.'),
('P06', 'Keratitis', 'Di sebabkan karena peradangan pada kornea', 'Dengan memberikan air mata buatan, antibiotic dan sikloplegik.', '-Menghindari penggunaan lensa kontak \r\n atau memastikan prosedur pemasangan \r\n dan pelepasan lensa kontak sesuai \r\n aturan. \r\n-Menggunakan pelindung mata saat terus \r\n bekerja terutama yang berkaitan \r\n dengan sinar UV.'),
('P07', 'Ulkus Kornea', 'Merupakan infeksi yang terjadi dari infeksi kuman pathogen batang gram negative pada kornea', 'Di berikan sikloplegik serta \r\nantibiotic topical dan subkonjungtiva.', '-Menggunakan pelindung mata. \r\n-Menghindari penggunaan lensa kontak.'),
('P08', 'Endoftalmitis', 'Di sebabkan akibat infeksi setelah trauma atau bedah, atau endogen akibat sepsis', '-Di opname\r\n-Antibiotika sistemik (infuse/suntik) \r\n-Antibiotica tetes\r\n-Anti nyeri', 'Menjaga kebersihan daerah sekitar mata dan tangan bila hendak menyentuh mata');

-- --------------------------------------------------------

--
-- Table structure for table `rule`
--

CREATE TABLE `rule` (
  `id` int(11) NOT NULL,
  `rules` varchar(45) NOT NULL,
  `penyakit_kode_p` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rule`
--

INSERT INTO `rule` (`id`, `rules`, `penyakit_kode_p`) VALUES
(1, 'G001 G002 G003 G004', 'P01'),
(2, 'G001 G002 G005 G006', 'P02'),
(3, 'G007 G008', 'P03'),
(4, 'G009 G010 G011 G012', 'P04'),
(5, 'G013 G014 G015 G016', 'P05'),
(6, 'G010 G015 G016 G017 G018 G019', 'P06'),
(7, 'G010 G019 G020 G021', 'P07'),
(8, 'G001 G010 G019 G022 G023', 'P08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`kode_g`);

--
-- Indexes for table `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`kode_p`);

--
-- Indexes for table `rule`
--
ALTER TABLE `rule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_rule_penyakit_idx` (`penyakit_kode_p`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rule`
--
ALTER TABLE `rule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `rule`
--
ALTER TABLE `rule`
  ADD CONSTRAINT `fk_rule_penyakit` FOREIGN KEY (`penyakit_kode_p`) REFERENCES `penyakit` (`kode_p`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
