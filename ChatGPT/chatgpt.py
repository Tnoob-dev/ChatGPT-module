import requests


class ChatGPT:
    
    def __init__(self, question: str) -> None:
        self.question = question
        pass

    def chatgpt(self):
        """
        This function returns output of your question
        """
        url = "https://chatgpt-api.shn.hk/v1/"

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{
                        "role": "user", 
                        "content": self.question
                        }]
        }

        header = {'Content-Type': 'application/json'}

        try:
            r = requests.post(url, headers=header, json=payload)
        except Exception as e:
            print(f"Something happens -> {e}")

        return r.json()['choices'][0]['message']['content']
