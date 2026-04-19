📧 Cold Mail Generator
An AI-powered cold email generator that scrapes job postings from career pages and automatically crafts personalized outreach emails — built with LangChain, Groq (LLaMA 3.3), ChromaDB, and Streamlit.
🚀 How It Works

Paste a job URL from any company's careers page
The app scrapes and cleans the page content
LLaMA 3.3 (via Groq) extracts structured job details — role, skills, experience, and description
ChromaDB performs a semantic search over your portfolio to find the most relevant work samples
The LLM drafts a personalized cold email from BumbleBee's BDE, Mohan, matching the job's requirements with portfolio links

🛠️ Tech Stack

Groq — Fast LLM inference with LLaMA 3.3 70B
LangChain — Prompt chaining and output parsing
ChromaDB — Vector database for portfolio retrieval
Streamlit — Interactive web UI
WebBaseLoader — Web scraping

📁 Project Structure
├── main.py          # Streamlit app entry point
├── chains.py        # LangChain chains for job extraction & email generation
├── portfolio.py     # ChromaDB portfolio loader and semantic search
├── utils.py         # Text cleaning utilities
└── resources/
    └── Portfolio.csv  # Your portfolio data (tech_stack, employee_link)
⚙️ Setup
bashpip install -r requirements.txt
Create a .env file:
Groq_API_KEY=your_groq_api_key_here
Run the app:
bashstreamlit run main.py
💡 Use Case
Built for consulting firms and freelancers who want to automate personalized outreach to companies actively hiring — matching their open roles with your team's proven expertise.
