# systems/story_builder.py - File that constructs the story tree.
# Author(s): 5752530
# ====================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice
from settings import *

def build_story() -> StoryTree:
    tree = StoryTree()

    tree.add_node(StoryNode(node_id = "act1_opening", node_type = NodeType.NARRATION, text = "It's a normal Monday morning...", next_node_id = "act1_player_wakes_up", act = ACT_1))

    # ... all other nodes
    
    tree.set_root("act1_opening")
    tree.validate()
    return tree