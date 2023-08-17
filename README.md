# Description

- this is a simple implementation of a chat bot that can taught to give certain responses according to the training data offered in the "intents.json" file

# Usage

- To implement this bot in your project do the following steps :

1.  Add to the intents.json file a json object with the following structure:

```
{
        "tag": "greeting",
        "patterns": [
          "Hello",
          "Hi",
          "Hey",
          "Greetings",
          "Good morning",
          "Good afternoon",
          "Good evening"
        ],
        "responses": [
          "Hello! How can I assist you today?",
          "Hi there! How may I help you?",
          "Hey, how can I be of assistance?",
          "Greetings! What can I do for you today?",
          "Good [morning/afternoon/evening]! How can I help you today?"
        ]
      },
```

- explanation:
  - the tag is the name of the speech pattern or context you want the bot to learn
  - patterns : are the different modalities that the specific context denoted by the tag can be presented to the chat bot , putting it short it's what you expect the human is going to say to the bot, put here as many as possible to train the bot thoroughly
  - responses : these are the hard coded responses that the bot will use to respond to the human they will be picked at random in the code

2. Make sure you have at least python 3.9 installed as this application was test on this python version

3. run on the command line
   - if you are on windows

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

4. run the training model by executing train.py

```
python run.py
```

5. once that is done a data.pth is created

6. expose the function inside get_response function located in the chat.py into your api

## NB:

make sure to adapt the paths to your operating system and project structure to both the intents.json and data.pth files
