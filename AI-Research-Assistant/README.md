This is an advanced AI-powered tool that uses autonomous agents to conduct real-time research and content generation on any topic. Unlike traditional chatbots, it employs two separate AI agents working as a team.

 Key Features
Autonomous Research: The Senior Research Analyst agent uses the internet (DuckDuckGo) to gather the latest trends and data.

Smart Content Writing: The Tech Content Strategist agent converts research data into a structured, engaging, and professional blog post or report.

Sequential Workflow: The output of one agent becomes the input for another agent, simulating a real-world office workflow.

Powered by CrewAI: An industry-standard multi-agent framework is used for complex task management.

 Tech Stack
Language: Python

Framework: CrewAI

Orchestration: LangChain

LLM: OpenAI GPT-4 / Gemini (via LangChain)

Tools: DuckDuckGo Search API

How It Works
Input: User provides a topic (e.g., "AI in Healthcare 2026").

Research Phase: Agent 1 browses the internet and collects key points.

Drafting Phase: Agent 2 summarizes those points and writes a professionally marked-down report.

Output: You get a final, ready-to-publish research article.