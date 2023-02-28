# OpenAI API Image Basics

This is just a simple command line utilities to create/modify images with OpenAI. Feel free to use the code in your projects.

This project has 2 programs: - **image-generator.py** to generate images using simple text like "a dog with a ball". - **image-variation.py** to modify an existent image by the OpenAI algorithm.

**_Run the programs without arguments to get help about usage._**

## Setup

1. Python installed is required

2. Navigate into the project directory

3. Create a new virtual environment... AND ACTIVATE IT!

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Under Windows use

   ```bath
   venv\Scripts\activate.bat
   ```

4. Install the requirements

   ```bash
   python -m pip install -r requirements.txt
   ```

5. You must Add your [API key](https://beta.openai.com/account/api-keys) in **open_ai_key.py** or set it in your environment, in any case, edit the file **open_ai_key.py** before run. Create an API Key, sing up for free.

6. All done. you can run the programs without params to get usage help.

## Copyright & License

By José Puga 2023. Under MIT License.

---

## _image-generator.py_ : Some samples (just typing the text)

### An alien organism adapted to water and land

![Alien organism](/doc/an_alien_organism_adapted_to_water_and_land.png)

### An 80's computer running tetris

![80's Computer](/doc/an_80's_computer_running_tetris-01293.png)

### The Last Supper impressionist style

![The Last Supper](/doc/the_last_supper_impressionist_style-08828.png)

### Rusted clock

![Rusted Clock](/doc/rusted_clock-09069.png)

### A blue cow with flowers

![Blue Cow](/doc/a_blue_cow_with_flowers-03622.png)

---

## _image-variation.py_ : Getting variations of the same image

### Original Image

![Multifruits](/doc/multifrutas.png)

### samples

![Multifruits 1 Out](/doc/multifrutas1-out.png)
![Multifruits 2 Out](/doc/multifrutas2-out.png)
![Multifruits 3 Out](/doc/multifrutas3-out.png)
