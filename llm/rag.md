# Retrieval Augmented Generation(RAG)

Retrieval-Augmented Generation is the de facto method for providing grounding information to large language models. Its based on embeddings stored in a vector database offering semantic search.

## Vector Embedding

- Converting text into numerical vector representation.
- The vector representation is obtained by running it through the embedding model.
- Model outputs a dense vector of 768 or 1536 dimensions.
- Cosine distance between vectors reflects how related the texts are.
- Used in Retrieval augmented generation(RAG). Large input text is chunked and each chunk is converted to an embedding.
- User query is converted to embedding via the same embedding model and then cosine similarity or dot product or euclidean distance can be computed to find the nearest ones.
- Highly relevant chunks of text are then added to the model's context. LLM generates response grounded on this context.

### Embedded Vector Sizes

- Embedding vector size depends on the embedding model used. Irrespective of the text chunk size, the vector sizes are fixed for a given embedding model (384, 512, 768, 1536, 3072).
- Most importantly the text chunk should not exceed the embedding model's token input limit.
For LLM's the context window is `input tokens+output tokens≤context window`, whereas the embedding model outputs a fixed size vector.
- Exceeding the max token input size, could lead to implicit truncation and may not be desirable.
- Variable length token sequences are embedded into a fixed size vector embedding via pooling/aggregation over token embeddings(mean pooling, max pooling etc)

### Vector dimensionality and search effectiveness

- Higher dimension vector can encode more fine grained semantic information.
- Lower dimensions are cheaper and faster. If the underlying model is strong, then even smaller dimensions can produce better results.

> **In practice, model quality and training often matter more than raw size: a better 768‑dim model can outperform a weaker 1536‑dim model on the same retrieval task.
**

- For most RAG systems with few million chunks 768-1536 is a good range.

- Model's embedding quality is evaluated using `Massive Text Embedding Benchmark`(MTEB). This benchmark is a suite of tasks involving retrieval, classification, clustering, semantic textual similarity, reranking etc. We have [leaderboards](https://huggingface.co/spaces/mteb/leaderboard) for this on Huggingface.

- As per the leaderboard, [**voyage models**](https://blog.voyageai.com/2024/12/04/voyage-code-3/) are too good for their size, be it English or code retrieval tasks. But its a closed source model. Qwen is the best among the open source models(Qwen 3 0.6B, 4B, 8B), there is also jina code embeddings v2, BGE-M3.
- There is an argument against QWEN as its trained on the benchmark styled data. BGE-M3 and Jina code V2. So experiment yourself on these models.

### Embedding quantization

- Usually Each vector in the embedding is a float F32. But then it consumes more memory/storage, but also increases the query time.
- But recently some of the embedding models can return quantized vectors (int8) or even bit(binary) quantization.
- Also databases like [lancedb can do embedding quantization](https://lancedb.com/blog/feature-rabitq-quantization/)

## Key terminologies in Vector Search

- ANN - Approximate Nearest Neighbors. Spotify developed `ANNOY`, which is a memory efficient ANN for large scale recommendation
- Meta developed FAISS - high speed similarity search
- Google - ScaNN - highly efficieny ANN search technique
- Microsoft - Product Quantization(PQ) - Compresses high dimensional vectors.

## Indexing algorithms

> In vector databases, a vector index is a data structure that organizes vector embeddings to enable efficient similarity search. Indexing vector databases properly is crucial for performance, and different index types serve different purposes - from the simple flat index to more sophisticated approaches like HNSW and HFresh.

- Hierarchical Navigable Small World (HNSW) - Graph based indexing algorithm
- Inverted File Product Quantization(IVF_PQ)
- FLAT - Lightweight index designed for small datasets
- Inverted File FLAT(IVF FLAT)
- ANNOY

## Vector Databases

Dedicated vector databases

- Milvus
- ChromaDB
- Qdrant - Open source, Rust based.
- Pinecone - Closed source, fully managed.
- Weaviate - GraphQL support
- Lancedb - Open source, multimodal, embedded, columnar database written in Rust

Vector Enabled Databases

- Redis
- Elasticsearch
- Postgresql
- MongoDB

Graph databases for Graph RAG

- Kuzu (now archived)
- [Falkordblite](https://github.com/FalkorDB/falkordblite)

## [Embedding based RAG shortcomings](https://www.freecodecamp.org/news/how-to-solve-5-common-rag-failures-with-knowledge-graphs/)

- Quality of embedding model impacts the semantic search.
- Interpretability is hard with vector embeddings
- Fails to capture the relationship between different entities in a prompt.
- Entity ambiguity (Apple company vs fruit)
- Incorrect relationship hallucination

## [RAG without embeddings](https://www.digitalocean.com/community/tutorials/beyond-vector-databases-rag-without-embeddings)

- Full text search (keyword based search) using BM25
- Prompt RAG - Similar to how we author skills in claude code. Put the table of contents or skill metadata in the model context and it can retrieve relevant information. Requires higher context size for larger document retrieval.
- LLM driven iterative retrieval - AI agent to search the documents for answer using reasoning. Embedding-Less Retrieval with Iterative Text Exploration(ELITE) - iteratively narrow down on relevant text.
- Knowledge graph based Graph RAG

## Graph RAG

> In a graph-based RAG, entities (such as people, places, or concepts) are represented as nodes and relationships are represented as edges, extracted from the source text or database. In response to the user’s query, the system retrieves relevant nodes and follows edges to gather a set of facts or related pieces of information, which is then passed to the LLM.

This is especially valuable for complex queries that require multi-hop reasoning or fact joins (e.g., recognizing that Person A who did X is related to Person B mentioned elsewhere).

> Microsoft’s GraphRAG suggests that incorporating these connections can significantly enhance how Retrieval Augmented Generation systems work, moving beyond finding similar information to understanding the deeper context in which that information exists.
