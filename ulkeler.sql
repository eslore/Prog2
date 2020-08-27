-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 27 Ağu 2020, 20:00:43
-- Sunucu sürümü: 10.1.38-MariaDB
-- PHP Sürümü: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `ulkeler`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ulke`
--

CREATE TABLE `ulke` (
  `ulkee` text COLLATE utf8_turkish_ci NOT NULL,
  `yil15` float NOT NULL,
  `yil16` float NOT NULL,
  `yil17` float NOT NULL,
  `yil18` float NOT NULL,
  `yil19` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `ulke`
--

INSERT INTO `ulke` (`ulkee`, `yil15`, `yil16`, `yil17`, `yil18`, `yil19`) VALUES
('Türkiye', 2.8, 1.9, 3.2, 5.1, 5.1),
('Hindistan', 1.1, 2.1, 3.1, 4.1, 4.1),
('İngiltere', 1.5, 3.4, 2.6, 4.7, 4.7),
('Almanya', 7.8, 6.5, 6.4, 7.1, 7.1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
