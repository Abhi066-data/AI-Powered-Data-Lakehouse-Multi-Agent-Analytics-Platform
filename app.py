from sql_agent import generate_sql
from athena import run_query
from analytics_agent import analyze

question = input("Ask a question: ")

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

result = run_query(sql)

print("\nQuery Result:\n")
print(result)

insights = analyze(result)

print("\nBusiness Insights:\n")
print(insights)