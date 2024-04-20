import openai

openai.api_key = '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'

def gera_texto(texto):
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = texto,
        max_tokens = 150,
        n = 5,
        stop = None,
        temperature = 0.8,
        )
    return response.choices[0].text.strip()

def main():
    print('\nBem Vindo ao Jorge-Bot')
    print("Digite 'sair' para deixar o Jorge em paz")

    while True:
        user_message = input("\nVocê: ")

        if user_message.lower() == 'sair':
            break

        prompt = f"\nUsuário: {user_message}\nJorge:"
        jorge_response = gera_texto(prompt)
        print(f"\nChatbot: {jorge_response}")

if __name__ == '__main__':
    main()