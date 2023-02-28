# Simple command line interface for image generator of OpenAI.
# José Puga 2023. Under MIT License.

import sys
import urllib.request
import random
import openai
from open_ai_key import *  # This module handles the api key!

# CHANGE THIS TO SET YOUR DEFAULT SAVE FOLDER !!!!!
DEST_FOLDER = "./"

if len(sys.argv) == 1:
    print(
"""Image creation through words using OpenAI API. 
Usage: {} whatever you want to create
       {} a dog playing with a ball
       
Note that quotes (") nor punctuation marks are necessaries.
For simplicily the image will be saved in the current directory by default(*)
with the name of all the words with underlines plus dash plus random number:
    a_dog_playing_with_a_ball-02352.png
    
(*) You can set a destination folder in the DEST_FOLDER variable in the code.
""".format(sys.argv[0], sys.argv[0]))
    quit()

# Generating output file name
file_out = ' '.join(sys.argv[1:])
file_out = file_out.replace(' ', '_')
file_out += '-' + str(random.randint(0,9999)).zfill(5) + '.png'

openai.api_key = (OPENAI_API_KEY)

print("Procesing image...")

# Generic way to handle errors, for more complex handling. See OpenAI doc in
# https://help.openai.com/en/articles/6897213-openai-library-error-types-guidance
try:
    response = openai.Image.create(
            prompt = ' '.join(sys.argv[1:]),
            n = 1,
            size = "1024x1024"
    )
except Exception as error:
    print("{}".format(error))
    quit()

image_url = response['data'][0]['url']

urllib.request.urlretrieve(image_url, DEST_FOLDER + file_out)
print("Done.")
