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
