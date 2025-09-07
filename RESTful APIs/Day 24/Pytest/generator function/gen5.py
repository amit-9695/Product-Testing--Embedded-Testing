# Generators vs Normal Collections wrt Performance

import random
import time 

name=["amit", "sachin", "rohit", "virat", "dhoni", "hardik", "kl"]
subject=["maths", "english", "science", "history", "geography", "computer"]

def generate_random_data(num_people):
    result= []
    for i in range(num_people):
        person = {
            id: i,
            "name": random.choice(name),
            "subject": random.choice(subject)
        }
        result.append(person)
    return result

# Using a generator to yield random data
def generate_random_data_gen(num_people):
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(name),
            "subject": random.choice(subject)
        }
        yield person
        
# Performance comparison
t1 = time.time()
data = generate_random_data(1000000)
t2 = time.time()
print("Time taken with list:", t2 - t1)
print("Took {}".format(t2 - t1))