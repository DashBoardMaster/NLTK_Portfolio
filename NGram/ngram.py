import nltk
import pickle
from nltk.util import ngrams
from collections import Counter


# Amol Perubhatla
# AVP180003
# CS4395.001
# Professor Karen Mazidi


def remove_newlines(fname):
    # This will remove the new line characters from the file
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]


def ngram(file_name):
    # Read the text file into text string
    f = open(file_name, 'r', encoding="utf8")
    text = f.read()
    f.close()

    # Remove newlines
    text = text.strip()

    # Lowercase and tokenize the text
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens]

    # Get the bigrams using the tokens
    bigrm = list(nltk.bigrams(tokens))

    # Create unigram
    unigrm = tokens

    # Create the noun dictionary and count the instances
    bigram_dict = {}
    unigram_dict = {}

    # Counting the instances for bigram
    count = Counter()
    for previous, current in zip(tokens, tokens[1:]):
        option1 = f"{previous}", f"{current}"
        option2 = f"{current}", f"{previous}"
        if option2 not in count:
            count[option1] += 1
            continue
        count[option2] += 1

    bigram_dict = dict(count)

    # Create count dict for unigrams
    for w in unigrm:
        unigram_dict[w] = tokens.count(w)

    return bigram_dict, unigram_dict


def main():
    english_bgrmd, english_unigrmd = ngram("LangId.train.English")
    french_bgrmd, french_unigrmd = ngram("LangId.train.French")
    italian_bgrmd, italian_unigrmd = ngram("LangId.train.Italian")

    # Pickle all of the dictionaries
    pickle.dump(english_bgrmd, open('enbi.p', 'wb'))
    pickle.dump(english_unigrmd, open('enui.p', 'wb'))
    pickle.dump(french_bgrmd, open('frbi.p', 'wb'))
    pickle.dump(french_unigrmd, open('frui.p', 'wb'))
    pickle.dump(italian_bgrmd, open('itbi.p', 'wb'))
    pickle.dump(italian_unigrmd, open('itui.p', 'wb'))


if __name__ == '__main__':
    main()
