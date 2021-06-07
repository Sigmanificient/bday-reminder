create table birthdays
(
    id       integer
        constraint table_name_pk
            primary key autoincrement,
    user_id  int,
    name     varchar(50),
    birthday date not null,
    constraint cc0_birthdays
        unique (user_id, name)
);

create table users
(
    id                    integer
        constraint users_pk
            primary key autoincrement,
    username              varchar(50)  not null,
    authentication_string varchar(128) not null,
    count                 int
);

