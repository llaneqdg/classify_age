classify_age = int(input("Enter your age: "))

if classify_age <= 12:
    print("You are a child.")
elif classify_age <= 19:
    print("You are a teen.")
elif classify_age <= 64:
    print("You are an adult.")
else:
    print("You are a senior citizen.")