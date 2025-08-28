from google.cloud import bigquery

# Initialize client
client = bigquery.Client()

print(f"Connected to project: {client.project}")

# Query: fetch some Stack Overflow questions
query = """
SELECT
  id,
  title,
  creation_date
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE tags LIKE '%python%'
ORDER BY creation_date DESC
LIMIT 5
"""

query_job = client.query(query)
results = query_job.result()

print("\nSample Stack Overflow Questions:")
for row in results:
    print(f"[{row.id}] {row.title} ({row.creation_date})")
