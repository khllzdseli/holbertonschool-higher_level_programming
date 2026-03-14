-- Create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table cities with id as primary key, auto-incremented and unique
-- state_id is a foreign key referencing states(id), name cannot be null
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state
        FOREIGN KEY (state_id)
        REFERENCES states(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
