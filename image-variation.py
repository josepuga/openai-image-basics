# Simple command line interface for image variations of OpenAI.
# José Puga 2023. Under MIT License.

import sys
from pathlib import Path
import urllib.request
import openai
from open_ai_key import *  # This module handles the api key!

# Check arguments

if len(sys.argv) != 3:
    print(
"""Image variation generation using OpenAI API. 
Image must be quared, PNG and less than 4Mb.
An OpenAi API key is necessary. You can get one for free from OpenAI.

Usage: {} <image_to_process.png> <output_image.png>
       {} "my best picture.png" output.png
       {} pretty_woman.png more_pretty.png""".format(sys.argv[0], sys.argv[0], sys.argv[0])) 
    quit()

file_in = sys.argv[1]
file_out = sys.argv[2]

# Check if input file exists

if not Path(file_in).is_file():
    print("{}: File not found.".format(file_in))
    quit()

openai.api_key = (OPENAI_API_KEY)

print("Procesing image...")

# Generic way to handle errors, for more complex handling. See OpenAI doc in
# https://help.openai.com/en/articles/6897213-openai-library-error-types-guidance
try:
    response = openai.Image.create_variation(
        image = open(file_in, "rb"),
        n = 1,
        size = "1024x1024"
    )
except Exception as error:
    print("{}".format(error))
    quit()

image_url = response['data'][0]['url']

urllib.request.urlretrieve(image_url, file_out)
print("Done.")
