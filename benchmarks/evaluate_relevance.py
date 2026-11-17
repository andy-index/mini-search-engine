
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sys

import ir_datasets
import ir_measures
from ir_measures import P, nDCG

# Allow imports from the project root
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import main


def evaluate():
    dataset = ir_datasets.load("cranfield")

    assert len(main.token_dict) == 1400

    queries = list(dataset.queries_iter())

    # Convert negative relevance judgments to zero.
    # Preserve the positive graded relevance labels.
    qrels = [
        qrel._replace(relevance=max(0, qrel.relevance))
        for qrel in dataset.qrels_iter()
    ]

    run = []

    for query in queries:
        # Hide informational missing-term messages.
        # Actual exceptions will still be raised.
        with redirect_stdout(StringIO()):
            results = main.tf_idf_funct(query.text)

        # A string means no ranked results were returned.
        if isinstance(results, str):
            continue

        for filename, score in results:
            doc_id = Path(filename).stem

            run.append(
                ir_measures.ScoredDoc(
                    query.query_id,
                    doc_id,
                    score
                )
            )

    measures = [P @ 3, nDCG @ 5]

    scores = ir_measures.calc_aggregate(
        measures, qrels, run
    )

    print(f"Queries evaluated: {len(queries)}")

    for measure in measures:
        print(f"{measure}: {scores[measure]:.4f}")


if __name__ == "__main__":
    evaluate()
