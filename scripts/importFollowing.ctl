OPTIONS (SKIP=1,ERRORS = 100)
load data
infile '/home/oracle/git/twitter/data/output.txt'
APPEND into table rawusers 
TRAILING NULLCOLS
(
	id		integer external terminated by ',',
	ondate		date 'YYYY-MM-DD HH24:MI:SS' terminated by ',', 		
	username	char terminated by ',',
	followingId	integer external terminated by ','
)
