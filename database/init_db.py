import sqlite3
import hashlib
from pathlib import Path

# Project database folder
BASE_DIR = Path(__file__).resolve().parent

# Create separate databases for three institutions
INSTITUTIONS = {
    "institution_a.db": {
        "institution_code": "UNI-A",
        "institution_name": "Sunrise Institute of Technology",
        "certificate_id": "UNI-A-2026-0001",
        "student_name": "Aarya Sharma",
        "course": "MCA Cloud Computing",
        "certificate_type": "Course Completion Certificate",
        "issue_date": "2026-06-15",
        "completion_year": 2026,
    },
    "institution_b.db": {
        "institution_code": "UNI-B",
        "institution_name": "Greenfield College",
        "certificate_id": "UNI-B-2026-0001",
        "student_name": "Riya Patil",
        "course": "BCA",
        "certificate_type": "Degree Certificate",
        "issue_date": "2026-05-20",
        "completion_year": 2026,
    },
    "institution_c.db": {
        "institution_code": "UNI-C",
        "institution_name": "Western Valley University",
        "certificate_id": "UNI-C-2026-0001",
        "student_name": "Neha Kulkarni",
        "course": "MCA",
        "certificate_type": "Degree Certificate",
        "issue_date": "2026-04-10",
        "completion_year": 2026,
    },
}


def calculate_hash(certificate):
    """Generate a SHA-256 hash for the certificate details."""

    certificate_data = "|".join([
        certificate["certificate_id"],
        certificate["student_name"],
        certificate["course"],
        certificate["certificate_type"],
        certificate["issue_date"],
        str(certificate["completion_year"]),
    ])

    return hashlib.sha256(
        certificate_data.encode("utf-8")
    ).hexdigest()


def initialize_database(filename, certificate):
    """Create a database and insert a sample certificate."""

    database_path = BASE_DIR / filename

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                certificate_id TEXT UNIQUE NOT NULL,
                institution_code TEXT NOT NULL,
                institution_name TEXT NOT NULL,
                student_name TEXT NOT NULL,
                course TEXT NOT NULL,
                certificate_type TEXT NOT NULL,
                issue_date TEXT NOT NULL,
                completion_year INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'VALID',
                certificate_hash TEXT NOT NULL
            )
        """)

        certificate_hash = calculate_hash(certificate)

        cursor.execute("""
            INSERT OR IGNORE INTO certificates (
                certificate_id,
                institution_code,
                institution_name,
                student_name,
                course,
                certificate_type,
                issue_date,
                completion_year,
                status,
                certificate_hash
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            certificate["certificate_id"],
            certificate["institution_code"],
            certificate["institution_name"],
            certificate["student_name"],
            certificate["course"],
            certificate["certificate_type"],
            certificate["issue_date"],
            certificate["completion_year"],
            "VALID",
            certificate_hash,
        ))

        connection.commit()

        print(f"Database created successfully: {filename}")
        print(
            f"Sample certificate added: "
            f"{certificate['certificate_id']}"
        )

    finally:
        connection.close()


if __name__ == "__main__":
    for filename, certificate in INSTITUTIONS.items():
        initialize_database(filename, certificate)

    print("\nAll institution databases are ready.")