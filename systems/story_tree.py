# story_tree.py - File that has the entire story stored in a tree structure
# Author(s): 5752530
# ====================================================
# The entire story is stored here as a tree structure.
# Each moment in the story is a node. Each node points to the next. Choices create branches in the tree.
# Contains a Depth First Search algorithm to find nodes.
# ====================================================

import enum

# --- The four types a story node can be ---
class NodeType(enum.Enum):
    NARRATION = "narration"
    DIALOGUE  = "dialogue"
    CHOICE    = "choice"
    CUTSCENE  = "cutscene"

# --- Represents one selectable option in a choice node ---
class Choice:

    def __init__(self, text, next_node_id, choice_to_record=None): # The =None makes it optional. You don't have to pass it in when creating a Choice — only when that choice needs to be remembered.
        self.text              = text
        self.next_node_id      = next_node_id
        self.choice_to_record  = choice_to_record

# --- One single moment in the story ---
class StoryNode:

    def __init__(self, node_id, node_type, text, speaker=None, portrait=None, next_node_id=None, choices=None, required_choices=None, choices_to_record=None, act=None, requires_flag=None, bg=None): # Most are optional because not every node will need all of them. For example, a choice node doesn't need a speaker or portrait, but it does need choices.
        self.node_id        = node_id # E.g. "act1_sado_wakes_up". This is how we will find the node in the tree.
        self.node_type      = node_type # One of the 4 node types defined in NodeType enum.
        self.text           = text # Words displayed on screen for this moment in the story.
        self.speaker        = speaker # Character name to display in dialogue box, None if narration or choice node.
        self.portrait       = portrait # Character portrait to display in dialogue box, None if narration or choice node.
        self.bg             = bg # Background image for the node, None if not specified.
        self.next_node_id   = next_node_id # The id of the node after this one.
        self.act            = act # Which act the node belongs to
        self.requires_flag  = requires_flag # A flag that must be set for this node to be accessible, only for NARRATION and DIALOGUE nodes.

        # Use empty list/dict if nothing was passed in usign ternary expression. "If choices is not None, use choices, otherwise use []". This is because using a mutable default value like a list or dict is shared across all intances of the class, which can lead to bugs.
        self.choices           = choices           if choices           is not None else [] # A list of objects of type Choice, only for CHOICE nodes.
        self.required_choices  = required_choices  if required_choices  is not None else [] # A list of choice_to_record values that must be in the player's record for this node to be accessible, only for CHOICE nodes.
        self.choices_to_record = choices_to_record if choices_to_record is not None else [] # A list of choice_to_record values that will be added to the player's record when this choice is made.

    def is_choice_node(self): # A helper function to check if this node is a choice node, since we will need to do that a lot.
        return self.node_type == NodeType.CHOICE
    
# --- Holds all story nodes and connects them ---
class StoryTree:

    def __init__(self):
        self.nodes    = {} # This is where every single node in the game gets stored. The key is the node_id string, the value is the StoryNode object.
        self.root_id  = None # None for now because we haven't added any nodes yet.

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def set_root(self, node_id): # Beginning of the story, the first node that gets loaded when the game starts. Should only be called once.
        self.root_id = node_id

    def get_node(self, node_id): 
        return self.nodes.get(node_id, None) # Returns the node with the given id, or None if it doesn't exist.
    
    def get_children(self, node_id): # Returns a list of all nodes that can come after a given node. For a linear node that's just one — the next_node_id. For a choice node it's multiple — one per choice option. This is what makes it a tree.
        node = self.get_node(node_id)

        if node is None:
            return []

        if node.is_choice_node(): # If it's a choice node, children are all the choice destinations.
            return [self.get_node(c.next_node_id) for c in node.choices] # It reads as: "for every choice c in this node's choices, get the node that choice points to."

        if node.next_node_id: # If it's a linear node, the only child is the next node.
            return [self.get_node(node.next_node_id)]

        return []
    
    def dfs_find(self, target_id, current_id=None, visited=None):
        if current_id is None: # # Start from the root if no starting point given.
            current_id = self.root_id

        if visited is None: # Keep track of visited nodes to avoid infinite loops.
            visited = set()

        if current_id is None or current_id in visited:  # If this node doesn't exist or was already visited, stop.
            return None

        visited.add(current_id) # Mark this node as visited.

        if current_id == target_id:  # If this is the node we're looking for, return it.
            return self.get_node(current_id)
        
        for child in self.get_children(current_id): # Search every child of this node recursively. It keeps going deeper and deeper until it either finds the target or runs out of nodes to check.
            if child is not None:
                result = self.dfs_find(target_id, child.node_id, visited)
                if result is not None:
                    return result

        return None # Nothing found down this branch.
    
    def validate(self): # When you've written the whole story tree, you call validate() once to check that every next_node_id actually exists. If you made a typo in an ID somewhere, it immediately catches it and tells you exactly where the problem is.
        errors = []

        for node_id, node in self.nodes.items():

            if node.next_node_id: #  Check linear nodes point to existing nodes.
                if node.next_node_id not in self.nodes:
                    errors.append(f"Node '{node_id}' points to missing node '{node.next_node_id}'")

            for choice in node.choices: # Check choice nodes point to existing nodes.
                if choice.next_node_id not in self.nodes:
                    errors.append(f"Node '{node_id}' choice '{choice.text}' points to missing node '{choice.next_node_id}'")

        if errors:
            print("[StoryTree] Validation failed:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("[StoryTree] Validation passed. All nodes connected.")

        return len(errors) == 0