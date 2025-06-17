#pip install PyPDF2

import tkinter as tk
from tkinter import filedialog, messagebox
import re
import PyPDF2

# Job keywords to match against
job_keywords = ["python", "html", "css", "javascript", "mysql", "communication", "teamwork", "problem-solving"]

# Extract text from uploaded PDF
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text.lower()
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't read file: {e}")
        return ""

# Analyze and match keywords
def analyze_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    resume_text = extract_text_from_pdf(file_path)
    if not resume_text:
        return

    matched = [kw for kw in job_keywords if re.search(rf'\b{kw}\b', resume_text)]
    score = len(matched) / len(job_keywords) * 100

    result = f"✅ Match: {len(matched)} / {len(job_keywords)} keywords\n"
    result += f"🎯 Match Percentage: {score:.2f}%\n\n"
    result += "Matched Keywords: " + ", ".join(matched) + "\n"

    missing = set(job_keywords) - set(matched)
    if missing:
        result += "\n🔍 Improve by adding: " + ", ".join(missing)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# GUI Setup
root = tk.Tk()
root.title("Resume Analyzer")
root.geometry("500x400")

tk.Label(root, text="Resume Analyzer", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(root, text="Upload Resume (PDF)", command=analyze_resume, font=("Arial", 12)).pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, width=60, height=15, font=("Courier", 10))
result_text.pack(padx=10, pady=10)

root.mainloop()
