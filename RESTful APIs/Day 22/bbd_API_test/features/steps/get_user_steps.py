from behave import given, when, then
@given(u'the API url is "https://api.restful-api.dev/objects?id=3&id=5&id=10"')
def step_impl(context):
    context.a=10
    raise NotImplementedError(u'STEP: Given the API url is "https://api.restful-api.dev/objects?id=3&id=5&id=10"')


@when(u'I send a GET request')
def step_impl(context):
    
    raise NotImplementedError(u'STEP: When I send a GET request')
    

@then(u'the response status code should be 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response status code should be 200')


@then(u'the response should contain  "3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response should contain  "3"')