import os
import csv
import shutil
import pandas as pd
import streamlit as st
from utils import generate_analysis, bullet_points

import openai


def main():


    st.title("DataFrame analysis")
    
    openai_key = st.text_input("Please Enter Your OpenAI key")
    
    prompts = ['Can you describe following dataframe', 'Can you generate industrial business outlook from the dataframe', 'Can you generate summary statistics from the dataframe',
               'Can you give me the outliers in the dataframe', 'Can you give me the missing values in the dataframe', 'Can you generate industry KPI']
    
    tasks = ['Description', 'Industry Business Outlook', 'Summary Statistics', 'Outliers', 'Missing Values', 'industry KPI']
    
    prompts_and_tasks = zip(prompts, tasks)
    
    if openai_key:
    
        openai.api_key = openai_key

        filepath = st.file_uploader("Please Upload a CSV file", type = ['csv', "xlsx"])

        if filepath is not None:
            
            if st.button('submit'):
                
                path = os.path.join(os.getcwd(), filepath.name)
                
                if path[:-3] == 'csv':
                    df = pd.read_csv(path)
                else:
                    df = pd.read_excel(path, engine='openpyxl')
                
                st.header("Uploaded dataframe")
                st.dataframe(df.head(5))
            
                
                results = [generate_analysis(x[0], x[1], df) for x in prompts_and_tasks]
                
                
                results = [result.split("\n") for result in results]
                
                results = [result[2:] for result in results]
                
                header = st.container()

                with header:
                    st.title("Description")
                    bullet_points(results[0])
                    
                    st.title("Industry Business Outlook")
                    bullet_points(results[1])
                    
                    st.title("Summary Statistics")
                    bullet_points(results[2])
                    
                    st.title("Outliers")
                    bullet_points(results[3])
                    
                    st.title("Missing Values")
                    bullet_points(results[4])
                    
                    st.title("Industry KPI")
                    bullet_points(results[5])
                    
    
                
                os.remove(path)
                
        else:
            st.write("Upload a valid CSV file")

        

if __name__ == '__main__':
    main()
    


        
        
    
    