#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message

    Args:
        fields (list): Fields to obfuscate.
        redaction (str): Replacement string for obfuscation.
        message (str): The log message to process.
        separator (str): Field separator in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = (
        f"({'|'.join(re.escape(field) for field in fields)})="
        f".+?{separator}"
    )
    return re.sub(
            pattern,
            lambda m: f"{m.group(1)}={redaction}{separator}",
            message
            )
