# scenes/act1.py
# Author(s): 5752530
# =======================================================================
# All Act 1 dialogue/narration/choice nodes, parsed directly from MONDAY.md
# Node structure:
#   NARRATION : { "type", "act", "text", "next" }
#   DIALOGUE  : { "type", "act", "speaker", "portrait", "text", "next" }
#   CHOICE    : { "type", "act", "choices": [{ "text", "next", "record" }] }
#   ENDING    : { "type", "act", "speaker", "portrait", "text", "ending_type" }
#              ending_type is "good" or "bad"
# =======================================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice

def build_act1() -> StoryTree:
    tree = StoryTree()

    tree.add_node(StoryNode(
        node_id="act1_bedroom_monday_morning",
        node_type=NodeType.NARRATION,
        text="It's Monday morning. Your alarm cuts through the silence of your room.",
        next_node_id="act1_bedroom_phone_buzz",
        act=1,
    ))
    # ... all other nodes ...

    tree.set_root("act1_bedroom_monday_morning")
    return tree
