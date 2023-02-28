import openai
import streamlit as st

def generate_analysis(prompt, task, csv_text):
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt}:\n{csv_text}\n\n{task}:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )

    result = response.choices[0].text
    
    return result


def bullet_points(list_of_text):
    
    for text in list_of_text:
        st.markdown(f"{text}")
