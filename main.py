from preprocess import preprocess_text
from apiCalls import callGPT3
from print import print_json
import json

with open('text.txt', 'r') as f:
    text = f.read()

preprocessed_text = preprocess_text(text)
# write the preprocessed text to a file
with open('preprocessed_text.txt', 'w') as f:
    f.write(preprocessed_text)

sysPrompt = """
You are a test setting guide designed to output JSON. of format {\questionType\: \question\, \answerType\: \answer\} make sure the answers are as distinct as possible"""

userPrompt = """Generate a JSON object with 5 * TRUE-FALSE, 3 *MCQ, 2 *LONG answer questions, 3 *APPLICATION BASED questions and a Summary from the text:"""

callGPT3(filePath="preprocessed_text.txt", systemPrompt=sysPrompt, userPrompt=userPrompt)

# read the response.json file to dict and print the content
with open('response.json', 'r') as f:
    res = json.load(f)
    
res = dict(res)

print_json(res)