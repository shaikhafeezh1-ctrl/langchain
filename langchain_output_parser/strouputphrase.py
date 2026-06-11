from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
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

promr1=template1.invoke({"topic":"stock market"})

result=model.invoke(promr1)

promr2=template2.invoke({"text":result.content})

result1=model.invoke(promr2)

print(result1.content)



