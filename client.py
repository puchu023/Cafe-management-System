import google.generativeai as genai
client = genai(
    api_key="AIzaSyCLHWknO1f2x3kQfoV45McI5MN5YOUESN4",
)
completion = client.chat.completions.create(
    model="gemini-pro",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "What is coding?"}
    ]
)
print(completion.choices[0].message.content)