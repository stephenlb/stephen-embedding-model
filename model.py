import re
import torch

## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model

## IDEA: Build a chessbot with pytorch
## TODO @DeeNA - add visualizer so we can see semanti relations!!!
## TODO define model with linear layers ✅
## TODO find dataset ✅
## TODO vectoirze data ( word indexing ) create dictionary ✅
## TODO forward pass
## TODO test vector similartity 
## TODO padding and max context Size
## TODO loss = NLLLoss
## TODO opitm = [4 of the common optimizers] RNG adam + adamw + Muon + SGD
## TODO traing loop
## TODO data iterator with yield for batching with words support
## TODO 
## TODO 


## "The dog ran up the hill"
##  1   2   3   4  1   5   " + 0 0 0 0 0 for padding
## 
## 5 = [ 0  0  0  0  1 ]
        ## -> 
        ## -->
        ## =>
        ## ==>
        ## ===
        ## >=
        ## <=

class Embedding(torch.nn.Module):
    def __init__(self, number_of_words, dictionary):
        super(Embedding, self).__init__()
        self.number_of_words  = number_of_words
        self.dictionary       = dictionary
        ## thank you @DeeNA - we will write our own Embedding
        self.embedding        = torch.rand(number_of_words, 256, requires_grad=True)
        #self.embedding = torch.nn.Embedding(number_of_words, 256)
        ## TODO maybe a norm layer
        ## note may alraedy be dividing by number_of_words
        ## Linear layer without bias and 
        ## LSTM???
        #self.activation = torch.nn.GELU()
        #self.linear1    = torch.nn.Linear(256, number_of_words)

    def forward(self, sentence):
        features = tokenizer(sentence, self.dictionary)
        out = self.embedding[features]
        #out = out.mean(dim=1)
        return out

        ## sigmoid(sqrt(sentenceA.dot(sentenceB)))
        ## OR???
        ## sigmoid(sentenceA.dot(sentenceB))

def normalize(words):
    return re.sub( r'[^a-z0-9 ]', '', words.lower() ).split()

def build_dictionary(data):
    dictionary = { 'pad' : 0 }
    for word in normalize(data):
        if not(word in dictionary):
            dictionary.update({word:len(dictionary)})
    return len(dictionary), dictionary

def tokenizer(sentence, dictionary):
    norms = normalize(words)
    tokens = [dictionary[word] for word in norms]
    return torch.tensor(tokens, dtype=torch.long)
        
#for X, y in data_iterator(data):

## N-Gram Iterator
def data_iterator(sentence):
    number_of_words, dictionary = build_dictionary(sentence)
    vectors = tokenizer(sentence, dictionary)
    words = normalize(sentence)

    ## TODO Shuffle
    for index, word in enumerate(sentence):
        features = vectors[index:index+3]
        labels = one_hot(vectors[index+3])

        yield features, labels
        if index + 3 >= len(vectors)-1: break

def one_hot(tensor):
    return torch.zeros(len(dictionary)).scatter_(0, tensor, 1)

words = "Found the bug, when you spam enter, the bot will send the messages automatically for the number of times you pressed. If you press 10 times it will answer 10 times automatically."
#print(normalize(words))
#print(dictionary)
##vectors = tokenizer(words, dictionary)
#print(vectors)
number_of_words, dictionary = build_dictionary(words)
model = Embedding(number_of_words, dictionary)
#loss_fn = torch.nn.NLLLoss() ### if we onehot then ew might need to use 
loss_fn = torch.nn.CrossEntropyLoss()
out = model(words)

#print(out)
#print(out.shape)
#print(len(vectors))

#print(one_hot(vectors[3]))

## TODO Train the model here.....
for feature, label in data_iterator(words):
    print(feature, label)
    out = model(features)
    print(out)
