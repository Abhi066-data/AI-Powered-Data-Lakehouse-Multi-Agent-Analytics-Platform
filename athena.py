from pyathena import connect
import pandas as pd

DATABASE = "ecommerce_db"

S3_STAGING_DIR = "s3://ai-data-lakehouse/athena-results/"

def run_query(sql):

    conn = connect(
        s3_staging_dir=S3_STAGING_DIR,
        region_name="us-east-1",
        schema_name=DATABASE
    )

    df = pd.read_sql(sql, conn)

    return df