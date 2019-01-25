# PythonCode_Serial_Number_Retrieval_Customer_Site
Retrieval of cisco device serial number per location, leveraging Cisco DNAC API’s.

Description:  
This code retrieves the serial number of a network device based on it's IP address.  User of the code is prompted for the IP address.  The code leverages the Network Device DNAC API.  This API contains a number of device information and the code parses out only the serial number and matches it the corresponding IP.  Both the IP address and corresponding serial number are printed to a csv file that it's created in the process.  

Only one entry is written to the csv file per iteration.

Installation:  
Environment:  DNAC, Python3.7, Microsoft Excel
File serial_number_IP.py is the only file that needs to run for the code to work.

Usage:  
The code will prompt for an IP address.  Only configured IP addresses in DNAC will invoke the code to provide a csv file.  Appropriate warnings will appear if a non-configured IP address is entered as well as if no IP address in entered.

No password our authentication is required.

Files:
The file code leverges two other python codes that return token authenticaion and DNAC credentials (userneame, password) to authenticate into the device.  The main code, serial_number_ip.py, performs the IP prompting and csv file created with the IP address and serial number.  The following files need to be in same folder:

1.  serial_number_IP.py main file and the only that needs to be run.  It leverages the following three files:
2.  dnac.py for DNAC token authentication
3.  dnac_config.py for DNAC credential retrival
4.  trabulate.py for formating purposes
5   SNReport.csv:  created once a configured IP address is entered.  File is created in the same folder as code exist.
