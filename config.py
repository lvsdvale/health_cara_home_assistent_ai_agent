"""This file contains config files for api calls"""

import os

from dotenv import load_dotenv

load_dotenv()


openAI_api_key = os.getenv("OPENAI_API_KEY")
headers = {"Authorization": f"Bearer {openAI_api_key}"}
