from pathlib import Path

DOCUMENTS_DIR = (
    Path(__file__).resolve().parent.parent
    / "documents_cranfield"
)

def test_document_count():
    files = list(DOCUMENTS_DIR.glob("*.txt"))

    assert len(files) == 1400


def test_documents_are_not_empty():
    files = DOCUMENTS_DIR.glob("*.txt")

    for file in files:
        content = file.read_text(encoding="utf-8")

        assert content.strip() != "", (
            f"{file.name} is empty"
        )
