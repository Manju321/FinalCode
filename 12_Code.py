"""Using Python 3.6

Ans for 12th Program

12. Write a program that can parse a JSON string {a:1,b:2,c:3} and print the keys and values. Then access the value 3 using its key ‘c’."""

import json 
inp = '{"a":1,"b":2,"c":3}'
data = json.loads(inp) 
for k, v in data.items(): 
    print(k, 'Value is:', v) 

print(data['c']) 
