# Intro to Web Dev

## Web Applications and Layers
- Web App: App software that runs on a web server
- End-user: Person who uses a product
- Front-end: Part of system concerned with dealing with user interaction
- Back-end: Part of system concerned with running logic and storing data
- Web APIs: Software built to translate messages nbetween a user and a web server.

## Web apps
When using a web app, a user interacts with the web app as the client. The web app connects to a web server. The web server returns responses back to the user (client).

Back-end can connect to a databse and do other tasks.
example: Social media site - fetch and modify the data stored about users, photos, posts, events, groups, friends, and more. Contains the logic and algorithms for what posts to show.

## APIs
Translate messages that go from Software A to Software B, usually from a user and webserver. 
Example: Yelp's fusion API - Within Yelp's databases, search for businesses by keyword, location, category, price level; get reviews for a specific business; get autocomplete suggestions for a business

Front-end layer (commonly referred to as "front-end") for a web app is responsible for containing the logic that works with user interaction.
Example: Social media site - arranges how data about users, photos, posts, events, and groups are shown on a social media timeline page. Determines what the user sees and does when they make social media posts.

## Front and Back interaction
Here is a simplified description of how the end-user, front-end, back-end, and database all interact with each other
1. An end-user (the person who actually uses a particular product) interacts with the front-end of a web app through their web browser
2. The front-end communicates with a web server, usually by sending a message to a back-end web API
3. The back-end web API communicates with a database for any stored data

## Cients, Servers, HTTPS
- Client: a computer who sends a request for a resource to a server, and receives back a response
- Server: a computer who receives requests for a resource from a client, and sends back a response
- Web Server: a server that is specifically connected to a client over the web
- HTTP: A specific protocol that determines how a clients and web servers communicate

## Client-Server Model
- Set up between 2+ machines. 
  - One comp = client
  - One comp = server
  - Client asks for specific data by sending a request to server.
  - Server receives reuqest and server tries to fulfill request.
  - Server gives back response.
  - Client receives response. 

Clients can make as many requests as they would like. Servers can take requests from many different clients.

Over the internet, we use a web server instead of a server. 
- A web server is a machine (computer) that hosts and serves a website or data specifically over the Internet.

## Protocol Communication
A protocol is a set of rules that define the format of data exchange.

HTTP, is the protocol of communication over the web. It's the specific set of rules that websites follow in order to send and receive data.

HTTP is a protocol that always assumes the client-server model. Again, this means that the client is usually a user's web browser, and the server is a web server.

HTTP defines the exact technical ways that:
- A client opens a network connection to a web server
- A request looks and behaves
- A response looks and behaves

**HTTPS**
HTTPS, or Hypertext Transfer Protocol Secure, is an extension of HTTP. Many implementations of HTTP (particularly early ones) did not have the best security. Because HTTP deals with how data travels between computers, data can be breached during that process. HTTPS's technical details address a lot of security concerns. 

## Sequence Diagrams
Sequence Diagrams Show Communication Over Time
- they depict one scenario or event. 
- each vertical column represents an object, actor, or process.
  - Ex: User, front-end, back-end API, database
- each horizontal line is usually an arrow that represents a message being sent. 
  - message = generic discrete communication
  - HTTP request or response

