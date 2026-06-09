# 🚀 AI-Powered Data Lakehouse & Multi-Agent Analytics Platform

## 📌 Overview

An end-to-end cloud-native analytics platform that enables business users to query enterprise data using natural language.

The platform combines AWS Data Engineering services with Local LLM-powered AI Agents to automatically:

* Convert natural language into SQL
* Execute queries on AWS Athena
* Generate business insights
* Create executive-level analytics reports

This project simulates a real-world enterprise analytics system used by data-driven organizations.

---

# 🎯 Problem Statement

Business users often struggle to write SQL queries and analyze large datasets.

This platform solves that problem by allowing users to ask questions such as:

> How many delivered orders do we have?

> Which order status contributes the highest volume?

> What is the total customer base?

The system automatically generates SQL, retrieves data, and explains the results in business language.

---

# 🏗️ System Architecture

```text
                    ┌───────────────────┐
                    │ Natural Language  │
                    │ User Question     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ SQL Agent         │
                    │ (Llama 3/Ollama)  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ AWS Athena        │
                    │ Query Engine      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Analytics Agent   │
                    │ Business Insights │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Report Agent      │
                    │ Executive Summary │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Streamlit UI      │
                    └───────────────────┘
```

---

# ☁️ AWS Architecture

```text
Raw CSV Files
      │
      ▼
AWS S3 Data Lake
      │
      ▼
AWS Glue Catalog
      │
      ▼
AWS Athena
      │
      ▼
AI Analytics Layer
      │
      ▼
Streamlit Dashboard
```

---

# 🧠 Multi-Agent System

### 1. SQL Agent

Converts natural language questions into Athena SQL queries.

Example:

Question:

How many delivered orders do we have?

Generated SQL:

SELECT COUNT(*) AS delivered_orders
FROM orders
WHERE LOWER(col2)='delivered';

---

### 2. Analytics Agent

Analyzes query outputs and generates business insights.

Example Output:

* Strong fulfillment performance
* High customer satisfaction indicators
* Low cancellation rate

---

### 3. Report Agent

Creates executive-level reports containing:

* KPIs
* Business Impact
* Recommendations
* Growth Opportunities

---

# 📊 Dataset

Brazilian E-Commerce Public Dataset

Processed Records:

| Dataset   | Records |
| --------- | ------: |
| Customers |  99,441 |
| Orders    |  99,442 |
| Products  | 32,951+ |

---

# ⚙️ Tech Stack

### Cloud

* AWS S3
* AWS Glue
* AWS Athena

### AI / ML

* Ollama
* Llama 3
* Prompt Engineering

### Backend

* Python
* Pandas
* PyAthena
* Requests

### Frontend

* Streamlit

### DevOps

* Git
* GitHub

---

# 🔥 Key Features

✅ Data Lake Architecture

✅ AWS Glue Metadata Catalog

✅ Serverless Query Processing

✅ Natural Language to SQL

✅ AI-Powered Business Insights

✅ Multi-Agent Architecture

✅ Interactive Analytics Dashboard

✅ Executive Reporting

---

# 📈 Example Workflow

User Question:

How many delivered orders do we have?

↓

SQL Agent

SELECT COUNT(*) AS delivered_orders
FROM orders
WHERE LOWER(col2)='delivered';

↓

Athena Result

96,478 Delivered Orders

↓

Analytics Agent

Strong order fulfillment rate with high delivery success.

↓

Report Agent

Recommendation:
Investigate cancellation patterns to further improve operational efficiency.

---

# 🚀 Running the Project

## Clone Repository

git clone <repository-url>

cd ai-powered-data-lakehouse

---

## Install Dependencies

pip install -r requirements.txt

---

## Run Streamlit Dashboard

streamlit run dashboard.py

---

# 📷 Screenshots

## Dashboard

(Add dashboard screenshot here)

## Generated SQL

(Add SQL screenshot here)

## Business Insights

(Add insight screenshot here)

---

# 📌 Future Enhancements

* RAG-powered Knowledge Agent
* Autonomous Query Optimization Agent
* Real-Time Streaming Pipeline
* Vector Database Integration
* Cloud Deployment on AWS ECS
* Agent-to-Agent Communication Layer

---

# 💡 What I Learned

* Building Data Lake Architectures on AWS
* Metadata Management using AWS Glue
* Serverless Analytics with Athena
* Multi-Agent AI System Design
* LLM Prompt Engineering
* Business Intelligence Workflows
* End-to-End Data Engineering Practices

---

# 👨‍💻 Author

Built as a production-style Data Engineering + AI Engineering project demonstrating cloud analytics, multi-agent systems, and business intelligence automation.
