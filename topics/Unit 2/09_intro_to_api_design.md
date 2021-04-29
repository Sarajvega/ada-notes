
# Intro to API Design

## Designing Endpoints
- REST: An architecture style for applications and APIs that uses the HTTP protocol and uses client-server architecture
  - Stands for **Representational state transfer**
  - An API that adheres to these specific design principles is called RESTful.
- Uniform Interface: A REST design principle that that prefers reliable and predictable endpoints, and doesn't prefer custom endpoints
- CRUD: "Create, Read, Update, Delete." An acronym that describes the four basic operations to work with saved resources

## HTTP Restful Web API's
A RESTful API will:
- Use HTTP for requests and responses
- Maintain statelessness in the server. The server will not track data about the client between requests; the client will track data about the server and send it back to the server each time.
- Return standard media types in responses, such as plain text, HTML, XML, and JSON
- Provide a uniform interface for the client

A non-RESTful API will:
- Use a different protocol for requests/responses, such as SOAP
- Store data about the state of each client between requests
- Return non-standard media types
- Prioritize custom and bespoke endpoints and responses for each user's needs

## Uniform Interface
- A uniform interface implies that the technical ways that a client interacts with the API should be predictable.

REST believes that a uniform interface follows these guidelines:
- Resource-based Paths: Request URLs and paths should be based around a resource. Recall that resources are any piece of data to return, such as user data or web pages.
- Manipulate Resources Through Representations: Clients can modify or delete resources on a server if they have a representation of it, such as an ID
- Self-Descriptive Messages: HTTP requests and responses should include the information of how to be read, by carrying information about their format (usually as a header)
  
In summary:
- REST prioritizes resources and representations of resources, and this will affect how URLs are made, what information to send with HTTP requests, and what we can expect from HTTP responses.
- REST prioritizes statelessness on the server between requests. It maintains statelessness between requests by relying on HTTP requests to send any details about client state.

## Meaningful Endpoints
**A well-designed RESTful API states that endpoints should be based on resources.**
Endpoint = an entry point URL to access a web API. 
  - in the LocationIQ API, /search is the endpoint to access the API's search functionality.
Resources are any piece of data to return, such as user data or web pages.

## Meaningful HTTP requests methods
Well-designed RESTful APIs use the HTTP request method in combination with resource-centered endpoints.
REST implies these meanings to HTTP methods:
- GET: Get a representation of the target resource's state.
- POST: Let the target resource process the representation enclosed in the request.
- PUT: Set the target resource's state to the state defined by the representation enclosed in the request.
- DELETE: Delete the target resource's state
- PATCH: Update the target resource's state with the state defined by the representation enclosed in the request.

## CRUD
- Create, Read, Update, Delete
  - describes four basic operations that developers want to do with stored resources.
- For every resource:
  - Create a single resource
  - Retrieve and Read details
  - Update a resource w/new data
  - Delete it

## REST, CRUD, and Designing an Endpoint
- Unifrom interace = combine REST and CRUD to make a formulaic set of API endpoints.
  
Example: An app needs to store every student's name, contact information, courses that they're enrolled in, and classes that they attend.

Read these as: "If a client sends an HTTP request with the HTTP Method method to the Endpoint/Path/Route path, the API server will Endpoint Description, and respond with Expected Response."

| HTTP Method | <div style="min-width:200px;">Endpoint/Path/Route</div>              | Request Body                 | Endpoint Description                                                           | Part of CRUD |
| -------------------- | -------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------ | ------------ |
| `POST`               | `/students`                                                          | New student data             | Creates and saves a new student to the database                                | Create       |
| `GET`                | `/students`                                                          | -                            | Get the data of all students, in a list                                        | Read         |
| `GET`                | `/students/<student_id>`, where `<student_id>` is a number like `13` | -                            | Get the data of the student with ID #13                                        | Read         |
| `PUT`                | `/students/<student_id>`, where `<student_id>` is a number like `13` | Updated student data         | Replaces the student ID #13 resource with the student data in the request body | Update       |
| `PATCH`              | `/students/<student_id>`, where `<student_id>` is a number like `13` | Part of updated student data | Updates the student ID #13 resource with the student data in the request body  | Update       |
| `DELETE`             | `/students/<student_id>`, where `<student_id>` is a number like `13` | -                            | Deletes the student ID #13 resource                   

## Designing Responses
*Anticipate possible outcomes to handle errors. *
Consider response for each endpoint based on CRUD:
- Create: Successfully/Unsuccessfully creating a new resource?
- Read: Reading the details of a resource that does or doesn't exist?
- Update: Updating a resource successfully/unsuccessfully? 
- Delete: Deleting a resource that does/doesn't exist. 

For a more advanced web API, we can also consider the following questions:
- For each endpoint, what is the response when a user is not logged in?
- For each endpoint, what is the response when a user is logged in, but they aren't authorized?

## Meaningful Status Codes
Look at list of standard HTTP codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- 100 - 199: Informational, rare to use.
- 200 - 299: Successful resp
  - Ex: 200 - Ok - Sucessful request
  - Ex: 201 - Created - Request sucess and new resource created
- 300 - 399: Redirects
  - Ex: 301 - Moved permanently - URL of req resource moved.
- 400 - 499: Client error
- 500 - 599: Sever error

## JSON response body
Consider: 
- What is the client expecting?
- What does the client need to know?
- What's the best way to structure what the client needs to know?

**Response Bodies Are Optional**
- RESTful APIs send back self-descriptive responses. Sometimes, an HTTP status code and message is all you need!

APP IDEA:
The name of the app is cleanUP. The responsibility of this app is to track groups of users and the location that they would like to clean up along with their availability. This app is unique because it connects groups based on their preferred location and availability, promoting the building of local community and increased sense of responsibility for their natural environment. Users will be able to set their preferred locations, select dates, and message other groups that match similar criteria. They will also be able to complete challenges as combined groups and individual groups. Users without a group will be able to join existing groups that match similar criteria. 

