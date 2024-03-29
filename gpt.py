from openai import OpenAI
import os
import sys
import io

message = sys.argv[1]

client = OpenAI(
    organization=os.environ["OPENAI_ORG_ID"]
)

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": message}],
    stream=True,
)

answer = ''

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        answer += chunk.choices[0].delta.content

with io.open("history.log", "a", encoding="utf-8") as log:
    log.write(f"{message}\n\n{answer}\n")
    log.write("─"*30 + "\n")
