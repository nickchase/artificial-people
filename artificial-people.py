from openai import OpenAI
client = OpenAI()

lastMessage = ""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a social director, skilled in starting and maintaining conversations. You're also an expert in science fiction, fantasy, and horror, as well as pop culture, science, and technology."},
    {"role": "user", "content": "Start a conversation on a topic related to science fiction, fantasy, or horror."}
  ]
)

lastMessage = completion.choices[0].message.content
print(lastMessage)

def process_input(user_input):

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": lastMessage},
        {"role": "user", "content": user_input}
      ]
    )

    return completion.choices[0].message.content

def main():
    while True:
        try:
            user_input = input("Please enter your input (type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting program.")
                break
            result = process_input(user_input)
            print(result)
        except KeyboardInterrupt:
            print("\nExiting program.")
            break

if __name__ == "__main__":
    main()
