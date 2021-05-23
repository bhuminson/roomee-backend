DROP TABLE IF EXISTS filters;
DROP TABLE IF EXISTS login_info;
DROP TABLE IF EXISTS profilepics;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS dislikes;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS userids;
DROP SEQUENCE IF EXISTS filterids;

CREATE SEQUENCE userids
start with 7
increment by 1
minvalue 7
maxvalue 100
cycle;

CREATE SEQUENCE filterids
start with 7
increment by 1
minvalue 7
maxvalue 100
cycle;


CREATE TABLE users (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('userids'), 
    username varchar(30) NOT NULL,
    firstname varchar(30) NOT NULL,
    lastname varchar(30) NOT NULL,
    nickname varchar(30) NOT NULL,
    phone varchar(40),
    email varchar(40) NOT NULL,
    bio varchar(300)
    UNIQUE(username),
    UNIQUE(phone),
    UNIQUE(email)
);

INSERT INTO "users" VALUES(1,'dayday23','Draymond','Green','Day day','5105105100','dayday23@gmail.com', 'pf/c at gsw');
INSERT INTO "users" VALUES(2,'goat43','LeBron','James','bron','9495628685','lebronjames@gmail.com', 'go lakers');
INSERT INTO "users" VALUES(3,'curry30','Stephen','Curry','steph','97979797979','curry@gmail.com', 'pg at gsw');
INSERT INTO "users" VALUES(4,'damedolla','Damian','Lilliard','dame','13131313131','dametime@gmail.com', 'pg at portland');
INSERT INTO "users" VALUES(5,'asdfasdf','Zion','Williamson','zion','6464646464','zion@gmail.com', 'pf/c at nop');
INSERT INTO "users" VALUES(6,'asdfasdf','Kim','Kardashian','kk','6464646464','kk@gmail.com', 'my bio');

CREATE TABLE profilepics (
    id SERIAL PRIMARY KEY,
    -- userId INTEGER NOT NULL,
    img bytea
    -- FOREIGN KEY (userId) REFERENCES users(id)
);

CREATE TABLE filters (
    userId INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('filterids'),
    age INTEGER NOT NULL,
    gender varchar(20) NOT NULL, -- male, female, non-binary, etc
    school varchar(50) NOT NULL, -- we might consider having a school table with locations, etc
    major varchar(50) NOT NULL,
    school_year varchar(50) NOT NULL, -- ie 4th year puts 4
    graduation_year INTEGER NOT NULL,
    leasing_q varchar(20) NOT NULL, -- leasing or searching
    car varchar(20) NOT NULL, -- 0 for false, 1 for true
    pet varchar(20) NOT NULL, -- 0 for false, 1 for true
    clean INTEGER NOT NULL, -- scale from 0 to 10
    noise INTEGER NOT NULL, --scale from 0 to 10
    drink varchar(20) NOT NULL, -- yes, no, sometimes
    smoke varchar(20) NOT NULL, -- yes, no, sometimes
    drugs varchar(20), -- yes, no, sometimes
    visible_phone varchar(20), -- true means show phone, false means hide it
    visible_email varchar(20), -- true means show email, false means hide it
    FOREIGN KEY (userId) REFERENCES users(id)
);

INSERT INTO "filters" VALUES(1,22,'Male', 'Cal Poly', 'Humanities', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', TRUE, TRUE);
INSERT INTO "filters" VALUES(2,18,'Male', 'Cal Poly', 'STEM', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', FALSE, TRUE);
INSERT INTO "filters" VALUES(3,25,'Male', 'Cal Poly', 'Humanities', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', TRUE, TRUE);
INSERT INTO "filters" VALUES(4,29,'Male', 'Cal Poly', 'STEM', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', FALSE, FALSE);
INSERT INTO "filters" VALUES(5,26,'Male', 'Cal Poly', 'Business', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', FALSE, FALSE);
INSERT INTO "filters" VALUES(6,26,'Female', 'Cal Poly', 'Business', 'Freshman', 2022,'Leasing', TRUE, TRUE, 4,2,'Yes', 'Yes', 'Yes', FALSE, FALSE);

CREATE TABLE login_info (
    userId SERIAL PRIMARY KEY,
    password varchar(30) NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);
INSERT INTO "login_info" VALUES(1,'dayday23');

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    userId INTEGER,
    likeId INTEGER,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (likeId) REFERENCES users(id)
);


CREATE TABLE dislikes (
    id SERIAL PRIMARY KEY,
    userId INTEGER,
    dislikeId INTEGER,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (dislikeId) REFERENCES users(id)
);
