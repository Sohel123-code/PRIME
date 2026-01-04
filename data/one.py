import json

def dataload(filename):
    with open(filename, "r") as f:
        return json.load(f)

def clean_data(data):
    text = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

    for user in data:
        # clean rating
        raw = user.get("rating")
        if isinstance(raw, str):
            raw = raw.lower().strip()
            if raw in text:
                user["rating"] = text[raw]
            else:
                try:
                    user["rating"] = float(raw)
                except:
                    user["rating"] = None

        # clean age
        raw_age = user.get("age")
        try:
            user["age"] = int(raw_age)
        except:
            user["age"] = None

    return data

data = dataload("data.json")
cleaned_data = clean_data(data)

print(cleaned_data)
