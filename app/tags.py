import re


def process(tag_string):
    cleaned_input = tag_string.strip().lower()
    return [tag for tag in re.split("[ ,]+", cleaned_input) if tag]


def as_string(tags):
    return " ".join(tags)
