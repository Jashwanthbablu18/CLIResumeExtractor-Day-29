# Day 29 - Resume Scanner.
# topic - Comprehensions.

# This imports extract_skills, skill_count and extract_resume_text from ResumeScanner 
from ResumeScanner import extract_skills, skill_count, extract_resume_text

# main
def main():
    # Example file path. You can replace it with your own path but file must support '.pdf' / '.docx' / '.txt' and make sure that file
    # is in correct path. 
    file_path = "C:/Users/student/Desktop/SampleResume.pdf"  
    
    # A try-except block is used to handle exceptions
    try:
        # Extract resume text from the file, by passing the file path to extract_resume_text() which extracts text in resume into a variable.
        resume_text = extract_resume_text(file_path)
        # If the resume file is empty(not found any text) then this msg will be displayed and exits the function here itself.
        if not resume_text:
            print("No text found in the resume.")
            return
        
        # Extract skills using list comprehension, by passing resume text into extract_skills()
        found_skills = extract_skills(resume_text)
        # And then displays skills which've founded
        print("Extracted Skills:")
        print(found_skills)

        # Count occurrences of each skill using dictionary comprehension, by passing resume text into skill_count()
        skill_count_data = skill_count(resume_text)
        # And then displays skills count 
        print("\nSkill Count:")
        print(skill_count_data)
    
    # If any exception occurs that will be managed by this statement
    except Exception as e:
        print(f"Error: {e}")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
