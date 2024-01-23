-- script that creates a trigger that resets the attribute valic_email.
DELIMITER //

CREATE TRIGGER before_update_users
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
//

DELIMITER ;
