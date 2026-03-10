# payload.py
import os, subprocess, sqlite3

# Hardcoded cloud creds (secrets finding)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def run_command(cmd):
    os.system(cmd)                       # command injection
    subprocess.call(cmd, shell=True)     # command injection

def risky_eval(expr):
    return eval(expr)                    # arbitrary code execution

def fetch_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"  # SQL injection
    cur.execute(query)
    return cur.fetchall()

if __name__ == "__main__":
    user_cmd = input("cmd: ")
    run_command(user_cmd)
    print(risky_eval(input("code: ")))
    print(fetch_user("users.db", input("uid: ")))
