
import pandas as pd
from pathlib import Path

# Find the project folders
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "dataset"
DATA_DIR.mkdir(exist_ok=True)

# Example input data
texts = [
    "I love learning Python!",
    "Artificial Intelligence helps computers solve problems.",
    "Hello, how are you?"
]

# Save input text to CSV
input_df = pd.DataFrame({"text": texts})
input_df.to_csv(DATA_DIR / "input_text.csv", index=False)

print("Input text saved successfully!")
print("Week 7 project is ready.")
