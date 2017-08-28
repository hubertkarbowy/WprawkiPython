import nltk

print ("NLTK loaded")
print (nltk.corpus.gutenberg.fileids())
md = nltk.corpus.gutenberg.words("melville-moby_dick.txt") # extract words

# WORD COUNTS
wrd = "whale"
print ("The word " + wrd + " appears " + str(md.count("whale")) + " times")

md_set = set(md) # unique words
print ("There are word " + str(len(md_set)) + " unique words in Moby Dick")
print ("Each word is used on average " + str(len(md)/len(md_set)) + " times")


# SENTENCE COUNTS
md_sents = nltk.corpus.gutenberg.sents("melville-moby_dick.txt") # extract sentences
print ("There are " + str(len(md_sents)) + " sentences words in Moby Dick")