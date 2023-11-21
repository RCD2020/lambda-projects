# status, body
# status code
# body: [
#   {'city', 'value', 'date':{'time'}}
# ]

# for entry in body:
#   entry['date']['time']

listy = [
    {'value': 4, 'date': {'utc': 'this date'}},
    {'value': 6, 'date': {'utc': 'that date'}},
    {'value': 10, 'date': {'utc': 'these dates'}}
]

tuplelist = []
for x in listy:
    tuplelist.append(x['value'])

print(tuplelist)