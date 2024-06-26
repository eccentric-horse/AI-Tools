import sys
import os
# Change working directory so files can 
# be found when debugging
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")
from utilities import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Write a short 3 chapter sci-fi novella on the theme of AI ethics.'}]})

plan = [
  'Step 1: Brainstorm ideas for the plot and characters of the science fiction novella focusing on AI ethics.',
  'Step 2: Create an outline for the three chapters, ensuring a clear structure and progression of the theme.',
  'Step 3: Develop the main characters, including an AI protagonist and human characters affected by the AI\'s actions.',
  'Step 4: Begin writing the first chapter, introducing the AI protagonist and the ethical dilemma it faces.',
  'Step 5: Write the second chapter, delving deeper into the AI\'s struggle with its programmed ethics and exploring the consequences of its choices.',
  'Step 6: Write the third and final chapter, resolving the ethical conflict and showing the impact on the AI, human characters, and society at large.',
  'Step 7: Revise and edit the novella, ensuring the plot is coherent, the character development is compelling, and the theme of AI ethics is effectively conveyed.'
]

for whatever in plan:
    chat.template['messages'].append({'role': 'user', 'content': whatever})

    message = chat.completion({}).choices[0].message
    print(message.content)
    print('-------')
    chat.template['messages'].append({'role': message.role, 'content': message.content})