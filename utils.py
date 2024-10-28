from prompt_template import system_template_text, user_template_text
from xiaohongshu_model import Xiaohongshu
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate


def generate_xiaohongshu(theme, openai_api_key, openai_api_base="https://api.gptapi.us/v1", model_name="gpt-4o"):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text),
    ])

    model = ChatOpenAI(model=model_name, api_key=openai_api_key, base_url=openai_api_base)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result