from behave import given, when,then
 
 
@given(u'I have numbers {num1:d} and {num2:d}')
def step_given_number(context,num1,num2):
    context.num1=num1
    context.num2=num2
 
 
 
@when(u'I add the numbers')
def step_when_add(context):
    context.result=context.num1+context.num2
 
 
@then(u'the result should be {expected:d}')
def step_then_result(context,expected):
    assert context.result==expected, f"Expected {expected}, got {context.result}"