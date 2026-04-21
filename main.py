import ollama
from tools.file_reader import read_file

file_content = read_file("attacks/malicious.txt")

response = ollama.chat(
    model='llama3',
    messages=[
        {"role": "system", "content": "You are an AI agent."},
        {"role": "user", "content": f"Summarize this:\n{file_content}"}
    ]
)

print(response['message']['content'])