from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Institution API configuration
INSTITUTIONS = {
    "UNI-A": {
        "name": "Sunrise Institute of Technology",
        "api_url": "http://127.0.0.1:5001"
    },
    "UNI-B": {
        "name": "Greenfield College",
        "api_url": "http://127.0.0.1:5002"
    },
    "UNI-C": {
        "name": "Western Valley University",
        "api_url": "http://127.0.0.1:5003"
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/verify")
def verify():
    return render_template("verify.html")


@app.route("/result", methods=["GET"])
def result():
    certificate_id = request.args.get(
        "certificate_id", ""
    ).strip().upper()

    institution_name = request.args.get(
        "institution", ""
    ).strip()

    holder_name = request.args.get(
        "holder_name", ""
    ).strip()

    # Validate Certificate ID
    if not certificate_id:
        return render_template(
            "invalid_result.html",
            message="Please enter a Certificate ID."
        )

    # Identify the issuing institution from Certificate ID
    institution_code = "-".join(certificate_id.split("-")[:2])

    institution = INSTITUTIONS.get(institution_code)

    if not institution:
        return render_template(
            "invalid_result.html",
            message="Invalid Certificate ID or unsupported institution."
        )

    try:
        # Send request to the appropriate institution API
        response = requests.get(
            f"{institution['api_url']}/verify/{certificate_id}",
            timeout=10
        )

        response.raise_for_status()
        certificate = response.json()

    except requests.exceptions.RequestException:
        return render_template(
            "invalid_result.html",
            message=(
                f"Unable to contact {institution['name']}. "
                "Please ensure that the institution API is running."
            )
        )

    # Check the verification response
    if not certificate.get("verified", False):
        return render_template(
            "invalid_result.html",
            message=certificate.get(
                "message",
                "Certificate could not be verified."
            )
        )

    # Check institution name entered in the form
    actual_institution = certificate.get(
        "institution_name", ""
    ).strip()

    if (
        institution_name
        and institution_name.casefold()
        != actual_institution.casefold()
    ):
        return render_template(
            "invalid_result.html",
            message="The entered institution name does not match the certificate record."
        )

    # Check certificate holder name if provided
    actual_holder = certificate.get(
        "student_name", ""
    ).strip()

    if (
        holder_name
        and holder_name.casefold()
        != actual_holder.casefold()
    ):
        return render_template(
            "invalid_result.html",
            message="The entered certificate holder name does not match the institutional record."
        )

    # Display verified certificate details
    return render_template(
        "result.html",
        certificate=certificate,
        verification_method="Certificate ID"
    )


@app.route("/invalid-result")
def invalid_result():
    return render_template(
        "invalid_result.html",
        message="The certificate could not be verified."
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)