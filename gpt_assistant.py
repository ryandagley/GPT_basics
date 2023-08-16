# This is a Python script for sending a prompt to the OpenAI API.
# This requires an API key to be placed in a separate file.
    
import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# location of the API key.
openai.api_key = open_file('openaiapikey.txt')
messages = [ {"role": "system", "content":
			"You are a friendly assistant."} ]


if __name__ == '__main__':
    print(f"I'm a friendly ChatGPT assistant.  Ask me for thinks like dinner suggestions.")
    while True:
        message = input("User: ")
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"ChatGPT assistant says: {reply}")
        messages.append({"role": "assistant", "content": reply})
