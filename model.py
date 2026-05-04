import torch

## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model

## IDEA: Build a chessbot with pytorch
## TODO define model with linear layers ✅
## TODO find dataset
## TODO vectoirze data ( word indexing ) create dictionary
## TODO forward pass
## TODO test vector similartity
## TODO padding
## TODO loss = NLLLoss
## TODO opitm = [4 of the common optimizers] RNG adam + adamw + Muon + SGD
## TODO 


## "The dog ran up the hill"
##  1   2   3   4  1   5   " + 0 0 0 0 0 for padding

class Embedding(torch.nn.Module):
    def __init__(self, number_of_words):
        super(Embedding, self).__init__()
        self.number_of_words = number_of_words
        self.embedding  = torch.nn.Embedding(number_of_words, 256)
        ## TODO maybe a norm layer
        ## note may alraedy be dividing by number_of_words
        ## Linear layer without bias and 
        #self.activation = torch.nn.GELU()
        #self.linear1    = torch.nn.Linear(256, number_of_words)

    def forward(self, sentence):
        features = vectorize(sentence)
        out = self.embedding(features)
        out = out.mean(dim=1)
        return out

        ## sigmoid(sqrt(sentenceA.dot(sentenceB)))
        ## OR???
        ## sigmoid(sentenceA.dot(sentenceB))

def normalize(words):
    return words.lower().replace(r'[^a-zA-Z0-9 ]+', '').split()

def build_dictionary(data):
    dictionary = { 'pad' : 0 }
    for word in normalize(data):
        if not(word in dictionary):
            dictionary.update({word:len(dictionary)})
    return len(dictionary), dictionary

def vectorize(sentence, dictionary):
    norms = normalize(words)
    tokens = [dictionary[word] for word in norms]
    return tokens
        
#for X, y in data_iterator(data):

## N-Gram Iterator
def data_iterator(sentence):
    ## TODO pre-build vectors 
    ## TODO yield 2 words, and 1 word target
    ## TODO 
    pass

words = "Found the bug, when you spam enter, the bot will send the messages automatically for the number of times you pressed. If you press 10 times it will answer 10 times automatically."
print(normalize(words))
number_of_words, dictionary = build_dictionary(words)
print(dictionary)
vec = vectorize(words, dictionary)
print(vec)
model = Embedding(number_of_words)
loss_fn = torch.nn.NLLLoss()

        
