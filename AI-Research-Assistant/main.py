import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Search Tool Setup
search_tool = DuckDuckGoSearchRun()

# 2. Agents Define Karein
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in {topic}',
  backstory="""You are an expert at a technology news outlet. 
  Your mission is to find the latest and most relevant information 
  about the given topic.""",
  tools=[search_tool],
  verbose=True,
  allow_delegation=False
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft a compelling content piece on {topic}',
  backstory="""You are a renowned Content Strategist, known for 
  your insightful and engaging articles. You transform complex 
  concepts into easy-to-understand narratives.""",
  verbose=True,
  allow_delegation=True
)

# 3. Tasks Define Karein
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest trends in {topic}.
  Identify key players, recent breakthroughs, and potential future impacts.""",
  expected_output="A full report on the latest AI trends in 2026.",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog post 
  that highlights the most significant developments. 
  The post should be informative yet accessible, catering to a tech-savvy audience.
  Make it look like a professional GitHub README or Medium post.""",
  expected_output="A 4 paragraph blog post formatted in markdown.",
  agent=writer
)

# 4. Crew (Team) Banaiye
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=True, 
  process=Process.sequential # Pehle research hoga, phir writing
)

# 5. Execution
print("### AI Research Assistant starting... ###")
result = crew.kickoff(inputs={'topic': 'Future of Generative AI in 2026'})

print("\n\n########################")
print("## FINAL OUTPUT ##")
print("########################\n")
print(result)