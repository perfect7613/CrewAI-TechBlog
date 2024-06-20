from crewai import Task
from tools import tool
from agents import news_researcher, news_writer


research_task = Task(
    description=(
        "Find the latest advancements and updates in the {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your Final Report should clearly articulate the key points."
        "Its market opportunities and potential impact in the industry."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest advancements and updates in {topic}.',
    tools=[tool],
    agent=news_researcher,
)


write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Your article should be engaging, informative, and well-structured."
        "Include key details, potential impact, and future implications."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)