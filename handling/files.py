import json

with open("sb.json","r") as f:
    py_str=json.load(f)

    print(type(py_str),py_str)
    

with open("dd.json","w") as d:
    details={
        "name":"saniya afreen",
        "college":"gitam ",
        "course":"BDS",
        "Year":"3rd",
        "Scholarship":"Yes"
    }
    json.dump(details,d,indent=4,sort_keys=True)

    


