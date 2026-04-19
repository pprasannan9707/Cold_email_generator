import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            if not url_input.strip():
                st.error("Please enter a valid URL.")
                return

            loader = WebBaseLoader(url_input)
            raw_data = loader.load().pop().page_content
            data = clean_text(raw_data)

            portfolio.load_portfolio()
            jobs = llm.extract_job(data)

            if not jobs:
                st.warning("No jobs were extracted from the page.")
                return

            for job in jobs:
                skills = job.get("skills", [])

                if isinstance(skills, list):
                    skills_query = ", ".join(skills)
                else:
                    skills_query = str(skills)

                links = portfolio.query_links(skills_query)
                email = llm.write_mail(job, links)

                st.subheader(job.get("role", "Job"))
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An error occurred while processing the URL: {e}")


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)