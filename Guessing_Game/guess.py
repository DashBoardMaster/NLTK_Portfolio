import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

# Amol Perubhatla
# AVP180003
# CS4395.001
# Professor Karen Mazidi

# This is a word guesssing game program and a lexical analysis program


def preprocess(text):
    # Lowercase and tokenize the text
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens]

    # Preprocess the tokens to remove stop words
    tokens = [t for t in tokens if t.isalpha(
    ) and t not in stopwords.words('english') and len(t) > 5]

    # Create set with unique lemmas
    uniqueLemmas = set(tokens)

    # POS tagging of the unique lemmas
    tags = nltk.pos_tag(uniqueLemmas)

    onlyNouns = [w[0] for w in tags if w[1] == 'NN' or w[1]
                 == 'NNS' or w[1] == 'NNP' or w[1] == 'NNPS']

    print("Tokens: " + str(len(tokens)))
    print("Nouns: " + str(len(onlyNouns)))

    return tokens, onlyNouns


def guess(topWords):
    # Start the score at 5
    points = 5

    # Generate a random word from the top 50
    randomWord = topWords[random.randint(0, 49)][0]

    print("Let's play a word guessing game!")

    pointsGained = 0
    currentGuess = ''
    alreadyGuessed = ""

    # This is the loop that runs the guessing game until the player loses or wins
    while (points != -1):
        # This will print the blanks and already guessed letters in blank letter format to aid the user in guessing
        for char in randomWord:
            if char in alreadyGuessed:
                print(char, end=" "),
            else:
                print("_", end=" "),
        print()

        # This checks for the win condition and will exit the loop if the player has won
        if (pointsGained == len(randomWord)):
            print("You solved it!")
            print()
            print("Current score: "+str(points))
            break

        # This prompts the user for his/her guess and then takes the guess
        currentGuess = input("Guess a letter:")

        # If the user has entered '!' then the game should exit
        if (currentGuess == '!'):
            print("Exit Game.")
            break

        # If the guess is correct then increment the score based on how many instances of that letter are there and print a success message
        if (currentGuess in randomWord):
            points += randomWord.count(currentGuess)
            pointsGained += randomWord.count(currentGuess)
            # Add the correct letter to the already guessed string so that we can easily ouput the guessed letter before prompting new input
            alreadyGuessed += currentGuess
            print("Right! Score is " + str(points))
        # If the guess is incorrect then decrement the score 1 point and print a fail message
        if (currentGuess not in randomWord):
            points -= 1
            print("Sorry, guess again. Score is " + str(points))

    # If the user failed to successfuly complete the game then print a fail message and display the correct word
    if points == -1:
        print("You failed to solve!")
        print("The correct word was "+randomWord)


def main():
    # Check if a sys arg was provided if not then give an error message and quit
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        print("Sys arg not provided.")
        quit()

    # Read the text file into text string
    f = open(data_path, 'r')
    text = f.read()
    f.close()

    # Lowercase and tokenize the text
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens]

    # Set with unique tokens
    uniqueSet = set(tokens)

    # Print the Lexical Diversity formatted
    print("\nLexical diversity: %.2f" % (len(uniqueSet) / len(tokens)))

    # Call the preprocess function to get the processed tokens and noun list
    processedTokens, nouns = preprocess(text)

    # Create the noun dictionary and count the instances of each noun in the processed tokens to build the dictionary
    noun_dict = {}
    for n in nouns:
        noun_dict[n] = processedTokens.count(n)

    # Sort the dictionary by
    sorted_noun_dict = dict(
        reversed(sorted(noun_dict.items(), key=lambda item: item[1])))

    # Store the top 50 words into a list
    topFiftyWords = list(sorted_noun_dict.items())[:50]

    # Print top 50 words
    print("Top 50 most common words: ")
    print(topFiftyWords)

    # Call guessing game function
    guess(topFiftyWords)


if __name__ == '__main__':
    main()
