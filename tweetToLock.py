# TweetBox by Gary Grossi
# Created 06/04/2014
# Updated 06/09/2014
# Version 0.4

# library imports
import time
import twitter

# Twitter authentication and setup
keys = twitter.Api(consumer_key="Enter consumer key here",
                   consumer_secret="Enter consumer secret here",
                   access_token_key="Enter access token here",
                   access_token_secret="Enter token secret here")
print "Starting TweetToLock"
status = ""
keywordLock = "colloportus"
keywordUnlock = "alohomora"
prevState = ""

# Tweet reading function
def tweetTL():
global prevState
status = keys.GetUserTimeline("TweetToLock")
receivedStatus = [s.text for s in status]
splitStatus = receivedStatus[0].split()
length = len(splitStatus)
for x in range (0,length):
if splitStatus[x] == keywordLock and splitStatus[x] != prevState:
print "locking"


def set(property, value):
try:
f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
f.write(value)
f.close()
except:
print("Error writing to: " + property + " value: " + value)	def setServo(angle):
set("servo", str(angle))
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")
delay_period = 0.01
for angle in range(0, 160): # Runs servo to close
setServo(180 - angle)
time.sleep(delay_period)
print(angle)
prevState = keywordLock
elif splitStatus[x] == keywordUnlock and splitStatus[x] != prevState:
print "unlocking"

def set(property, value):
try:
f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
f.write(value)
f.close()
except:
print("Error writing to: " + property + " value: " + value)

def setServo(angle):
set("servo", str(angle))
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")
delay_period = 0.01
for angle in range(0, 160): # Runs servo to open
setServo(angle)
time.sleep(delay_period)
print(angle)
prevState = keywordUnlock
else:
print "neutral"

# Running tweetTL function on loop
while True:
tweetTL()
time.sleep(5)
