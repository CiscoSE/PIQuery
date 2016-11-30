import requests
import ConfigParser

print "Prime Infrastructure Query Engine Starting...\n"

# Open up the configuration file and get all application defaults
config = ConfigParser.ConfigParser()
config.read('package_config.ini')

serveraddress = config.get("application","serveraddress")
username = config.get("application","username")
password = config.get("application","password")

print "Prime Infrastructure Server: "+serveraddress
print "Username for API Queries: "+username

# Construct the url for querying Prime Infrastructure
base_url="https://"+username+":"+password+"@"+serveraddress
config_url="/webacs/api/v2/data/Clients.json?.full=true"

# Send the query to the Prime Infrastructure Server
r = requests.get(base_url+config_url,verify=False)

# Retrieve the results in JSON format
json_string = r.json()

# Find the total device records that where returned from the query
total_device_count =  json_string['queryResponse']['@count']

print "Total Records Retrieved from Prime Infrastructure: "+str(total_device_count)+"\n"

print '{0:20} {1:20} {2:20} {3:30} {4:20} {5:20}'.format("Parent Switch", "MAC Address", "Device Vendor", "Interface", "IP Address","Device Type")
print '==============================================================================================================================='

# Iterate through each record that was returned from Prime Infrastructure
for count in range(total_device_count):

    # Store the individual record in a dictionary entry
    mydict = json_string['queryResponse']['entity'][count]['clientsDTO']

    # Extract all the appropriate fields
    devicename = mydict.get("deviceName")
    macAddress = mydict.get("macAddress")
    vendor = mydict.get("vendor")
    devicetype = mydict.get("deviceType")
    clientint = mydict.get("clientInterface")
    ipaddress = mydict.get("ipAddress",None)
    if ipaddress <> None :
        ipaddress = ipaddress.get("address")

    # Print the resulting data to the screen
    print '{0:20} {1:20} {2:20} {3:30} {4:20} {5:20}'.format(devicename, macAddress, vendor, clientint,ipaddress, devicetype)
