from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def MyAi(recipe_message):
    SECRET_KEY = config('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "Your name is Aarul. You are a Python Developer  so First Introduce yourself as Aarul . You can give sweet and short code. You are only allowed to answer python related queries. If You don't know the answer then tell I don't know the answer.")
    humanMessagePrompt = HumanMessagePromptTemplate.from_template(
        '{asked_recipe}')

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(
        asked_recipe=recipe_message)
    # print("Formatted Chat Prompt: ", formattedChatPrompt)
    response = chat.invoke(formattedChatPrompt)
    return response.content
