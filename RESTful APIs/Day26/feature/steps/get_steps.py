import requests
from behave import given, when, then

@given('the JSON API endpoint "{url}"')
def step_given_api_endpoint(context, url):
    context.api_url = url

@when('I send a GET request to the endpoint')
def step_when_send_get_request(context):
    context.response = requests.get(context.api_url)

@then('I should receive a JSON response with posts')
def step_then_validate_json_response(context):
    assert context.response.status_code == 200, f"Status code: {context.response.status_code}"
    assert context.response.headers["Content-Type"].startswith("application/json")
    context.posts = context.response.json()
    assert isinstance(context.posts, list), "Expected a list of posts"

@then('I print each post title')
def step_then_print_titles(context):
    for post in context.posts:
        print(f"Post {post['id']}: {post['title']}")
