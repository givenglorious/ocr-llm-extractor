# ocr-llm-extractor

A pipeline that turns receipts (PDF/images) into structured, categorized data using OCR + an LLM, then exports the results to a categorized Excel report.

## Why This Project

Receipts and invoices pile up as loose paper or scattered photos, and manually copying their contents into a spreadsheet is slow and error-prone. This project was built to automate that process end-to-end: read a receipt image or PDF, understand its content with an LLM, validate the extracted data against a strict schema, and roll everything up into a categorized Excel report ready for expense tracking or bookkeeping.

It also started as a hands-on way to learn core AI engineering skills that don't require a GPU or model fine-tuning: OCR/text extraction, LLM structured output via tool calling, schema design with Pydantic, and batch data pipelines — skills directly transferable to real-world document-processing systems.

## How It Works

```
Folder of receipts (PDF/JPG/PNG)
            |
            v
   loader.py      -> extract text (native PDF text, or OCR via
                      Tesseract for scanned files/images)
            |
            v
   pipeline.py     -> send text to an LLM (Groq), forced via tool
                       calling to return JSON matching the schema
            |
            v
   schemas.py       -> validate the result into a typed object
                        (shop info + list of items, each with a category)
            |
            v
   batch.py / batch_main.py  -> repeat for every file in a folder,
                                 skipping files that fail without
                                 stopping the whole batch
            |
            v
   excel.py          -> export all extracted items into one Excel
                         file, split into separate sheets per category
```

## Features

- Handles both native PDFs (direct text extraction) and scanned PDFs/images (automatic OCR fallback via Tesseract)
- Structured, validated output using [Pydantic](https://docs.pydantic.dev/) — the LLM is forced to return data matching an exact schema instead of free-form text
- Gracefully handles missing fields (e.g. a receipt with no phone number or no timestamp) without crashing
- Batch-processes an entire folder of receipts in one run, logging which files succeeded or failed
- Exports results to Excel, automatically split into one sheet per item category

## Project Structure

```
.
├── main.py           # process a single receipt file end-to-end
├── batch.py          # process every receipt in a folder
├── batch_main.py      # entry point for running the full batch pipeline
├── loader.py           # extracts text from PDF/image files
├── pipeline.py          # sends text to the LLM and returns validated data
├── schemas.py            # Pydantic schemas (shop info + item, incl. category)
├── excel.py                # exports results to a categorized Excel file
├── data/                     # input receipts go here
├── result/                     # generated Excel output goes here
└── requirements.txt
```

## Installation

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/givenglorious/ocr-llm-extractor.git
cd ocr-llm-extractor
pip install -r requirements.txt
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

**Process a single receipt:**
```bash
python main.py data/receipt.jpg
```

**Process a whole folder and export to Excel:**
```bash
python batch_main.py
```
This reads every PDF/image inside `data/`, extracts and validates each one, and writes a categorized report to `result/hasil_ekstraksi.xlsx` — with a separate sheet for each item category (e.g. Food, Electronics, Stationery).

## Data Schema

```python
class FoodItem(BaseModel):
    name: str
    price: int
    quantity: int
    kategori: str  # e.g. "Makanan", "Elektronik", "Alat Tulis", "Lainnya"

class FoodShop(BaseModel):
    nama_toko: Optional[str] = None
    nama_pelanggan: Optional[str] = None
    deskripsi: Optional[str] = None
    no_telepon: Optional[str] = None
    tanggal: date
    jam: Optional[str] = None
    biaya_admin: Optional[int] = None
    daftar_menu: list[FoodItem]
```

## Tech Stack

- Python
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [PyMuPDF](https://pymupdf.readthedocs.io/) — PDF reading
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) via `pytesseract` — image OCR
- [Groq API](https://groq.com/) — LLM inference for structured extraction
- [pandas](https://pandas.pydata.org/) + [openpyxl](https://openpyxl.readthedocs.io/) — Excel export

---

*Status: complete. The pipeline reliably extracts, validates, and exports receipt data end to end, from a single file or a full batch folder.*
