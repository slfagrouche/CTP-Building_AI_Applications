from transformers import pipeline


classifier = pipeline("sentiment-analysis")
res = classifier("I need to get better and better at Building AI applications .")
print(res, '\n\n')



generator =  pipeline("text-generation", model = "gpt2")
res = generator(
    "In this file I will teach you how to build your AI application and make sure it works",
    max_length=30,
    num_return_sequences = 2
)
print(res, '\n\n')



classifier  =  pipeline("zero-shot-classification")
res = classifier(
    "This file code is case-sensitive and indentation matters on it.",
    candidate_labels = ["Apple", "Python","Arabic"]

)
print(res)

