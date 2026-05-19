import torch
import json
from fastapi import FastAPI, Body
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")

@torch.no_grad()
def embedding(text:str):
    encoded_input = tokenizer(text, return_tensors='pt')
    #print(encoded_input)
    output = model(**encoded_input)
    print(output.pooler_output)
    return output.pooler_output.tolist()[0]

app = FastAPI()
@app.post("/")
def index(body: bytes = Body()):
    text = body.decode("utf-8").strip()
    output = embedding(text)
    return output

## NAME = Embert
## NAME = Embert
## NAME = Embert
## NAME = Embert
## NAME = Embert


## TODO normalized vecotrs then dot product
## TODO
## TODO 
## @nevokrien95
## (model(tokenizer(heystack))@model@tokenizer(needle))).sum(1) 
## TODO
## 
