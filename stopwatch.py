import time

def stopwatch():
    print("Stopwatch started. Press Enter to stop...")
    start = time.time()
    input()
    end = time.time()
    print(f"Elapsed Time: {round(end - start, 2)} seconds")

stopwatch()
