import random
import time

responses = {'statement': ['tell me more!', 'why do you think that?', 'how long have you felt this way?', 'I find that extremely interesting', 'can you back that up?', 'oh wow!', ':)'], 
             'question': ["I don't know :(", 'you tell me!']}

# create templates
bot_template = "BOT: {0}"
user_template = "USER : {0}"

def send_message(message):
    """Define a function that sends a message to the bot
       Parameter:
        - message: the message to be delivered
    """
    # print user_template including the user_message
    print(user_template.format(message))

    # Get the bot's response to the message
    response = respond(message)

    # Print the bot template including the bot's response with a tiny delay
    time.sleep(0.8)
    print(bot_template.format(response))

def respond(message):
    # Check for a question mark
    if message.endswith('?'):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")