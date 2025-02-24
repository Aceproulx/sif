# SIF - Snapshot Inspection & File Finder

SIF (**Snapshot Inspection & File Finder**) is a tool designed to retrieve historical URLs from the Wayback Machine and check for available snapshots of files with specific extensions. It helps security researchers and penetration testers discover potentially sensitive files that have been archived.

## Features
- Fetches URLs from the Wayback Machine for a given domain.
- Checks for available snapshots of the extracted URLs.
- Identifies files with extensions like `.xls`, `.xml`, `.json`, `.pdf`, `.sql`, `.docx`, `.zip`, `.tar.gz`, `.log`, `.db`, etc.
- Displays snapshot availability and provides direct archive links.
- Supports scanning a single domain or a list of domains from a file.

## Installation
Ensure you have **Python 3** installed. Then, install the required dependencies:

```bash
pip install requests
```
Clone this repository

```bash
git clone https://github.com/Aceproulx/sif.git
```

## Usage
Run **SIF** using the command line:

### **1. Search for a single domain**
```bash
python sif.py -d example.com
```

### **2. Search for multiple domains from a file**
```bash
python sif.py -list domains.txt
```
- `domains.txt` should contain one domain per line.

### **3. Interrupt Handling**
You can stop execution at any time using `CTRL + C`. The script handles interruptions gracefully.

## Example Output
```
Fetching URLs from Wayback Machine for example.com...
Checking for matching files...
📁 https://example.com/backup.sql ✅ (Snapshot Available) 🔗 https://web.archive.org/web/20220101010101/https://example.com/backup.sql
📁 https://example.com/secret.json ❌ (No Snapshot)
Done!
```

## Notes
- The tool relies on the **Wayback Machine** for historical data; results may vary.
- It is intended for **educational** and **security research** purposes only.

## Author
👑 Created by **Mike Masanga**
