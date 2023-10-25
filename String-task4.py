def check_str(s: str):
    string=""
    for i in s:
        if i.isalnum():
            string+=i

    x = len(string) - 1
    for i in range(len(string)):
        #print(f"{s[x]}=={s[i]}")
        if string[x].lower()!=string[i].lower():
            return False
        x=x-1

    return True


