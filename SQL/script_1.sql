USE db24;

DELIMETER $$
CREATE TRIGGER MyTBL_05A_guard1 BEFORE INSERT ON MyTBL_05A
FOR EACH ROW
BEGIN
DECLARE a varchar (100);
SELECT CURRENT_USER() INTO @a;
SIGNAL SQLSTATE '50000' SET message_text=@a;
END;$$
DELIMITER ; 


INSERT INTO MyTBL_05A (Title) VALUE ('AAA');
