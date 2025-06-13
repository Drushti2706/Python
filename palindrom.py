text = input("Enter word or number: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
