

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


# Generative AI Invoice Processor

An AI-powered system for processing and generating invoices using generative AI models.

\\\
## 📁 Project Structure

```text
LanGraph_Invoice_processor/
├── app.py                  # Main Streamlit application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── README.md
│
├── invoice_generator/      # Invoice generation module
│   └── ...                 # (templates, logic, etc.)
│
├── invoices/               # Uploaded invoice images
│
├── invoices.sqlite         # Main database (processed invoices)
│
├── Dataprep.py             # OCR & data extraction logic
├── Fileload.py             # File handling utilities
├── email_notify.py         # Email notification service
│
└── processed.json          # Temporary/intermediate processed data (optional)
```
\\\

### 🔵 Project Overview
![App Screenshot](docs/app-screenshot.png)
The **LangGraph Agent Invoice Processor** automates end-to-end invoice management using generative AI and smart orchestration. Built with a clean Streamlit UI, it transforms raw invoice images into structured, validated data—reducing manual effort and improving accuracy.

Key capabilities include:

- 📤 **Upload** invoice images directly through an intuitive web interface  
- 🔍 **Extract** text using **EasyOCR** (robust OCR for scanned documents)  
- 🧠 **Clean & normalize** unstructured text using **LangGraph-powered AI agents**  
- 📊 **Extract structured fields**: vendor, invoice number, date, total, currency, and line items  
- ✅ **Validate** data integrity and persist results in a local **SQLite database**  
- 📧 **Notify** recipients via email upon successful processing  
- 🌐 **Visualize** the full processing pipeline as an interactive, color-coded knowledge graph  

This solution bridges document intelligence and workflow automation—ideal for finance teams, small businesses, or anyone drowning in paper invoices! 💼📄


### 🔵 Features
|--------------------------------------------------------------------------|
| Feature                    | Description                                 |
|----------------------------|---------------------------------------------------------------------------|
| **Upload Invoice**         | Supports PNG, JPG, and JPEG image uploads                                   |
| **OCR**                    | Extracts raw text from invoice images using EasyOCR                      |
| **AI Cleaning & Extraction** | Uses LangGraph-powered AI agents to clean, normalize, and extract structured data (vendor, date, total, line items, etc.) |
| **Heuristic Fallback**     | Applies regex-based rules if AI extraction fails — ensuring robustness       |
| **Database**               | Stores validated invoice records in a local SQLite database                     |
| **Email Notification**     | Sends automated success notifications via Gmail                        |
| **Knowledge Graph**        | Visualizes the processing pipeline as a horizontal, pink-colored flow graph |
| **Dark/Light Theme**       | Modern UI with Streamlit’s default theme and optional dark mode support     |

### 🔧 Technology  Stack

- **Python 3.10+** – Core programming language  
- **Streamlit** – Interactive web interface for file upload and visualization  
- **EasyOCR** – Optical Character Recognition (OCR) for extracting text from invoice images  
- **LangGraph (EurAI)** – AI-powered pipeline for cleaning, normalizing, and extracting structured data  
- **SQLite3** – Lightweight local database for storing processed invoice records  
- **Graphviz** – Generates color-coded knowledge graph visualizations of the processing pipeline  
- **SMTP/Gmail** – Sends email notifications upon successful invoice processing  

### 🔷 Installation

Follow these 5 steps to set up the **LangGraph Agent Invoice Processor** locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/LanGraph_Invoice_processor.git
   cd LanGraph_Invoice_processor
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   ```
   - **Linux/macOS**:  
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:  
     ```powershell
     venv\Scripts\activate
     ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AI settings**  
   Open `config.py` and add your API key and model:
   ```python
   API_KEY = "your_api_key_here"
   MODEL = "gpt-4"  # or your preferred LangGraph-compatible model
   ```

5. **Set up email notifications**  
   - Enable **2-Factor Authentication** on your Gmail account  
   - Generate a **Google App Password** for `xxxxxx.yyyyyy@gmail.com`  
   - Paste the 16-character app password into `email_notify.py`:
     ```python
     EMAIL_PASSWORD = "your_app_password_here"  # Used for SMTP auth
     ```

---

### ▶️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

#### 🖥️ UI Workflow
- **📤 Upload Invoice**: Choose a PNG, JPG, or JPEG file  
- **📧 Email Notification**: Enter the recipient’s email address  
- **📨 Send Email**: Click the button to trigger a success notification  
- **🌐 Processing Pipeline**: View the horizontal, pink-colored knowledge graph showing each AI step  
- **🖼️ Invoice Preview**: Uploaded invoice displays on the side (~6 cm width)



### 📁 File Structure

```text
LangGraph-Invoice-Processor/
│
├── app.py                 # Main Streamlit UI application
├── Fileload.py            # Handles file uploads and SQLite database operations
├── DataPrep.py            # OCR (EasyOCR), LangGraph AI nodes, and pipeline logic
├── email_notify.py        # Sends email notifications via Gmail SMTP
│
├── invoices/              # Stores uploaded invoice images (PNG/JPG)
├── processed.json         # Tracks already-processed invoice files (idempotency)
├── invoice.sqlite         # Local SQLite database for structured invoice data
│
├── requirements.txt       # Python dependencies (Streamlit, LangGraph, EasyOCR, etc.)
└── README.md              # Project documentation
```

### 🔵 Knowledge Graph Nodes

The processing pipeline is modeled as a stateful graph with the following nodes:

- **WATCH** – Monitors the `invoices/` folder for newly uploaded invoice images  
- **OCR** – Performs optical character recognition (OCR) to extract raw text from the image using EasyOCR  
- **CLEAN** – Applies AI-powered normalization to fix typos, spacing, and layout artifacts in the extracted text  
- **EXTRACT** – Uses LangGraph agents to parse and output structured invoice data in JSON format (vendor, date, total, line items, etc.)  
- **VALIDATE** – Runs sanity checks and schema validation to ensure data integrity and completeness  
- **PERSIST** – Saves the validated invoice record into the local `invoice.sqlite` database  
- **NOTIFY** – Sends a success email notification to the recipient with processing details  



### 🖥️ UI Layout  
The Streamlit interface features:  
- A **horizontal pink knowledge graph** visualizing the processing pipeline  
- **Side-by-side layout**: invoice preview (~6 cm width) + interactive controls  
- Real-time status updates and email notification input  

---

### 🔮 Future Improvements  
Planned enhancements to expand functionality and robustness:  
- ✅ **PDF invoice support** – Extract text from PDF uploads (via PyMuPDF or pdf2image)  
- 🌍 **Multi-language OCR** – Support invoices in non-English languages (EasyOCR already enables this!)  
- ☁️ **Cloud database integration** – Enable multi-user access with PostgreSQL or Firebase  
- 🎯 **Fine-tuned AI extraction** – Custom models for complex or industry-specific invoices  
- 📧 **Dynamic email templates** – Include invoice summary, total, and download link in notifications  

---

### 📄 License  
Distributed under the **MIT License**.  
See [`LICENSE`](LICENSE) for full details.

---

### 📬 Contact  
**Author**: Shewan Dagne  
📧 **Email**: [shewan.dagne1@gmail.com](mailto:shewan.dagne1@gmail.com)  
🐙 **GitHub**: [@sdagne](https://github.com/sdagne)  

---

### ▶️ Quick Start  
```bash
git clone https://github.com/sdagne/GenAI-Public.git
cd GenAI-Public
```

