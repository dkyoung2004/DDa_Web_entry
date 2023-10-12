import openai
openai.api_key = "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"

answer = openai.Completion.create(
  model="text-davinci-003",
  prompt="write short story about school",
  max_tokens=500,
  temperature=1 #2는 엄청 창의적 0은 완전 보수적
)

print(answer.choices[0].text)

