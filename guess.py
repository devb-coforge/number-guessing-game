import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
TIME_LIMIT_SECONDS = 60 # Max seconds in timed challenge mode
print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
level_map = {'E': (1, 50, 10), 'M': (1, 100, 8), 'H': (1, 500, 10)} # Maps level to (start, end, attempts_allowed)

level = input("Select a level, E for Easy, M for Medium, H for Hard: ").strip().capitalize() #Supports case-insensitive input

while level not in level_map.keys(): #keep looping until user enters a valid level
    level = input("Select a level, E for Easy, M for Medium, H for Hard").strip().capitalize()

range_start, range_end, attempts_allowed = level_map[level]


# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
mode = input("Enter 1 for timed mode, 2 for Classic mode: ").strip() #todo: need to show in numbered list format
while not mode in ('1', '2'):
    mode = input("Enter 1 for timed mode, 2 for Classic mode: ").strip()
isTimed = True if mode == '1' else False
# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
secret = random.randint(range_start, range_end) if not DEBUG_SECRET else DEBUG_SECRET #select random secret if default is none

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
num_attempts = 0
start_time = time.time()
user_won = False
while num_attempts < attempts_allowed:
    print(f"Number of attempts remaining: {attempts_allowed-num_attempts}")
    if isTimed:
        print(f"Time remaining: {TIME_LIMIT_SECONDS - (time.time() - start_time)} seconds")
    user_guess = input(f"Guess a number between {range_start} to {range_end}: ").strip()
    if not user_guess.isdigit(): #reject user input if it is string/ letters
        print("Not a valid number, only integers supported")
        continue
    user_guess_int = int(user_guess) #convert string input to integer
    if user_guess_int < range_start or user_guess_int > range_end:
        print(f"Numbers are out of range, range is between {range_start} and {range_end}")
        continue
    
    num_attempts += 1

    if isTimed:
        time_elapsed = time.time() - start_time
        if time_elapsed > TIME_LIMIT_SECONDS:
            print(f"Time limit expired, the number was: {secret}")
            break #No need to continue after the secret is revealed

    if user_guess_int == secret:
        user_won = True
        break # Once user guesses the secret break the loop
    elif user_guess_int < secret:
        print("Too Low")
    else:
        print("Too High")

if user_won:
    print(f"CONGRATS, you are correct, you took {num_attempts} attempts to solve this")
else:
    print(f"GAME OVER!!, the secret number was {secret}")
    
    

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.