def encode(msg):
    return ''.join([chr(ord(c) + 3)for c in msg])

def decode(code):
    return ''.join([chr(ord(c) - 3) for c in code])

choice = input("Enter 'e' to encode or 'd' to decode: ").lower()
text = input("Enter your message: ")

if choice == 'e':
    print("Encoded:", encode(text))
elif choice == 'd':
    print("Decoded:", decode(text))
else:
    print("Invalid choice.")
    
