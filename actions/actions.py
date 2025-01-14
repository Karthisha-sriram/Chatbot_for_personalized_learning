import streamlit as st
import requests
import json

# Set up the Streamlit UI components
st.title("Edubot")
st.write("Chat with the Rasa bot!")

# Initialize conversation history in session_state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Get user input
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
            for res in bot_response:
                if "text" in res:
                    bot_message = res["text"]
                    st.session_state.conversation_history.append({"role": "bot", "content": bot_message})
                elif "image" in res:
                    st.session_state.conversation_history.append({"role": "bot", "content": res["image"], "type": "image"})
    except requests.exceptions.RequestException as e:
        st.error(f"Error with the Rasa server: {e}")

# Display the conversation history using st.chat_message
for message in st.session_state.conversation_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    elif message["role"] == "bot":
        with st.chat_message("assistant"):
            if message.get("type") == "image":
                st.image(message["content"])
            else:
                st.write(message["content"])