OPTIONS (SKIP=1,ERRORS = 100)
load data
infile '/home/oracle/import/followers.csv'
APPEND into table FOLLOWERS
TRAILING NULLCOLS
(
	id		external integer,
	date		char terminated by ',',		
	screen_name	char terminated by ',',
	follower	char terminated by ',' 
)
