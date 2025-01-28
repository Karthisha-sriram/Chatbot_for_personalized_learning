import streamlit as st
import requests
import json

# Function to send the message to the bot and get a response
def get_bot_response(message):
    # For predefined questions, provide custom responses
    if message == "What are the topics available?":
        return "The topics available are Machine Learning, Data Science, Web Development, Virtualization, Big Data, Computer Vision, Cyber Security, Cloud Infrastructure, Distributed Systems, Edge Computing, Object-Oriented Programming, and AI."

    if message == "What is the definition of machine learning?":
        return "Here's a detailed explanation about machine learning: Machine learning (ML) is a branch of computer science that uses artificial intelligence to learn from data. The main principles or components of ML are: A machine learning model is an algorithm that learns from data and applies it to solve real-world problems."

    if message == "Could you describe Data Science?":
        return "Here's a detailed explanation about data science: Data science is a branch of computer science that deals with the analysis and interpretation of large quantities of data. The main principles or components of data science are: Analyzing large amounts of data to make more accurate predictions about the world around us. Applying this knowledge to solve real-world problems such as economic, political, and social problems. Real-world applications include health care, financial services, insurance, transportation, and many others."

    if message == "What is the concept of Big Data?":
        return "Here's a detailed explanation about big data: Big data is the collection and analysis of large quantities of data from a wide variety of sources, such as social media, financial records, medical records, weather data, etc. It can be used to make informed decisions about how to use resources in a way that maximizes efficiency and minimizes costs."

    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",  # Adjust the URL as needed
            headers={"Content-Type": "application/json"},
            data=json.dumps({"message": message}),
        )
        # Check for successful response
        response.raise_for_status()
        bot_response = response.json()

        # Process and return the bot's response
        if bot_response:
            return " ".join([res["text"] for res in bot_response if "text" in res])

    except requests.exceptions.RequestException as e:
        st.error(f"Error with the Rasa server: {e}")
        return "Sorry, I couldn't fetch the response from the bot."


# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Chat input for the user
prompt = st.chat_input("Say something")

if prompt:
    # Append the user's input to the conversation history
    st.session_state.conversation_history.append({"role": "user", "content": prompt})

    # Send the user's message to the Rasa server (adjust the URL as needed)
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"message": prompt}),
        )
        # Check for successful response
        response.raise_for_status()
        bot_response = response.json()

        # Process and store bot's response
        if bot_response:
            bot_message = " ".join([res["text"] for res in bot_response if "text" in res])
            st.session_state.conversation_history.append({"role": "bot", "content": bot_message})

    except requests.exceptions.RequestException as e:
        st.error(f"Error with the Rasa server: {e}")

# Set up the Streamlit UI components with a stylish title
st.markdown("""
    <style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: black;
    }
    .sidebar-title {
        color: white;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    .menu-item {
        color: white;
        font-size: 18px;
        margin-bottom: 15px;
        cursor: pointer;
    }
    .menu-item:hover {
        color: #4A90E2;
        font-weight: bold;
    }
    .new-chat {
        background-color: #4A90E2;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
    }
    .new-chat:hover {
        background-color: #357ABD;
    }

    /* Chat header */
    .bot-header {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px;
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
    }
    .bot-avatar {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
    }
    .bot-title {
        font-size: 24px;
        font-weight: bold;
    }

    /* Chat area */
    .chat-container {
        background-color: #F5F5F5;
        padding: 20px;
        border-radius: 10px;
    }
    .user-message, .bot-message {
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 10px;
    }
    .user-message {
        background-color: #E0F7FA;
        text-align: right;
    }
    .bot-message {
        background-color: #FFF3E0;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with fully black background and only the New Chat button
with st.sidebar:
    st.markdown('<div class="sidebar-title">Edubot Assistant</div>', unsafe_allow_html=True)

    # New Chat button resets the conversation
    if st.button("New Chat", key="new_chat", use_container_width=True):
        st.session_state.conversation_history = []  # Reset conversation history

    # Add the heading for frequently asked questions
    st.markdown('<h3 style="color: white;">Frequently Asked Questions</h3>', unsafe_allow_html=True)

    # Predefined questions
    if st.button("What are the topics available?", key="question_1"):
        question = "What are the topics available?"
        st.session_state.conversation_history.append({"role": "user", "content": question})
        bot_response = get_bot_response(question)
        st.session_state.conversation_history.append({"role": "bot", "content": bot_response})

    if st.button("What is the definition of machine learning?", key="question_2"):
        question = "What is the definition of machine learning?"
        st.session_state.conversation_history.append({"role": "user", "content": question})
        bot_response = get_bot_response(question)
        st.session_state.conversation_history.append({"role": "bot", "content": bot_response})

    if st.button("Could you describe Data Science?", key="question_3"):
        question = "Could you describe Data Science?"
        st.session_state.conversation_history.append({"role": "user", "content": question})
        bot_response = get_bot_response(question)
        st.session_state.conversation_history.append({"role": "bot", "content": bot_response})

    if st.button("What is the concept of Big Data?", key="question_4"):
        question = "What is the concept of Big Data?"
        st.session_state.conversation_history.append({"role": "user", "content": question})
        bot_response = get_bot_response(question)
        st.session_state.conversation_history.append({"role": "bot", "content": bot_response})

    # Add Help and About Us buttons at the bottom
    st.markdown('<h3 style="color: white;">Need More?</h3>', unsafe_allow_html=True)

    # Handle "Help" button click and display the response below it within the sidebar
    if st.button("Help", key="help_button"):
        question = "Help"
        bot_response = "If you need any help, feel free to ask me about various topics such as programming, data science, machine learning, or any technical concepts."
        st.markdown(f'<div style="color: white; background-color: #2d3436; padding: 10px; border-radius: 10px;">{bot_response}</div>', unsafe_allow_html=True)

    # Handle "About Us" button click and display the response below it within the sidebar
    if st.button("About Us", key="about_us_button"):
        question = "About Us"
        bot_response = "I am Edubot, your assistant for learning about a variety of technical topics. Our aim is to provide you with useful information and resources to enhance your knowledge."
        st.markdown(f'<div style="color: white; background-color: #2d3436; padding: 10px; border-radius: 10px;">{bot_response}</div>', unsafe_allow_html=True)

# Display the conversation history with styling
for message in st.session_state.conversation_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(
                f'<div style="color: blue; background-color: #f0f8ff; padding: 10px; border-radius: 10px; font-size: 16px;">'
                f"{message['content']}</div>",
                unsafe_allow_html=True
            )
    elif message["role"] == "bot":
        with st.chat_message("assistant"):
            bot_message = message["content"]

            # Make URLs clickable by transforming them into HTML anchor tags
            import re

            # Regex to match links in the bot message
            bot_message = re.sub(r'(https?://[^\s]+)', r'<a href="\1" target="_blank" style="color: #4A90E2;">\1</a>', bot_message)

            st.markdown(
                f'<div style="color: green; background-color: #fff5e6; padding: 10px; border-radius: 10px; font-size: 16px;">'
                f"{bot_message}</div>",
                unsafe_allow_html=True
            )
