import streamlit
import pandas
import openai

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
# set the title
streamlit.title("Summarizer")

# set uyser input
user_input = streamlit.text_input("Enter the url for the news you want to summarize:")

# set the button
if streamlit.button("Summarize"):
    # pull news data from url
    news = pandas.read_html(user_input)
    
    # push the news to the AI
    prompt = prompt + "\n" + news[0][0][0]

    # set the messages so far
    messages_so_far = [
        {
            "AI": user,
            "Me": prompt
        },]
    
    # set the response
    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages_so_far)
    
    # show response to client
    streamlit.write(response)

