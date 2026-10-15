import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT_SECONDS = 60 # Seconds allowed in Time Challenge mode
print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# Each choice maps to (minimum number, maximum number, allowed attempts).
level_map = {
    '1': (1, 50, 10), # easy
    '2': (1, 100, 8), # medium
    '3': (1, 500, 10) # hard
} 

level_prompt = "Select a level:\n1. Easy\n2. Medium\n3. Hard\nEnter the level number (1, 2, or 3): "
level = input(level_prompt).strip()

while level not in level_map.keys(): # Retry invalid choices without converting them to integers.
    level = input(level_prompt).strip()

range_start, range_end, attempts_allowed = level_map[level]

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
mode_prompt = "Select a mode:\n1. Time Challenge\n2. Classic\nEnter the mode number (1 or 2): "
mode = input(mode_prompt).strip() # Choices: 1 = Time Challenge, 2 = Classic.
while not mode in ('1', '2'):
    mode = input(mode_prompt).strip()
isTimed = True if mode == '1' else False
# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
secret = random.randint(range_start, range_end) if not DEBUG_SECRET else DEBUG_SECRET # A positive debug value makes tests repeatable.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
num_attempts = 0
start_time = time.time()
user_won = False
while num_attempts < attempts_allowed:
    if isTimed:
        print(f"Time remaining: {TIME_LIMIT_SECONDS - (time.time() - start_time)} seconds")
    user_guess = input(f"Guess a number between {range_start} to {range_end}: ").strip()
    # Reject ordinary nonnumeric input before counting an attempt.
    if not user_guess.isdigit():
        print("Not a valid number, only integers supported")
        continue
    user_guess_int = int(user_guess) #convert string input to integer
    if user_guess_int < range_start or user_guess_int > range_end:
        print(f"Numbers are out of range, range is between {range_start} and {range_end}")
        continue
    
    # Only guesses within the selected range are considered valid
    num_attempts += 1

    # input() blocks: check elapsed time after a valid guess, before checking a win.
    if isTimed:
        time_elapsed = time.time() - start_time
        if time_elapsed >= TIME_LIMIT_SECONDS:
            break #No need to continue after the secret is revealed

    if user_guess_int == secret:
        user_won = True
        break # Once user guesses the secret break the loop
    elif user_guess_int < secret:
        print("Too Low")
    else:
        print("Too High")

    print(f" You have {attempts_allowed-num_attempts} attempts remaining")


# ---------- End of round ----------
# Report the winning attempt total, or reveal the secret after a loss.
if user_won:
    print(f"CONGRATS, you are correct, you took {num_attempts} attempts to solve this")
else:
    print(f"GAME OVER!!, the secret number was {secret}")
