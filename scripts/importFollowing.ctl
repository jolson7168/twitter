OPTIONS (SKIP=1,ERRORS = 100)
load data
infile '../data/RawFollowing.csv'
APPEND into table FOLLOWING
TRAILING NULLCOLS
(
	id		integer external terminated by ',',
	tweet_date	char terminated by ',',		
	screen_name	char terminated by ',',
	followingId	integer,
	following	char terminated by ',' 
)
