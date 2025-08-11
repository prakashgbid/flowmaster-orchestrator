"""Setup configuration for langgraph-orchestrator."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="langgraph-orchestrator",
    version="1.0.0",
    author="OSA Contributors",
    author_email="osa@omnimind.ai",
    description="Production-ready multi-agent orchestration using LangGraph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prakashgbid/langgraph-orchestrator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "langgraph>=0.0.20",
        "langchain>=0.1.0",
        "langchain-core>=0.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "langgraph-orchestrator=langgraph_orchestrator.cli:main",
        ],
    },
    keywords="agents orchestration langgraph langchain multi-agent supervisor swarm",
    project_urls={
        "Bug Reports": "https://github.com/prakashgbid/langgraph-orchestrator/issues",
        "Source": "https://github.com/prakashgbid/langgraph-orchestrator",
        "Documentation": "https://langgraph-orchestrator.readthedocs.io",
    },
)