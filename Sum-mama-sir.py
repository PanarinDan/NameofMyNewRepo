import streamlit
import pandas
import openai
import json

# get the API from sidebar called OpenAI API key
openai.api_key = streamlit.secrets["openai_api_key"]

# set the roles for the AI
# set the user to be the me
ai = "AI:"
user = "Me:"

# set the default prompt
prompt = """Act as an AI summarizer for English news. You will receive url 
            for the news you need to summarize and you should summarize it's 
            with a vocabulary that suitable for high school students.
            """

# set the default response
response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages_so_far)

# set the default messages
messages_so_far = [
    {
        "id": "1",
        "message": prompt,
    },
    {
        "id": "2",
        "message": response["choices"][0]["text"],
    },
]

# pull the data from the url to sent to Chat gpt
def pull_data(url):
    # get the data from the url
    data = pandas.read_csv(url)
    # get the data from the url
    data = data.to_dict()
    # return the data
    return data

# set the title of the app
streamlit.title("Sum-mama-sir")