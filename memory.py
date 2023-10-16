
from langchain.memory import ConversationBufferWindowMemory


def load_memory() -> ConversationBufferWindowMemory:
    """Load memory from session state

    Returns:
        memory_loader: ConversationBufferMemory object
    """
    memory = ConversationBufferWindowMemory(k=3, return_messages=True)
    return memory