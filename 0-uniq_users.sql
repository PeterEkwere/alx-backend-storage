-- script that creates a table users
CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
