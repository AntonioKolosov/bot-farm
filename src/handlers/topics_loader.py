"""
Load topics utilities
"""

import json
from pathlib import Path
from src.handlers.schemas.topic import Topic


# TODO: get from config
path_to_topics_root = "./datatopics"


def load_topics_by_type(type: str) -> list[Topic]:
    """"""
    topics = list()
    path = Path(f"{path_to_topics_root}")

    for file in path.iterdir():
        if file.suffix == '.json':
            ffn = f'{path_to_topics_root}/{file.name}'
            top_obj = read(ffn)
            topic = Topic(**top_obj)
            if topic.type == type:
                topics.append(topic)
    return topics


def read(ffn: str) -> dict:
    with open(ffn, 'r') as f:
        data = json.load(f)
        return data
