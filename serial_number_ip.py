"""
This script calls "GET /network-device/ip-address/" API and print out
Serial Number
All simplify REST request functions and get authentication token function are in dnac.py
Controller ip, username and password are defined in dnac_config.py
"""
from  dnac import *
from tabulate import *
import csv

#Prompt for IP Address
ip = input ("Please enter IP address to search for the device serial number: ")

#Use DNAC Network Device API to acquire network device data 
device = []
try:
    # The request and response of "GET /network-device" API
    resp = get(api="network-device/ip-address/{}/".format(ip))
    #resp = get(api="network-device/")
    status = resp.status_code
    # Get the json-encoded content from response
    response_json = resp.json()
    # All network-device detail is in "response"
    device = response_json["response"]

    #Exception and if statements if wrong IP address or no IP address is entered
except ValueError:
    sys.exit()

if status == 400:
    print ("Something went wrong, cannot get network device information")
    sys.exit()

if status == 404:
    print ("IP Address is not configured.  Please try again")
    sys.exit()

#Parse only IP address ad serial number
serialNumber = (device['managementIpAddress'],device['serialNumber'])

#Create csv file
myFile = open('SNReport.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows([serialNumber])
    myFile.close()

#Wriing IP address and serial number to csv file
print("Writing to SNReport.csv complete")
print (device['serialNumber'])
