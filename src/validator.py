def validate(data, required_fields):
    if not data:
        raise ValueError('Invalid data: None or empty')

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f'Missing Fields: {', '.join(missing_fields)}')
