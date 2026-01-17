from src.validation import validate_supplier_file


def test_supplier_validation():
    valid, invalid = validate_supplier_file("sample_supplier.csv")

    assert len(valid) == 1
    assert len(invalid) == 3
