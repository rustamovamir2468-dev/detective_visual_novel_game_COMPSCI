# systems/story_tree.py
# =============================================================
# LOGIC TEAM: The Story Tree — the core data structure.
# Every line of dialogue, every choice, every story branch is here as a tree of StoryNode objects.
# Authors: 5752530
# =============================================================

import enum

class NodeType(enum.Enum):
    """All possible types of story nodes."""
    NARRATION = "narration"
    DIALOGUE  = "dialogue"
    CHOICE    = "choice"
    CUTSCENE   = "cutscene"

class Choice:
    """Represents one selectable option in a choice node.
    
    Attributes:
        text: The text shown to the player for this choice.
        next_node: The StoryNode that this choice leads to.
        flag_to_set: Optional string name of a flag to set when this choice is selected (for tracking player decisions).
    """

    def __init__(self, text: str, next_node_id:str, flag_to_set: str = None):
        self.text = text
        self.next_node_id = next_node_id
        self.flag_to_set = flag_to_set

    def __repr__(self):
        return f"Choice('{self.text}' --> '{self.next_node_id}')"
    
class StoryNode:
    """A sinde node in a story tree
    
    Attributes:
        node_id (str): Unique ID, e.g. "act_1_001"
        node_type (NodeType): One of the NodeType enum values.
        speaker (str): Who is speaking (NOT NARRATION!)
        text (str): The line of dialogue or narration to show.
        next_node_id (str): ID of the next node
        choices (list): List of Choice objects (only for CHOICE nodes)
        required_flags (dict): Flags required to be true for this node to be accessible.
        flags_to_set (dict): Flags to set when this node is reached (for tracking player decisions).
        act (str): Which act this node belongs to
        portrait (str): Filename of speaker portrait (for creative team)
        """
    
    def __init__(self, node_id: str, node_type: NodeType,
                 text: str, speaker: str = None,
                 next_node_id: str = None, choices: list = None,
                 required_flags: dict = None, flags_to_set: dict = None,
                 act: str = "act1", portrait: str = None):

        self.node_id        = node_id
        self.node_type      = node_type
        self.speaker        = speaker
        self.text           = text
        self.next_node_id   = next_node_id
        self.choices        = choices or []
        self.required_flags = required_flags or {}
        self.flags_to_set   = flags_to_set or {}
        self.act            = act
        self.portrait       = portrait

    def is_choice_node(self) -> bool:
        return self.node_type == NodeType.CHOICE

    def is_ending(self) -> bool:
        return self.next_node_id is None and len(self.choices) == 0

    def __repr__(self):
        return (f"StoryNode(id='{self.node_id}', "
                f"type={self.node_type.value}, "
                f"speaker='{self.speaker}')")
    
class StoryTree:
    """The full story tree for the game, containing all StoryNodes in a dictionary keyed by node_id
    Methods:
        add_node: Add a StoryNode to the tree.
        get_node: Retrieve a StoryNode by its ID.
        dfs_find: Search for a target node using DFS
        get_children: Get all direct children of a node
        validate: Check for broken links in the tree
        """
    
    def __init__(self, root_id: str = None):
        self.nodes   = {}
        self.root_id = root_id

    # --- Building the tree ---
    def add_node(self, node: StoryNode):
        if node.node_id in self.nodes:
            raise ValueError(f"Duplicate node ID: '{node.node_id}'")
        self.nodes[node.node_id] = node

    def set_root(self, node_id: str):
        if node_id not in self.nodes:
            raise ValueError(f"Root node '{node_id}' not found in tree")
        self.root_id = node_id

    # --- Retrieving nodes ---
    def get_node(self, node_id: str):
        node = self.nodes.get(node_id)
        if node is None:
            print(f"Node '{node_id}' not found in tree")
        return node
    
    def get_children(self, node_id: str) -> list:
        node = self.get_node(node_id)
        if node is None:
            return []
        
        children = []

        if node.next_node_id:
            child = self.get_node(node.next_node_id)
            if child:
                children.append(child)

        for choice in node.choices:
            child = self.get_node(choice.next_node_id)
            if child:
                children.append(child)

        return children
    
    # --- DFS Search Algorithm ---
    def dfs_find(self, start_id: str, target_id: str, visited=None) -> bool:
        
        if visited is None:
            visited = set()

        if start_id == target_id:
            return True

        if start_id in visited:
            return False
        
        visited.add(start_id)

        node = self.get_node(start_id)
        if node is None:
            return False
        
        for child in self.get_children(start_id):
            if self.dfs_find(child.node_id, target_id, visited):
                return True
            
        return False
    
    # --- Validation ---
    def validate(self):
        print("[StoryTree] Validating story tree...")
        errors = 0

        for node_id, node in self.nodes.items():

            if node.next_node_id and node.next_node_id not in self.nodes:
                print(f"ERROR: '{node_id}' -> next_node_id '{node.next_node_id}' not found")
                errors += 1

            for choice in node.choices:
                if choice.next_node_id not in self.nodes:
                    print(f"ERROR: '{node_id}' -> choice '{choice.text}' -> next_node_id '{choice.next_node_id}' not found")
                    errors += 1

        if errors == 0:
            print("Validation passed: No broken links found!")
        else:
            print(f"Validation failed: {errors} broken links found.")