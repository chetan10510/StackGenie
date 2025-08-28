from google.cloud import bigquery
from datetime import datetime, timezone

def insert_log(message):
    client = bigquery.Client()
    table_id = "resolute-future-470007-a4.stackgenie_dataset.logs"

    rows = [
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "message": message,
        }
    ]

    # Use load_table_from_json instead of streaming insert
    job = client.load_table_from_json(rows, table_id)
    job.result()  # Wait for the load job to complete

    print(f"Inserted log: {message}")

if __name__ == "__main__":
    insert_log("System initialized ")
    insert_log("Warning: CPU usage crossed 75% ")
    insert_log("Error: Database connection failed ")
