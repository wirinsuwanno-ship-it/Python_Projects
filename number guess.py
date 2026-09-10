guessanswer = 67
guessnum = int(input("guess the number"))

if guessnum > guessanswer:
    print("too high")
elif guessnum < guessanswer:
    print("too low")
elif guessnum == guessanswer:
    print("correct!")
else:
    print("are you even trying?")
