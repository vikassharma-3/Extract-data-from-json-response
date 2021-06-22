#PY by Vikas Sharma
# Module Installation
# pip install simple-geoip

# Required API key from the "https://ip-geolocation.whoisxmlapi.com/"
''' Logic :
    1. Capture the respone of the request
    2. Filter out the request(removing \n)
    3. Converting the response into json
    4. Extracting IP from json
    5. Using API of GeoIP extracting details from IP
    6. Storing it into csv
'''

import requests
import json
from simple_geoip import GeoIP
import csv


for x in range(30):
    URL = "https://threatlabip1.forenzy.net/threatinfo.php"

    response = requests.get('https://threatlabip1.forenzy.net/threatinfo.php')
    data = (response.text).replace("\n",'')
    data_json = json.loads(data)

    ip = data_json['ip']
    # API key from "https://ip-geolocation.whoisxmlapi.com/"
    geoip = GeoIP("#Enter your API key from above website here") #Fetching ISP , country using API
    data = geoip.lookup(ip)
    final_data=data['ip']+','+data['location']['country']+','+data['isp']
    print(final_data)
    with open('data.csv', 'a', newline='') as file:   # Writing it into csv file
        writer = csv.writer(file)
        writer.writerow([data['ip'],data['location']['country'],data['isp']])

print("Done!! Completed")
#print(data)
#print(ip)
#print(data_json)


