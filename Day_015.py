# Week 2
#Day 15 ------------------------------>>>>>>

# ---------- Short hand if-else statement ----------------

a=10
b=200

print("A") if a>b else print("B")

# Multiple statement in one line 

c=500
d=1000
 
print("C") if c>d else print("=") if a==b else print("D")

# ----------------- Virtual Environment -------------------

# Create a virtual environment
#   python -m venv myenv

# Activate the virtual environment (Linux/macOS)
#   source myenv/bin/activate

# Activate the virtual environment (Windows)
#   myenv\Scripts\activate.bat

# Deactivate the virtual environment
#   deactivate

# Output the list of installed packages and their versions to a file
#   pip freeze > requirements.txt

# Install the packages listed in the requirements.txt file
#   pip install -r requirements.txt