# Mini Search Engine

A lightweight search engine built in Python that indexes local text
documents and retrieves results based on query relevance.

## Problem

Finding documents containing a keyword is straightforward. Ranking those
documents according to how well they satisfy a user's query is more difficult.

This project explores how a small search product can provide relevant results
without relying on an existing search engine framework.

## Target User

Someone searching across a collection of local text documents who wants the
most relevant documents returned first.

## Product Goal

Build the smallest useful search system capable of indexing documents,
retrieving matches, and ranking them according to relevance.

## Current Features

- Document discovery and loading
- Text normalization/tokenization
- Inverted index
- Single-term search
- Multi-term AND queries
- Multi-term OR queries

## Non-Goals for MVP

- Semantic/vector search
- Embeddings
- Elasticsearch
- Distributed architecture
- Microservices

These capabilities could be useful at greater scale, but they do not address
the primary question being explored by the MVP: how should documents be
retrieved and ranked?

## How It Works
```
Documents
    ↓
Tokenizer
    ↓
Document Token Store
    ↓
Inverted Index
    ↓
Query Processor
    ↓
Candidate Documents
    ↓
TF-IDF Ranking
    ↓
Top Results
```

## Product Decisions

### Why an inverted index?

Scanning every document for every search would become increasingly expensive.
An inverted index maps each term to the documents containing that term,
reducing the search space.

### Why TF-IDF?

Raw term frequency alone does not account for document length or how common
a term is throughout the collection. TF-IDF increases the importance of
terms that are distinctive within the corpus.

## Success Metrics

- Ranking correctness on predefined test queries
- Precision of top search results
- Query latency
- Index construction time

## Running the Project

Requirements
Python 3.x
No external libraries are required
The project uses only Python's standard library.

### Run Locally

1. Clone the repository:
git clone <your-repository-url>

2. Move into the project directory:
cd Mini-Search-Engine

3. Make sure the documents/ directory contains the .txt files you want to search. Example:
```
Mini-Search-Engine/
│
├── main.py
├── README.md
└── documents/
    ├── python.txt
    ├── java.txt
    ├── redis.txt
    └── ...
```

4. Run the search engine:
python main.py
Depending on your system, you may need to use:
python3 main.py

5. Enter a search query when prompted:
Search for a document: Type ':quit' when finished. python backend
The search engine will return matching documents ranked by their TF-IDF relevance score.

Example output:
Search results for: python backend

1. python.txt      Score: 2.47
2. backend.txt     Score: 1.82
3. api.txt         Score: 0.91

To exit the program, enter:
:quit

## Tests

The search engine is currently tested using a collection of controlled text documents and predefined search queries.

Testing focuses on verifying the major stages of the search pipeline:
- Document loading
- Text normalization and tokenization
- Inverted-index construction
- AND query behavior
- OR query behavior
- Missing search terms
- Empty or invalid queries
- TF-IDF score calculation
- Search-result ranking

### Example Test Cases

| Query | Expected Behaviour |
|---|---|
| python | Returns documents containing python |
| python backend | Returns and ranks documents containing the query terms |
| nonexistentword | Returns a message indicating no matching documents were found |
| Empty input | Returns an invalid-input message |
| :quit | Exits the search program |

### Ranking Tests

TF-IDF ranking is tested using documents with intentionally different term frequencies.

For example, if python appears frequently throughout the document collection while redis appears in only a small number of documents, redis should receive a higher inverse-document-frequency value.
These controlled cases are used to verify that documents containing more relevant and distinctive query terms receive higher ranking scores.

### Current Testing Approach

Testing is currently performed manually through predefined documents and queries. Automated unit tests may be added in a future iteration to validate individual components such as tokenization, Boolean retrieval, inverted-index construction, and TF-IDF calculations.

## Roadmap

- [x] Document ingestion
- [x] Tokenization
- [x] Inverted indexing
- [x] Boolean AND/OR queries
- [x] TF-IDF ranking
- [x] Top-k retrieval
- [x] Benchmarking
