# systems/flag_tracker.py
# =============================================================
# LOGIC TEAM: Tracks all story flags for the current playthrough.
# A flag is a True/False (or integer) value that records what Sado has done, seen, or discovered.
# The story tree reads these to decide which branches to unlock.
# Authors: 5752530
# =============================================================

class FlagTracker:
    """Stores and manages all story flags.

    All flags start as False by default.
    The story tree checks flags to unlock branches.
    The save system reads this entire dict to save progress.
    """

    def __init__(self):
        self._flags = {}

    def set_flag(self, name: str, value=True):
        self._flags[name] = value
        print(f"[Flags] '{name}' set to {value}")

    def get_flag(self, name: str, default=False):
        return self._flags.get(name, default)

    def check_flags(self, required: dict) -> bool:

        for flag_name, expected_value in required.items():
            if self.get_flag(flag_name) != expected_value:
                return False
        return True

    def get_all(self) -> dict:
        return dict(self._flags)

    def load_from_dict(self, data: dict):
        self._flags = data
        print(f"[Flags] Loaded {len(data)} flags from save.")

    def reset(self):
        self._flags = {}
        print("[Flags] All flags reset.")