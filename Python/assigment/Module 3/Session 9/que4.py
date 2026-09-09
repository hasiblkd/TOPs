import re

order_ids = ['ORD1234', 'ORD5678', 'ORD9999', 'ORD0001']

for order_id in order_ids:
    result = re.match(r"^ORD\d*[02468]$", order_id)
    if result:
        print(order_id)