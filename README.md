# Extract-data-from-json-response
Problem Statement:

Each time hitting below URL or any url  will return a live JSON response of some, write a code to parse the IP field from the JSON output and provide following additional fields and store it in CSV at least for 30 records [You may use for/while loop].


Logic Used:
1. Capture the respone of the request
2. Filter out the request(removing \n)
3. Converting the response into json
4. Extracting IP from json
5. Using API of GeoIP extracting details from IP
6. Storing it into csv


Code attached in the repository is specific to the problem statement but can be used to modify into various different case scenerios accordingly.

Requirement:

1. Python modules - request , csv and geoip
2. API key from "https://ip-geolocation.whoisxmlapi.com/" for location , ISP  of an IP
