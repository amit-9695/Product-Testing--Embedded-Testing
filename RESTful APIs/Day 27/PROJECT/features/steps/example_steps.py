from behave import given, when, then

@given('I have two numbers {a:d} and {b:d}')
def step_impl(context, a, b):
    context.a = a
    context.b = b

@when('I add them')
def step_impl(context):
    context.result = context.a + context.b


@then('the result should be {expected:d}')
def step_impl(context,expected):
    assert context.result == expected
    