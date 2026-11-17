
import sys
import time
import statistics
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO

import ir_datasets

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import main


def benchmark():
    # Measure document loading and index construction
    start = time.perf_counter()

    raw_docs = main.read_files()

    tokens = {
        name: main.my_tokens(text)
        for name, text in raw_docs.items()
    }

    index = main.build_inverted_index(tokens)

    indexing_ms = (time.perf_counter() - start) * 1000

    print(f"Documents indexed: {len(tokens)}")
    print(f"Unique terms: {len(index)}")
    print(f"Indexing time: {indexing_ms:.2f} ms")

    # Measure query performance
    dataset = ir_datasets.load("cranfield")
    queries = list(dataset.queries_iter())

    latencies = []

    # Suppress missing-term messages during benchmarking
    with redirect_stdout(StringIO()):

        # Warm up the search function
        for query in queries[:5]:
            main.tf_idf_funct(query.text)

        for query in queries:
            start = time.perf_counter()

            main.tf_idf_funct(query.text)

            elapsed = (time.perf_counter() - start) * 1000
            latencies.append(elapsed)

    # Calculate performance statistics
    latencies.sort()

    avg = statistics.mean(latencies)
    median = statistics.median(latencies)

    p95_index = int(0.95 * (len(latencies) - 1))
    p95 = latencies[p95_index]

    print(f"Queries tested: {len(latencies)}")
    print(f"Average latency: {avg:.3f} ms")
    print(f"Median latency: {median:.3f} ms")
    print(f"P95 latency: {p95:.3f} ms")


if __name__ == "__main__":
    benchmark()
