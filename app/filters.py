import datetime

import wenmode
from wenmode.plugins import definition_list

markdown_renderer = wenmode.Wenmode(plugins=[definition_list])


def markdown(markdown):
    return markdown_renderer.render(markdown)


def iso_date(a_date):
    return a_date.isoformat(timespec="seconds")


custom_filters = (
    ("markdown", markdown),
    ("iso_date", iso_date),
)
