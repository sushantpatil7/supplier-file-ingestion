import csv

MANDATORY_FIELDS = ["supplier_id", "supplier_name", "amount", "date"]


def validate_supplier_file(file_path):
    valid_records = []
    invalid_records = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            errors = []

            # Check mandatory fields
            for field in MANDATORY_FIELDS:
                if field not in row or row[field].strip() == "":
                    errors.append(f"{field} is missing or empty")

            # Data type check
            if "amount" in row and row["amount"].strip() != "":
                try:
                    float(row["amount"])
                except ValueError:
                    errors.append("amount must be a number")

            if errors:
                invalid_records.append(
                    {
                        "row_number": row_number,
                        "errors": errors,
                        "data": row
                    }
                )
            else:
                valid_records.append(row)

    return valid_records, invalid_records
