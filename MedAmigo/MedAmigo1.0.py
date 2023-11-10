import openai

# Your OpenAI API key
api_key = ''

openai.api_key = api_key

def ask_mediman(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=50
    )
    return response.choices[0].text.strip()

print("Welcome to MediMan! How can I assist you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("MediMan: Goodbye! Take care.")
        break

    prompt = f"You: {user_input}\nMediMan:"

    mediman_response = ask_mediman(prompt)
    print("MediMan:", mediman_response)
