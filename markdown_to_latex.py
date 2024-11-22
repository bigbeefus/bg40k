import re
import json

def filter(doc):
    json_output = []
    for block in doc.blocks:
        if block.startswith('header'):
            level = block.get('header_level')
            if level == 1:  # First-level header (Chapter)
                block['latex_command'] = '{\chapter{' + block.text.strip() + '}}'
            elif level <= 3:  # Subsequent headers (Sections)
                block['latex_command'] = '{\section{' + block.text.strip() + '}}'
            else:
                block['latex_command'] = '' # Handle higher levels as needed
        json_output.append(block.__dict__)  

    return json.dumps(json_output) 

