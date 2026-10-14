import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
DEFAULT_ATTEMPTS_ALLOWED = 10   #Max attempts allowed in Classic mode
DEFAULT_RANGE_START, DEFAULT_RANGE_END = 0, 50 # Start and end values when not speified by user is Phase 1

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
secret = random.randint(DEFAULT_RANGE_START, DEFAULT_RANGE_END) if not DEBUG_SECRET else DEBUG_SECRET

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
num_attempts = 0
while num_attempts < DEFAULT_ATTEMPTS_ALLOWED:
    print(f"Number of attempts remaining: {DEFAULT_ATTEMPTS_ALLOWED-num_attempts}")
    user_guess = input(f"Guess a number between {DEFAULT_RANGE_START} to {DEFAULT_RANGE_END}: ").strip()
    if not user_guess.isdigit():
        print("Not a valid number, only integers supported")
        continue
    user_guess_int = int(user_guess)
    if user_guess_int < DEFAULT_RANGE_START or user_guess_int > DEFAULT_RANGE_END:
        print(f"Numbers are out of range, range is between {DEFAULT_RANGE_START} and {DEFAULT_RANGE_END}")
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