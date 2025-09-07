Feature: :Get User details
Scenario: Retrieve user information sucssessfully
Given the API url is "https://api.restful-api.dev/objects?id=3&id=5&id=10"
When I send a GET request
Then the response status code should be 200
And the response should contain  "3"