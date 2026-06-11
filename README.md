# langchain
LLMs: LangChain abstracts access to models like OpenAI, Anthropic, and Hugging Face. It supports both completion and chat models, enabling flexible text generation
Prompts: At the heart of every LLM call is a prompt. LangChain offers PromptTemplate for reusable text templates and ChatPromptTemplate for multi-turn conversations. These ensure inputs are structured and dynamic.
Chains: Chains link prompts, models, and other utilities into sequences. A simple LLMChain runs a prompt through a model, while SequentialChain executes multiple steps. Router chains direct inputs to specialized subchains
Agents: Agents introduce decision-making. They select tools and actions dynamically to solve tasks. Tools can be calculators, search APIs, or custom functions. The AgentExecutor manages the agent loop.
Memory: Memory stores context across interactions. Options include BufferMemory for full transcripts, SummaryMemory for condensed context, and VectorStoreRetrieverMemory for embedding-based recall.
Indexes & Retrieval: LangChain integrates with vector databases like FAISS, Pinecone, and Chroma. Retrievers fetch relevant documents, enabling semantic search and question answering
Document Loaders: These import data from text, CSV, PDFs, or web sources, making external knowledge accessible to LLMs.
Embeddings: Text is converted into vectors for similarity search, clustering, and retrieval. Embeddings power context-aware applications.
Callbacks: Hooks provide observability, logging, and debugging. They help track performance and execution flow.
LangSmith: A companion platform for tracing, evaluating, and debugging LangChain applications. It supports experiment comparison and production monitoring.
