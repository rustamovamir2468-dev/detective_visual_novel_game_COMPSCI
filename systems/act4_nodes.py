# systems/act4_nodes.py - Act 4 story nodes (Tuesday 2 — the final confrontation)
# Author(s): 5752530
# ====================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice


def add_act4_nodes(tree: StoryTree):

    # ── TUESDAY 2 MORNING ──────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_walkie_intro",
        node_type=NodeType.NARRATION,
        act=4,
        text="Tuesday starts with a burst of static from the walkie-talkie on your desk, the one Maya insisted you both carry for fun.",
        next_node_id="act4_tue_morning_try_contact_maya"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_try_contact_maya",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="nervous",
        text="Maya? You awake? Say something if you're there.",
        next_node_id="act4_tue_morning_silence"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_silence",
        node_type=NodeType.NARRATION,
        act=4,
        text="The speaker hisses, then falls completely quiet. No voice, no reply — just dead air.",
        next_node_id="act4_tue_morning_check_phone"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_check_phone",
        node_type=NodeType.NARRATION,
        act=4,
        text="You grab your phone. Her chat is empty, your last message left on read from last night. The tracking app shows her icon greyed out — phone offline.",
        next_node_id="act4_tue_morning_player_worried"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_player_worried",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="scared",
        text="This isn't like her… Something's wrong.",
        next_node_id="act4_tue_morning_choice_tell_mom"
    ))

    # ── CHOICE: Tell mom or hide it ────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_choice_tell_mom",
        node_type=NodeType.CHOICE,
        act=4,
        text="What do you do before leaving the house?",
        choices=[
            Choice("Tell mom Maya is missing.", "act4_tue_morning_tell_mom", choice_to_record="told_mom_about_maya"),
            Choice("Keep it to yourself and head to school.", "act4_tue_morning_hide_from_mom", choice_to_record="hid_maya_disappearance"),
        ]
    ))

    # ── BRANCH A: Tell mom (unlocks true good ending later) ────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_tell_mom",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="scared",
        text="Mom… Maya's not answering her phone, and her location is offline. I think something might've happened.",
        next_node_id="act4_tue_morning_mom_response"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_mom_response",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="mom",
        portrait="nervous",
        text="That's serious. If she still doesn't answer by the time you're at school, I'm calling the police. Promise me you'll be careful and stay with teachers you trust.",
        next_node_id="act4_tue_morning_leave_house"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_leave_house",
        node_type=NodeType.NARRATION,
        act=4,
        text="You nod, heart hammering, and head out the door. The air feels colder than any other morning this week.",
        next_node_id="act4_tue_morning_school_arrival"
    ))

    # ── BRANCH B: Hide from mom (doomed endings later) ─────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_hide_from_mom",
        node_type=NodeType.NARRATION,
        act=4,
        text="You force your voice to sound normal as you head for the door, swallowing the knot of fear in your throat.",
        next_node_id="act4_tue_morning_mom_casual"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_mom_casual",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="mom",
        portrait="happy",
        text="Have a good day, okay? Text me if you and Maya hang out after school.",
        next_node_id="act4_tue_morning_leave_house_quiet"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_leave_house_quiet",
        node_type=NodeType.NARRATION,
        act=4,
        text="You mumble a quick goodbye and step outside, carrying the secret like an extra weight in your backpack.",
        next_node_id="act4_tue_morning_school_arrival"
    ))

    # ── SCHOOL ARRIVAL (both branches merge here) ──────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_school_arrival",
        node_type=NodeType.NARRATION,
        act=4,
        text="The school looks oddly hollow when you arrive. Conversations feel thinner, and a few desks sit empty in every class you pass.",
        next_node_id="act4_tue_morning_notice_elias_missing"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_notice_elias_missing",
        node_type=NodeType.NARRATION,
        act=4,
        text="In chemistry, the classroom door stays shut. A printed note on the board reads: \"Dr. Elias is absent today.\"",
        next_node_id="act4_tue_morning_player_reacts_elias"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_player_reacts_elias",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="suspicious",
        text="Perfect. The one person we were starting to suspect just… doesn't show up.",
        next_node_id="act4_tue_morning_hannah_short_scene"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_morning_hannah_short_scene",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="hannah",
        portrait="nervous",
        text="If any of you hear from missing classmates — or see anything strange — you come to me or the office immediately. No rumors, only facts.",
        next_node_id="act4_tue_day_montage_agitated"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_day_montage_agitated",
        node_type=NodeType.NARRATION,
        act=4,
        text="The rest of the day blurs into restless lessons and unanswered questions. Every time your phone buzzes, you hope it's Maya. It never is.",
        next_node_id="act4_tue_afternoon_tell_hannah"
    ))

    # ── AFTERNOON: TELL H ───────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_afternoon_tell_hannah",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="scared",
        text="Dr. Hannah, I need to talk to you. Maya's missing… and so is Dr. Elias.",
        next_node_id="act4_tue_afternoon_hannah_reacts"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_afternoon_hannah_reacts",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="hannah",
        portrait="shocked",
        text="Both of them? Stay after school. We're not handling this alone.",
        next_node_id="act4_tue_after_school_with_hannah"
    ))

    # ── AFTER SCHOOL: TRACKING PING ───────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_after_school_with_hannah",
        node_type=NodeType.NARRATION,
        act=4,
        text="After the final bell, the two of you — Dr. Hannah and you — sit in her empty classroom, the space where Maya should be felt more than seen.",
        next_node_id="act4_tue_after_school_tracking_ping"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_after_school_tracking_ping",
        node_type=NodeType.NARRATION,
        act=4,
        text="As you sit in Dr. Hannah's classroom, your phone vibrates. The tracking app flickers — Maya's icon suddenly lights up, far outside town, then holds steady.",
        next_node_id="act4_tue_after_school_old_church_reveal"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_after_school_old_church_reveal",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="shocked",
        text="The signal's back… It's coming from some abandoned spot past the fields. Looks like — an old church?",
        next_node_id="act4_tue_after_school_hannah_decision"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_after_school_hannah_decision",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="hannah",
        portrait="nervous",
        text="If that's where she is, Elias might be there too. We don't have much time. But going in alone could be a trap.",
        next_node_id="act4_tue_choice_call_police"
    ))

    # ── CHOICE: Call police or go alone ───────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_choice_call_police",
        node_type=NodeType.CHOICE,
        act=4,
        text="Maya's signal is holding. You have to decide — now.",
        choices=[
            Choice("Call the police and wait for backup.", "act4_tue_call_police", choice_to_record="called_police_church"),
            Choice("Go with Dr. Hannah alone to the church.", "act4_tue_go_with_hannah", choice_to_record="went_with_hannah_alone"),
        ]
    ))

    # ── BRANCH A: Call police (everyone dies — bad ending) ─────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_call_police",
        node_type=NodeType.NARRATION,
        act=4,
        text="Dr. Hannah dials emergency services with shaking hands while you read the coordinates off your phone. Within minutes, sirens growl in the distance.",
        next_node_id="act4_tue_police_arrive"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_police_arrive",
        node_type=NodeType.NARRATION,
        act=4,
        text="Police cars and a small tactical van line the dirt road leading to the abandoned church. Officers fan out, guns raised, as you and Dr. Hannah are held back behind the cars.",
        next_node_id="act4_tue_elias_trap_revealed"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_elias_trap_revealed",
        node_type=NodeType.NARRATION,
        act=4,
        text="The front doors creak open on their own. For a heartbeat, everything is silent — then a faint, rapid beeping echoes from inside the building.",
        next_node_id="ending_bad_police_explosion"
    ))

    tree.add_node(StoryNode(
        node_id="ending_bad_police_explosion",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="narrator",
        portrait="none",
        text="Elias had planned for heroes. The explosion tore through the church and the road alike, swallowing police, teachers, and students in one blinding wave.",
        next_node_id=None
    ))

    # ── BRANCH B: Go with Dr. Hannah alone (main route to 3 finales) ────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_go_with_hannah",
        node_type=NodeType.NARRATION,
        act=4,
        text="You and Dr. Hannah share a look, then slip out the side door before anyone can stop you. The last bell's echo fades behind you as you head for the edge of town.",
        next_node_id="act4_tue_church_approach"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_church_approach",
        node_type=NodeType.NARRATION,
        act=4,
        text="The old church looms at the end of a cracked road, its windows boarded and its doors hanging crooked. The air feels heavier with each step closer.",
        next_node_id="act4_tue_church_elias_greeting"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_church_elias_greeting",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="elias",
        portrait="suspicious",
        text="I was wondering when you'd arrive.",
        next_node_id="act4_tue_church_interior_reveal"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_church_interior_reveal",
        node_type=NodeType.NARRATION,
        act=4,
        text="Inside, candles throw long shadows across broken pews. The missing kids are chained along the walls, and from the ceiling, Maya hangs upside down, wrists bound but still moving.",
        next_node_id="act4_tue_church_cup_and_demon"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_church_cup_and_demon",
        node_type=NodeType.NARRATION,
        act=4,
        text="At the altar, Elias stands with a red-gold cup in his hands. Dark liquid swirls inside, reflecting a colour deeper than blood.",
        next_node_id="act4_tue_elias_monologue_start"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_elias_monologue_start",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="elias",
        portrait="angry",
        text="Do you know what it's like to be invisible? To give everything and still be forgotten? This cup… it remembers me.",
        next_node_id="act4_tue_elias_transform"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_elias_transform",
        node_type=NodeType.NARRATION,
        act=4,
        text="His eyes flare an unnatural red. The air around him ripples as his smile twists, features sharpening into something inhuman.",
        next_node_id="act4_tue_elias_demon_form"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_elias_demon_form",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="elias",
        portrait="demon",
        text="Every soul feeds the bargain. One more, and I go home. One more, and the rest of you walk free.",
        next_node_id="act4_tue_final_choice_setup"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_final_choice_setup",
        node_type=NodeType.NARRATION,
        act=4,
        text="Dr. Hannah steps in front of you, shielding you with one arm. Maya's muffled shout echoes from above as the cup's glow pulses brighter.",
        next_node_id="act4_tue_final_choice"
    ))

    # ── THE FINAL CHOICE ───────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_final_choice",
        node_type=NodeType.CHOICE,
        act=4,
        text="The cup glows. Elias waits. One soul to end this.",
        choices=[
            Choice("Offer yourself to save everyone else.", "ending_sacrifice_self"),
            Choice("Let Dr. Hannah forward to save you and Maya.", "ending_sacrifice_hannah"),
            Choice("Refuse to choose and stall for time.", "act4_tue_stall_for_time"),
        ]
    ))

    # ── ENDING 1: Sacrifice self (Good Ending) ─────────────────────────────

    tree.add_node(StoryNode(
        node_id="ending_sacrifice_self",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="sad",
        text="If it's one soul you want… take mine. Let them go.",
        next_node_id="ending_sacrifice_self_narration"
    ))

    tree.add_node(StoryNode(
        node_id="ending_sacrifice_self_narration",
        node_type=NodeType.NARRATION,
        act=4,
        text="The cup's surface splits into a spiral of red as the air rushes out of your lungs. Elias is dragged screaming into the dark, and when the light fades, the chains are empty and the kids are free.",
        next_node_id=None
    ))

    # ── ENDING 2: Sacrifice Dr. Hannah (Bad Ending) ──────────────────────────────

    tree.add_node(StoryNode(
        node_id="ending_sacrifice_hannah",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="hannah",
        portrait="happy",
        text="If it has to be someone… it doesn't have to be the kids!",
        next_node_id="ending_sacrifice_hannah_narration"
    ))

    tree.add_node(StoryNode(
        node_id="ending_sacrifice_hannah_narration",
        node_type=NodeType.NARRATION,
        act=4,
        text="Dr. Hannah's eyes stay calm as Elias drags her toward the altar. The cup swallows her valiant expression, and the demon vanishes with her, leaving you, Maya, and the rescued kids to face a future built on the choice you made.",
        next_node_id="act4_credits_or_return_menu"
    ))

    # ── PATH 3: Stall for time (branches on mom choice) ──────────────────────

    tree.add_node(StoryNode(
        node_id="act4_tue_stall_for_time",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="player",
        portrait="angry",
        text="No. I'm not playing your game. You don't get to choose who matters.",
        next_node_id="act4_tue_stall_chase"
    ))

    tree.add_node(StoryNode(
        node_id="act4_tue_stall_chase",
        node_type=NodeType.NARRATION,
        act=4,
        text="Elias snarls and hurls the cup aside as he lunges from the altar. Candles topple, chains rattle, and the kids scream as you and Dr. Hannah run between the pews.",
        next_node_id="act4_tue_true_ending_branch"
    ))

    # ── BRANCH 3A: True Good Ending (only if told_mom_about_maya is set) ───

    tree.add_node(StoryNode(
        node_id="act4_tue_true_ending_branch",
        node_type=NodeType.NARRATION,
        act=4,
        text="You duck behind a pew as Elias sweeps a candle rack aside. Every second you stay alive is a second the door might burst open.",
        next_node_id="ending_true_final"
    ))

    tree.add_node(StoryNode(
        node_id="ending_true_final",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="narrator",
        portrait="none",
        text="Just as Elias closes in, sirens wail outside. Police flood the church, and under your shout to \"shoot the cup\", bullets shatter the cursed relic. The demon howls, the red in his eyes burning out as he collapses for the last time.",
        next_node_id="act4_credits_or_return_menu",
        requires_flag="told_mom_about_maya"
    ))

    # ── BRANCH 3B: No-mom version (you die) ────────────────────────────────

    tree.add_node(StoryNode(
        node_id="ending_bad_no_mom_help",
        node_type=NodeType.DIALOGUE,
        act=4,
        speaker="narrator",
        portrait="none",
        text="No help ever comes. Your legs give out before your courage does, and the last thing you see is the cup's red glow closing in. Somewhere far away, the world keeps turning, never knowing how close it came.",
        next_node_id=None
    ))

    # ── CREDITS / RETURN TO MENU ──────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act4_credits_or_return_menu",
        node_type=NodeType.NARRATION,
        act=4,
        text="The church falls silent. Somewhere behind you, Maya breathes out a shaky breath. It's over.",
        next_node_id=None
    ))