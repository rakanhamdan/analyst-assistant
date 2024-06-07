# Business Analyst Assistant with Llama3

This project was  uses the Llama3 8B large language model (LLM) to help business and data analysts understand their data by deriving insights from it. The model also suggests graphs and column relationships to use when building dashboards.
It also optionally cleans the dataset for the user. The project leverages LangChain and Ollama to set up and run the model, and Streamlit to upload the files and interact with the model.

## Overview

The Business Analyst Assistant:
- Processes CSV files to extract insights.
- Recommends relationships between columns.
- Suggests potential graphs for data visualization.
- Optionally cleans the dataset

## Setup

- **Llama3 Model**: You can download the Llama3 8B model from the [Ollama website](https://www.ollama.com/).
- **Run the Streamlit App**: Run the `streamlit run llama3.py` command to open the Streamlit intereface and start using the app.
