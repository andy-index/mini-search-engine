
from pathlib import Path
import ir_datasets

# Locate the directory containing this Python file
project_dir = Path(__file__).resolve().parent

# Create a separate directory for Cranfield documents
output_dir = project_dir / "documents_cranfield"
output_dir.mkdir(exist_ok=True)

# Load the Cranfield dataset
dataset = ir_datasets.load("cranfield")

# Export each document as a UTF-8 text file
count = 0

for doc in dataset.docs_iter():
    filename = f"{doc.doc_id}.txt"
    filepath = output_dir / filename

    text = f"{doc.title}\n\n{doc.text}"
    filepath.write_text(text, encoding="utf-8")

    count += 1

print(f"Successfully exported {count} documents!")
