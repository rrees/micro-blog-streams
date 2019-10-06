from typing import NamedTuple, List

from datetime import datetime

class Topic(NamedTuple):
	id: int
	title: str
	tags: List[str]

class BlogPost(NamedTuple):
	id: int
	title: str
	content: str
	tags: List[str]
	updated: datetime