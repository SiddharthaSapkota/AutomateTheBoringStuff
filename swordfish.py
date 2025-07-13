while True:
    print("Who are you?")
    name = input()
    if name.lower() != 'joe':
        continue
    print("Hello, Joe. What's the password?(It is a fish)")
    password =input().strip()
    if password =="swordfish":
        break
    print("Access Denied! Incorrect password.")
print("Access Granted!")
