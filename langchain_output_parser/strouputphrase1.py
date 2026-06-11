from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


model=ChatOpenAI()

# 1st promt -> detailed report
template1= PromptTemplate(

    template="Write a detaile report in {topic}",
    input_variables=["topic"]
)

# 2st promt-> summary
template2=PromptTemplate(

    template="Write detailed summary on./n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic":"IPO"})

print(result)