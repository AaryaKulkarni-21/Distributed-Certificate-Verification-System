from flask import Flask, jsonify
import sqlite3
import hashlib
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "institution_c.db"


def calculate_hash(certificate):
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


@app.route("/")
def home():
    return jsonify({
        "institution": "Western Vally University",
        "institution_code": "UNI-C",
        "message": "Institution C Certificate Verification API is running."
    })


@app.route("/verify/<certificate_id>", methods=["GET"])
def verify_certificate(certificate_id):
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM certificates
            WHERE certificate_id = ?
            """,
            (certificate_id,)
        )

        record = cursor.fetchone()

        if record is None:
            return jsonify({
                "verified": False,
                "institution_code": "UNI-C",
                "message": "Certificate not found in Institution c."
            }), 404

        certificate = dict(record)

        calculated_hash = calculate_hash(certificate)

        integrity_passed = (
            calculated_hash == certificate["certificate_hash"]
        )

        verified = (
            certificate["status"] == "VALID"
            and integrity_passed
        )

        return jsonify({
            "verified": verified,
            "institution_code": certificate["institution_code"],
            "institution_name": certificate["institution_name"],
            "certificate_id": certificate["certificate_id"],
            "student_name": certificate["student_name"],
            "course": certificate["course"],
            "certificate_type": certificate["certificate_type"],
            "issue_date": certificate["issue_date"],
            "completion_year": certificate["completion_year"],
            "integrity_check": (
                "PASSED" if integrity_passed else "FAILED"
            ),
            "message": (
                "Certificate verified successfully."
                if verified
                else "Certificate is invalid or its integrity check failed."
            )
        })

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=True, port=5003)