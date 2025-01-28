# Chatbot_for_personalized_learning
## Infosys springboard
This project focuses on creating a personalized learning chatbot to enhance educational experiences. The chatbot will be developed using Rasa, an open-source conversational AI framework, and integrated with Streamlit, a Python library for building interactive web applications.\
1.Provide tailored educational assistance based on user needs.\
2.Deliver interactive learning sessions for students.



## Installation
### prerequisites
Python 3.10 or later\
Rasa Open Source\
Virtual environment (recommended)
### Steps
1.Clone the repository:
```
https://github.com/Karthisha-sriram/Chatbot_for_personalized_learning.git
```
2.Navigate to the Project Directory

3.Create and Activate a Virtual Environment
4.Install dependencies
```
pip install -r requirements.txt
```
5.Train the model
```
Rasa train
```
### Running the bot
1.**rasa shell**(in shell)\
2.**rasa run**(as a server)
### Start the rasa action server
run the following commands
```
rasa run --enable-api --cors "*" --port 5005
rasa run actions
streamlit run "filename.py"
```
## The final User Interface
1. ![Screenshot 2025-01-28 001845](https://github.com/user-attachments/assets/75a5bee9-0439-46eb-a107-ecfccf4775b9)
2. ![Screenshot 2025-01-28 002111](https://github.com/user-attachments/assets/e2e0213e-249a-4c37-85ba-d0c83d6da6c5)

### Features
 1.Basic Q&A Functionality: Answer Student Queries.\
 2.API Integration: Integration with other educational tools, such as youtube to enhance the learning experience.\
 3.Resource Recommendations: Suggest Learning Materials.\
 4.Interactive Conversations: Simple dialogues that focus on one topic at a time.


## License
This project is shared under the terms of **MIT License.**
