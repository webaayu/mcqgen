import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import get_table_data, read_data_from_url
import streamlit as st
# from langchain.llms import Ollama
from langchain_community.llms import Ollama
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks import StreamlitCallbackHandler
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# loading JSON file
with open(r'C:\Users\Hardik\mcqgen\response.json', 'r', encoding="utf-8") as file:
    RESPONSE_JSON = json.load(file)

#create a title
st.title("MCQ Creator Application with Ollama")

#create a form using st.form
with st.form("user_inputs"):
    url_add=st.text_input("URL", max_chars=100)
    mcq_count=st.number_input("No. of MCQ", min_value=3, max_value=50)
    subject=st.text_input("Insert Subject", max_chars=20)
    tone=st.text_input("Complexity level of Questions", max_chars=20, placeholder="simple")
    button=st.form_submit_button("Create MCQs")

    if button and url_add is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_data_from_url(url_add) 
                response = generate_evaluate_chain({
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    })
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
    
            if isinstance(response,dict):
                #extract quiz data from the response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in a textbox as well
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")
            else:
                st.write(response)    
                    
