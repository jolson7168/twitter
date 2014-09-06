import time
import tweepy
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
		print ('getUserName.py -c <configfile>')
      		sys.exit(2)
	for opt, arg in opts:
      		if opt == '-h':
         		print ('getUserName.py -c <configfile>')
         		sys.exit()
		elif opt in ("-c", "--configfile"):
			configFile=arg
			try:
   				with open(configFile): pass
			except IOError:
   				print ('Configuration file: '+configFile+' not found')
				sys.exit(2)
	execfile(configFile, config)

	auth = tweepy.OAuthHandler(config["oauth1"],config["oauth2"])
	auth.set_access_token(config["access_token1"],config["access_token2"])

	api = tweepy.API(auth)
	ofile = open(config["outputFile"], 'a')
	conn = boto.sqs.connect_to_region(config["region"],aws_access_key_id=config["aws_access_key_id"],aws_secret_access_key=config["aws_secret_access_key"])
	q = conn.get_queue(config["queueName"])
	count = 0
	done = False
	while not done:
		if (q.count() == 0):
			done = True
		else:
			m = q.read(60)
			userIDjson = m.get_body()
			try:
				userIn=json.loads(userIDjson)
				print("    ID: "+str(userIn["userID"]))
				user=api.get_user(id=userIn["userID"])
				count=count+1	
				try:
					ofile.write(str(userIn["userID"])+","+user.screen_name+"\n")
					q.delete_message(m)
				except Exception as error:
					print(str(userIn["userID"])+","+user.screen_name+"    File Exception: "+str(error))	
				if (count % 12 == 0):
					ofile.flush()
					time.sleep(60)	# 180 requests every 15 minutes
			except tweepy.TweepError as error:
				print("Twitter Exception: Lookup - "+str(userIn["userID"])+"   Error: "+str(error))
				if (str(error)).find("Sorry, that page does not exist")>0:
					ofile.write(str(userIn["userID"])+","+"NO PAGE"+"\n")
				q.delete_message(m)



if __name__ == "__main__":
	main(sys.argv[1:])
