
import main


def test_full_search_pipeline(tmp_path, monkeypatch):
    # Create a temporary document directory
    folder = tmp_path / "documents_cranfield"
    folder.mkdir()

    # Create three sample documents
    documents = {
        "a.txt": "python python search",
        "b.txt": "python systems",
        "c.txt": "cooking recipes",
    }

    for filename, content in documents.items():
        (folder / filename).write_text(
            content, encoding="utf-8"
        )

    # Make read_files() use the temporary directory
    monkeypatch.chdir(tmp_path)

    # Step 1: Read the documents
    raw_docs = main.read_files()
    assert len(raw_docs) == 3

    # Step 2: Tokenize the documents
    tokens = main.tokenized_dict()
    assert tokens["a.txt"] == [
        "python", "python", "search"
    ]

    # Step 3: Build the inverted index
    index = main.build_inverted_index(tokens)
    assert index["python"] == {"a.txt", "b.txt"}

    # Step 4: Supply this test corpus to the search functions
    monkeypatch.setattr(main, "token_dict", tokens)
    monkeypatch.setattr(main, "inverted_dict", index)

    # Step 5: Search and verify ranking
    results = main.tf_idf_funct("python")

    assert [doc for doc, score in results] == [
        "a.txt", "b.txt"
    ]
