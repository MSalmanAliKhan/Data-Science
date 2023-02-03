# Count how many times a letter is repeated in user input
Name,Letter=input("Enter your name and the letter you want to count ").split(",")
print(f"The number of letters in {Name.strip()} are {len(Name.strip())} and the letter {Letter.strip()} is repeated {Name.strip().lower().count(Letter.strip().lower())} times")

