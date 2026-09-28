##################  AI SQL & ETL DATA AGENT ###########################
1. Project Structure:
This project is organized into separate modules for the SQL Analyst and ETL Analyst subagents, with dedicated folders for agents, database utilities, extraction, transformation, and output data. The structure keeps the code modular, clean, and easy to extend.
<img width="1774" height="887" alt="AI_Dat_Agent_Project_Structure" src="https://github.com/user-attachments/assets/77dcd22b-94bb-4253-9a03-101c5f20e52b" />

2. Project Code – VS Code:

Project Implementation:
The project is implemented in Python with separate components for the AI subagents, SQL safety validation, PostgreSQL interaction, and ETL operations. The modular design makes it easier to maintain and add new capabilities.

<img width="959" height="538" alt="Screenshot 2026-09-27 212001" src="https://github.com/user-attachments/assets/5ea0a2e5-c1a2-4e38-a82f-c43378531999" />
<img width="959" height="539" alt="Screenshot 2026-09-29 012139" src="https://github.com/user-attachments/assets/1993b731-3e83-4843-a5ab-320abd2dc25a" />

3. Claude Console – API Cost:
Claude API Usage:
Claude API is used as the LLM powering the AI agent and its subagents. The Claude Console screenshot shows the API usage and cost incurred while developing and testing this project, which was approximately $0.17.
<img width="959" height="555" alt="Screenshot 2026-09-29 012326" src="https://github.com/user-attachments/assets/2778dcc9-5094-4c02-84c7-29875110184d" />

4. PostgreSQL Database:
PostgreSQL is used by the SQL Analyst subagent to execute safe, read-only queries and retrieve database results. The ETL Analyst operates independently and does not interact with PostgreSQL.
<img width="955" height="558" alt="Screenshot 2026-09-29 012349" src="https://github.com/user-attachments/assets/8dbc6ef0-1654-4206-9a8c-60c2bf0ff754" />


