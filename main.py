import requests
API_KEY = "3818ecadc510ddeeffe0466578a5438f"
WS_URL = "http://api.weatherstack.com/current"

cities = []
with open("cities.txt") as f:
    for line in f:
        cities.append(line.strip())
print(cities)

for city in cities:
    parameters = {'access_key': API_KEY, 'query': city}
    response = requests.get(WS_URL, parameters)
    js = response.json()

    try:
        temperature = js['current']['temperature']
    except KeyError as ke:
        if not js['success']:
            print(js['error'])
    date = js['location']['localtime']

    with open(f"{city}.txt", "a") as f:
        f.write(f"{date},{temperature}\n")







