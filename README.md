<p align="center">
  <img src="https://raw.githubusercontent.com/givenglorious/ocr-llm-extractor/main/assets/banner.png" alt="ocr-llm-extractor" width="100%" />
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44d" alt="License: MIT"></a>
  <a href="https://github.com/givenglorious/ocr-llm-extractor/releases"><img src="https://img.shields.io/github/v/release/givenglorious/ocr-llm-extractor?label=version&color=1f6feb" alt="Version"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/OCR-Tesseract-green" alt="Tesseract OCR">
  <img src="https://img.shields.io/badge/LLM-Groq-orange" alt="Groq">
</p>

# OCR + LLM Extractor

> **Turn receipt photos and PDFs into structured Excel data.**
>
> An end-to-end document processing pipeline that combines OCR, LLM structured extraction, schema validation, and batch processing to automatically convert unstructured receipts into categorized data.

---

## What it does

* **Reads receipts and invoices** from PDF, JPG, and PNG files
* **Extracts text automatically** using native PDF extraction or Tesseract OCR
* **Uses an LLM** to understand and structure the extracted information
* **Validates the output** with Pydantic schemas
* **Processes multiple files** in a single batch
* **Categorizes extracted items** automatically
* **Exports structured results** directly to Excel
* **Continues processing** even when individual files fail

---

## How it works

```text
Receipt PDF / Image
        │
        ▼
   Text Extraction
   ├── Native PDF text
   └── Tesseract OCR
        │
        ▼
     Groq LLM
        │
        ▼
 Structured Output
        │
        ▼
 Pydantic Validation
        │
        ▼
 Batch Processing
        │
        ▼
 Categorized Excel
```

The goal is simple:

**Unstructured document → structured business data**

---

## Example

### Input

```text
receipt.jpg
receipt_02.pdf
receipt_03.png
```

### Output

```text
result/
└── hasil_ekstraksi.xlsx
```

The generated Excel file contains structured receipt information and separates items into categories such as:

```text
Food
Electronics
Stationery
Others
```

---

## Tech Stack

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Core application            |
| Tesseract OCR | Text extraction from images |
| PyMuPDF       | Native PDF text extraction  |
| Groq          | LLM inference               |
| Pydantic      | Structured data validation  |
| Pandas        | Data processing             |
| OpenPyXL      | Excel generation            |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/givenglorious/ocr-llm-extractor.git
cd ocr-llm-extractor
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Tesseract is required for scanned PDFs and image-based receipts.

After installation, configure the executable path in `loader.py`:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

### 4. Configure the Groq API key

Set your API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY="your_api_key"
```

> Never hardcode API keys or commit them to Git.

---

## Usage

### Process a single receipt

```bash
python main.py data/receipt.jpg
```

### Process an entire folder

```bash
python batch_main.py
```

The batch pipeline reads supported files from `data/` and generates:

```text
result/hasil_ekstraksi.xlsx
```

---

## Project Structure

```text
ocr-llm-extractor/
│
├── data/
│   └── receipt files
│
├── result/
│   └── generated Excel files
│
├── loader.py
│   └── PDF/image text extraction
│
├── pipeline.py
│   └── LLM extraction pipeline
│
├── schemas.py
│   └── Pydantic data schemas
│
├── excel.py
│   └── Excel export
│
├── batch.py
│   └── Batch processing logic
│
├── batch_main.py
│   └── Batch entry point
│
├── main.py
│   └── Single-file entry point
│
├── requirements.txt
└── README.md
```

---

## Data Flow

```text
Input Document
      │
      ▼
┌───────────────┐
│ Text Extractor│
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Groq LLM    │
│ Structured    │
│   Extraction  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Pydantic    │
│   Validation  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Categorization│
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     Excel     │
│    Export     │
└───────────────┘
```

---

## Why this project?

Manual receipt processing is repetitive and error-prone.

This project explores how modern AI engineering techniques can be combined to build a practical document-processing system:

* OCR for unstructured visual data
* LLMs for semantic extraction
* Pydantic for deterministic validation
* Batch pipelines for scalable processing
* Excel generation for practical business output

The project focuses on the **engineering pipeline**, not just calling an LLM.

---

## Limitations

* OCR quality depends on image quality
* LLM extraction may require schema or prompt adjustments for different receipt formats
* Tesseract must be installed separately
* The current schema is optimized for receipt-style documents

---

## Roadmap

* [ ] Add confidence scoring for extracted fields
* [ ] Improve OCR preprocessing
* [ ] Support more document formats
* [ ] Add configurable extraction schemas
* [ ] Add automated tests
* [ ] Add CLI configuration
* [ ] Add web interface
* [ ] Add evaluation dataset and extraction accuracy metrics

---

## License

MIT License — see [LICENSE](LICENSE).

---

<p align="center">
  Built by <a href="https://github.com/givenglorious">Given Glorious</a>
</p>
