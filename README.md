# News Parser

## Description
This project is a news parser that collects article titles, processes them, and performs frequency analysis on the most common words. The results are saved in structured files for further use.

## Features
- Fetches multiple pages of news articles
- Cleans and processes text data
- Removes stop words and noise
- Performs word frequency analysis
- Saves results in structured formats (JSON and CSV)

## Project Structure
```
utils/
  ├── get_pages.py      # Collects links to news pages
  ├── get_dataset.py    # Extracts and cleans news titles
  ├── get_top.py        # Analyzes word frequency and saves the top results
app.py                  # Main script to run the program
requirements.txt         # Dependencies for the project
outputs/                 # Directory for saving results
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ErzhanAb/news-parser.git
   cd news-parser
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the main script:
```sh
python app.py
```

You will be prompted to enter the number of pages to parse and the number of top words to retrieve. The processed results will be saved in the `outputs/` directory.

## Output Files
- `outputs/links.json` – List of collected news page links
- `outputs/dataset.jsonl` – Cleaned dataset of words
- `outputs/top_words.csv` – CSV file with the most frequent words and their counts

## Requirements
- Python 3.x
- Required libraries (installed via `requirements.txt`):
  - requests
  - beautifulsoup4
  - numpy
  - pandas
  - tqdm

## License
This project is open-source and free to use for educational and research purposes.