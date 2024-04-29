import streamlit as st
import random
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure NLTK resources are downloaded (if not already done)
import nltk
nltk.download('punkt')

# Greetings message - Keyword matching
Greeting_input = ["greetings", "hi", "hope you're good", "hiya", "hey", "hello"]
Greeting_output = ["hi", "hey", "hiya", "*nods*", "hi there", "hello", "It's nice to meet you!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_input:
            return random.choice(Greeting_output)

def tokenize(text):
    return word_tokenize(text.lower())

def tokenize_text_file(text):
    return sent_tokenize(text)

# Reading chatbot responses from file
@st.cache  # This decorator caches the data so it's only reloaded when necessary
def load_responses(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

data_content = load_responses("OneDrive\Desktop\chatbot.txt")
tokenized_responses = [tokenize(response) for response in tokenize_text_file(data_content)]

def response(user_response):
    majibot_response = ""
    user_tokens = set(tokenize(user_response))
    max_overlap = -1
    max_overlap_response = ""

    for response_tokens in tokenized_responses:
        overlap = len(user_tokens.intersection(response_tokens))
        if overlap > max_overlap:
            max_overlap = overlap
            max_overlap_response = " ".join(response_tokens)

    if max_overlap == 0:
        return "I'm sorry! I'm unable to provide the requested information."
    else:
        return max_overlap_response

# Streamlit interface
st.title('MajiBot Chatbot')
user_input = st.text_input("Talk to the chatbot:")

if user_input:
    if user_input.lower() == 'bye':
        st.write("MajiBot: Bye! Take care..")
    elif user_input.lower() in ['thanks', 'thank you']:
        st.write("MajiBot: You are welcome..")
    else:
        bot_response = greeting(user_input) if greeting(user_input) else response(user_input)
        st.text_area("MajiBot:", value=bot_response, height=100)
import streamlit as st

# Define the style using a Python multi-line string
def load_css():
    st.markdown("""
        <style>
            .stTextInput > label, .stTextArea > label {
                font-size: 20px;
                font-weight: bold;
            }
            .stTextInput > div > div > input {
                font-size: 18px;
            }
            .stTextArea > div > textarea {
                font-size: 16px;
                height: 100px !important;
            }
            .stButton > button {
                font-size: 18px;
                width: 100%;
                height: 50px;
                margin-top: 5px;
            }
        </style>
        """, unsafe_allow_html=True)

# Load the CSS styles
load_css()

st.title('MajiBot Chatbot')

# Sidebar for chatbot information
with st.sidebar:
    st.header('MajiBot Info')
    st.write("This chatbot can answer questions related to MajiAcademy.")

# Main chat interface
st.header('Chat with MajiBot')

user_input = st.text_input("Type your message here:")
if st.button('Send'):
    # Here you would call your function to get the chatbot's response
    bot_response = "Your function to get chatbot's response goes here"
    st.text_area('Bot:', value=bot_response, height=150)
