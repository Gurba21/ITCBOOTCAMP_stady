-- CREATE TABLE devlopers(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR DEFAULT 'no name',
--     skill VARCHAR,
--     programming_lang VARCHAR DEFAULT 'HTMl'
-- );
-- ALTER TABLE devlopers RENAME COLUMN skill TO age;
-- INSERT INTO devlopers(name,age,programming_lang) VALUES('Bakyt',23,'Python');
-- INSERT INTO devlopers(name,age,programming_lang) VALUES('Beka',15,'Java');
-- INSERT INTO devlopers(name,age,programming_lang) VALUES('Gulya',30,'JavaScript');
-- INSERT INTO devlopers(name,age,programming_lang) VALUES('Beka',39,'Assembler');
-- ALTER TABLE devlopers ADD COLUMN cash INT;
-- INSERT INTO devlopers (name,age,programming_lang,cash) VALUES('Katya',16,'Python',3000);
-- UPDATE devlopers SET age = '27' WHERE age > '25';
-- COMMENT ON COLUMN devlopers. name is 'Имя пользователя';
-- UPDATE devlopers SET name = 'Ekatirina II' WHERE name = 'Katya';
DELETE FROM devlopers id = 3;


-- SELECT * FROM devlopers;