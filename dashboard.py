import streamlit as st
from sql_agent import generate_sql
from athena import run_query
from analytics_agent import analyze_data

st.title("AI-Powered Analytics Platform")

question = st.text_input("Ask a business question")


def clean_sql(sql: str) -> str:
    """
    Removes LLM garbage text and keeps only valid SQL
    """
    import re
    sql = sql.strip()

    match = re.search(r"(SELECT|WITH|INSERT|CREATE|UPDATE|DELETE)\s", sql, re.IGNORECASE)
    if match:
        sql = sql[match.start():]

    return sql


if st.button("Run"):

    # 1. Generate SQL
    raw_sql = generate_sql(question)
    sql = clean_sql(raw_sql)

    st.subheader("Generated SQL")
    st.code(sql)

    try:
        # 2. Run query safely
        result = run_query(sql)

        st.subheader("Query Result")
        st.dataframe(result)

        # 3. Analytics only if data exists
        if result is not None and not result.empty:
            insights = analyze_data(result)

            st.subheader("Business Insights")
            st.write(insights)
        else:
            st.warning("No data returned from query")

    except Exception as e:
        st.error("Query execution failed")
        st.exception(e)