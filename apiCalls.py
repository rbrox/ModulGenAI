import json
from openai import OpenAI

def callGPT3(filePath="preprocessed_text.txt", systemPrompt="", userPrompt=""):
    client = OpenAI(api_key="sk-proj-CL6KrFv2wxJfxs2jI68yT3BlbkFJQ5b6UNH252qwWn4cEkPF")
    with open(filePath, 'r') as f:
        txt = f.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt + txt},
        ]
    )

    # Extracting the content from response.choices
    content_str = response.choices[0].message.content
    content_dict = json.loads(content_str)

    # Writing the content to response.txt
    with open('response.txt', 'w') as f:
        f.write(content_str)

    # Dumping the content as JSON to response.json
    with open('response.json', 'w') as f:
        json.dump(content_dict, f, indent=4)

    return content_dict

if __name__ == "__main__":
    sysPrompt = "You are a test setting guide designed to output JSON. of format {\questionType\: \question\, \answerType\: \answer\}"
    userPrompt = "Generate a JSON object with 5 * TRUE-FALSE, 3 *MCQ, 2 *LONG answer questions from the text:"
    res = callGPT3(systemPrompt=sysPrompt, userPrompt=userPrompt)
    print(res)
