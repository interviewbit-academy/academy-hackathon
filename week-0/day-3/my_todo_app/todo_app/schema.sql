DROP TABLE IF EXISTS user;

create table user(
    username VARCHAR(100) NOT NULL,
    todo VARCHAR(100) NOT NULL,
    PRIMARY KEY(username,todo));
    
INSERT INTO user(username,todo) VALUES ('ayush','eat');
INSERT INTO user(username,todo) VALUES ('ayush','read');
INSERT INTO user(username,todo) VALUES ('ayush','sleep');
INSERT INTO user(username,todo) VALUES ('raj','code');
INSERT INTO user(username,todo) VALUES ('raj','coffee');
INSERT INTO user(username,todo) VALUES ('raj','play');
INSERT INTO user(username,todo) VALUES ('depo','sleep');
INSERT INTO user(username,todo) VALUES ('depo','brush');
INSERT INTO user(username,todo) VALUES ('depo','run');