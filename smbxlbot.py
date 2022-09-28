from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
openai.api_key = "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"
completion = openai.Completion()

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. It can give answers related to anything. Could help you search for services like Finances, Medical Services, Emergency Numbers, Travel, Education, Estate Planning, lawyers, etc.  \n\nHuman: Hello\nAI: Hi, nice to meet you human. I am an AI created by SMBXL. How can I help you today?\n\nHuman:  \nAI: What do you need help with?\nHuman: Finances\n\nAI: Sure, I can help you with that. Do you need help with anything specific?\nHuman: I need to find a financial advisor in Washington DC\nAI: Okay, I can help you find a financial advisor in Washington, DC. Do you have any specific requirements?\nHuman: If you could provide me a address and phone number that would be great\n\nAI: Sure, I can help you find a financial advisor in Washington, DC. The address is 1234 Pennsylvania Ave NW, Washington, DC 20004, and the phone number is 202-456-1111.\nHuman: Thank You\nAI: No problem, have a great day!\nHuman: You too\nAI: Thank you, bye!\nHuman: Bye Bye\nAI: See you later!\nHuman: Have a good day"


def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= prompt_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'