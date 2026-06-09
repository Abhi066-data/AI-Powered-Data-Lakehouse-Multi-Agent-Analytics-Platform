# AI-Powered Data Lakehouse & Multi-Agent Analytics Platform

## Overview

An end-to-end cloud analytics platform built using AWS and Local LLMs.

The platform allows users to ask business questions in natural language, automatically converts them into Athena SQL queries, executes them on AWS Athena, and generates business insights using AI agents.

## Architecture

Raw Data → AWS S3 → AWS Glue → AWS Athena → SQL Agent → Analytics Agent → Streamlit Dashboard

## Features

* AWS S3 Data Lake
* AWS Glue Data Catalog
* AWS Athena Query Engine
* Natural Language to SQL using Llama 3 (Ollama)
* AI Business Insights Generation
* Interactive Streamlit Dashboard
* Multi-Agent Architecture

## Tech Stack

* Python
* AWS S3
* AWS Glue
* AWS Athena
* Ollama
* Llama 3
* Streamlit
* Pandas

## Sample Questions

* How many delivered orders do we have?
* Count all customers
* Show order status distribution

## Results

* Processed 99,000+ customer records
* Generated SQL automatically from natural language
* Produced AI-generated business insights

## Future Improvements

* Report Agent
* Multi-Agent Orchestrator
* Real-time Data Pipeline
* RAG-based Knowledge Agent
