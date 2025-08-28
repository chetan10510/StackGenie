from google.cloud import bigquery

# Initialize client
client = bigquery.Client()

# Example query on a public dataset (USA names)
query = """
    SELECT name, SUM(number) as total
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total DESC
    LIMIT 10
"""

# Run query
query_job = client.query(query)

print("Top 10 names in Texas:")
for row in query_job:
    print(f"{row.name}: {row.total}")
