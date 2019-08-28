import requests

def obtener_ramas():
    url = "http://192.168.26.64:8080/api/v3/repos/TheWildCats/Selenium_Updated/branches"
    payload = ""
    headers = {
        'Authorization': "Basic SGJ1ZWx2YXM6bmFjaW9uYWw4NTIw"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    return response.json()