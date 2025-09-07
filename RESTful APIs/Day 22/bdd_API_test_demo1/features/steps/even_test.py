from behave import given, when, then

@given(u'the number is {number:d}')
def step_impl(context, number):
    context.number = number
      


@when(u'I check if the number is even')
def step_impl(context):
    if context.number % 2 == 0:
        context.result = "even"
    else:
        context.result = "odd"
    


@then(u'the result should be "{expected_result}"')
def step_impl(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"