import requests


def getNum(access_key, number, country_code):
    api_result = requests.get("http://apilayer.net/api/validate"+
                              "?access_key=" + access_key + "&number=" + number +
                              "&country_code=" + country_code +
                              "&format=1")
    api_response = api_result.json()
    return api_response