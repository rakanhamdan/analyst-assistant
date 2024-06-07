import pandas as pd
import streamlit as st
import tempfile
import os

from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser


def main():
    st.set_page_config(page_title="Business Analyst Assistant")
    st.header("BizShifter Team")

    # Create a file uploader in the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload File", type="csv")

    # Handle file upload
    if uploaded_file:
        # st.write(uploaded_file.name)

        df = pd.read_csv(uploaded_file)
        context = f"""
            df:
            {df.sample(n=5).to_string()}
            
            df.shape:
            {df.shape}

            df.dtypes:
            {df.dtypes}

            """

        
        # show user input
        user_question = st.text_input("Do you have any Notes/instructions to commit to ?")


        prompt_template = PromptTemplate.from_template(

             """
            Your role is : **Business Analyst Assistant**

            You are a business analyst assistant, you will be used by data analysts and business analysts by giving them a starting point to work on with their data. You will do the following:

            when the user uploads the csv file, you will use the information provided in the context to gather general information about the data
            
            your context:
            {context}

            **Instructions:**

            As a business analyst assistant, Your main task is to generate a report.
            This report is divided into two parts:
            1. Insights about the CSV file:  brief Useful information to understand what this data file is about. with meta data about the columns for understanding what each column represents.
            
            
            2. Recommended relationships: Based on your understanding of the data, suggest some relationships about how some columns affect each other. these relationships should be applicable later when creating dashboards. be specific and precise about the relationships and show potential graphs to use between the columns in a suggested relationship. Add an explaination for choosing each relationship. Always show the response of this step in a table

            **Analyst Notes:**
            In this part after the csv is loaded, you will ask the analyst about any notes or Instructions you want to consider when creating the response.
            You must follow the analyst notes 100% . 
            if the analyst doesn't add any notes work as usual 

            The Analyst Notes: 

            {question}

            **The report:**

            """ 
        ) 
        
        # here we structure the prompt to pass it to the llm
        prompt_val = prompt_template.invoke({"context": context, "question":user_question })


        if user_question:
            
            # load the model (llm)
            llm = ChatOllama(model="llama3")
            # get the response .  Invoke = it's simialr to .predit()
            response = llm.invoke(prompt_val)       
        

            # show the output            
            st.write(response.content)
            # Create buttons for Yes and No options
            cleaned = st.button("Yes")  # Button for cleaning data
            not_cleaned = st.button("No")  # Button for skipping cleaning            if Cleaned:
            FILENAME =uploaded_file.name
            # Conditional logic based on button clicks
            if cleaned:
                # Perform data cleaning actions here
                
                st.write("Data cleaning in progress...")
                cleaned_prompt = PromptTemplate.from_template(
                      """
                        using this context:
                        {context}
                        write a python code that cleaned the data that user loaded
                        also suggest some features engenering between the columns

                        Note:when you read the DataFrame, the name of the Data file that the user loaded is {FILENAME} 
                        """
                )
                prompt_code = cleaned_prompt.format(context=context,FILENAME=FILENAME )
                response = llm.invoke(prompt_code)
                st.write(response.content)


                # Replace this with your actual cleaning logic
            elif not_cleaned:
                st.write("Skipping data cleaning.")
            else:
                # Handle the case where no button is clicked (optional)
                st.write("Please choose an option.")
 
if __name__ == '__main__':
    main() 
