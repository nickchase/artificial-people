from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a social director, skilled in starting and maintaining conversations. You're also an expert in science fiction, fantasy, and horror, as well as pop culture, science, and technology."},
    {"role": "user", "content": "Start a conversation on a topic related to science fiction, fantasy, or horror."}
  ]
)

print(completion.choices[0].message.content)
