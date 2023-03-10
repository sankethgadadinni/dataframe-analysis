import os
import csv
import shutil
import pandas as pd
import streamlit as st
from utils import generate_analysis, bullet_points, text_cleaning

import openai


def main():


    st.title("DataFrame analysis")
    
    openai_key = st.text_input("Please Enter Your OpenAI key")
    
    prompts = ['Can you describe following dataframe', 'Can you generate industrial business outlook from the dataframe', 'Considering the dataframe what summary metrics can you provide',
               'Can you identify any anomalies or outliers in above data', 'Check if there are any missing values in the dataframe', 'What are the most important KPIs in above data',
                'Can you give me value counts of all the categorical columns in above data']
    
    tasks = ['Description', 'Industry Business Outlook', 'Summary Statistics', 'Outliers', 'Missing Values', 'Industry KPI', 'Value Counts']
    
    prompts_and_tasks = zip(prompts, tasks)
    
    if openai_key:
    
        openai.api_key = openai_key

        filepath = st.file_uploader("Please Upload a CSV file", type = ['csv'])

        if filepath is not None:
            
            if st.button('submit'):
                
                path = os.path.join(os.getcwd(), filepath.name)
                
                try:
                    data = pd.read_csv(filepath)
                    data.to_csv('data.csv', index=False)
                except Exception as e:
                    print(e)
                    data = pd.read_excel(filepath)
                    data.to_csv('data.csv', index=False)
                
#                 if path[:-3] == 'csv':
#                     df = pd.read_csv(path)
#                     df.to_csv("data.csv", index=False)
#                 else:
#                     df = pd.read_excel(path, engine='openpyxl')
#                     df.to_excel("data.xlsx", index=False)
                
#                 st.header("Uploaded dataframe")
#                 st.dataframe(df.head(5))
                
                
#                 if path[:-3] == 'csv':
                full_path = os.path.join(os.getcwd(), "data.csv")
                df = pd.read_csv(full_path)
        
                st.header("Uploaded dataframe")
                st.dataframe(df.head(5))
#                 else:
#                     full_path = os.path.join(os.getcwd(), "data.xlsx")
#                     df = pd.read_excel(path, engine='openpyxl')
            
                
                results = [generate_analysis(x[0], x[1], df) for x in prompts_and_tasks]
            
                results = text_cleaning(results)

                
                
#                 results = [result.split("\n") for result in results]
                
#                 results = [result[2:] for result in results]
                
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
                    
    
                
                os.remove(full_path)
                
        else:
            st.write("Upload a valid CSV file")

        

if __name__ == '__main__':
    main()
    


        
        
    
    
