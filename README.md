# number-guessing-game

A terminal number guessing game. The computer picks a random secret number; the player receives `Too Low` or `Too High` hints until they win or run out of attempts or time. All game code is in `guess.py`.

## Setup and running

Python 3 is required. Only the standard-library `random` and `time` modules are used; no extra packages are needed. From the repository directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python guess.py
```

## How to play

Choose a difficulty:

1. Easy: range 1–50, with 10 attempts.
2. Medium: range 1–100, with 8 attempts.
3. Hard: range 1–500, with 10 attempts.

Choose a mode:

1. Time Challenge: 60 seconds for the whole round, with the selected difficulty's attempt limit.
2. Classic: the selected difficulty's attempt limit, without a time limit.

Enter an integer within the chosen range. Ordinary invalid entries (letters, symbols, blank entries, decimals, and out-of-range numbers) are rejected without consuming an attempt. Surrounding spaces are removed. Invalid difficulty and mode choices are requested again. Adversarial input limitations are recorded below.


## Test Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Hints and winning attempt count | Easy, Classic, secret 42; guess 20, 45, then 42. | Show `Too Low`, `Too High`, then win in 3 attempts. | Both hints were correct winning total was 3. | Yes |
| 2 | Letters, blanks, symbols, and decimals | In separate rounds, enter `abc`, blank, `@`, or `1.5`, then 42. | Reject invalid input without counting it; win in 1 attempt. | Each invalid entry rejected; only 42 counted. | Yes |
| 3 | Below-range and above-range guesses | Easy; enter 0 and 51, then 42. | Reject both out-of-range guesses without consuming attempts. | Both rejected; won in 1 valid attempt. | Yes |
| 4 | Invalid level and mode choices | Enter `abc`, blank, and 4 before selecting level 1; enter `abc`, blank, and 3 before selecting mode 2. | Retry both menus without crashing. | Both menus retried successfully. Earlier difficulty conversion crash was fixed by keeping choices as strings. | Yes |
| 5 | Easy range and attempt limit | Inspect settings, test secrets 1 and 50, and use 10 wrong guesses in a separate round. | Inclusive range 1–50; limit 10. | Both endpoints accepted; loss after 10 valid guesses. | Yes |
| 6 | Medium range and attempt limit | Inspect settings, test secrets 1 and 100, and use 8 wrong guesses in a separate round. | Inclusive range 1–100; limit 8. | Both endpoints accepted; loss after 8 valid guesses. | Yes |
| 7 | Hard range and attempt limit | Inspect settings, test secrets 1 and 500, and use 10 wrong guesses in a separate round. | Inclusive range 1–500; limit 10. | Both endpoints accepted; loss after 10 valid guesses. | Yes |
| 8 | Attempt exhaustion in both modes | Secret 42; guess 1 up to each level's limit in Classic and timed mode, with the simulated clock unexpired. | End at 10/8/10 attempts and reveal 42 in either mode. | All limits applied and the secret was revealed, including with time left. | Yes |
| 9 | Win on final allowed attempt | Guess 1 repeatedly, then 42 on attempt 10 for Easy/Hard or 8 for Medium. | Allow the final guess to win and report the exact count. | Won with counts 10, 8, and 10. | Yes |
| 10 | Timed wins on all levels | Submit 42 at simulated second 59 on each difficulty. | Win before the deadline using the selected level's settings. | All three levels won in 1 attempt. | Yes |
| 11 | Timeout and exact deadline | Submit correct guess 42 at simulated seconds 60 and 61 in separate rounds. | Reject either win and reveal 42 once. | Both lost and revealed 42 once. Fixed the earlier `>` boundary check to `>=` and removed duplicate ending output. | Yes |
| 12 | Remaining time before each guess | Simulate display times 1 and 3 seconds into the round; guess 1, then 42. | Display 59 and 57 seconds before the respective guesses. | Both remaining-time messages appeared before their guesses. | Yes |
