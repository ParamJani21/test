# vulnerable_code.py - DO NOT USaaaaaaaaaaaaaaaaaaaaE IN PRODUCTION!

import os
import subprocess

# SAST: Command Injection
def run_command(user_input):
    os.system(f"echo {user_input}")  # Dangerous!
    
# SAST: SQL Injection  
def get_user(db, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Dangerous!
    return db.execute(query)

# SAST: Hardcoded Secret
API_KEY = "sk-live-1234567890abcdef"
AWS_SECRET = "AKIAIOSFODsssssssssssssssNN7EXAMPLE"

# SAST: Eval/Exec
def dangerous_eval(code):
    return eval(code)  # Dangerous!
