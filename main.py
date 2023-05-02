# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:31:58 2023

@author: Renato Marino Henz

This script aims to implement a Question & Answers system.

It makes use of Hugging Face's transformers tool.
Specifically, it uses BERT for question answering
BERT: Bidirectional Encoder Representations from Transformers

Other models can be found at: https://huggingface.co/models

"""

# Importing dependencies
from transformers import BertForQuestionAnswering # This is specific for PyTorch
from transformers import AutoTokenizer, pipeline
import time

# Defining the model name to be used
# You can see more options at: https://huggingface.co/models?pipeline_tag=question-answering
MODEL_NAME = 'deepset/bert-base-cased-squad2' #'bert-large-uncased-whole-word-masking-finetuned-squad'

# Defining the data source to be used
DATA_SOURCE_NAME = 'google-ads-dashboard.txt'

# Loading the pre-trained BERT model and the tokenizer
# If the pre-trained model is not already present in your machine,
# it will be downloaded, and this will take some minutes
print('Loading the pre-trained model...')
model = BertForQuestionAnswering.from_pretrained(MODEL_NAME)
print('Loading the tokenizer...')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Getting the context
print('Loading context...')
# For the defined dataset file
with open(f"data/{DATA_SOURCE_NAME}", 'r', encoding='utf8') as f:
    context = f.read()

# Defining the function to perform the question answering task
def answer_question(context, question):
    # Tokenize the question and context
    tokenizer.encode(question, truncation=True, padding=True)

    # Creating the Natural Language Processing pipeline
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    # Requesting an answer for the provided question
    print('Loading the answer...')
    answer = nlp({
        'question': question,
        'context': context
    })

    # Returning the resulting answer
    return answer

# Main script
if __name__ == "__main__":
    # Flag to exti the program
    flag_exit = False
    # While user has not requested to exit the program
    while not flag_exit:
        question = input("Please, provide the question to be answered (input 'q' or 'exit' to quit the program): ")
        # If user requested to exit the program
        if question.lower() == 'q' or question.lower() == 'exit':
            flag_exit = True
        # Otherwise, we request an answer to the question
        else:
            # Measuring time required to calculate the answer
            start = time.time()
            res = answer_question(context, question)
            print(f'Answer: {res["answer"]}\nScore: {res["score"]}')
            end = time.time()
            print(f"Elapsed time: {'%.2f' % (end-start)} s")
