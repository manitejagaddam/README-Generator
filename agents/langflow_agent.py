# import requests
# import json
# import os
# from dotenv import load_dotenv

# # Load the .env variables (if needed)
# load_dotenv()
# LANGFLOW_API = os.getenv("LANGFLOW_TOKEN")  # Make sure this is set in your .env

# # Load JSON file (your GitHub repo tree)
# with open("Data/data_cleaned.json", "r", encoding="utf-8") as f:
#     repo_json_data = json.load(f)

# # Replace this URL with your actual Langflow flow URL
# url = "https://api.langflow.astra.datastax.com/lf/a199f637-ca2a-4f7d-b8e0-40434ebff603/api/v1/run/f37f25fa-8ba1-4f2d-b2cf-924cec206dd9"

# # Construct the request payload
# payload = {
#     "input_value": json.dumps(repo_json_data, indent=2),  # Send the JSON as a pretty string
#     "output_type": "text",
#     "input_type": "text"
# }

# # Headers
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {LANGFLOW_API}"
# }

# # Send the request
# try:
#     response = requests.post(url, json=payload, headers=headers)
#     response.raise_for_status()

#     markdown_text = response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]

#     print("✅ Markdown received:\n")
#     # print(markdown_text)

#     # Save to README.md
#     with open("README.md", "w", encoding="utf-8") as f:
#         f.write(markdown_text)

#     print("✅ README.md written successfully!")

# except requests.exceptions.RequestException as e:
#     print(f"❌ API request failed: {e}")
# except ValueError as e:
#     print(f"❌ Response parsing failed: {e}")



# agents/langflow_agent.py

import requests
import json
import os
from dotenv import load_dotenv

def langflow_agent():
    load_dotenv()
    LANGFLOW_API = os.getenv("LANGFLOW_TOKEN")

    if not LANGFLOW_API:
        raise EnvironmentError("❌ LANGFLOW_TOKEN not found in .env file")

    # Load cleaned repo structure
    with open("Data/data_cleaned.json", "r", encoding="utf-8") as f:
        repo_json_data = json.load(f)

    url = "https://api.langflow.astra.datastax.com/lf/a199f637-ca2a-4f7d-b8e0-40434ebff603/api/v1/run/f37f25fa-8ba1-4f2d-b2cf-924cec206dd9"

    payload = {
        "input_value": json.dumps(repo_json_data, indent=2),
        "output_type": "text",
        "input_type": "text"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LANGFLOW_API}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        markdown_text = response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(markdown_text)

        print("✅ README.md written successfully!")

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
    except ValueError as e:
        print(f"❌ Response parsing failed: {e}")
