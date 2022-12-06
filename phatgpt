"""
Python based interface for chatgpt.

Version
-------
0.0.1

Author
------
th3r00t
"""
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
while True:
    user_input = input("phatgpt > ")
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=user_input,
                                        temperature=0.9,
                                        max_tokens=4000,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0.6)
    if (response["choices"].__len__() > 1):
        print("There is more then one response availalbe\nShall I print them all?")
        user_input = input("y/n > ")
        if user_input  == "y":
            for i in response["choices"]:
                print(i.text)
                continue
    print(response["choices"][0].text)
