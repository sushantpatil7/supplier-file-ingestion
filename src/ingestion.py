from validation import validate_supplier_file


def ingest_supplier_file(file_path):
    valid_records, invalid_records = validate_supplier_file(file_path)

    print(f"Valid records count: {len(valid_records)}")
    print(f"Invalid records count: {len(invalid_records)}")

    if invalid_records:
        print("Invalid Records Details:")
        for record in invalid_records:
            print(record)

    # In real project:
    # - valid_records → load to DB / S3
    # - invalid_records → error bucket / logs


if __name__ == "__main__":
    ingest_supplier_file("sample_supplier.csv")
