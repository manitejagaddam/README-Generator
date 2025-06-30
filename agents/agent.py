# import requests
# import json
# import os
# from dotenv import load_dotenv

# class ReadmeGeneratorAgent:
#     def __init__(self, prompt_path, repo_json_path, output_path="README.md"):
#         load_dotenv()
#         self.api_url = "https://api.groq.com/openai/v1/chat/completions"
#         self.api_key = os.getenv("GROQ_API_KEY")
#         self.model = "qwen-qwq-32b"
#         self.prompt_path = prompt_path
#         self.repo_json_path = repo_json_path
#         self.output_path = os.path.abspath(output_path)
#         self.headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }

#     def load_prompt(self):
#         with open(self.prompt_path, "r", encoding="utf-8") as f:
#             return f.read()

#     def load_repo_data(self):
#         with open(self.repo_json_path, "r") as f:
#             repo_data = json.load(f)
#         return json.dumps(repo_data.get("tree", []), indent=2)

#     def build_payload(self, prompt):
#         return {
#             "model": self.model,
#             "messages": [
#                 {"role": "user", "content": prompt}
#             ],
#             "temperature": 0.7,
#             "max_tokens": 2048
#         }

#     def generate_readme(self):
#         try:
#             print("📦 Loading prompt and repo data...")
#             prompt = self.load_prompt()
#             tree_json = self.load_repo_data()

#             # Optional: format prompt with tree_json if needed
#             # prompt = prompt.format(repo_json=tree_json)

#             payload = self.build_payload(prompt)
#             print("🚀 Sending request to Groq API...")
#             response = requests.post(self.api_url, headers=self.headers, json=payload)
#             response.raise_for_status()

#             print("🧠 Parsing response...")
#             content = response.json()['choices'][0]['message']['content']
#             with open(self.output_path, "w", encoding="utf-8") as f:
#                 f.write(content)

#             print(f"✅ README.md generated at: {self.output_path}")

#         except Exception as e:
#             print("❌ Failed to generate README:", e)


# if __name__ == "__main__":
#     agent = ReadmeGeneratorAgent(
#         prompt_path="prompts/promt2.txt",
#         repo_json_path="Data/data_cleaned.json",
#         output_path="README.md"
#     )
#     agent.generate_readme()




# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/a199f637-ca2a-4f7d-b8e0-40434ebff603/api/v1/run/f37f25fa-8ba1-4f2d-b2cf-924cec206dd9"  

# Request payload configuration
payload = {
    "input_value": "hello world!",  # The input value to be processed by the flow
    "output_type": "text",  # Specifies the expected output format
    "input_type": "text"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR_APPLICATION_TOKEN>"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    