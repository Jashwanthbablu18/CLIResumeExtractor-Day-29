# This imports 'Regular Expressions' module which is used for string searching and manipulation.
# And also imports 'read_pdf', 'read_docx' and 'read_txt' from FileReader module. 

import re
from FileReader import read_pdf, read_docx, read_txt

# This function takes an argument called resume_text which is string.
def extract_skills(resume_text):
    # These are pre-defined skills list, which we are searching in resume.(This can be expanded as per requirement)
    skills = ["Python", "JavaScript", "Java", "C++", "SQL", "HTML", "CSS", "React", "Node", "Django"]
    
    # Using list comprehension to extract found skills from resume text using the re.search() which checks for whole match of word, with
    # word boundaries(\b) and ignores cases like weather is it in Upper case or in Lower case it searches for that particular one skill 
    # in the resume_text.
    found_skills = [skill for skill in skills if re.search(r'\b' + skill + r'\b', resume_text, re.IGNORECASE)]
    
    # After founding skills, it returns the founded skills in resume
    return found_skills

# This function takes an argument called resume_text which is string.
def skill_count(resume_text):
    # Using dictionary comprehension to count occurrences of each skill
    skills = ["Python", "JavaScript", "Java", "C++", "SQL", "HTML", "CSS", "React", "Node", "Django"]
    count = {skill: resume_text.lower().count(skill.lower()) for skill in skills if skill.lower() in resume_text.lower()}
    
    # After that it return the count of skills
    return count

# This function determines which function have to be called based on file extension 
def extract_resume_text(file_path):
    """Extract text based on file type"""
    
    # If the file path ends with '.pdf' then it calls read_pdf() 
    if file_path.endswith('.pdf'):
        return read_pdf(file_path)
    
    # If the file path ends with '.docx' then it calls read_docx() 
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    
    # If the file path ends with '.txt' then it calls read_txt() 
    elif file_path.endswith('.txt'):
        return read_txt(file_path)
    
    # If user attaches unsupported file like; .png, .jpg, .jpeg, ... etc then it raises a value error and displays an user friendly msg.
    else:
        raise ValueError("Unsupported file type! Please provide a .pdf, .docx, or .txt file.")
