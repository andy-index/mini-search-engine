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

[ ]

## Tests

[  ]

## Roadmap

- [x] Document ingestion
- [x] Tokenization
- [x] Inverted indexing
- [x] Boolean AND/OR queries
- [x] TF-IDF ranking
- [x] Top-k retrieval
- [ ] Basic user interface
- [ ] Benchmarking
