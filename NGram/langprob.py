import nltk
import pickle
from nltk.util import ngrams
import difflib


def compute_prob(text, unigram_dict, bigram_dict, V):
    # V is the vocabulary size in the training data (unique tokens)

    unigrams_test = nltk.word_tokenize(text)
    unigrams_test = [t.lower() for t in unigrams_test]
    bigrams_test = list(ngrams(unigrams_test, 2))

    p_laplace = 1  # calculate p using Laplace smoothing

    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace = p_laplace * ((n + 1) / (d + V))

    return p_laplace


def main():
    # Load the pickled dictionaries
    enbi = pickle.load(open('enbi.p', 'rb'))
    enui = pickle.load(open('enui.p', 'rb'))
    frbi = pickle.load(open('frbi.p', 'rb'))
    frui = pickle.load(open('frui.p', 'rb'))
    itbi = pickle.load(open('itbi.p', 'rb'))
    itui = pickle.load(open('itui.p', 'rb'))

    testFile = open('LangId.test', 'r', encoding="utf8")
    Lines = testFile.readlines()
    testFile.close()
    probFile = open("probtest.txt", 'w')
    lineNum = 1
    # Compute the probablities for each language and then write the name of the language with the highest probablity to the prediction file
    for line in Lines:
        enprob = compute_prob(line.strip(), enui, enbi, len(enui))
        frprob = compute_prob(line.strip(), frui, frbi, len(frui))
        itprob = compute_prob(line.strip(), itui, itbi, len(itui))

        if enprob > frprob and enprob > itprob:
            probFile.write(str(lineNum)+' English\n')
        elif frprob > enprob and frprob > itprob:
            probFile.write(str(lineNum)+' French\n')
        else:
            probFile.write(str(lineNum)+' Italian\n')
        lineNum += 1
    probFile.close()

    # Find the different lines by comparing our results versus the solutions
    with open("LangId.sol", 'r', encoding="utf8") as file1:
        with open("probtest.txt", 'r') as file2:
            diff = set(file1).difference(file2)

    for i in diff:
        print(i)

    # Calculate and print the accuracy
    acc = (lineNum-len(diff))/lineNum
    print("Accuracy: "+str(acc))


if __name__ == '__main__':
    main()
