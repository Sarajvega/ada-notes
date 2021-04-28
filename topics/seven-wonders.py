import requests

def seven_wonders():
    results = {}
    seven_wonders_list = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu"]#, "Taj Mahal", "Christ the Redeemer"]
    # seven_wonders_list = ["Great Wall of China", "Petra"]
    for i in seven_wonders_list:
        coordinates = get_lat_lon(i)
        results[i] = coordinates 

    print(results)

def get_body(search_term):
    path = "https://us1.locationiq.com/v1/search.php"
    LOCATIONIQ_API_KEY = "pk.f05ee5905693d76d6ff522dbd4a5ca2c"

    query_params = {
    "key": LOCATIONIQ_API_KEY,
    "q": search_term,
    "format": "json"}

    response = requests.get(path, params=query_params)
    response_body = response.json()
    print(response_body)
    body = response_body[0]
    return body

def get_lat_lon(search_term):

    coordinates_dict = {}
    body = get_body(search_term)
    coordinates_dict['latitude'] = body['lat']
    coordinates_dict['longitude'] = body['lon']
    return(coordinates_dict)

seven_wonders()

