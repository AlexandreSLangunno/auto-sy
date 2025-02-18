cookies = []

def extract_name_and_value(data):
    for cookie in data:
        cookies.append({"name": cookie["name"], "value": cookie["value"]})
    return cookies