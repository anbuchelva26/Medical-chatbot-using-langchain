from setuptools import setup, find_packages

setup(
    name="Medical-Chatbot",  # Your project/package name
    version="0.1.0",
    author="Anbuchelvan M",
    author_email="anbuchelvann2006@gmail.com",
    description="Medical chatbot using LangChain, Flask, Pinecone, and OpenAI",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    url="https://github.com/yourusername/Medical-chatbot-using-langchain",
    packages=find_packages(),  # Automatically find packages in your folder
    install_requires=[

    ]
    )