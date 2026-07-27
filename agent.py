import os
from dotenv import load_dotenv

try:
    from langchain_openai import ChatOpenAI
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.agents import create_agent
    from langchain_core.messages import HumanMessage
    from tools import search_google_scholar
except ImportError as e:
    print(f"Dependencies not found. Error details: {e}")
    exit(1)

load_dotenv()

def get_llm():
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(model="gpt-4o-mini", temperature=0, max_retries=5)
    elif os.getenv("GOOGLE_API_KEY"):
        return ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0, max_retries=5)
    else:
        raise ValueError("No API key found in .env file. Please add OPENAI_API_KEY or GOOGLE_API_KEY.")

def run_agent(research_proposal: str):
    llm = get_llm()
    
    # Define our tools (the agent's "senses")
    tools = [search_google_scholar]
    
    # Create the system prompt
    system_prompt = """You are an expert academic researcher and peer reviewer. 
Your job is to act as an Academic Novelty Checker.
The user will provide a proposed research pipeline or abstract.
1. Extract the core methodologies, algorithms, dataset, and problem domain.
2. Use the search_google_scholar tool to find related academic papers. You may need to search multiple times.
3. Analyze the returned abstracts. Compare them against the user's proposal.
4. Write a detailed Markdown "Novelty Report" explaining:
   - What similar research exists.
   - What the user's novel contribution is.
   - Any recommendations for their paper.
Always cite the titles and authors of the papers you found."""
    
    # Construct the tool calling agent using LangChain v1.x
    agent_executor = create_agent(llm, tools=tools, system_prompt=system_prompt)
    
    print("\n[Agent is thinking and searching Google Scholar. This may take a minute...]\n")
    
    # Run the agent
    response = agent_executor.invoke({"messages": [HumanMessage(content=research_proposal)]})
    
    # Get the last message from the agent
    final_output = response["messages"][-1].content
    return final_output

if __name__ == "__main__":
    print("Welcome to the Academic Novelty Checker Agent!")
    proposal = input("\nPlease paste your proposed research abstract or pipeline here:\n> ")
    
    if proposal.strip():
        try:
            report = run_agent(proposal)
            print("\n================ NOVELTY REPORT ================\n")
            print(report)
            print("\n================================================\n")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
    else:
        print("No input provided. Exiting.")
