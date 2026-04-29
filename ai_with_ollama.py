import requests


def LLM(prompt):
    response= requests.post("http://localhost:11434/api/generate", json={"model":"phi3.5", "prompt": prompt, "stream":False})
    result = response.json()
    message = result.get("response", "")
    return message


test_prompt = "What is the tallest mountain in the world"
print(LLM(test_prompt))
