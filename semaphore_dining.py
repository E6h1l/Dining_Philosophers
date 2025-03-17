import threading
import time
import random

# Number of philosophers
N = 5

# Counting semaphore to limit philosophers at the table
room = threading.Semaphore(N-1)  # Allow at most N-1 philosophers to enter

# Printing lock for clean output
print_lock = threading.Lock()

def safe_print(message):
    with print_lock:
        print(message)

def think(i):
    safe_print(f"Philosopher {i} is thinking")
    time.sleep(random.randint(1, 3))  # Think for 1-3 seconds

def eat(i):
    safe_print(f"Philosopher {i} is eating")
    time.sleep(random.randint(1, 3))  # Eat for 1-3 seconds

def philosopher(i):
    while True:
        think(i)
        
        safe_print(f"Philosopher {i} is hungry")
        
        # Enter the dining room (only N-1 philosophers allowed at once)
        room.acquire()
        
        safe_print(f"Philosopher {i} has entered the dining room")
        safe_print(f"Philosopher {i} picked up both forks")
        eat(i)
        safe_print(f"Philosopher {i} put down both forks")
        safe_print(f"Philosopher {i} has left the dining room")
        
        # Leave the dining room
        room.release()

def main():
    # Create philosopher threads
    philosophers = []
    for i in range(N):
        thread = threading.Thread(target=philosopher, args=(i,))
        thread.daemon = True  # Set as daemon so we can exit with Ctrl+C
        philosophers.append(thread)

    # Start all threads
    for thread in philosophers:
        thread.start()
    
    try:
        # Keep the program running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting the dining philosophers simulation")

if __name__ == "__main__":
    main()