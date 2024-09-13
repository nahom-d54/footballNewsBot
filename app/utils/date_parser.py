import datetime

def parse_date(date_string: str, date_format: str = r"%a, %d %b %Y %H:%M:%S %z") -> datetime:
    parsed_date = datetime.datetime.strptime(date_string, date_format)

    return parsed_date

def date_stringify(date_obj:datetime.datetime ):
    date_format: str = r"%a, %d %b %Y %H:%M:%S %z"

    return date_obj.strftime(date_format)