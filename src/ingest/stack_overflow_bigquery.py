from google.cloud import bigquery
import os
import json

# Set GOOGLE_APPLICATION_CREDENTIALS env var to your service account key JSON path
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/path/to/your/key.json"

def query_stackoverflow(tags=['python', 'pandas'], min_score=5, limit=1000):
    client = bigquery.Client()

    # Format tags for SQL
    tags_filter = " OR ".join([f"tags LIKE '%<{tag}>%'" for tag in tags])

    query = f"""
    SELECT
      q.id as question_id,
      q.title,
      q.body as question_body,
      a.id as answer_id,
      a.body as answer_body,
      a.score as answer_score,
      a.is_accepted
    FROM
      `bigquery-public-data.stackoverflow.posts_questions` q
    JOIN
      `bigquery-public-data.stackoverflow.posts_answers` a
    ON
      q.id = a.parent_id
    WHERE
      ({tags_filter})
      AND q.score >= @min_score
      AND a.score >= 0
    ORDER BY
      q.score DESC, a.is_accepted DESC, a.score DESC
    LIMIT @limit
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("min_score", "INT64", min_score),
            bigquery.ScalarQueryParameter("limit", "INT64", limit),
        ]
    )

    query_job = client.query(query, job_config=job_config)
    results = query_job.result()

    data = []
    for row in results:
        data.append({
            "question_id": row.question_id,
            "title": row.title,
            "question_body": row.question_body,
            "answer_id": row.answer_id,
            "answer_body": row.answer_body,
            "answer_score": row.answer_score,
            "is_accepted": row.is_accepted,
        })

    return data

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download Stack Overflow Q/A from BigQuery")
    parser.add_argument("--tags", nargs="+", default=['python', 'pandas'], help="Tags to filter by")
    parser.add_argument("--min_score", type=int, default=5, help="Minimum question score")
    parser.add_argument("--limit", type=int, default=1000, help="Max number of Q/A pairs")
    parser.add_argument("--output", type=str, default="data/raw/so_qa.json", help="Output JSON file path")

    args = parser.parse_args()

    data = query_stackoverflow(tags=args.tags, min_score=args.min_score, limit=args.limit)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(data)} Q/A pairs to {args.output}")
