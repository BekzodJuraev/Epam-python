def replacer(s: str) -> str:
    string=""
    for i in s:
        if i == "'":
            string += '"'
        elif i == '"':
            string += "'"
        else:
            string += i

    return string


