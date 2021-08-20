import requests

#SIMPLE and funny free and useful ip location scanner batch bunch of ip's from ip-api.com

#Create a response variable holding value request.post with the api url, get your choosen ip numbers ready.
response = requests.post("http://ip-api.com/batch", json=[

        {"query": "208.80.152.201"}, #random ip
        {"query": "13.49.132.198"}, #random ip
        {"query": "52.28.72.46"}, #random ip
        {"query": "52.28.72.46"} #random ip
    ]).json()

#make a for loop and then loop the dictionary!
for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")
