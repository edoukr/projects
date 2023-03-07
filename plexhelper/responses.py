from datetime import datetime
import re


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['topmovies'], 'imdb.com/chart/top?sort=us,desc&mode=simple&page=1'),
        process_message(message, ['toptv'], 'imdb.com/chart/toptv?sort=us,desc&mode=simple&page=1'),
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there! How\'s it going?'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thank you!'),
        process_message(message, ['your', 'name'], 'My name is PlexerHelper, Nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you! If you need more help, You should message Kay: @Linashakrabina')
        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'Sorry, I didn\'t get that.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')
