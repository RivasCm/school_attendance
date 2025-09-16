-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-09-2025 a las 02:04:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `school_attendance_ai`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `colegio_curso`
--

CREATE TABLE `colegio_curso` (
  `id` int(11) NOT NULL,
  `nombre_curso` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `colegio_materia`
--

CREATE TABLE `colegio_materia` (
  `id` int(11) NOT NULL,
  `nombre_materia` varchar(100) NOT NULL,
  `id_curso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacion_asistencia`
--

CREATE TABLE `evaluacion_asistencia` (
  `id` int(11) NOT NULL,
  `fecha_clase` date NOT NULL,
  `estado` varchar(1) NOT NULL,
  `id_alumno_id` int(11) NOT NULL,
  `id_materia_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacion_nota`
--

CREATE TABLE `evaluacion_nota` (
  `id` int(11) NOT NULL,
  `ser` decimal(5,2) DEFAULT NULL,
  `saber` decimal(5,2) DEFAULT NULL,
  `hacer` decimal(5,2) DEFAULT NULL,
  `decidir` decimal(5,2) DEFAULT NULL,
  `calificacion_trimestral` decimal(5,2) DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  `id_alumno_id` int(11) NOT NULL,
  `id_materia_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacion_profesormateriacurso`
--

CREATE TABLE `evaluacion_profesormateriacurso` (
  `id` int(11) NOT NULL,
  `id_profesor_id` int(11) NOT NULL,
  `id_materia_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal_alumno`
--

CREATE TABLE `personal_alumno` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal_especialidad`
--

CREATE TABLE `personal_especialidad` (
  `id` int(11) NOT NULL,
  `nombre_especialidad` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal_profesor`
--

CREATE TABLE `personal_profesor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `id_especialidad_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `colegio_curso`
--
ALTER TABLE `colegio_curso`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_curso` (`nombre_curso`);

--
-- Indices de la tabla `colegio_materia`
--
ALTER TABLE `colegio_materia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_curso_id` (`id_curso_id`);

--
-- Indices de la tabla `evaluacion_asistencia`
--
ALTER TABLE `evaluacion_asistencia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `evaluacion_asistencia_id_alumno_id_id_materia_id_818a7c2e_uniq` (`id_alumno_id`,`id_materia_id`,`fecha_clase`),
  ADD KEY `id_materia_id` (`id_materia_id`);

--
-- Indices de la tabla `evaluacion_nota`
--
ALTER TABLE `evaluacion_nota`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `evaluacion_nota_id_alumno_id_id_materia_id_a824e6c3_uniq` (`id_alumno_id`,`id_materia_id`),
  ADD KEY `id_materia_id` (`id_materia_id`);

--
-- Indices de la tabla `evaluacion_profesormateriacurso`
--
ALTER TABLE `evaluacion_profesormateriacurso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_profesor_id` (`id_profesor_id`),
  ADD KEY `id_materia_id` (`id_materia_id`);

--
-- Indices de la tabla `personal_alumno`
--
ALTER TABLE `personal_alumno`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `personal_especialidad`
--
ALTER TABLE `personal_especialidad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_especialidad` (`nombre_especialidad`);

--
-- Indices de la tabla `personal_profesor`
--
ALTER TABLE `personal_profesor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_especialidad_id` (`id_especialidad_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `colegio_curso`
--
ALTER TABLE `colegio_curso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `colegio_materia`
--
ALTER TABLE `colegio_materia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluacion_asistencia`
--
ALTER TABLE `evaluacion_asistencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluacion_nota`
--
ALTER TABLE `evaluacion_nota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluacion_profesormateriacurso`
--
ALTER TABLE `evaluacion_profesormateriacurso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `personal_alumno`
--
ALTER TABLE `personal_alumno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `personal_especialidad`
--
ALTER TABLE `personal_especialidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `personal_profesor`
--
ALTER TABLE `personal_profesor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `colegio_materia`
--
ALTER TABLE `colegio_materia`
  ADD CONSTRAINT `colegio_materia_ibfk_1` FOREIGN KEY (`id_curso_id`) REFERENCES `colegio_curso` (`id`);

--
-- Filtros para la tabla `evaluacion_asistencia`
--
ALTER TABLE `evaluacion_asistencia`
  ADD CONSTRAINT `evaluacion_asistencia_ibfk_1` FOREIGN KEY (`id_alumno_id`) REFERENCES `personal_alumno` (`id`),
  ADD CONSTRAINT `evaluacion_asistencia_ibfk_2` FOREIGN KEY (`id_materia_id`) REFERENCES `colegio_materia` (`id`);

--
-- Filtros para la tabla `evaluacion_nota`
--
ALTER TABLE `evaluacion_nota`
  ADD CONSTRAINT `evaluacion_nota_ibfk_1` FOREIGN KEY (`id_alumno_id`) REFERENCES `personal_alumno` (`id`),
  ADD CONSTRAINT `evaluacion_nota_ibfk_2` FOREIGN KEY (`id_materia_id`) REFERENCES `colegio_materia` (`id`);

--
-- Filtros para la tabla `evaluacion_profesormateriacurso`
--
ALTER TABLE `evaluacion_profesormateriacurso`
  ADD CONSTRAINT `evaluacion_profesormateriacurso_ibfk_1` FOREIGN KEY (`id_profesor_id`) REFERENCES `personal_profesor` (`id`),
  ADD CONSTRAINT `evaluacion_profesormateriacurso_ibfk_2` FOREIGN KEY (`id_materia_id`) REFERENCES `colegio_materia` (`id`);

--
-- Filtros para la tabla `personal_profesor`
--
ALTER TABLE `personal_profesor`
  ADD CONSTRAINT `personal_profesor_ibfk_1` FOREIGN KEY (`id_especialidad_id`) REFERENCES `personal_especialidad` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
