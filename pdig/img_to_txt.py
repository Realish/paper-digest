import base64
import os
import re
from openai import OpenAI

client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to extract text from an image using OpenAI api.
def extract_txt(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages=[
        {"role": "system",
         "content": "You are a helpful assistant helping a user to extract text from an image of a document."},
        {"role": "user", 
         "content": [
           {"type": "text",
            "text": "Extract text, and textual data in tables from this image and convert to markdown format."
            },
           {"type": "image_url",
            "image_url":{
              "url": f"data:image/png;base64,{base64_image}"
            } 
            }
                    ]
         },
      ],
      max_tokens=3000
    )
  
    return response.choices[0].message.content
  
# Function to extract the number from a filename
def extract_fname_num(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group()) if match else 0
  
# Function to extract text from a collection of image docs in order.
def extract_doc_txt(image_doc_path, output_dir):
    doc_name = os.path.basename(image_doc_path)
    extracted_txt = r""""""
    
    fnames = os.listdir(image_doc_path)
    sorted_fnames = sorted(fnames, key=extract_fname_num)
    for image_name in sorted_fnames:
        image_path = os.path.join(image_doc_path, image_name)
        extracted_txt += extract_txt(image_path) + "\n"
        
    output_fpath = os.path.join(output_dir, f"{doc_name}.txt")
    with open(output_fpath, "w", encoding="utf-8") as output_file:
        output_file.write(extracted_txt)
        
    print(f"Text extracted from images in {doc_name} and saved in {output_fpath}")
  
  
