# Conversational front-end for OpenAI Davinci

## Preparation on Mac

In a terminal window, do the following:

1. `brew install portaudio`
2. `pip install -r requirements.txt`
3. `python3 -m advise --signup` to get your OpenAI API key (copy it)
4. `python3 -m advise --apikey=PASTE_YOUR_KEY_HERE`

## Configuration

1. Edit `config.json` and set your name, and the Apply voice you want the speaker to use.

## Running

1. Run `python3 -m speak` in a terminal. Give the terminal permission to access your microphone
2. When 'Listening...' is displayed, you may ask your question.
3. Be patient, neither the Google recognizer nor the OpenAI ChatGPT system is fast.
