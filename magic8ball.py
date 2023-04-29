# Ruslan Gusakov
import random
answers_8ball = ("As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "It is Certain", "It is decidedly so", "Most likely",
                 "My reply is no", "My sources say no", "Outlook good", "Outlook no so good", "Reply hazy, try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes", "Yes, definitely", "You may rely on it", )


def main():
    print("I am the MAGIC-8 BALL and can answer any YEs or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8ball)

        print("\nShake the MAGIC-8 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question?")
        print("The MAGIC-8 BALL says: " + answer)

        askAgain = input(
            "\nWould you like to ask me another question (Yor N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions.")
    print("...Magic-8 Ball OUT.")


main()
