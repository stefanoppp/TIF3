-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-06-2024 a las 00:08:26
-- Versión del servidor: 8.0.35
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `datasettif`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos`
--

CREATE TABLE `datos` (
  `id` int NOT NULL,
  `fecha` date NOT NULL,
  `aceitunas` float(10,2) NOT NULL,
  `inflacion` float(10,2) NOT NULL,
  `precio` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `datos`
--

INSERT INTO `datos` (`id`, `fecha`, `aceitunas`, `inflacion`, `precio`) VALUES
(1, '2017-04-17', 0.00, 3.14, 146),
(2, '2018-01-14', 0.00, 1.76, 146),
(3, '2018-02-05', 0.00, 2.42, 146),
(4, '2018-03-18', 0.00, 2.34, 146),
(5, '2018-04-11', 0.00, 2.74, 190),
(6, '2018-05-25', 37.26, 2.08, 190),
(7, '2018-06-15', 260.85, 3.74, 190),
(8, '2018-07-30', 72.56, 3.10, 190),
(9, '2018-08-20', 0.00, 3.89, 190),
(10, '2018-09-29', 0.00, 6.53, 210),
(11, '2018-10-13', 0.00, 5.39, 210),
(12, '2018-11-18', 0.00, 3.15, 210),
(13, '2018-12-10', 0.00, 2.57, 250),
(14, '2019-01-14', 0.00, 2.91, 250),
(15, '2019-02-06', 0.00, 3.77, 280),
(16, '2019-03-03', 0.00, 4.68, 280),
(17, '2019-04-22', 0.00, 3.44, 290),
(18, '2019-05-08', 53.49, 3.06, 310),
(19, '2019-06-30', 234.10, 2.72, 310),
(20, '2019-07-18', 88.71, 2.20, 310),
(21, '2019-08-14', 0.00, 3.95, 310),
(22, '2019-09-25', 0.00, 5.89, 360),
(23, '2019-10-24', 0.00, 3.29, 360),
(24, '2019-11-05', 0.00, 4.25, 360),
(25, '2019-12-17', 0.00, 3.47, 360),
(26, '2020-01-30', 0.00, 2.25, 430),
(27, '2020-02-09', 0.00, 2.01, 430),
(28, '2020-03-06', 0.00, 3.34, 430),
(29, '2020-04-06', 0.00, 1.50, 430),
(30, '2020-05-15', 70.21, 1.54, 430),
(31, '2020-06-19', 279.73, 2.24, 430),
(32, '2020-07-14', 49.58, 1.93, 480),
(33, '2020-08-15', 0.00, 2.70, 480),
(34, '2020-09-08', 0.00, 2.84, 480),
(35, '2020-10-31', 0.00, 3.76, 530),
(36, '2020-11-07', 0.00, 3.16, 530),
(37, '2020-12-13', 0.00, 4.01, 530),
(38, '2021-01-29', 0.00, 4.04, 530),
(39, '2021-02-22', 0.00, 3.57, 530),
(40, '2021-03-26', 0.00, 4.81, 600),
(41, '2021-04-27', 0.00, 4.08, 600),
(42, '2021-05-12', 74.96, 3.32, 600),
(43, '2021-06-21', 226.65, 3.17, 690),
(44, '2021-07-13', 80.19, 3.00, 730),
(45, '2021-08-25', 0.00, 2.47, 730),
(46, '2021-09-04', 0.00, 3.55, 750),
(47, '2021-10-29', 0.00, 3.52, 750),
(48, '2021-11-16', 0.00, 2.53, 750),
(49, '2021-12-17', 0.00, 3.84, 930),
(50, '2022-01-10', 0.00, 3.88, 930),
(51, '2022-02-26', 0.00, 4.69, 1050),
(52, '2022-03-11', 0.00, 6.73, 1050),
(53, '2022-04-24', 0.00, 6.05, 1050),
(54, '2022-05-18', 36.45, 5.05, 1150),
(55, '2022-06-17', 248.09, 5.30, 1150),
(56, '2022-07-12', 92.00, 7.41, 1300),
(57, '2022-08-26', 0.00, 6.97, 1300),
(58, '2022-09-28', 0.00, 6.17, 1300),
(59, '2022-10-02', 0.00, 6.35, 1450),
(60, '2022-11-27', 0.00, 4.92, 1450),
(61, '2022-12-11', 0.00, 5.12, 1450),
(62, '2023-01-23', 0.00, 6.03, 1600),
(63, '2023-02-16', 0.00, 6.63, 1850),
(64, '2023-03-18', 0.00, 7.68, 1850),
(65, '2023-04-15', 0.00, 8.40, 2200),
(66, '2023-05-22', 43.90, 7.77, 2300),
(67, '2023-06-10', 293.95, 5.95, 2300),
(68, '2023-07-17', 66.02, 6.34, 2700),
(69, '2023-08-11', 0.00, 12.44, 3700),
(70, '2023-09-02', 0.00, 12.75, 4400),
(71, '2023-10-22', 0.00, 8.30, 4800),
(72, '2023-11-08', 0.00, 12.81, 6300),
(73, '2023-12-29', 0.00, 25.47, 9700),
(74, '2024-01-18', 0.00, 20.61, 12500),
(75, '2024-02-01', 0.00, 13.24, 15000),
(76, '2024-03-08', 0.00, 11.01, 15000),
(131, '2024-04-29', 0.00, 8.80, 15000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos`
--
ALTER TABLE `datos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos`
--
ALTER TABLE `datos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
