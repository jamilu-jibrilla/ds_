# This project is a toy project for training and quality assurance purposes

# day 9

DO NOT COMMIT OPENAI KEY TO REPO

I want you get use to the agent concept.

https://agentgpt.reworkd.ai/

https://logankilpatrick.medium.com/what-are-gpt-agents-a-deep-dive-into-the-ai-interface-of-the-future-3c376dcb0824

I want you make flask api to create agent process:

- Make agent to do the different departments in company.
- CFO Agent (we can upload company balance sheet, financial statements, etc.) to do embedding and CFO can answer any questions about it
- CMO Agent (collect a bunch of branding, marketing material online, etc.) to do embedding and CMO can answer any questions about it, predict what the next marketing campaign will be
- Recruiter Agent (list of resumes of candidates) can do embedding and and suggest best candidate for the roles need to be placed

## Task

- As CEO, you can ask question to CFO Agent, CMO Agent, Recruitment Agent and they can collectively give you answer
- You need to hire Product manager, ask all 3 for feedback and choose a candidate from recruiter list

Leverage openai, llama-index, gpt-index, PyPDF2
