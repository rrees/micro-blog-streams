from typing import NamedTuple, List

class Topic(NamedTuple):
	id: int
	title: str
	tags: List[str]
