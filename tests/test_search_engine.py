
import math
import pytest
import main


SAMPLE_DOCS = {
    "doc1.txt": "python python python search",
    "doc2.txt": "python programming language",
    "doc3.txt": "search ranking algorithm",
    "doc4.txt": "cooking recipes kitchen",
}


@pytest.fixture
def sample_corpus(monkeypatch):
    tokens = {
        name: main.my_tokens(text)
        for name, text in SAMPLE_DOCS.items()
    }

    index = main.build_inverted_index(tokens)

    monkeypatch.setattr(main, "token_dict", tokens)
    monkeypatch.setattr(main, "inverted_dict", index)


def test_tokenizer():
    result = main.my_tokens("Python's SEARCH-engine!")

    assert result == ["python", "s", "search", "engine"]


def test_inverted_index():
    tokens = {
        name: main.my_tokens(text)
        for name, text in SAMPLE_DOCS.items()
    }

    index = main.build_inverted_index(tokens)

    assert index["python"] == {"doc1.txt", "doc2.txt"}
    assert index["search"] == {"doc1.txt", "doc3.txt"}


def test_boolean_and(sample_corpus):
    result = main.inter_function("python search")

    assert result == {"doc1.txt"}


def test_boolean_or(sample_corpus):
    result = main.union_function("python search")

    assert result == {
        "doc1.txt", "doc2.txt", "doc3.txt"
    }


def test_and_does_not_modify_index(sample_corpus):
    original = main.inverted_dict["python"].copy()

    main.inter_function("python search")

    assert main.inverted_dict["python"] == original


def test_tfidf(sample_corpus):
    results = main.tf_idf_funct("python")
    scores = dict(results)

    expected_doc1 = (3 / 4) * math.log(4 / 2)
    expected_doc2 = (1 / 3) * math.log(4 / 2)

    assert scores["doc1.txt"] == pytest.approx(expected_doc1)
    assert scores["doc2.txt"] == pytest.approx(expected_doc2)
    assert results[0][0] == "doc1.txt"


def test_no_results(sample_corpus):
    result = main.tf_idf_funct("nonexistentword")

    assert isinstance(result, str)
