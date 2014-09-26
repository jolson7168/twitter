import time
import csv
import json
import boto.sqs
from boto.sqs.message import Message
import sys
import getopt

config = {}

def main(argv):
 	try:
      		opts, args = getopt.getopt(argv,"hc:",["configfile="])
	except getopt.GetoptError:
		print ('enQueue.py -c <configfile>')
      		sys.exit(2)
	for opt, arg in opts:
      		if opt == '-h':
         		print ('enQueue.py -c <configfile>')
         		sys.exit()
		elif opt in ("-c", "--configfile"):
			configFile=arg
			try:
   				with open(configFile): pass
			except IOError:
   				print ('Configuration file: '+configFile+' not found')
				sys.exit(2)
	execfile(configFile, config)

	ifile = open(config["inputFile"], "rb")
	reader = csv.reader(ifile,delimiter=',')	
	count = 0
	conn = boto.sqs.connect_to_region(config["region"],aws_access_key_id=config["aws_access_key_id"],aws_secret_access_key=config["aws_secret_access_key"])
	q = conn.get_queue(config["queueName"])
	m = Message()
	
	for row in reader:
		message = '{"userID":'+row[0]+'}'
		print(message)
		m.set_body(message)
		q.write(m)



if __name__ == "__main__":
	main(sys.argv[1:])
