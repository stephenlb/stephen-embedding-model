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
    def __init__(self, dictionary, context):
        super(Embedding, self).__init__()
        self.number_of_words = len(dictionary)
        self.context = context
        self.dictionary = dictionary
        ## thank you @DeeNA - we will write our own Embedding
        self.embedding = torch.rand(self.number_of_words, 64, requires_grad=True)
        #self.embedding = torch.nn.Embedding(number_of_words, 256)
        ## LSTM???
        self.linear1 = torch.nn.Linear(context * 64, 32)
        self.linear2 = torch.nn.Linear(32, self.number_of_words)
        self.activation1 = torch.nn.GELU()
        self.activation2 = torch.nn.LogSoftmax(dim=1)

    def forward(self, sentence):
        out = tokenizer(sentence, self.dictionary)
        out = self.embedding[out]
        #out = out.mean(dim=0)
        out = out.view((1, -1))
        out = self.activation1(self.linear1(out))
        out = self.activation2(self.linear2(out))
        return out

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
def data_iterator(sentence, context):
    dictionary = build_dictionary(sentence)
    tokens = tokenizer(sentence, dictionary)
    words = normalize(sentence)

    ## TODO Shuffle
    for index, word in enumerate(sentence):
        features = ' '.join(words[index:index+context])
        labels = one_hot(tokens[index+context+1], dictionary)

        yield features, labels
        if index + context >= len(tokens)-2: break

def one_hot(tensor, dictionary):
    return torch.zeros(len(dictionary)).scatter_(0, tensor, 1)

words = "Found the bug, when you spam enter, the bot will send the messages automatically for the number of times you pressed. If you press 10 times it will answer 10 times automatically."
#print('words',words)
#print('normalize(words)',normalize(words))
#print(dictionary)
context_length = 3
dictionary = build_dictionary(words)
#tokens = tokenizer("Found when you", dictionary)
#print('tokens',tokens)
model = Embedding(dictionary, context_length)
loss_fn = torch.nn.NLLLoss() ### if we onehot then ew might need to use 
#loss_fn = torch.nn.CrossEntropyLoss()
out = model('when found bug')

print(out)
print(out.shape)

#print(one_hot(vectors[3]))

## TODO Train the model here.....
for feature, label in data_iterator(words, context_length):
    print('feature:', feature)
    print('label:',label)
    print('label.shape:',label.shape)
    #out = tokenizer(feature, dictionary)
    out = model(feature)
    print('out:',out)
    print('out.shape:',out.shape)
    #print(feature.shape)
    #loss = loss_fn(out, label)
    #print(loss)
    break
