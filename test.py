# hackme.py - Security test file
import os
import subprocess

# Command injection vulnerability
user_input = input("Enter command: ")
os.system(user_input)

# Hardcoded AWS credentials  
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# SQL injection
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return query

# Dangerous eval
eval(input("Code: "))
