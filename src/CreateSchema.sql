create table followers
(
    id integer,
    tweet_date varchar2(100),
    screen_name varchar2(50),
    follower varchar2(50)
)

create table following
(
    id integer,
    tweet_date varchar2(100),
    screen_name varchar2(50),
    followingId integer,	
    following varchar2(50)
)

create table rawusers (
    id          integer,
    onDate      date,
    username    varchar2(100),
    followingId integer
)

create table users (
    userId  integer,
    userName  varchar2(200)
)

