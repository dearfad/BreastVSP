from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(
        model_name="chatglm",
        openai_api_base="http://127.0.0.1:8000/v1",
        openai_api_key="EMPTY",
        streaming=False,
    )

#使用会话实体内存，利用ChatGLM在会话过程中分析提到的实体(Entity)
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
entity_memory = ConversationEntityMemory(llm=llm, k=5 )

#生成会话链
from langchain.chains import ConversationChain
Conversation = ConversationChain(
            llm=llm, 
            prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
            memory=entity_memory,
            verbose=True,
        ) 
#开始测试
Conversation.run("你好，我名字叫Loui，在清华工作")