import re
import torch

## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model
## Today's task: Create our own from-scratch word embedding model

## TODO Custom Correlation Coefficient Heatmap
## TODO Custom Correlation Coefficient Heatmap
## TODO Custom Correlation Coefficient Heatmap
## TODO Custom Correlation Coefficient Heatmap
## TODO Custom Correlation Coefficient Heatmap
## TODO Custom Correlation Coefficient Heatmap


##   Code    Result  Description
##   U+2580  ▀       Upper half block
##   U+2581  ▁       Lower one eighth block
##   U+2582  ▂       Lower one quarter block
##   U+2583  ▃       Lower three eighths block
##   U+2584  ▄       Lower half block
##   U+2585  ▅       Lower five eighths block
##   U+2586  ▆       Lower three quarters block
##   U+2587  ▇       Lower seven eighths block
##   U+2588  █       Full block
##   U+2589  ▉       Left seven eighths block
##   U+258A  ▊       Left three quarters block
##   U+258B  ▋       Left five eighths block
##   U+258C  ▌       Left half block
##   U+258D  ▍       Left three eighths block
##   U+258E  ▎       Left one quarter block
##   U+258F  ▏       Left one eighth block
##   U+2590  ▐       Right half block
##   U+2591  ░       Light shade
##   U+2592  ▒       Medium shade
##   U+2593  ▓       Dark shade


##  TODO cosine similarity ✅
##  TODO test vector similartity 
##  TODO graph it in the Terminal ( how accurate it is )
##  TODO @DeeNA - add visualizer so we can see semanti relations!!!
##  TODO variable context size (train for this)
##  TODO opitm = [4 of the common optimizers] RNG adam + adamw + Muon + SGD
##  TODO 

## IDEA: Build a chessbot with pytorch
## TODO ✅ cleanup -- 
## TODO ✅ padding and
## TODO ✅ define model with linear layers 
## TODO ✅ find dataset ✅
## TODO ✅ vectoirze data ( word indexing ) create dictionary ✅
## TODO ✅ forward pass ✅
## TODO ✅ max context Size ✅
## TODO ✅ loss = NLLLoss ✅
## TODO ✅ data iterator with yield for batching with words support ✅

## "The dog ran up the hill"
##  1   2   3   4  1   5   " + 0 0 0 0 0 for padding
##  "hill" = 5 = [ 0  0  0  0  1 ]

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
        ## TODO PaDD IF TOO SHORT
        out = tokenizer(sentence, self.dictionary)

        ## Token Padding
        if (len(out) < self.context):
            padding = torch.zeros(self.context - len(out), dtype=torch.long)
            out = torch.cat((out, padding))

        out = self.embedding[out]
        out = out.view((1, -1))
        if self.training:
            out = self.activation1(self.linear1(out))
            out = self.activation2(self.linear2(out))
        return out.squeeze(dim=0)

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

## N-Gram Iterator
def data_iterator(sentence, context):
    dictionary = build_dictionary(sentence)
    tokens = tokenizer(sentence, dictionary)
    words = normalize(sentence)

    ## TODO Shuffle
    ## TODO Create various length of context (1 and 10) <-> 3
    for index, word in enumerate(sentence):
        features = ' '.join(words[index:index+context]) ## TODO variable context size
        #labels = one_hot(tokens[index+context+1], dictionary)#.unsqueeze(dim=0)
        labels = tokens[index+context+1]#.unsqueeze(dim=0)

        yield features, labels
        if index + context >= len(tokens)-2: break

def one_hot(tensor, dictionary):
    return torch.zeros(len(dictionary)).scatter_(0, tensor, 1)

words = "Found the bug, when you spam enter, the bot will send the messages automatically for the number of times you pressed. If you press 10 times it will answer 10 times automatically."
context_length = 3
epochs = 1000
dictionary = build_dictionary(words)
model = Embedding(dictionary, context_length)
loss_fn = torch.nn.NLLLoss() ### if we onehot then ew might need to use 
optim = torch.optim.SGD(model.parameters(), lr=0.001)

model.load_state_dict(torch.load('model_weights.pth'))

## Train the AI
for epoch in range(epochs):
    break
    for feature, label in data_iterator(words, context_length):
        model.zero_grad()
        out = model(feature)
        loss = loss_fn(out, label)
        print(f'{loss.item():.2f}', f'epoch: {epoch}')
        loss.backward()
        optim.step()

torch.save(model.state_dict(), 'model_weights.pth')
