import time
alarm_time = input("Set alarm (HH:MM:SS): ")

while True:
    current = time.strftime("%H:%M:%S")
    if current == alarm_time:
        print("⏰ Time to Wake Up!")
        break
    time.sleep(1)
