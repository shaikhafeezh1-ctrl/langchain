from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel ,RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatOpenAI()

parser= StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal["postive","Negtive"]= Field(description="Gives the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

promt1=PromptTemplate(
    template="Classify the senriment of the following feedback into postive or negitive  \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

classifier_chain = promt1 | model | parser2

promt2=PromptTemplate(
    template="Write an approrprite responce to this postive feedback \n {feedback}",
    input_variables=['feedback']
)

promt3=PromptTemplate(
    template="Write an approrprite responce to this negtive feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x : x.sentiment=="positive", promt2 | model | parser),
    (lambda x : x.sentiment=="negative", promt3 | model | parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback":"This a terrible phone"}))