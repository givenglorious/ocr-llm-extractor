# doc2data

A lightweight pipeline that turns unstructured documents (receipts, invoices, notes) into structured data using OCR + LLM.

## About

`doc2data` reads a PDF or image of a receipt/invoice, extracts its text (either directly from native PDF text or via OCR for scanned/image files), then sends that text to an LLM to be converted into validated, structured JSON based on a defined schema.

Useful for digitizing receipt archives, automating expense tracking, or as a foundation for other document extraction use cases (invoices, ID cards, resumes, etc.).

## How It Works

```
File (PDF/JPG/PNG)
      |
      v
DataLoader   -> extract text (native PDF text / OCR via Tesseract)
      |
      v
extract_food_shop()  -> send text to LLM (Groq), forced to return JSON
                         matching the schema via tool calling
      |
      v
FoodShop (Pydantic)  -> validated data: shop name, date, item list, etc.
      |
      v
main.py  -> display results + calculate total
```

## Features

- Supports both native PDFs (direct text extraction) and scanned PDFs/images (automatic OCR fallback)
- Structured, validated output using [Pydantic](https://docs.pydantic.dev/)
- Uses LLM *tool calling* / *structured output* (via [Groq](https://groq.com/)) so results always match the schema, instead of free-form text
- Gracefully handles documents with missing fields (e.g. a receipt without a phone number or timestamp) without crashing

## Project Structure

```
.
├── main.py       # entry point, run from CLI
├── pipeline.py   # extract_food_shop() function -> calls the LLM
├── loader.py     # DataLoader class -> extracts text from PDF/images
├── schemas.py    # Pydantic data schemas (FoodShop, FoodItem)
└── README.md
```

## Installation

### 1. Install dependencies

```bash
pip install groq pydantic pymupdf pytesseract pillow
```

### 2. Install Tesseract OCR (needed to read scanned images/PDFs)

Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

After installing, set the path in `loader.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. Set up a Groq API key

Sign up for free at https://console.groq.com to get an API key, then set it as an environment variable:

```bash
# Windows PowerShell
$env:GROQ_API_KEY="your_key_here"
```

> ⚠️ Never hardcode your API key in the code or commit it to Git.

## Usage

```bash
python main.py path/to/receipt.jpg
```

Example output:

```
Nama Toko: Pelita Dunia Electric
No Telepon: None
Tanggal: 2018-08-01
Jam: None
Daftar Menu:
  - SUPREME NYM 3X2,5: 1 x 535000 = Rp.535,000.00
  - Kap Lampu: 1 x 484000 = Rp.484,000.00
```

## Data Schema

```python
class FoodItem(BaseModel):
    name: str
    price: int
    quantity: int

class FoodShop(BaseModel):
    nama_toko: str
    no_telepon: Optional[str] = None
    tanggal: date
    jam: Optional[time] = None
    daftar_menu: list[FoodItem]
```

## Roadmap

- [ ] Batch processing for multiple files at once
- [ ] Save results to CSV / SQLite
- [ ] Simple UI with Streamlit
- [ ] Extend schema to other document types (invoices, ID cards, resumes)

## Tech Stack

- Python
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [PyMuPDF](https://pymupdf.readthedocs.io/) — PDF reading
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) via `pytesseract` — image OCR
- [Groq API](https://groq.com/) — LLM inference for structured extraction
