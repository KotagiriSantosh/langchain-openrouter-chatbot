from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key="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",  # Replace with your key
    openai_api_base="https://openrouter.ai/api/v1"
)

while True:
    query = input("Ask a question to GPT Bot:\n")
    if query.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    try:
        result = chat_model.invoke(query)
        print("Bot:", result.content)  # ✅ cleaner output
    except Exception as e:
        print("⚠️ Error:", e)
