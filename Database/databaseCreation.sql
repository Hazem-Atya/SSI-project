DROP TABLE  IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT CHECK(
        password is not null
        and length(password) >= 5
    ),
    salt Text
);
-- Index creation
CREATE UNIQUE INDEX index_email
on users (email);
insert into users (name,email,password,salt) values("hazem1","hazem1@gmail.com","qwerty","1234");
insert into users (name,email,password,salt) values("hazem2","hazem2@gmail.com","qwerty","1234");
insert into users (name,email,password,salt) values("hazem3","hazem3@gmail.com","qwerty","1234");
insert into users (name,email,password,salt) values("hazem4","hazem4@gmail.com","qwerty","1234");
