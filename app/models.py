from dataclasses import dataclass
from typing import NamedTuple, List

from datetime import datetime


class Topic(NamedTuple):
    id: int
    title: str
    description: str
    tags: List[str]
    updated: datetime
    active: bool


class BlogPost(NamedTuple):
    id: int
    title: str
    content: str
    tags: List[str]
    url: str
    updated: datetime


@dataclass(frozen=True)
class ReturnLink:
    path: str
    text: str
