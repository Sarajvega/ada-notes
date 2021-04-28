# Requests and Responses

Web apps follow **client-server model**
- The end-user's web browser is a client, and sends HTTP requests to a web server over the Internet
- The web server sends an HTTP response for every request back to the client

## Vocab
- Sending a request: Act of sending an HTTP request from a client to server.
- Endpoint: Name for the path of a resource, usually in the context of an API. 

## Clients Make Requests, Servers Give Responses
HTTP requests usually request a resource.
- A resource = data that can be sent over the Internet, whether it's a full website, a piece of JSON with specific data, some XML, or a string of text.

## Parts of HTTP Request
- HTTP Method (required): Operation that the client wnats ot perform. Method implies the nature of the request. Can be getting or sending info, among other things.
  - Examples:
    - GET: Requests retrieving the data of a specified resource
      - Going to a URL is a GET request by default.
    - POST: Requests submitting data to the server, and changing the state of the server. Usually associated with submitting forms.
    - PUT: Requests replacing a resource with a new resource
    - PATCH: Requests replacing parts of a resource
    - DELETE: Requests deleting a resource
- Path for request URL (required): The URL that the requested resource is located at.
  - the requested resource could be a website, a PDF file, an image file, or something else.
  - Endpoint: In API's, path that expects API requests. 
- Query parameters (not required): Key-value pairs that describe information that can make this request more specific. 
  - Query parameters ultimately become formatted as a string as part of the request URL. The text-formatting happens in this pattern: `http://fake.org?example_1=value_1&example_2&value_2`
    - http://fake.org/products?page=2 - Goes to second page of products.
- HTTP Headers (not required): Colon-separated pairs of information to describe additional details that the server may need
  - useful when giving information for how the client and server should connect, details about authentication and authorization, and formats of data sent between client and server. 
- HTTP Body (not required): Additional resources.
  - example resources that would be attached a request body:
    - A POST request that holds the form data for a loan application that someone fills out online
    - A POST request that holds an image that someone is uploading as their profile picture


## Parts of HTTP Response
- Status code (req'd): A number that indicates if a request was successful or unsuccessful, and why.
  - There is a number of pre-defined HTTP status codes and status messages.
  - 3 digit codes - first digit indicate the kind of reponse. 
    - Examples:
      - 100-199	: Information, not common
      - 200-299	: Successful response, request completed.
      - 300-399	: Redirects, resource has been moved.
      - 400-499	: Client error
      - 500-599 : Server error
- Status message (req'd): A description attached to the status code	
  - 200 - OK - Request succeeded.
  - 201 - Created - Req suceeded and new resourced created.
  - 301 - Moved permanently - URL of req'd resource changed.
  - 404 - Not Found - Server can't locate.
  - 500 - Internal Server Error - Server got an situation it doesn't know how to handle. 
- HTTP Headers (not req): Colon-separated pairs of information to describe additional details that the client may need.
  - Same as requests.
- HTTP body (not req): Resources that needs to be sent to the client.
  - responses tend to utilize the body much more frequently than requests do.
  - Examples: 
    - After the client requests for all videos within a specific playlist, a response that holds the data of all videos within that playlist

## Requests from Postman 
Postman  is software that is designed to improve API development. The feature we care about the most is using Postman as an API client. This means that Postman will send any HTTP requests we design. Also, Postman will receive the HTTP responses that the server sends back.
There are other ways to make HTTP requests and see HTTP responses. However, Postman is great at showing us requests and responses easily. There are so many ocassions when this is beneficial:

## When to use Postman
- In the middle of Python coding, needing to manually test and confirm an API call
- Satisfying your curiosity
- Checking to see if something is possible with an API

## API Keys 
Whenever an API receives a request and gives back a response, we can consider the following things:
- Handling requests, responses, and maintaining internet connectivity takes resources (money, labor, skill)
- Running the web server takes resources (money, labor, skill)
- The response that the API gives back has valuable data that the client wants

API keys are strings that an API gives to a project which will uniquely identify the project. This API key will authenticate the project (and the project's HTTP requests) to the web API.

Without this API key or the correct permissions, web APIs may respond with HTTP Status Code 401 Unauthorized, or something similar.

We can include API keys in our HTTP requests in any of the following ways:
1. As a query parameter
2. As a request header
3. Inside a cookie

**API keys aren't secure;** they're usually a single string of text sent with the request. It's relatively easy for people to "steal" API keys, which could result in sensitive data being exposed or having your rate limits for that key met. 
1. Don't post the API key on any public place, such as social media or your blog
2. Don't include any API keys inside any git commits that get pushed onto Github.com

## API rate limits
Rate limit is the number of HTTP requests that an app is allowed to make within a given time period. API services don't want apps and users to call an API too often.

## Sending Requests with Python
- The requests package : A Python package. The package defines methods whose responsibility is to make HTTP requests and receive HTTP responses. 

## Writing Python to Make Requests
Ex:
```python
import requests

path = "https://us1.locationiq.com/v1/search.php"
# no query params in path
LOCATIONIQ_API_KEY = "...ec6a8368a..."
# constant that holds API key
query_params = {
    "key": LOCATIONIQ_API_KEY,
    "q": "Great Wall of China",
    "format": "json"
}
# dict w/ query params
response = requests.get(path, params=query_params)
# local var that holds return val of ur params to the path.
print("The value of response is", response)
print("The value of response.text, which contains a text description of the request, is", response.text)
```
request.get() returns a Response object. 

## Using .json() on a response obj
```python
response_body = response.json()
print("The value of response.json()", response_body)
```
What data structure does response.json() return? How do we get the latitude and longitude? We can either use another breakpoint to debug with the debugger, or we can replace the print statements with the following:
```python
print("The value of response.json():", response_body)
print("The length of the response_body list:", len(response_body))
print("The first item of response_body:", response_body[0])
print("The latitude of the first item of response_body:", response_body[0]['lat'])
```

### Seven Wonders Challenge

```python
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
    LOCATIONIQ_API_KEY = "KEY"

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
```