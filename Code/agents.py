from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover the Latest Updates and Upgrades in the given {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer=Agent(
    role="Senior Writer",
    goal='Write a Comprehensive Article on the Latest Updates and Upgrades',
    verbose=True,
    memory=True,
    backstory=(
        "With a passion for storytelling, you're dedicated to"
        "communicating the latest news and trends in a way that captivates"
        "and informs your audience"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
