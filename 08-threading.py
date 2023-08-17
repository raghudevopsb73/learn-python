import threading
import subprocess

def print_numbers():
    for i in range(1, 6):
        print("Number:", i)

def print_letters():
    subprocess.run(["sleep", "20"], capture_output=True, text=True)

# Create two thread objects
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

