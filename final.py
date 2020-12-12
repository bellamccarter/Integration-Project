# Bella McCarter
# The Decade Quiz (A quiz that figures out which decade you'd thrive in)
import sys
username = input("What is your name? ")


def greeting(name):
    # greets and welcomes the quiz taker
    print("Hey, " + name + "! Welcome to the Decade Quiz!", sep="")


greeting(username)
score = 0
cancel_o_start = input("Type Enter to start the quiz or type Cancel: ")
if cancel_o_start == "Cancel":
    sys.exit("Cancelling quiz...")
# end * 3 is to make an ellipses
elif cancel_o_start == "Enter" or "enter":
    print("Out of the following, which color is your favorite? \n")
    print("a. Yellow.\n")
    print("b. Black.\n")
    print("c. Light Blue.\n")
    print("d. Bright Blue.\n")
    print("e. Scarlet.\n")
    print("f. Indigo.\n")
    print("g. Pink.\n")
    print("h. Beige.\n")
    answer_1 = input("Answer: ")
    if answer_1 == "a":
        score = score - 2
    if answer_1 == "b":
        score = score - 1
    if answer_1 == "c":
        score = score + 0
    if answer_1 == "d":
        score = score + 1
    if answer_1 == "e":
        score = score + 2
    if answer_1 == "f":
        score = score + 3
    if answer_1 == "g":
        score = score + 4
    if answer_1 == "h":
        score = score + 5

    # these are the calculations to determine decade

# https://vintagedancer.com/1940s/1940s-mens-fashion/
# https://www.crfashionbook.com/fashion/g27033975/
# fashion-staples-throughout-decade/?slide=6
if input("Press enter or return to continue: ") == "Enter" or "enter":
    print("Which artists are you most likely to listen to?\n")
    print("a. Frank Sinatra.\n")
    print("b. Queen.\n")
    print("c. Nirvana.\n")
    print("d. Louis Armstrong.\n")
    print("e. Glenn Miller.\n")
    print("f. Michael Jackson.\n")
    print("g. The Beatles.\n")
    print("h. Elvis Presley.\n")
    answer_2 = input("Answer: ")
    if answer_2 == "a":
        score = score - 2
    if answer_2 == "b":
        score = score - 1
    # subtracts from score to decide decade
    if answer_2 == "c":
        score = score + 0
    if answer_2 == "d":
        score = score + 1
    if answer_2 == "e":
        score = score + 2
    if answer_2 == "f":
        score = score + 3
    if answer_2 == "g":
        score = score + 4
    if answer_2 == "h":
        score = score + 5


# adds 5 pts to the score
# https://grammar.yourdictionary.com/slang/
# 1970-s-slang.html

if input("Press enter or return to continue: ") == "Enter" or "enter":
    print("Which event sounds the most intriguing?\n")
    print("a. Camping trip.\n")
    print("b. Going to the disco.\n")
    print("c. Spending the day at a skate park.\n")
    print("d. A night out dancing at the club.\n")
    print("e. A concert.\n")
    print("f. Break Dance Contest.\n")
    print("g. Going to the drive in.\n")
    print("h. A game night with friends.\n")
    answer_3 = input("Answer: ")
    if answer_3 == "a":
        score = score - 2
    if answer_3 == "b":
        score = score - 1
    if answer_3 == "c":
        score = score + 0
    if answer_3 == "d":
        score = score + 1
    if answer_3 == "e":
        score = score + 2
    if answer_3 == "f":
        score = score + 3
    if answer_3 == "g":
        score = score + 4
    if answer_3 == "h":
        score = score + 5


# https://medium.com/@Rifftime_Music/
# music-trends-through-the-decades-b8c5cbbae08b

