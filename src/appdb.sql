DROP TABLE IF EXISTS filters;
DROP TABLE IF EXISTS login_info;
DROP TABLE IF EXISTS test_login_info;
DROP TABLE IF EXISTS profilepics;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS dislikes;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS test_filters;
DROP TABLE IF EXISTS test_likes;
DROP TABLE IF EXISTS test_dislikes;
DROP TABLE IF EXISTS test_users;
DROP SEQUENCE IF EXISTS userids;
DROP SEQUENCE IF EXISTS filterids;
DROP SEQUENCE IF EXISTS likeids;
DROP SEQUENCE IF EXISTS dislikeids;
DROP SEQUENCE IF EXISTS pfpids;
DROP SEQUENCE IF EXISTS loginids;

CREATE SEQUENCE userids
start with 7
increment by 1
minvalue 1
no maxvalue
no cycle;

CREATE SEQUENCE filterids
start with 7
increment by 1
minvalue 1
no maxvalue
no cycle;

CREATE SEQUENCE pfpids
start with 1
increment by 1
minvalue 1
no maxvalue
no cycle;

CREATE SEQUENCE loginids
start with 7
increment by 1
minvalue 1
no maxvalue
no cycle;


CREATE SEQUENCE likeids
start with 1
increment by 1
minvalue 1
no maxvalue
no cycle;


CREATE SEQUENCE dislikeids
start with 1
increment by 1
minvalue 1
no maxvalue
no cycle;

CREATE TABLE users (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('userids'), 
    username varchar(30) NOT NULL,
    firstname varchar(30) NOT NULL,
    lastname varchar(30) NOT NULL,
    nickname varchar(30) NOT NULL,
    phone varchar(40),
    email varchar(40) NOT NULL,
    bio varchar(300),
    UNIQUE(username),
    UNIQUE(phone),
    UNIQUE(email)
);

CREATE TABLE profilepics (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('pfpids'),
    userId INT NOT NULL,
    img bytea,
    FOREIGN KEY (userId) REFERENCES users(id)
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
    clean INTEGER NOT NULL, -- scale from 0 to 10
    noise INTEGER NOT NULL, --scale from 0 to 10
    drink boolean NOT NULL, -- boolean
    smoke boolean NOT NULL, -- boolean
    drugs boolean NOT NULL, -- boolean
    car boolean NOT NULL, -- boolean
    pet boolean NOT NULL, -- boolean
    visible_phone varchar(20), -- boolean
    visible_email varchar(20), -- boolean
    FOREIGN KEY (userId) REFERENCES users(id)
);

CREATE TABLE likes (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('likeids'),
    userId INTEGER,
    likeId INTEGER,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (likeId) REFERENCES users(id)
);


CREATE TABLE dislikes (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('dislikeids'),
    userId INTEGER,
    dislikeId INTEGER,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (dislikeId) REFERENCES users(id)
);

CREATE TABLE login_info (
    userId INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('loginids'),
    password varchar(30) NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);

CREATE TABLE test_users (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('userids'), 
    username varchar(30) NOT NULL,
    firstname varchar(30) NOT NULL,
    lastname varchar(30) NOT NULL,
    nickname varchar(30) NOT NULL,
    phone varchar(40),
    email varchar(40) NOT NULL,
    bio varchar(300),
    UNIQUE(username),
    UNIQUE(phone),
    UNIQUE(email)
);

CREATE TABLE test_filters (
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
    FOREIGN KEY (userId) REFERENCES test_users(id)
);

CREATE TABLE test_login_info (
    userId INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('loginids'),
    password varchar(30) NOT NULL,
    FOREIGN KEY (userId) REFERENCES test_users(id)
);

CREATE TABLE test_dislikes (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('dislikeids'),
    userId INTEGER,
    dislikeId INTEGER,
    FOREIGN KEY (userId) REFERENCES test_users(id),
    FOREIGN KEY (dislikeId) REFERENCES test_users(id)
);

CREATE TABLE test_likes (
    id INT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('likeids'),
    userId INTEGER,
    likeId INTEGER,
    FOREIGN KEY (userId) REFERENCES test_users(id),
    FOREIGN KEY (likeId) REFERENCES test_users(id)
);

--------------------------------------------------------------------------------------------------------------------------

INSERT INTO "users" VALUES(1,'dayday23','Draymond','Green','Day day','5105105100','dayday23@gmail.com', 'pf/c at gsw');
INSERT INTO "users" VALUES(2,'goat43','LeBron','James','bron','9495628685','lebronjames@gmail.com', 'go lakers');
INSERT INTO "users" VALUES(3,'curry30','Stephen','Curry','steph','97979797979','curry@gmail.com', 'pg at gsw');
INSERT INTO "users" VALUES(4,'damedolla','Damian','Lilliard','dame','13131313131','dametime@gmail.com', 'pg at portland');
INSERT INTO "users" VALUES(5,'asdfasdf','Zion','Williamson','zion','525234235','zion@gmail.com', 'pf/c at nop');
INSERT INTO "users" VALUES(6,'asdfafd','Kim','Kardashian','kk','6464646464','kk@gmail.com', 'my bio');

INSERT INTO "filters" VALUES(1,22,'Male', 'Cal Poly', 'Humanities', 'Freshman', 2022,'Leasing', 4, 2, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
INSERT INTO "filters" VALUES(2,18,'Male', 'Cal Poly', 'STEM', 'Freshman', 2022,'Leasing', 4, 2, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE);
INSERT INTO "filters" VALUES(3,25,'Male', 'Cal Poly', 'Humanities', 'Freshman', 2022,'Leasing', 4, 2, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
INSERT INTO "filters" VALUES(4,29,'Male', 'Cal Poly', 'STEM', 'Freshman', 2022,'Leasing', 4, 2, FALSE, FALSE, FALSE, FALSE, FALSE,  FALSE, FALSE);
INSERT INTO "filters" VALUES(5,26,'Male', 'Cal Poly', 'Business', 'Freshman', 2022,'Leasing', 4, 2, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE);
INSERT INTO "filters" VALUES(6,26,'Female', 'Cal Poly', 'Business', 'Freshman', 2022,'Leasing', 4, 2, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE);

INSERT INTO "login_info" VALUES(1,'dayday23');
INSERT INTO "login_info" VALUES(2,'asdf');
INSERT INTO "login_info" VALUES(3,'asdf');
INSERT INTO "login_info" VALUES(4,'asdf');
INSERT INTO "login_info" VALUES(5,'asdf');
INSERT INTO "login_info" VALUES(6,'asdf');