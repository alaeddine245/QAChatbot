from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from prompts import CONDENSE_QUESTION_PROMPT, POLICY_QA_PROMPT
from langchain.prompts import PromptTemplate

def create_qa_chain(retriever):
    
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    
    chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever,
        condense_question_llm=llm,
        condense_question_prompt=PromptTemplate.from_template(CONDENSE_QUESTION_PROMPT),
        verbose=True,
        combine_docs_chain_kwargs={"prompt": PromptTemplate.from_template(POLICY_QA_PROMPT)}
    )
    return chain