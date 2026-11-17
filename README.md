# Mini Search Engine

# Mini Search Engine

A Python-based text search engine implementing fundamental information retrieval techniques, including inverted indexing, Boolean retrieval, and TF-IDF ranking.

The project was developed to explore how search engines organize text documents, process queries, and rank results by relevance.

## Features

- **Text preprocessing:** Lowercase normalization, punctuation removal, and tokenization.
- **Inverted index:** Maps terms to the documents containing them using Python dictionaries and sets.
- **Boolean retrieval:** Supports AND and OR operations for finding matching documents.
- **TF-IDF ranking:** Calculates relevance scores using normalized term frequency and inverse document frequency.
- **Top-5 results:** Returns up to five documents ranked by TF-IDF score.
- **Command-line interface:** Accepts text queries and displays ranked results.
- **Automated testing:** Includes unit tests, integration tests, and retrieval evaluation.

## How It Works

The search engine processes documents through the following pipeline:

1. Read UTF-8 text files from the document directory.
2. Normalize and tokenize their contents.
3. Construct an inverted index mapping terms to documents.
4. Tokenize incoming search queries.
5. Find matching documents using the inverted index.
6. Calculate TF-IDF scores for matching documents.
7. Return the five highest-scoring results.

The current command-line interface uses TF-IDF ranking. Boolean retrieval is implemented as separate search functions.

## Technologies Used

- Python
- Python standard-library data structures
- pytest
- ir_datasets
- ir-measures

## Getting Started

**1. Clone the repository**

Clone the repository to your computer and navigate into its root directory.

**2. Install dependencies**

Run `python -m pip install -r requirements.txt`.

**3. Import the dataset**

Run `python import_cranfield.py`.

This downloads and exports the Cranfield collection into a local directory containing 1,400 text documents.

**4. Start the search engine**

Run `python main.py`.

Enter a text query to receive the five highest-ranked matching documents. Type `:quit` to exit.

## Testing

The project includes automated tests for text preprocessing, inverted indexing, Boolean retrieval, TF-IDF scoring, and end-to-end search functionality.

Run the test suite using:

`python -m pytest tests/ -v`

## Evaluation

Retrieval quality was measured using the Cranfield collection, which contains 1,400 documents and 225 evaluation queries.

| Metric | Result |
|---|---:|
| Precision@3 | 0.2711 |
| nDCG@5 | 0.2445 |
| Average query latency | 23.992 ms |
| Median query latency | 23.112 ms |
| P95 query latency | 40.334 ms |
| Warm indexing time | 50.34 ms |
| Unique indexed terms | 7,493 |

**Evaluation methodology:** Retrieval quality was calculated using Cranfield's relevance judgments. Negative relevance labels were treated as zero. Precision@3 treats positive relevance grades as relevant, while nDCG@5 uses graded relevance.

Latency was measured across 225 queries against an already constructed in-memory index. The indexing benchmark includes reading, tokenizing, and building the index during a subsequent warm pass.

Results may vary based on hardware and runtime conditions.

To reproduce the evaluations:

- `python benchmarks/evaluate_relevance.py`
- `python benchmarks/benchmark_performance.py`

## Current Limitations

- Supports local text documents rather than web pages or other media types.
- Uses basic tokenization without stemming or lemmatization.
- Returns only the five highest-scoring documents.
- Stores the document collection and inverted index in memory.
- Uses straightforward TF-IDF scoring without more advanced ranking techniques.

## Potential Improvements

- Precompute document term frequencies to improve query performance.
- Implement persistent indexing.
- Introduce improved normalization and stemming.
- Compare TF-IDF against BM25 ranking.
- Evaluate scalability using larger document collections.

## Dataset

This project uses the Cranfield information retrieval dataset, accessed through the ir_datasets library.

https://ir-datasets.com/cranfield.html
