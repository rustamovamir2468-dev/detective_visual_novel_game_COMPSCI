# detective_visual_novel_game_COMPSCI
FP016 SA2 - Python Detective Visual Novel - Amir, David, Nicolette, Federico

# Teams
- Amir — Logic
- David — Logic
- Nicolette — Creative
- Federico — Creative

# How to Run
1. Install pygame: pip install pygame
2. Run: python main.py

# Project Structure
- settings.py     — all constants (colours, sizes, etc.)
- core/           — game loop, state machine, scene manager, save system
- systems/        — story tree, choice tracker, evidence, deduction
- ui/             — all visual renderers (dialogue box, menus etc.)
- scenes/         — story content organised by act
- assets/         — images and audio (creative team's responsibility)

# Key Decisions
- Pure visual novel — no top-down movement
- Dual colour palette: warm (Act 1) and cold (Acts 2-4)
- Story stored as a tree with DFS search algorithm
- Choices tracked in choice_tracker.py
- Characters: Sado, Maya, Dr. Elias, Mother (and more maybe?)

# Logic Team Notes
- Never write story content in systems/ files
- All constants go in settings.py — never hardcode numbers
- Commit often with clear messages
- Run main.py to test, never game.py directly