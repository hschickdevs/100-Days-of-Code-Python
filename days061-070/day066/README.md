# Day 66 - Remote Work Cafe Database RESTful API

Run the API locally using the RESTful-API-cafe/main.py script.

View the API Documentation here: https://documenter.getpostman.com/view/22565244/UzkV1vwZ#438bedf3-21d3-4c03-8968-5c6a608c3c2e

### Features:
* Full CRUD - GET / POST / PUT or PATCH / DELETE
* 7 Endpoints

### <--------- Lesson Notes --------->

- **REST** = **RE**presentational **S**tate **T**ransfer

- Requests are made using HTTPS, HTTP, or FTP requests.

- HTTP vs. HTTPS:
  - HTTPS requests are secure requests, while HTTP are not.

- HTTP Request Verbs (Language):
  - GET: 
  - POST:
  - PUT: 
  - PATCH: Newly added to the HTTP request lang in 2010
  - DELETE: 

- RESTful Routing - Proper structure for REST routes using a /articles endpoint as an example:

  | HTTP Verbs | /articles                   | /articles/NVDA                  |
  |-----------------------------|---------------------------------|-----------------------------|
  | GET        | Fetches **all** articles    | Fetches **the** article on NVDA     |
  | POST       | Creates **one** new article | N/A                             |
  | PUT        | N/A                         | Updates **the** article on NVDA |
  | PATCH      | N/A                         | Updates **the** article on NVDA |
  | DELETE     | Deletes **all** the articles    | Deletes **the** article on NVDA |

- 