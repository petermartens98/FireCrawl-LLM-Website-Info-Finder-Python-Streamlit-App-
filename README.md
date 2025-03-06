# FireCrawl LLM Website Info Finder Python Streamlit App

A Streamlit-based web application that leverages Firecrawl to scrape multiple websites using a user-defined schema. Input your API key, specify the data fields you want to extract (e.g., strings, numbers, booleans), list the URLs, and retrieve structured JSON results—all through an intuitive interface.

## Features
- **Dynamic Schema Creation**: Define custom extraction fields on the fly.
- **Multi-URL Scraping**: Scrape multiple websites with a single schema in one operation.
- **Interactive UI**: Real-time schema preview and easy input via Streamlit.
- **Error Handling**: Per-URL error reporting ensures robust scraping.
- **JSON Output**: Structured results for easy data processing.

## Requirements
- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [Firecrawl](https://github.com/mendableai/firecrawl) (Python SDK)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/firecrawl-website-scraper.git
   cd firecrawl-website-scraper
   ```
2. Install dependencies:
   ```bash
   pip install streamlit firecrawl-py pydantic
   ```
3. Ensure you have a valid Firecrawl API key (sign up at [Firecrawl](https://www.firecrawl.dev/) if needed).

## Usage
1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to `http://localhost:8501`.
3. Enter your Firecrawl API key.
4. Define your schema by adding field names and types (e.g., "title" as String, "price" as Number).
5. Click "Update Schema" to save your schema.
6. Enter URLs (one per line) in the text area.
7. Click "Scrape URLs" to extract data.
8. View the JSON results, with each URL’s data or errors displayed.

## Example
**Input URLs:**
```
https://example.com
https://anothersite.com
```

**Schema:**
- title: String
- description: String

**Output:**
```json
{
    "https://example.com": {
        "title": "Example Site",
        "description": "This is an example"
    },
    "https://anothersite.com": {
        "error": "404 Not Found"
    }
}
```

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests. Contributions to enhance functionality (e.g., more field types, export options) are welcome!

## Screenshot
![Screenshot 2025-03-06 090354](https://github.com/user-attachments/assets/480cf4ec-63ae-4bf1-b24d-8ed0fc1dbd77)
