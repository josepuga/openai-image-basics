import os

# You can put the key value directly or use the Enviroment variables.
# COMMENT THAT YOU DO NOT WANT.
# =============================

# Direct method (easy, but less safe if you are going to share your code).
#OPENAI_API_KEY="sk-YOUR API KEY"

# Using enviroment variables. You must import your api key to the enviroment.
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
