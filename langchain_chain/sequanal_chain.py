from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prmpt1=PromptTemplate(
    template="Genrate a detailed report on {topic}",
    input_variables=['topic']
)

prmpt2=PromptTemplate(
    template="Genrate a 5 pointer summary  from the following text /n {text}",
    input_variables=["text"]
)

model= ChatOpenAI()

parser = StrOutputParser()

chain = prmpt1 | model | parser | prmpt2 | model | parser

result = chain.invoke({"topic":"IPO"})

print(result)

chain.get_graph().print_ascii()