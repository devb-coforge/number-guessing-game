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
level_map = {'E': (1, 50, 10), 'M': (1, 100, 8), 'H': (1, 500, 10)} # Maps level to (start, end, attempts_allowed)

level = input("Select a level, E for Easy, M for Medium, H for Hard: ").strip().capitalize()

while level not in level_map.keys():
    level = input("Select a level, E for Easy, M for Medium, H for Hard").strip().capitalize()

range_start, range_end, attempts_allowed = level_map[level]


# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
secret = random.randint(range_start, range_end) if not DEBUG_SECRET else DEBUG_SECRET

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
num_attempts = 0
while num_attempts < attempts_allowed:
    print(f"Number of attempts remaining: {attempts_allowed-num_attempts}")
    user_guess = input(f"Guess a number between {range_start} to {range_end}: ").strip()
    if not user_guess.isdigit():
        print("Not a valid number, only integers supported")
        continue
    user_guess_int = int(user_guess)
    if user_guess_int < range_start or user_guess_int > range_end:
        print(f"Numbers are out of range, range is between {range_start} and {range_end}")
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