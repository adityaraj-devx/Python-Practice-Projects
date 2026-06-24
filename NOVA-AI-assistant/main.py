import warnings
warnings.filterwarnings("ignore")
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


def main():
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    print("Welcome! I'm NOVA, your AI assistant. Type 'quit' to exit\n")
    print("You can chat with me and ask me anything")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("\nGoodbye! 👋")
            break

        messages = [
            SystemMessage(
                content="""
                You are NOVA, a helpful AI assistant.
                Be concise, friendly, and accurate.
                """
            ),
            HumanMessage(content=user_input)
        ]

        try:
            response = model.invoke(messages)
            print(f"\nNOVA: {response.content}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()