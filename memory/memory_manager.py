from langchain_community.memory import ConversationBufferMemory


memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


def save_interaction(question, answer):

    memory.save_context(
        {"input": question},
        {"output": answer}
    )


def load_history():

    return memory.load_memory_variables({})