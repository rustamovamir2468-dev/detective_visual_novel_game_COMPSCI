# systems/act3_nodes.py - Act 3 story nodes (Friday, Weekend, Monday 2)
# Author(s): 5752530
# ====================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice


def add_act3_nodes(tree: StoryTree):

    # ── FRIDAY ─────────────────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act3_fri_morning_school_intro",
        node_type=NodeType.NARRATION,
        act=3,
        text="By Friday morning, the halls feel thinner, like the school itself is holding its breath.",
        next_node_id="act3_fri_morning_hannah_reserved"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_morning_hannah_reserved",
        node_type=NodeType.NARRATION,
        act=3,
        text="In computer science, Dr. Hannah moves through the lesson with less of her usual energy, eyes flicking to the door and windows more than the code on the board.",
        next_node_id="act3_fri_player_notices_hannah"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_player_notices_hannah",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="suspicious",
        text="Hannah's acting weird today… almost like she's hiding something.",
        next_node_id="act3_fri_maya_whispers"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_maya_whispers",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="maya",
        portrait=("maya", "nervous"),
        text="She keeps checking her phone and staring at the hallway. Think she knows more than she's saying?",
        next_node_id="act3_fri_internal_bulletin_board"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_internal_bulletin_board",
        node_type=NodeType.NARRATION,
        act=3,
        text="In your head, the pieces from the last days slide across an invisible bulletin board — red beanie, missing kids, Finn cleared, Elias's scarf still pinned in the corner.",
        next_node_id="act3_fri_player_decides_follow"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_player_decides_follow",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="suspicious",
        text="If she's involved, she might slip up after school. We should follow her and see where she goes.",
        next_node_id="act3_fri_maya_agrees_follow"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_maya_agrees_follow",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="maya",
        portrait=("finn", "nervous"),
        text="That's risky, detective… but you're right. We won't get answers sitting in class.",
        next_node_id="act3_fri_after_school_hannah_leaves"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_after_school_hannah_leaves",
        node_type=NodeType.NARRATION,
        act=3,
        text="After the final bell, you and Maya hang back near the staff parking lot. Dr. Hannah eventually appears with her bag, heading toward her car.",
        next_node_id="act3_fri_choice_follow_style"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_choice_follow_style",
        node_type=NodeType.CHOICE,
        act=3,
        text="How do you follow her?",
        choices=[
            Choice("Follow Hannah directly.", "act3_fri_follow_direct", choice_to_record="followed_hannah_direct"),
            Choice("Follow Hannah from a distance.", "act3_fri_follow_discreet", choice_to_record="followed_hannah_discreet"),
        ]
    ))

    # ── BRANCH A: Follow directly (bad ending) ──

    tree.add_node(StoryNode(
        node_id="act3_fri_follow_direct",
        node_type=NodeType.NARRATION,
        act=3,
        text="You stride straight toward Hannah's car before Maya can stop you, footsteps loud on the pavement.",
        next_node_id="act3_fri_direct_hannah_confronted"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_direct_hannah_confronted",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait=("hannah", "shocked"),
        text="[PLAYER]? Maya? Why are you two following me?",
        next_node_id="act3_fri_direct_player_accuses"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_direct_player_accuses",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="angry",
        text="Kids are going missing and you're acting secretive. We know you're hiding something. Where are you going?",
        next_node_id="act3_fri_direct_elias_appears"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_direct_elias_appears",
        node_type=NodeType.NARRATION,
        act=3,
        text="Before Hannah can answer, a shadow falls across the car. Dr. Elias steps out from behind a nearby pillar, expression unreadable.",
        next_node_id="act3_fri_direct_elias_comment"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_direct_elias_comment",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="elias",
        portrait=("elias", "nervous"),
        text="Following teachers now? That's dangerous behavior… you never know who might feel threatened.",
        next_node_id="ending_bad_hannah_follow"
    ))

    tree.add_node(StoryNode(
        node_id="ending_bad_hannah_follow",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="narrator",
        portrait="none",
        text="The parking lot lights flickered on as the world dimmed. You were right about danger — just wrong about who it was aimed at.",
        next_node_id=None
    ))

    # ── BRANCH B: Follow discreetly (main route) ──

    tree.add_node(StoryNode(
        node_id="act3_fri_follow_discreet",
        node_type=NodeType.NARRATION,
        act=3,
        text="You tug Maya back behind a row of parked cars, keeping just enough distance that Hannah can't see you in her mirrors.",
        next_node_id="act3_fri_follow_drive"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_follow_drive",
        node_type=NodeType.NARRATION,
        act=3,
        text="Hannah's car slips out of the lot and into late-afternoon traffic. You and Maya trail from a distance, turning whenever her indicator flashes.",
        next_node_id="act3_fri_follow_weird_turn"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_follow_weird_turn",
        node_type=NodeType.NARRATION,
        act=3,
        text="After a few normal turns past shops and houses, she suddenly cuts down a narrow side street you barely recognise.",
        next_node_id="act3_fri_corner_disappears"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_corner_disappears",
        node_type=NodeType.NARRATION,
        act=3,
        text="By the time you and Maya reach the corner, her car is gone. Just parked cars and a dead-end alley.",
        next_node_id="act3_fri_maya_reacts_lost"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_maya_reacts_lost",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="maya",
        portrait=("maya", "nervous"),
        text="Great. Either she drives like a ninja, or she didn't want anyone to see where she was going.",
        next_node_id="act3_fri_player_still_suspicious"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_player_still_suspicious",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="suspicious",
        text="Yeah… that felt way too intentional. She definitely noticed something. Maybe she noticed us.",
        next_node_id="act3_fri_walk_home_with_maya"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_walk_home_with_maya",
        node_type=NodeType.NARRATION,
        act=3,
        text="You and Maya give up the chase and walk home, replaying every turn in your heads and wondering where she disappeared to.",
        next_node_id="act3_fri_home_shenanigans"
    ))

    tree.add_node(StoryNode(
        node_id="act3_fri_home_shenanigans",
        node_type=NodeType.NARRATION,
        act=3,
        text="Back in your room, you bounce between homework, games, and checking the tracking app. Nothing unusual pops up — but the unanswered questions make it hard to relax.",
        next_node_id="act3_weekend"
    ))

    # ── WEEKEND ────────────────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act3_weekend",
        node_type=NodeType.NARRATION,
        act=3,
        text="The weekend slides by in a blur of half-finished homework, muted news reports about the kidnappings, and long stretches of staring at the tracking app on your phone. Nothing obvious happens, but the silence only makes Monday feel heavier.",
        next_node_id="act3_mon_morning_school_intro"
    ))

    # ── MONDAY 2 ───────────────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act3_mon_morning_school_intro",
        node_type=NodeType.NARRATION,
        act=3,
        text="Monday morning feels heavier than usual. The school looks the same from the outside, but the air around the gates buzzes with quiet fear.",
        next_node_id="act3_mon_morning_corridor"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_morning_corridor",
        node_type=NodeType.NARRATION,
        act=3,
        text="In the corridor, teachers talk in low voices, and students move in tight groups. Dr. Hannah passes by with her red beanie wrapped neatly, offering a tired smile.",
        next_node_id="act3_mon_morning_player_suspicion"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_morning_player_suspicion",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="suspicious",
        text="She looks normal… but after Friday, I still can't tell if she's hiding something or trying to help.",
        next_node_id="act3_mon_morning_maya_reply"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_morning_maya_reply",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="maya",
        portrait=("maya", "nervous"),
        text="Whoever it is, they're still out there. Let's just get through today without ending up on the news, yeah?",
        next_node_id="act3_mon_day_montage"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_day_montage",
        node_type=NodeType.NARRATION,
        act=3,
        text="The school day crawls past — lessons, roll calls, teachers pretending nothing is wrong. Every time you spot Hannah or Elias, your brain adds another pin to the mental bulletin board.",
        next_node_id="act3_mon_after_school_parking_intro"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_after_school_parking_intro",
        node_type=NodeType.NARRATION,
        act=3,
        text="After the final bell, you and Maya drift toward the staff parking lot. The sky is dimming, and most students have already gone home.",
        next_node_id="act3_mon_after_school_hannah_heading_to_car"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_after_school_hannah_heading_to_car",
        node_type=NodeType.NARRATION,
        act=3,
        text="Dr. Hannah crosses the lot with her bag over her shoulder, heading for her small car parked near the end of the row.",
        next_node_id="act3_mon_choice_confront_hannah"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_choice_confront_hannah",
        node_type=NodeType.CHOICE,
        act=3,
        text="Hannah reaches for her keys.",
        choices=[
            Choice("Say nothing and let Hannah start the car.", "act3_mon_no_confront_hannah", choice_to_record="didnt_warn_hannah"),
            Choice("Run over and warn Hannah about the car.", "act3_mon_confront_hannah", choice_to_record="warned_hannah"),
        ]
    ))

    # ── BRANCH A: Do not warn Hannah (bad ending) ──

    tree.add_node(StoryNode(
        node_id="act3_mon_no_confront_hannah",
        node_type=NodeType.NARRATION,
        act=3,
        text="You freeze, torn between doubt and fear. Maya opens her mouth to speak, then hesitates when you don't move.",
        next_node_id="act3_mon_no_confront_car_starts"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_no_confront_car_starts",
        node_type=NodeType.NARRATION,
        act=3,
        text="Hannah unlocks the car, tosses her bag onto the passenger seat, and turns the key in the ignition.",
        next_node_id="ending_bad_car_explosion"
    ))

    tree.add_node(StoryNode(
        node_id="ending_bad_car_explosion",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="narrator",
        portrait="none",
        text="The engine roared once, then the world shattered into light and sound. In a single flash, the parking lot, the car, and every doubt you held vanished together.",
        next_node_id=None
    ))

    # ── BRANCH B: Warn Hannah (main route, Hannah becomes ally) ──

    tree.add_node(StoryNode(
        node_id="act3_mon_confront_hannah",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="scared",
        text="Hannah! Wait — don't start the car!",
        next_node_id="act3_mon_confront_maya_backs_up"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_confront_maya_backs_up",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="maya",
        portrait=("maya", "scared"),
        text="Seriously, don't! Something's wrong. Please just listen for a second.",
        next_node_id="act3_mon_hannah_confused"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_hannah_confused",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait=("hannah", "cold"),
        text="What are you two talking about? Is this some kind of joke?",
        next_node_id="act3_mon_player_explains_suspicion"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_player_explains_suspicion",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="nervous",
        text="We saw someone near your car earlier — around the time the halls were empty. With everything that's been happening, it felt wrong. Just… please don't turn the key yet.",
        next_node_id="act3_mon_hannah_trusts_enough"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_hannah_trusts_enough",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait=("hannah", "suspicious"),
        text="You realise how wild this sounds. But fine — show me what you think is wrong before I call the principal.",
        next_node_id="act3_mon_check_car"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_check_car",
        node_type=NodeType.NARRATION,
        act=3,
        text="The three of you move to the back of the car. Your stomach knots as you crouch beside the fuel cap, fingers trembling.",
        next_node_id="act3_mon_find_boom_boom"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_find_boom_boom",
        node_type=NodeType.NARRATION,
        act=3,
        text="Inside the compartment, a strange canister is wedged against the tank, thin wires coiled around it. Faint chemical fumes drift out as the evening air hits it.",
        next_node_id="act3_mon_player_realises_bomb"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_player_realises_bomb",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="shocked",
        text="This isn't a prank. This is… some kind of bomb.",
        next_node_id="act3_mon_hannah_reacts_bomb"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_hannah_reacts_bomb",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait=("hannah", "shocked"),
        text="Who would do this? I knew something was wrong with how the staff meetings felt, but this —",
        next_node_id="act3_mon_hannah_reveals_investigation"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_hannah_reveals_investigation",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait="nervous",
        text="I've been trying to piece this together on my own — talking to parents, checking schedules, comparing when the kids vanished. I thought Finn might be involved at first, but the times didn't line up.",
        next_node_id="act3_mon_player_and_hannah_align"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_player_and_hannah_align",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="player",
        portrait="suspicious",
        text="We followed Finn. He's innocent. Whoever's doing this is smarter than just yelling in class… and they like red.",
        next_node_id="act3_mon_hannah_resolve"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_hannah_resolve",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="hannah",
        portrait=("hannah", "cold"),
        text="Then our list is down to one person. But until we have proof, we can't go to the police. They'll say it's stress talking.",
        next_node_id="act3_mon_elias_watching"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_elias_watching",
        node_type=NodeType.NARRATION,
        act=3,
        text="Across the lot, a classroom window glints. For a second, you're sure you see the outline of a man with a familiar scarf watching you before the light flicks off.",
        next_node_id="act3_mon_evening_part_ways"
    ))

    tree.add_node(StoryNode(
        node_id="act3_mon_evening_part_ways",
        node_type=NodeType.NARRATION,
        act=3,
        text="Hannah locks her car and agrees to call someone to safely remove the device. You and Maya head home, the weight of what you almost walked away from pressing on your shoulders.",
        next_node_id="act3_end_of_act3"
    ))

    tree.add_node(StoryNode(
        node_id="act3_end_of_act3",
        node_type=NodeType.DIALOGUE,
        act=3,
        speaker="narrator",
        portrait="none",
        text="That night, the school's shadows feel longer in your memory. You're no longer just suspicious students — Hannah is on your side now, and all eyes are turning toward Elias.",
        next_node_id=None
    ))