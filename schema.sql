-- schema.sql for COL-BI Project

-- Drop database if exists
DROP DATABASE IF EXISTS `col-bi`;
CREATE DATABASE `col-bi`;
USE `col-bi`;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Teammate Finder table
CREATE TABLE find_teammate (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male','Female','Other') NOT NULL,
    field VARCHAR(100) NOT NULL,
    current_proj VARCHAR(255) NOT NULL,
    teammate_specs VARCHAR(255) NOT NULL
);
