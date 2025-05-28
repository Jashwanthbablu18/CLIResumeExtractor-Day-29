# 🧩 Day 29 - Resume Scanner with File Handling

Welcome to Day 29 of my **#30DaysOfPythonChallenge**!

This project demonstrates the use of **List Comprehensions** and **Dictionary Comprehensions** in Python to extract and count specific skills from resumes in various formats.

## 📌 Topic

- 🔹 List Comprehensions  
- 🔹 Dictionary Comprehensions  
- 🔹 File Handling (PDF, DOCX, TXT)  
- 🔹 Text Extraction and Processing

## 🔧 What It Does

This project:

- 📄 Reads resume data from **PDF**, **DOCX**, and **TXT** files  
- 🧠 Extracts specified skills (e.g., Python, JavaScript, etc.) using **list comprehensions**  
- 📊 Counts occurrences of each skill using **dictionary comprehensions**

> ⚠️ Before running the code, make sure to install the required packages:

```bash
pip install PyPDF2 python-docx pdfplumber
```

## 🗂️ File Structure

```
Day-29/
├── ResumeScanner.py       # Main logic for scanning resumes and extracting skills
├── Day-29Code.py          # Driver script for running the scanner
├── FileReader.py          # Handles file reading based on file format
```

## 🧪 Sample Output

```
Extracted Skills: ['Python', 'JavaScript', 'Django', 'HTML', 'CSS', 'React', 'Node']
Skill Count: {'Python': 2, 'JavaScript': 1, 'Django': 2, 'HTML': 1, 'CSS': 1, 'React': 1, 'Node': 1}
```

## 💡 Concepts Practiced

- Efficient text parsing from multiple file types  
- Advanced Python data structures (lists & dictionaries)  
- Comprehension techniques for concise and readable code  
- Working with external libraries for document processing

## 💻 How to Run

1. Clone the repository or navigate to the `Day-29/` directory.  
2. Place some sample resumes (PDF, DOCX, TXT) in the working directory.  
3. Run the script:

```bash
python Day-29Code.py
```

## 🚀 Technologies Used

- Python 3.x  
- PyPDF2  
- pdfplumber  
- python-docx

## 📬 Feedback

Got suggestions or improvements? Feel free to open an issue or submit a pull request!

---

**© 2025 Jashwanth — #30DaysOfPythonChallenge**
