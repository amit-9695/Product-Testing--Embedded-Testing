from behave import given, when, then

@given(u': the number is {number:d}')
def step_impl(context, number):
    context.number = number
   


@when(u'I chek if the number is "{message}"')
def step_impl(context, message):
    if context.number % 2 == 0:
        context.result = message
    

@then(u'The result should be "{result}"')
def step_impl(context,result):
    assert context.result == result, f"Expected {result}, but got {context.result}"
    print(f"Test passed: {context.result} matches expected result {result}")