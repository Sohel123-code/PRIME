# mainly in python the json data and dictionaries are handled with the help of some functions
# loads is used to load the json string and convert into python onject i.e dictionaries
# dumps is used to convert the dictionaries in python to json string .
# and when we work with the files then we use load and dump functions to read the data

import json


js_str='{"name":"mohamed khaja eshaq","student":true}'

print(type(js_str))

py_str=json.loads(js_str)

print(type(py_str),py_str)






