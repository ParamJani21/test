import { exec } from "child_process";

class TypeScriptVuln {
    public runCmd(input: string): void {
        // 1. Command Injection (High confidence pattern)
        const cmd = "ls -la " + input;
        exec(cmd, (err, stdout) => {
            console.log(stdout);
        });
    }

    public dangerousEval(code: string): void {
        // 2. Eval usage (Standard security finding)
        eval(code);
    }

    public hardcodedKey(): string {
        // 3. Hardcoded Secret (Generic pattern)
        const API_KEY = "AIzaSyB-fake-key-12345";
        return API_KEY;
    }
}