if input("Press enter or return to continue: ") == "Enter" or "enter":
    print("Which slang phrase/word do you like the most?\n")
    print("a. 'Eager Beaver' - meaning 'enthusiastic'\n")
    print("b. 'Peace out, home fry' - meaning 'Goodbye'\n")
    print("c. 'Booyah' - meaning excitement\n")
    print("d. 'Meat Wagon' - meaning 'Ambulance'\n")
    print("e. 'Blow your wig' - meaning 'Get Excited'\n")
    print("f. 'Gnarly' - meaning 'Exciting'\n")
    print("g. 'Groovy' - meaning 'Cool'\n")
    print("h. 'Ankle-Biter' - meaning 'small child'\n")
    answer_4 = input("Answer: ")
    if answer_4 == "a":
        score = (score - 2) ** 1
    # the exponential numeric puts calculations to the first power
    if answer_4 == "b":
        score = (score - 1) ** 1
    if answer_4 == "c":
        score = (score + 0) ** 1
    if answer_4 == "d":
        score = (score + 1) ** 1
    if answer_4 == "e":
        score = (score + 2) ** 1
    if answer_4 == "f":
        score = (score + 3) ** 1
    if answer_4 == "g":
        score = (score + 4) ** 1
    if answer_4 == "h":
        score = (score + 5) ** 1

print("Bonus Question: Which movie would you watch out of the following?")
# https://www.imdb.com/list/ls023614474/

fi_qu_1 = ("a. Dumbo.", "b. Catch-22.", "c. Pulp Fiction.",
           "d. Way Down East.")
fi_qu_2 = ("e. Hell's Angels.", "f. Breakfast Club.",
           "g. Psycho.", "h. Cinderella.")
# bonus is decided by score on first 4
if -8 <= score <= 5 and not score > 5:
    for x in fi_qu_1:
        print(x)
    fi_ans_1 = input("Answer: ")
    if fi_ans_1 == "a":
        score = (score - 2) * 2  # to make the question hold more weight
    if fi_ans_1 == "b":
        score = (score - 1) * 2
    if fi_ans_1 == "c":
        score = (score + 0) / 1
    # because dividing something by 0 doesn't change #
    if fi_ans_1 == "d":
        score = (score + 1) * 2


if 6 <= score <= 20 and not score == 0:
    for x in fi_qu_2:
        print(x)
    fi_ans_2 = input("Answer: ")
    if fi_ans_2 == "e":
        score = (score + 2) * 2  # to make the question hold more weight
    if fi_ans_2 == "f":
        score = (score + 3) * 2
    if fi_ans_2 == "g":
        score = (score + 4) * 2
    if fi_ans_2 == "h":
        score = (score + 5) * 2


print("Your score is: ", score // 1)
# Floor division is used to round score to nearest whole number

# A = 40's
# B = 70's
# C = 90's
# D = 20's
# E = 30's
# F = 80's
# G = 60's
# H = 50's

print(input("Please press enter or return to see results! : "))

print("Calculating in...")
x = 3
while x > 0 < 4:
    rng_1 = print(x) in range(3, 1)
    x -= 1

if -20 <= score <= -11 and score != 0:
    print("You would thrive in the 40s!/\n"
          "You would be described as modern. You like to\n"
          "be up to date with what's new.")

if -10 <= score <= -1 and score != 0:
    print("You would thrive in the 70's!\n"
          "This was the decade of acceptance. An adjective\n"
          " commonly used ot describe yourself is 'non-judgmental")

if 0 <= score <= 10 and score:
    print("You would thrive in the 90's!\n"
          "Peaceful is probably how you've been described and social.\n"
          "You also strive for success rather than giving into what is\n"
          " thrown your way.")

if 11 <= score <= 20 and score != 0:
    print("You would thrive in the 20's!\n"
          "Your answers reflect that you have a carefree way of living. \n"
          "You probably welcome change rather than avoid it.")

if 21 <= score <= 30 and score != 0:
    print("You would thrive in the 30's!\n"
          "You love to be entertained. Whether it be from the TV, the\n"
          " radio, or just by a person. You don't like the feeling of\n"
          " boredom and like to stay busy.")

if 31 <= score <= 40 and score != 0:
    print("You would thrive in the 80's!\n"
          "Not to say you love attention, but you probably love attention.\n"
          "The eighties were very much the 'look at me' decade.")

if 41 <= score <= 50 and score != 0:
    print("You would thrive in the 60's!\n"
          "This was the decade for standing up for what you \n"
          "believe in. You are not one to bite your tongue.")

if 17 <= score <= 20 and score != 0:
    print("You would thrive in the 50's!\n"
          "This is the decade for doing what you think is right.\n"
          "You've probably been described as a good person.")
# scores added up decide the decade you belong in
