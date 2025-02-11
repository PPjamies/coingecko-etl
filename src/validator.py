import json


def sanitize(data: str, default_value=None):
    data = data.replace("'", '"')
    data = data.replace('null', f'"{default_value}"')
    data = data.replace('None', f'"{default_value}"')
    data = data.replace('""', f'"{default_value}"')

    try:
        data = json.loads(data)
        return data
    except json.JSONDecodeError as e:
        print(f'JSONDecodeError: {e}')
        return None


def validate(data, required_fields):
    if not data:
        raise ValueError('Invalid data: None or empty')

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f'Missing Fields: {', '.join(missing_fields)}')
