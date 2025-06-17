

import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

def main():
    try:
        user_input = int(input("Enter time in seconds: "))
        countdown(user_input)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
