from transformers import DistilBertTokenizer
import torch 
from transformers import get_linear_schedule_with_warmup
from transformers import DistilBertForSequenceClassification, AdamW, DistilBertConfig

import wget

import re

# import tensorflow as tf
# from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
# from torch.utils.data import TensorDataset, random_split

# import pandas as pd
# import os

# import matplotlib.pyplot as plt
# % matplotlib inline

# import seaborn as sns
# import random
# import numpy as np

model_dir = "/model_save"

tokenizer = DistilBertTokenizer.from_pretrained(model_dir)
model_loaded = DistilBertForSequenceClassification.from_pretrained(model_dir)

# code to be put into a function

def model_call(txt_input):
  # regex to parse string into array
  sentence_enders = "(?<=[!.?])\s"

  sent_array = re.split(sentence_enders, txt_input)

  txt_output=[]
  option = ["Gramatically correct", "Gramatically incorrect"]

  for i in range(len(sent_array)):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    seq = tokenizer.encode_plus(
                          sent_array[i],                      # Sentence to encode.
                          add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                          max_length = 64,           # Pad & truncate all sentences.
                          pad_to_max_length = True,
                          return_attention_mask = True,   # Construct attn. masks.
                          return_tensors = 'pt',     # Return pytorch tensors.
                    )

    # Add the encoded sentence to the list.    
    # And its attention mask (simply differentiates padding from non-padding).
    input_id = seq['input_ids']
    attention_mask = seq['attention_mask']
    input_id = torch.LongTensor(input_id)
    attention_mask = torch.LongTensor(attention_mask)

    # block 2
    model_loaded = model_loaded.to(device)
    input_id = input_id.to(device)
    attention_mask = attention_mask.to(device)

    # block 3
    with torch.no_grad():
    # Forward pass, calculate logit predictions
      outputs = model_loaded(input_id, token_type_ids=None, attention_mask=attention_mask)

    logits = outputs[0]
    # print(logits)
    index = logits.argmax()
    if index == 1:
      print(option[0])
      txt_output.append(option[0])
    else:
      print(option[1])
      txt_output.append(option[1])


  return txt_output #array
