from transformers import pipeline 

summarizer = pipeline('summarization', model = 'facebook/bart-large-cnn')

text = '''
What Is Siri and How Does the Voice-Activated AI Assistant Work?
Siri is Apple's voice-enabled virtual assistant, part of iOS, iPadOS, watchOS, and other Apple operating systems. It uses AI, voice queries, and natural-language processing to answer questions, perform tasks, and make recommendations. Voice actor Susan Bennett is the original voice of Siri.
by businessinsider.com'''

print(summarizer(text, max_length=130, min_length=30, do_sample=False))