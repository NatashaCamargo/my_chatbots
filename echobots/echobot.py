import time

def respond(message):
    """This funcion defines the echobot answer
       Parameter:
        - message: the message to be delivered
    """
    bot_message =  "I can hear you! You said : {}".format(message)
    # return the bot msg
    return bot_message


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


# saves the user input
user_message = input("Hi! I'm an echobot! Please, enter your message: ")

# send a message to the bot
send_message(user_message)