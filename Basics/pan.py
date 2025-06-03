pan=input()
print(len(pan)==10 and pan[:5].isalpha() and pan[:5].isupper() and pan[5:-1].isdigit() and pan[-1].isalpha() and pan[-1].isupper())
