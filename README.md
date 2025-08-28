# StackGenie

StackGenie is a Python-based tool that integrates with Google BigQuery to fetch, process, and analyze Stack Overflow data. The project is designed for data ingestion, query execution, and testing workflows with modular scripts.

## Features

- **BigQuery Integration**: Fetch and query Stack Overflow datasets efficiently.
- **Modular Structure**: Organized project structure for easy maintenance.
- **Docker Support**: Containerized environment to ensure consistent dependencies.
- **Testing**: Includes test scripts for validating BigQuery queries.





## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/chetan10510/StackGenie.git
   cd StackGenie
Install dependencies


pip install -r requirements.txt
Set up GCP credentials

Place your GCP service account JSON key in the gcp/ directory.

The .gitignore ensures that credentials are not pushed to GitHub.

Run the application

python app.py
Run tests


python test_bq.py
python src/stackgenie/test_bigquery.py
python test_query.py
Docker Setup
Build the Docker image:


docker build -t stackgenie:latest ./docker
Run the Docker container:


docker run -it stackgenie:latest
Notes
Ensure your GCP project has the necessary BigQuery permissions.

All sensitive files (like service account keys) are ignored in .gitignore.

Author
Chetan Kumar Korivi
Email: korivichetan5@gmail.com
GitHub: https://github.com/chetan10510


