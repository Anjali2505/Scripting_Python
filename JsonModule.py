#JavaScript Object Orientation
#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.
import json

employee_data = '''
{
  "people": [
    {
      "name": "Anjali",
      "email": "xyz@gmail.com",
      "married": false
    },
    {
      "name": "Anu",
      "email": "xyz19996@gmail.com",
      "married": true
    }
  ]
}
'''

#printing json
print(employee_data)

#printing data in python by converting json to dictionary, array to list , null -> None , true -> True and so on
data=json.loads(employee_data)
print(data)

# convert into JSON:
y = json.dumps(data)
print(y)
