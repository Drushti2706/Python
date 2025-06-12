

import time

def calculate_wpm(start_time, end_time, typed_text):
    words = typed_text.split()
    num_words = len(words)
    time_minutes = (end_time - start_time) / 60
    wpm = num_words / time_minutes
    return wpm

def main():
    sample_text = (
        "Python is a powerful programming language that is easy to learn and fun to use."
    )
    print("Typing Speed Test")
    print("Type the following sentence exactly as shown:\n")
    print(sample_text)
    input("\nPress Enter when you're ready to start typing...")

    start_time = time.time()
    typed_text = input("\nStart typing:\n")
    end_time = time.time()

    if typed_text.strip() == "":
        print("\nYou didn't type anything!")
        return

    wpm = calculate_wpm(start_time, end_time, typed_text)
    print(f"\nYour typing speed is {wpm:.2f} WPM.")

    # Optional accuracy check
    accuracy = sum(1 for a, b in zip(typed_text, sample_text) if a == b) / len(sample_text) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
