This is a Python-based personal assistant that can perform various tasks such as opening applications, searching YouTube videos, setting timers, recording audio and video, adding and reading notes, and more. It uses speech recognition to take commands and responds with speech.

## Features

- Greet the user and ask for their name
- Open applications
- Search and play YouTube videos
- Set timers
- Record audio and video
- Add and read notes
- Open files
- Search Wikipedia
- Open websites
- Provide the current time and day
- Ask questions to OpenAI
- Search for weather information

## Requirements

- Python 3.x
- The following Python libraries:
  - [`pyttsx3`](https://pypi.org/project/pyttsx3/)
  - [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
  - [`webbrowser`](https://docs.python.org/3/library/webbrowser.html) (built-in)
  - [`datetime`](https://docs.python.org/3/library/datetime.html) (built-in)
  - [`wikipedia`](https://pypi.org/project/wikipedia/)
  - [`os`](https://docs.python.org/3/library/os.html) (built-in)
  - [`openai`](https://pypi.org/project/openai/)
  - [`pafy`](https://pypi.org/project/pafy/)
  - [`python-vlc`](https://pypi.org/project/python-vlc/)
  - [`ctypes`](https://docs.python.org/3/library/ctypes.html) (built-in)
  - [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
  - [`requests`](https://pypi.org/project/requests/)
  - [`time`](https://docs.python.org/3/library/time.html) (built-in)
  - [`json`](https://docs.python.org/3/library/json.html) (built-in)
  - [`opencv-python`](https://pypi.org/project/opencv-python/)

## Installation

1. Clone the repository or download the source code.
2. Install the required libraries using pip:
   ```sh
   pip install pyttsx3 SpeechRecognition wikipedia openai pafy python-vlc beautifulsoup4 requests opencv-python
Ensure VLC media player is installed and the path to (libvlc.dll) is correctly specified in the script.
Usage
# Run the script:
The assistant will greet you and ask for your name. Respond with "my name is [your name]".
Give commands to the assistant. Some example commands include:
- "Open Notepad"
- "Search Despacito on YouTube"
- "Set timer for 10 seconds"
- "Record audio my_audio"
- "Record video my_video 10"
- "Add note Buy groceries"
- "Read notes"
- "Open file C:\path\to\file.txt"
- "What is the time?"
- "What is the day?"
- "Ask AI about Python programming" (i will add more ai feature in fucture :)
- "Open website google.com"
- "Weather"
# Example Commands
- Greet and Ask for Name:

"Hello, how can I assist you today?"
"What is your name?"
"My name is [your name]"
"Nice to meet you, [your name]!"
Open Applications:

- "Open Notepad"
- "Open Calculator"
# Search and Play YouTube Videos:

"Search Despacito on YouTube"
"On YouTube search Despacito"
# Set Timers:

"Set timer for 10 seconds"
# Record Audio and Video:

- "Record audio my_audio"
- "Record video my_video 10"
# Add and Read Notes:

- "Add note Buy groceries"
- "Read notes"
# Open Files:

"Open file C:\path\to\file.txt"
# Search Wikipedia:

"Wikipedia Python programming"
# Open Websites:

"Open website google.com"
# Provide Current Time and Day:

"What is the time?"
"What is the day?"
# Ask Questions to OpenAI:

- "Ask AI about Python programming"
Search for Weather Information:
## to end the program 
- you can also say exit to end the program
# application 
- this is he link for the [applicaion ](github.com)

"Weather"
License
This project is licensed under the MIT License.
