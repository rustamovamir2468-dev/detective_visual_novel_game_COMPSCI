# systems/story_builder.py - File that constructs the story tree.
# Author(s): 5752530
# ====================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice
from systems.act1_nodes import add_act1_nodes
from systems.act2_nodes import add_act2_nodes
from systems.act3_nodes import add_act3_nodes
from systems.act4_nodes import add_act4_nodes
from settings import *

def build_story() -> StoryTree:
    tree = StoryTree()
    add_act1_nodes(tree)
    add_act2_nodes(tree)
    add_act3_nodes(tree)
    add_act4_nodes(tree)
    tree.set_root("act1_bedroom_monday_morning") # Set the first node of the story, the one that gets loaded when the game starts.
    tree.validate() # Check that all node references are valid, and that there are no unreachable nodes. Will raise an error if something is wrong with the story tree.
    return tree