import random
from nltk.tokenize import word_tokenize, sent_tokenize 
# Libraries have been obtained by downloading Anaconda.
# -------------------------------------------------------------------------------


# Greetings message - Keyword matching
Greeting_input = ["greetings", "hi", "hope you're good", "hiya", "hey", "hello",] #Most common greetings a user can give
Greeting_output = ["hi", "hey", "hiya", "*nods*", "hi there", "hello", "Its nice to meet you!"] #chatbot will respond with one of these greetings from the tuple


def greeting(sentence):
    for word in sentence.split(): #this splits input sentence into seperate words to identify if the user has responded with a greeting
        if word.lower() in Greeting_input: #resonse will be provided in lower case
            return random.choice(Greeting_output) #allows the chatbot to provide a random response from Greeting_output
#---------------------------------------------------------------------------------


#sets the environment for the text
with open("OneDrive\Desktop\chatbot.txt", 'r', encoding='utf-8', errors='ignore') as file: #opens the specified file in r (read mode)
    data_content = file.read() # Reads the contents of the files and stores it in content


# Tokenization
def tokenize(text):
    return word_tokenize(text.lower()) #tokenizes words


# Tokenizes text file
def tokenize_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        raw_text = file.read() 
        return sent_tokenize(raw_text)
#---------------------------------------------------------------------------------


# Generating response
def response(user_response, tokenized_responses):
    majibot_response = ""
    user_tokens = set(tokenize(user_response))
    
    # Find the most relevant response from Chatbot.txt file
    max_overlap = -1
    max_overlap_response = ""
    for response_tokens in tokenized_responses:
        overlap = len(user_tokens.intersection(response_tokens))
        if overlap > max_overlap:
            max_overlap = overlap
            max_overlap_response = " ".join(response_tokens)
    
    if max_overlap == 0:
        majibot_response = "I'm sorry! I'm unable to provide the requested information."
    else:
        majibot_response = max_overlap_response
        
    return majibot_response
# Tokenize responses from text file
tokenized_responses = [tokenize(response) for response in tokenize_text_file("OneDrive\Desktop\chatbot.txt")]
#---------------------------------------------------------------------------------


print("MajiBot: My name is MajiBot. If you have any questions relating to MajiAcademy, I am here to help! If you want to exit, type Bye!")
while True:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("MajiBot: You are welcome..")
        else:
            if greeting(user_response) is not None:
                print("MajiBot: " + greeting(user_response))
            else:
                print("MajiBot: ", end="")
                print(response(user_response, tokenized_responses))


    else:
        print("MajiBot: Bye! take care..")