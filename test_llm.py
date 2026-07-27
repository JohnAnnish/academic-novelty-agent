import os
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    if os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        print("Found OPENAI_API_KEY. Testing connection...")
        llm = ChatOpenAI(model="gpt-4o-mini")
    elif os.getenv("GOOGLE_API_KEY"):
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("Found GOOGLE_API_KEY. Testing connection...")
        llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    else:
        print("Error: No API key found in .env file.")
        print("Please open the .env file and add your OPENAI_API_KEY or GOOGLE_API_KEY.")
        return

    try:
        print("Sending prompt to LLM...")
        response = llm.invoke("Hello, are you ready to act as an Academic Novelty Checker?")
        print("\n--- LLM Response ---")
        print(response.content)
        print("--------------------")
        print("\nConnection successful! You are ready for Phase 2.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_connection()
