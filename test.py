"""
There is a input .csv file containing 3.000.000 rows as follow:

John,Doe,20-05-1985,Engineer,javascript
Frodo,Baggins,10-07-1985,Architect,GCP
John,Doe,20-05-1985,Engineer,python
John,Doe,20-05-1985,Engineer,javascript

We need a script that loads the data into a queue, to be processed async for another component:


full_name: string concat of first and last name

age: int person's age given his date of birth

fav_tech: string as is in source separated by comma, aggregated by name


	{
		"full_name" : "john doe",
		"age" : "36",
		"fav_tech" : "javascript, python"
	}
"""


import csv 
from collections import deque
from datetime import date

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            yield line



def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def find(q: deque, full_name: str):
   return next((x for x in q if x["full_name"] == full_name), None)


def parse_line(line, q: deque):
    full_name = f"{line[0]} {line[1]}"
    element = find(q, full_name)
    if element:
        element["fav_tech"].append(line[4])

    else:
        element = {
            "full_name" : full_name,
            # "age" : calculate_age(date(line[2])),
            "fav_tech" : [line[4]]
        }
    return element

def process():
    gen = lines("data.csv")
    q = deque()

    for item in gen:
       print(parse_line(item, q))
       q.append(parse_line(item, q))

    ", ".join(item["fav_tech"])
    # print(q)
    
process()

  


  