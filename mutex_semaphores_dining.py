import threading
import time
import random

# Number of philosophers
N = 5

# Mutex for protecting fork access
mutex = threading.Lock()

# Semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(N)]

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

def take_forks(i):
    left_fork = i
    right_fork = (i + 1) % N
    
    # Critical section: pick up both forks atomically
    mutex.acquire()
    forks[left_fork].acquire()
    forks[right_fork].acquire()
    mutex.release()
    
    safe_print(f"Philosopher {i} picked up forks {left_fork} and {right_fork}")

def put_forks(i):
    left_fork = i
    right_fork = (i + 1) % N
    
    # Release both forks
    forks[left_fork].release()
    forks[right_fork].release()
    
    safe_print(f"Philosopher {i} put down forks {left_fork} and {right_fork}")

def philosopher(i):
    while True:
        think(i)
        
        safe_print(f"Philosopher {i} is hungry")
        
        take_forks(i)
        eat(i)
        put_forks(i)

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