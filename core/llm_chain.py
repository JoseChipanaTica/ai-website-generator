import os
from langchain.llms import AI21
from langchain import PromptTemplate, LLMChain

AI21_API_KEY = os.environ['AI21_API_KEY']


def generate_content(prompt):
    """
    Generate content about business idea
    :return: str
    """

    template = """
    Business Idea: {businessIdea}
    Answer: ...
    """
    prompt = PromptTemplate(template=template, input_variables=["businessIdea"])

    llm = AI21(ai21_api_key=AI21_API_KEY)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    return llm_chain.run(prompt)


