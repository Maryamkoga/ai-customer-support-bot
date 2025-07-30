from qa_chain import setup_chain, ask_bot

def main():
    db = setup_chain()
    print("🤖 AI Support Bot ready! Ask your onboarding or support questions.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        answer = ask_bot(db, user_input)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    main()


