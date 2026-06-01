def valid_palimdrome(str):
    cleaned=""
    for char in str:
        if char == " ":
            continue
        if char.isalnum():
            cleaned+=char.lower()
        return cleaned==cleaned[::-1]


assert valid_palimdrome("Was it a car or a cat")==True 
print("All cases passed")