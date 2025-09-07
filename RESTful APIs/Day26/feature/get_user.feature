Feature: Fetch posts from JSONPlaceholder API

  Scenario: Get all posts from JSON URL
    Given the JSON API endpoint "https://jsonplaceholder.typicode.com/posts"
    When I send a GET request to the endpoint
    Then I should receive a JSON response with posts
    And I print each post title
