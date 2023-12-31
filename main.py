import streamlit as st
import pandas as pd
import openai
import os

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('Research_paper.csv')


# Function to analyze user input using GPT-3.5 Turbo
def search_titles(topic):
    topic = topic.lower()
    matches = df[df['Domain'].str.lower().str.contains(topic)]
    return matches[['Title', 'Abstract','Link']]


# Main function to run the chatbot
def main():
    st.title("Researcher Chatbot")
    
    openai.api_key = ""

    

    # User input
    st.write("How may I help you?")
    user_input = st.text_input("Please type here", "")
    sys_prp = '''
    You have been given the following user_input,
    Analyze the text and find whether the text is about the following domains: 
    Health or Artificial Intelligence or Machine Learning or Mathematics.
    Return only the Domain Name
    If the Domain Name is not in the above topics please return the following text:
    "Sorry I dont have research papers on this topic. I will make them available soon."
    '''

    if user_input and api_key:
        conversation = [
            {"role": "system", "content": sys_prp},
            {"role": "user", "content": user_input}
        ]

        # Create OpenAI GPT-3.5 Turbo response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0,
            max_tokens=150,
        )
        analysis_result = response['choices'][0]['message']['content']

        # Display analysis result
        st.text_area("Analysis Result:", analysis_result, height=100)

        # Search for titles in the domain column
        titles = search_titles(analysis_result)
        if titles.empty:
            st.write("No Research papers found.")
        else:
            st.subheader(
                "As per your request, I am pleased to submit the following research papers for your consideration:")
            st.table(titles)


if __name__ == "__main__":
    main()
