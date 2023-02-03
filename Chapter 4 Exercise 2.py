# Check if the user entered word is a palindrome
a_word=input("Enter a word ")
def palindrome(word):
    if word==word[::-1]:
        return(f"{word} is a palindrome")
    return(f"{word} is not a palindrom as its reverse is {reverse}")
print(palindrome(a_word.lower()))
