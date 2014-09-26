OPTIONS (SKIP=1,ERRORS = 100)
load data
infile '/home/oracle/git/twitter/data/output2.txt'
APPEND into table users 
TRAILING NULLCOLS
(
	userid		integer external terminated by ',',
	username	char terminated by ','
)
