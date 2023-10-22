import json
import random
from faker import Faker

fake = Faker()

communication_sets = []

for i in range(1, 100001):
    communication_set = {
        "communication_set_id": i,
        "sender": fake.name(),
        "receiver": fake.name(),
        "message": fake.sentence(),
    }
    communication_sets.append(communication_set)

with open("communication_sets.json", "w") as json_file:
    json.dump(communication_sets, json_file, indent=2)

print("JSON file created with 1000 communication sets.")
