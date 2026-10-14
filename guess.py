import random
import time

# ---------- Settings ----------
DEBUG_SECRET = 33   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
TOTAL_ATTEMPTS = 10   #Max attempts allowed in Classic mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
start, end = 0, 100
secret = random.randint(start, end) if not DEBUG_SECRET else DEBUG_SECRET

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
num_attempts = 0
while num_attempts < TOTAL_ATTEMPTS:
    print(f"Number of attempts remaining: {TOTAL_ATTEMPTS-num_attempts}")
    user_guess = input(f"Guess a number between {start} to {end}: ").strip()
    if not user_guess.isdigit():
        print("Not a valid number, only integers supported")
        continue
    user_guess_int = int(user_guess)
    if user_guess_int < start or user_guess_int > end:
        print(f"Numbers are out of range, range is between {start} and {end}")
    num_attempts += 1

    
    if user_guess_int == secret:
        print("Correct, CONGRATS!!")
        break
    elif user_guess_int < secret:
        print("Too Low")
    else:
        print("Too High")

print("GAME OVER!!")
    
    

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.