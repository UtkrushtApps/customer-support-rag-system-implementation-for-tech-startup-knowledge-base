# Customer Support RAG System Implementation

## Task Overview
Build a working retrieval-augmented generation (RAG) system for customer support by implementing core logic for document processing, retrieval, and answer generation. You will support customer queries over a collection of support documents (FAQs, troubleshooting, manuals) that you source or generate yourself, using an empty Chroma vector database as your persistent backend.

## Guidance
- Source, create, or assemble customer support content and place your files in `data/documents/`. Typical document types include FAQs, manuals, and step-by-step guides.
- Implement a pipeline that ingests, cleans, de-duplicates, chunks with overlap, attaches metadata, generates embeddings, and batch-inserts them into Chroma DB.
- Implement optimized vector retrieval, handling top-k similarity search, proper distance metrics, and appropriate metadata filtering.
- Build end-to-end query processing: encode input, retrieve relevant chunks, build context, and generate a cited, referenced final support response.
- Evaluate quality with recall@k, precision@k, and answer relevance for the provided sample queries in `sample_queries.txt`.
- All key architectural and implementation decisions (embedding model, chunk size, retrieval logic, prompt design) are at your discretion.

## Database Access Information
- Chroma DB service is available at `localhost:8000`. Your client code connects directly to this endpoint.
- All collections, schemas, and indexes must be created by your implementation as needed.
- Use the provided `database_client.py` as a starting utility for DB operations.
- Validate batch insert, retrieval, and deletion operations as you build the pipeline.

## Objectives
- Build an ingest pipeline to parse and chunk customer support docs; generate and store embeddings with relevant metadata.
- Implement an optimized top-k retrieval system, choosing and configuring appropriate distance metrics.
- Assemble query contexts and generate support responses referencing source chunks.
- Evaluate retrieval accuracy and system response quality.
- Ensure all implementation is well-documented and reproducible on the provided template.

## How To Verify
- Spot-check document ingestion, chunking, and metadata attachment for accuracy.
- Use `database_client.py` or your own tests to validate correct embedding storage and retrieval.
- Run queries from `sample_queries.txt`; measure recall@k, precision@k, and check that responses accurately reference appropriate sources.
- Review performance logs (latency, recall, etc.), and test corrective actions for retrieval misses or poor responses.
