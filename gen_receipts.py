import random
import os
import json

count = int(os.getenv("FILE_COUNT") or 10)
words = [word.strip() for word in open('words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount #change amount to currency
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)
