## Installation
1. Downloading and installing Python

Download and install the latest version of Python from https://www.python.org/downloads/. Make sure it's 3.xx.x and for MacOS; that should be the first option in downloads anyway

1. Downloading the app

Open a terminal and enter the following:
```
cd PATH
git clone https://github.com/ericwang4904/Canvas_API.git
```
where PATH is the place you want to put the program (`cd Desktop` is a good choice). After you've downloaded the program, type
`cd Canvas_API` to enter the program folder.

1. Installing app requirements

Run `pip install -r requirements.txt` to install the relevant modules the program is using. Alternatively, just do `pip install requests` to install the latest version, as it is the sole dependancy.

## Setup
1. Setting up the API token
   1. Go to your Canvas homepage > Account > Settings and scroll to "Approved Integrations".
   2. Click "New Access Token", enter a purpose, and click "Generate Token".
   3. Copy down the access token.
   4. Open the `data.json` file in your `Canvas_API` folder.
   5. Paste in your token in the TOKEN_GOES_HERE section.
   6. Return to the Canvas homepage and copy the url, before pasting it into the URL_GOES_HERE section of `data.json`.
   7. It should look like this: `{"API_KEY": "abcd~efghijklmnop", "API_URL": "https://nuevaschool.instructure.com/"}`.
   8. Save the file.

2. Setting up the course groups
   1. Open the `data.json` file and go to the `courses_groups` section
   2. Make sure you have a list of courses you want to put in a group. At this point, if you have done step one you can run main.py to see a list of your courses and their IDs.
   3. Format your course groups according the examples in the file (key–value pairs separated by commas). That is,
   ```
   "courses_groups": {
    "example_1": ["238", "591", "512"],
    "example_2": ["1234567", "1239877", "1857116"]
   }
   ```
   4. IMPORTANT NOTE: Don't put the course that you manually add items to into a course group. If you do, every time you push an item to a course group, you will duplicate the original. Instead, have one course be your "master course" that you modify from Canvas, and put the others into a course group.
   - Example: `Block1` is the master course, course group `"History"` contains `["Block2", "Block3", ..., "Block8"]`

## Using the Program.
Congrats! You're done setting up. Simply run `main.py` to test your code for functionality. You can figure out the rest by yourself. If you have any questions, just ask!


