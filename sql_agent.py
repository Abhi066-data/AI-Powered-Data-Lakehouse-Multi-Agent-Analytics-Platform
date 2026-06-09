import requests

SCHEMA = """
Database: ecommerce_db

customers
- customer_id
- customer_unique_id
- customer_city
- customer_state

orders
- col0 = order_id
- col1 = customer_id
- col2 = order_status

Possible order_status values:
- delivered
- shipped
- canceled
- unavailable
- invoiced
- processing

products
- product information
"""

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def generate_sql(question):

    prompt = f"""
You are an expert Athena SQL engineer.

Database Schema:

{SCHEMA}

Rules:
1. Return ONLY executable SQL.
2. No explanations.
3. No markdown.
4. No ```sql blocks.
5. Use aliases for metrics.
6. For text comparisons use LOWER().
7. Output must start with SELECT.

Examples:

Question:
Count all customers

SQL:
SELECT COUNT(*) AS total_customers
FROM customers;

Question:
Count all orders

SQL:
SELECT COUNT(*) AS total_orders
FROM orders;

Question:
How many delivered orders do we have

SQL:
SELECT COUNT(*) AS delivered_orders
FROM orders
WHERE LOWER(col2)='delivered';

User Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    # Remove markdown if model still returns it
    if "```sql" in result:
        result = result.split("```sql")[1].split("```")[0]

    elif "```" in result:
        result = result.split("```")[1].split("```")[0]

    return result.strip()