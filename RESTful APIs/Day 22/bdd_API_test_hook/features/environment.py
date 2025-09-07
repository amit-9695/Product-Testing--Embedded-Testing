# This is the example of a Python file that sets up hooks for a testing framework.
def before_senario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    
def after_senario(context, scenario):
    print(f"Finished scenario: {scenario.name}")