import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, format_instructions
from pydantic import BaseModel , Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
    
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name:str=Field(description="Name of thr person")
    age: int=Field(gt=18,description="Age of the person")
    city: str= Field(description="Name of the city the person belong to")

parser=PydanticOutputParser(pydantic_object=Person)


template1 =PromptTemplate(
    template="Genrate the name , age and city of a fictional {place} person\n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt=template1.invoke({'place':'india'})

result=model.invoke(prompt)

final_result=parser.parse(result.content) # type: ignore

print(final_result)
