from docx import Document
import os

def print_json(obj: dict):
    # Create a new document if it doesn't exist
    if not os.path.exists('Module.docx'):
        doc = Document()
        doc.save('Module.docx')
    
    # Open the document
    doc = Document('Module.docx')
    
    for key, value in obj.items():
        # Add heading for each question number
        doc.add_heading(f"Question {key}", level=2)
        
        # Add details of the question
        for k, v in value.items():
            if k == "options":
                # For MCQ questions, add options
                doc.add_paragraph(f"{k}:")
                for option in v:
                    doc.add_paragraph(option, style='ListBullet')
            else:
                # For other question types, add question and answer
                doc.add_paragraph(f"{k}: {v}")
        # Add a new line between questions
        doc.add_paragraph()

    # Save the document
    doc.save('Module.docx')

# Example usage

if __name__ == "__main__":
    import json
    print("Reading response.json")
    with open('response.json', 'r') as f:
        res = json.load(f)
        res = dict(res)
    print(res)
    print_json(res)

