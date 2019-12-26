# guess the secret word

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
# check to see if guess = secret word, if not, guess count +1
# if the user isn't already out of guesses, allow the loop to continue
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    # if guess_count is over 3, then make out_of_guesses True


if out_of_guesses:
    print("Out of guesses")
else:
    print("You guessed right!")

