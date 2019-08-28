import requests

def obtener_ramas():
    url = "http://192.168.26.64:8080/api/v3/repos/TheWildCats/Selenium_Updated/branches"
    payload = ""
    headers = {
        'Authorization': "Basic SGJ1ZWx2YXM6bmFjaW9uYWw4NTIw",
        'cache-control': "no-cache",
        'Postman-Token': "37512018-3b5e-4551-ac80-34a4927a0dd2"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    return response.text