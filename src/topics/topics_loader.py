"""
Load topics utilities
"""

import json
from pathlib import Path
from src.topics.schemas.topic import Topic


# TODO: get from config
path_to_topics_root = "./datatopics"


def load_topics_by_type(type: str) -> list[Topic]:
    """"""
    topics = list()
    path = Path(f"{path_to_topics_root}")

    for file in path.iterdir():
        if file.suffix == '.json':
            ffn = f'{path_to_topics_root}/{file.name}'
            with open(ffn, 'r') as json_file:
                top_obj = json.load(json_file)
                # top_obj = read(ffn)
            # Read topic
            content_f_path = top_obj.get("content")
            if content_f_path:
                content_f_path = f'{path_to_topics_root}/{content_f_path}'
                with open(content_f_path, "r") as content_file:
                    content = content_file.read()
                top_obj["content"] = content
            else:
                top_obj["content"] = "NotFound"
            topic = Topic(**top_obj)
            if topic.type == type:
                topics.append(topic)
    return topics


def read(ffn: str) -> dict:
    with open(ffn, 'r') as f:
        data = json.load(f)
        return data
