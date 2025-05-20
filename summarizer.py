# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)
import subprocess
import shutil

def summarize_with_ollama(text, model_name="llama2"):
    if shutil.which("ollama") is None:
        return "⚠️ Ollama not found. Please install it and make sure it's in your system PATH."

    prompt = f"Summarize this resume in 3-5 bullet points:\n{text}"
    result = subprocess.run(
        ["ollama", "run", model_name],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode()
