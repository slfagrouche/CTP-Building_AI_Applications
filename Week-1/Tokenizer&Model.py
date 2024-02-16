from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


classifier = pipeline("sentiment-analysis")
res = classifier("I need to get better and better at Building AI applications.")
print(res, '\n\n')



model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)
res = classifier("I need to get better and better at Building AI applications.")
print(res, '\n\n')


# Tokenizer: basically puts text in a mathematical representation that the model understand.

sequence = "Using a Transformer network is simple"
res = tokenizer(sequence)
print(res)
tokens = tokenizer.tokenize(sequence)
print(tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
decoded_string = tokenizer.decode(ids)
print(decoded_string)


from transformers import pipeline
from transformers import TFAutoTokenizer, TFAutoModelForSequenceClassification
import torch
import torch.nn.functional as F


