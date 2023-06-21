print("Lyric Guessing Game!")
print()
print("fill in the blank lyrics!")
print("(type in the blank lyrics and see if you are as cool as me.)")
print()
counter = 1
while True:
    print("All circles presuppose they'll end where they ___")
    guess = input()
    if guess == "begin":
        break
    else:
        print("nope, try again")
        counter += 1

print()
print("Well done! it only took you " + str(counter) + " atempts.")
