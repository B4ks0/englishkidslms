import openai

# === CLIENT 1: OpenRouter ===
router_client = openai.OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# === CLIENT 2: OpenAI langsung ===
openai_client = openai.OpenAI(
    api_key="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"
)

def ask_chat(client, user_input):
    return client.chat.completions.create(
        model="gpt-4o",  # Sama untuk OpenRouter dan OpenAI sekarang
        messages=[
            {"role": "system", "content": "Kamu adalah chatbot pintar dan ramah."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=500
    )

def chatbot():
    print("🤖 Chatbot Aktif! (Ketik 'exit' untuk keluar)")
    while True:
        user_input = input("Kamu: ")
        if user_input.lower() == "exit":
            break

        # Coba pakai OpenRouter dulu
        try:
            response = ask_chat(router_client, user_input)
            print("Bot (OpenRouter):", response.choices[0].message.content)

        except Exception as e:
            print("⚠️ Gagal pakai OpenRouter, coba pakai OpenAI langsung...")
            try:
                response = ask_chat(openai_client, user_input)
                print("Bot (OpenAI):", response.choices[0].message.content)
            except Exception as e2:
                print("❌ Gagal dua-duanya:", e2)

chatbot()
