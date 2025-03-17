# Dining Philosophers Problem

This repository contains an implementation of the classic Dining Philosophers problem, a well-known synchronization and concurrency challenge in distributed systems.

## Problem Description

Five philosophers sit at a round table, alternating between thinking and eating. In the center of the table is a bowl of rice, and between each pair of adjacent philosophers is a single chopstick. To eat, a philosopher needs both the chopstick to their left and the chopstick to their right. The challenge is to design a protocol that allows the philosophers to eat without deadlocking.

## Usage

```bash
# Clone the repository
git clone https://github.com/username/Dining_Philosophers.git
cd Dining_Philosophers

# Run the application for realization with 1 semaphore
python semaphore_dining.py 

#OR

# Run the application for realization with 1 mutex and 5 semaphores
python mutex_semaphores_dining.py 
```

## Implementation Details

The solution is implemented using [programming language/technologies], with key components:
- Philosopher threads that alternate between thinking and eating
- Chopstick resources with mutex locks
- Deadlock prevention mechanism

## Results

The solution guarantees:
- No deadlock
- No starvation (each philosopher eventually gets to eat)
- Efficient resource utilization

## Code author

Prystaichuk Dmytro
