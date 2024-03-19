#Utility package /helperfile
import os
import json
import traceback
import PyPDF2
import requests
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
#import requests
from bs4 import BeautifulSoup as Soup
from langchain_community.document_loaders import RecursiveUrlLoader

def read_data_from_url(url):
    try:
        loader = RecursiveUrlLoader(url=url, max_depth=2, extractor=lambda x: Soup(x, "html.parser").text)
        text = loader.load()
        return text
    except Exception as e:
        return f"Error: {str(e)}"

"""def read_data_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Unable to fetch data from {url}. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

def read_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content_type = response.headers.get('content-type')

        if 'text' in content_type:
            return response.text
        elif 'pdf' in content_type:
            # Assuming you have PyPDF2 installed
            import PyPDF2
            pdf_reader = PyPDF2.PdfFileReader(response.content)
            text = ""
            for page in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page).extractText()
            return text
        # Add support for other content types here
        else:
            raise Exception("Unsupported content type! Only text and PDF supported.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching content from URL: {e}")
    except Exception as e:
        raise Exception(f"Error processing content: {e}")
def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the pdf file")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise Exception(
            "unsupported file format! only pdf and text file supported"
            ) 
"""
def get_table_data(quiz_str):
    try:
        #convert quiz from string to dictinary
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        #iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                    ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
    
        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
