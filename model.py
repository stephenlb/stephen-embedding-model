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
    def __init__(self, dictionary):
        super(Embedding, self).__init__()
        self.number_of_words  = len(dictionary)
        self.dictionary       = dictionary
        ## thank you @DeeNA - we will write our own Embedding
        self.embedding        = torch.rand(self.number_of_words, 256, requires_grad=True)
        #self.embedding = torch.nn.Embedding(number_of_words, 256)
        ## LSTM???
        self.activation = torch.nn.GELU()
        self.linear1    = torch.nn.Linear(256, 256)
        self.linear2    = torch.nn.Linear(256, 128)
        self.linear3    = torch.nn.Linear(128, self.number_of_words)

    def forward(self, sentence):
        out = tokenizer(sentence, self.dictionary)
        return out
        out = self.embedding[out]
        out = out.mean(dim=1)
        return out

        ## sigmoid(sqrt(sentenceA.dot(sentenceB)))
        ## OR???
        ## sigmoid(sentenceA.dot(sentenceB))

def normalize(words):
    return re.sub( r'[^a-z0-9 ]', '', words.lower() ).split()

def build_dictionary(data):
    dictionary = { 'PAD' : 0 }
    for word in normalize(data):
        if not(word in dictionary):
            dictionary.update({word:len(dictionary)})
    return dictionary

def tokenizer(sentence, dictionary):
    norms = normalize(sentence)
    tokens = [dictionary[word] for word in norms]
    return torch.tensor(tokens, dtype=torch.long)
        
#for X, y in data_iterator(data):

## N-Gram Iterator
def data_iterator(sentence):
    length = 3
    dictionary = build_dictionary(sentence)
    vectors = tokenizer(sentence, dictionary)
    words = normalize(sentence)

    ## TODO Shuffle
    for index, word in enumerate(sentence):
        features = words[index:index+length]#.unsqueeze(dim=-1)
        labels = one_hot(vectors[index+length+1], dictionary)

        yield features, labels
        if index + length >= len(vectors)-1: break

def one_hot(tensor, dictionary):
    return torch.zeros(len(dictionary)).scatter_(0, tensor, 1)

words = "Found the bug, when you spam enter, the bot will send the messages automatically for the number of times you pressed. If you press 10 times it will answer 10 times automatically."
print('words',words)
print('normalize(words)',normalize(words))
#print(dictionary)
dictionary = build_dictionary(words)
vectors = tokenizer("Found when you", dictionary)
print('vectors',vectors)
model = Embedding(dictionary)
#loss_fn = torch.nn.NLLLoss() ### if we onehot then ew might need to use 
loss_fn = torch.nn.CrossEntropyLoss()
out = model(words)

#print(out)
#print(out.shape)
#print(len(vectors))

#print(one_hot(vectors[3]))

## TODO Train the model here.....
for feature, label in data_iterator(words):
    break
    print('feature', feature)
    out = model(feature)
    print('out',out)
    print('out.shape',out.shape)
    break
    print('label',label)
    print('label.shape',label.shape)
    print('len(dictionary)',len(dictionary))
    break
    #print(feature.shape)
    #loss = loss_fn(out, label)
    #print(loss)
