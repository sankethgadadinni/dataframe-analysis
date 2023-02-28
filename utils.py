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
        

def text_cleaning(original_list):

    # Create an empty list to hold the cleaned values
    cleaned_list = []

    # Loop through each item in the original list
    for item in original_list:
        # Check if the item starts with "\n\n" or "\n"
        if item.startswith("\n\n"):
            # If it does, remove those characters from the beginning of the string
            cleaned_item = item.lstrip("\n")
            cleaned_item = cleaned_item.split("\n")

            
        elif item.startswith("\n"):
            cleaned_item = item.lstrip("\n")
            cleaned_item = cleaned_item.split("\n")
            
        else:
            cleaned_item = item
            cleaned_item = cleaned_item.split("\n")

        # Add the cleaned item to the new list
        cleaned_list.append(cleaned_item)
    
    # cleaned_list = [item for sublist in cleaned_list for item in sublist]

    return cleaned_list
