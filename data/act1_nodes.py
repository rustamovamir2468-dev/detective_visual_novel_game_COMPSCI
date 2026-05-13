ACT1_NODES = {

    # =========================================================
    #  MONDAY
    # =========================================================

    "act1_bedroom_monday_morning": {
        "type": "NARRATION",
        "act": 1,
        "text": "It's Monday morning. Your alarm cuts through the silence of your room.",
        "next": "act1_bedroom_phone_buzz",
    },

    "act1_bedroom_phone_buzz": {
        "type": "NARRATION",
        "act": 1,
        "text": "Your phone buzzes on the nightstand with a new message.",
        "next": "act1_bedroom_player_reads_maya",
    },

    "act1_bedroom_player_reads_maya": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "sad",
        "text": "Maya again\u2026 She says she\u2019s still sick and won\u2019t be in today.",
        "next": "act1_bedroom_player_thinks_maya",
    },

    "act1_bedroom_player_thinks_maya": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "nervous",
        "text": "It\u2019s been days now. I really hope she\u2019s okay.",
        "next": "act1_house_hallway_mom_calls",
    },

    "act1_house_hallway_mom_calls": {
        "type": "NARRATION",
        "act": 1,
        "text": "You grab your bag and head for the front door. The smell of toasted bread and peanut butter drifts from the kitchen.",
        "next": "act1_house_door_mom_lunch",
    },

    "act1_house_door_mom_lunch": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "mom",
        "portrait": "happy",
        "text": "I packed your favourite today, peanut\u2011butter jelly sandwiches.",
        "next": "act1_house_door_player_reply",
    },

    "act1_house_door_player_reply": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "happy",
        "text": "Thanks, mom. You\u2019re the best.",
        "next": "act1_house_exit_walk_to_school",
    },

    "act1_house_exit_walk_to_school": {
        "type": "NARRATION",
        "act": 1,
        "text": "You step out into the cool morning air, lunchbox in hand, and start the walk to school.",
        "next": "act1_school_cs_class_intro",
    },

    "act1_school_cs_class_intro": {
        "type": "NARRATION",
        "act": 1,
        "text": "The day blurs by until computer science, your last and favourite class of the day.",
        "next": "act1_school_cs_player_thought",
    },

    "act1_school_cs_player_thought": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "happy",
        "text": "I love this class\u2026 but as a final period, it always drags.",
        "next": "act1_school_cs_look_out_window",
    },

    "act1_school_cs_look_out_window": {
        "type": "NARRATION",
        "act": 1,
        "text": "Your attention drifts to the window. Outside, a tall figure leads a younger student in a red jacket toward the side gate.",
        "next": "act1_school_cs_strange_line",
    },

    "act1_school_cs_strange_line": {
        "type": "NARRATION",
        "act": 1,
        "text": "You can\u2019t hear everything, but one sentence cuts through the noise: \u201cYou need some disciplining.\u201d",
        "next": "act1_school_cs_player_reacts",
    },

    "act1_school_cs_player_reacts": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "suspicious",
        "text": "Unlucky kid...",
        "next": "act1_street_sunset_walk_home",
    },

    "act1_street_sunset_walk_home": {
        "type": "NARRATION",
        "act": 1,
        "text": "Classes end. You walk home alone under an orange sunset, the image of the red jacket still stuck in your mind.",
        "next": "act1_monday_end_fade",
    },

    "act1_monday_end_fade": {
        "type": "NARRATION",
        "act": 1,
        "text": "The street grows darker as you turn the last corner toward home.",
        "next": "act1_tuesday_morning_house_front",
    },

    # =========================================================
    #  TUESDAY
    # =========================================================

    "act1_tuesday_morning_house_front": {
        "type": "NARRATION",
        "act": 1,
        "text": "It\u2019s the next morning. You stand by the front door, tying your laces as the sun creeps over the rooftops.",
        "next": "act1_tuesday_morning_bye_mom",
    },

    "act1_tuesday_morning_bye_mom": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "happy",
        "text": "Bye, mom! I\u2019m off to school!",
        "next": "act1_tuesday_morning_mom_reply",
    },

    "act1_tuesday_morning_mom_reply": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "mom",
        "portrait": "happy",
        "text": "Have a good day, sweetie. Text me if you need anything.",
        "next": "act1_tuesday_walk_maya_surprise",
    },

    "act1_tuesday_walk_maya_surprise": {
        "type": "NARRATION",
        "act": 1,
        "text": "You pull the door shut and start down the familiar street. Footsteps rush up behind you.",
        "next": "act1_tuesday_walk_maya_appears",
    },

    "act1_tuesday_walk_maya_appears": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "maya",
        "portrait": "happy",
        "text": "Guess who\u2019s finally back from the dead?",
        "next": "act1_tuesday_walk_player_reacts",
    },

    "act1_tuesday_walk_player_reacts": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "happy",
        "text": "Maya! You scared me. I thought you were still sick.",
        "next": "act1_tuesday_walk_chat_leads_red_jacket",
    },

    "act1_tuesday_walk_chat_leads_red_jacket": {
        "type": "NARRATION",
        "act": 1,
        "text": "You fall into step together, trading stories about homework, teachers, and how boring the past 3 days were without her.",
        "next": "act1_tuesday_walk_player_mentions_yesterday",
    },

    "act1_tuesday_walk_player_mentions_yesterday": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "nervous",
        "text": "Actually\u2026 something weird did happen yesterday. I saw a kid in a red jacket being led away by some tall teacher near the side gate.",
        "next": "act1_tuesday_walk_maya_reacts_red_jacket",
    },

    "act1_tuesday_walk_maya_reacts_red_jacket": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "maya",
        "portrait": "suspicious",
        "text": "That\u2019s creepy. Maybe it was just detention or something? Still, red jacket\u2026 kind of stands out.",
        "next": "act1_tuesday_school_corridor_transition",
    },

    "act1_tuesday_school_corridor_transition": {
        "type": "NARRATION",
        "act": 1,
        "text": "The school buildings rise into view. The morning bell shrieks, and the corridor floods with students hurrying to class.",
        "next": "act1_tuesday_physics_finn_intro",
    },

    "act1_tuesday_physics_finn_intro": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "neutral",
        "text": "First up: physics with Dr. Finn. Lucky me.",
        "next": "act1_tuesday_physics_classroom_scene",
    },

    "act1_tuesday_physics_classroom_scene": {
        "type": "NARRATION",
        "act": 1,
        "text": "You take your seat. Dr. Finn, the stern, grey\u2011haired teacher, scribbles equations across the board while the class half\u2011listens.",
        "next": "act1_tuesday_physics_finn_line",
    },

    "act1_tuesday_physics_finn_line": {
        "type": "NARRATION",
        "act": 1,
        "text": "A student loudly laughs with his friends. Dr. Finn slams the chalk down and snaps, \u201cYou need some disciplining!\u201d",
        "next": "act1_tuesday_physics_player_ears_prick",
    },

    "act1_tuesday_physics_player_ears_prick": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "shocked",
        "text": "Wait\u2026 that\u2019s the exact same line from yesterday.",
        "next": "act1_tuesday_chem_elias_intro",
    },

    "act1_tuesday_chem_elias_intro": {
        "type": "NARRATION",
        "act": 1,
        "text": "Physics drags to an end. Later, in chemistry, the air feels lighter. Dr. Elias smiles as he wipes his hands on his red scarf.",
        "next": "act1_tuesday_chem_elias_no_homework",
    },

    "act1_tuesday_chem_elias_no_homework": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "elias",
        "portrait": "happy",
        "text": "No homework today, guys. Just make sure you actually listened this time.",
        "next": "act1_tuesday_chem_player_still_thinking",
    },

    "act1_tuesday_chem_player_still_thinking": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "nervous",
        "text": "Everyone else is cheering, but I can\u2019t stop thinking about Finn and that red jacket.",
        "next": "act1_tuesday_chem_overhear_red_jacket",
    },

    "act1_tuesday_chem_overhear_red_jacket": {
        "type": "NARRATION",
        "act": 1,
        "text": "Across the room, a girl whispers to her friends. The words \u201cred jacket\u201d and \u201cyesterday\u201d drift over the bubbling beakers.",
        "next": "act1_tuesday_choice_candy",
    },

    # =========================================================
    #  CHOICE — candy / speak up vs stay quiet
    # =========================================================

    "act1_tuesday_choice_candy": {
        "type": "CHOICE",
        "act": 1,
        "choices": [
            {
                "text": "Speak up about what you saw.",
                "next": "act1_tuesday_candy_speak_up",
                "record": "spoke_up_red_jacket",
            },
            {
                "text": "Stay quiet and mind your own business.",
                "next": "act1_tuesday_candy_stay_quiet",
                "record": "stayed_quiet_red_jacket",
            },
        ],
    },

    # =========================================================
    #  BRANCH 1 — Speak up (bad ending: poisoned candy)
    # =========================================================

    "act1_tuesday_candy_speak_up": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "nervous",
        "text": "Hey\u2026 about that red jacket. I think I saw someone being led away yesterday near the side gate.",
        "next": "act1_tuesday_candy_class_reacts",
    },

    "act1_tuesday_candy_class_reacts": {
        "type": "NARRATION",
        "act": 1,
        "text": "The girl you heard whispering goes quiet. Her friends trade uneasy looks, while a few other students turn in their seats to listen.",
        "next": "act1_tuesday_candy_elias_reassures",
    },

    "act1_tuesday_candy_elias_reassures": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "elias",
        "portrait": "happy",
        "text": "Whoa, that sounds serious. But let\u2019s not panic, okay? If something\u2019s wrong, the school and the police will handle it.",
        "next": "act1_tuesday_candy_elias_uses_candy",
    },

    "act1_tuesday_candy_elias_uses_candy": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "elias",
        "portrait": "happy",
        "text": "You all look exhausted. Here\u2014little sugar never hurt anyone. I brought candy to celebrate finishing the topic.",
        "next": "act1_tuesday_candy_distribution",
    },

    "act1_tuesday_candy_distribution": {
        "type": "NARRATION",
        "act": 1,
        "text": "Dr. Elias moves between the rows with an easy smile, placing a bright, wrapped candy on each desk. The girl from before laughs it off and unwraps hers right away.",
        "next": "act1_tuesday_candy_player_eats",
    },

    "act1_tuesday_candy_player_eats": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "neutral",
        "text": "Guess I could use something sweet.",
        "next": "act1_tuesday_candy_player_feels_odd",
    },

    "act1_tuesday_candy_player_feels_odd": {
        "type": "NARRATION",
        "act": 1,
        "text": "The candy tastes strangely bitter at the end. A heavy fog settles behind your eyes as the bell rings.",
        "next": "act1_tuesday_candy_dizzy_hallway",
    },

    "act1_tuesday_candy_dizzy_hallway": {
        "type": "NARRATION",
        "act": 1,
        "text": "You drift into the hallway, each step heavier than the last. Students pass by in a blur of color and muffled voices.",
        "next": "ending_bad_candy",
    },

    "ending_bad_candy": {
        "type": "ENDING",
        "act": 1,
        "speaker": "narrator",
        "portrait": "none",
        "text": "You reached for answers too soon. The world tilted, the lights went out, and no one was there to see you fall.",
        "ending_type": "bad",
    },

    # =========================================================
    #  BRANCH 2 — Stay quiet (main route)
    # =========================================================

    "act1_tuesday_candy_stay_quiet": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "nervous",
        "text": "If I say something now and I\u2019m wrong, I\u2019ll just sound paranoid. Maybe it\u2019s nothing.",
        "next": "act1_tuesday_candy_homework_check",
    },

    "act1_tuesday_candy_homework_check": {
        "type": "NARRATION",
        "act": 1,
        "text": "Dr. Elias strolls between the desks, glancing at open notebooks. When he reaches the girl and her group, his smile fades just a little.",
        "next": "act1_tuesday_candy_elias_scolds_student",
    },

    "act1_tuesday_candy_elias_scolds_student": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "elias",
        "portrait": "neutral",
        "text": "You didn\u2019t do the homework again? Come on, you\u2019re smart. You can do better than this. See me after class, alright?",
        "next": "act1_tuesday_candy_elias_softens",
    },

    "act1_tuesday_candy_elias_softens": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "elias",
        "portrait": "happy",
        "text": "Everyone else, relax. You\u2019ve worked hard this week.",
        "next": "act1_tuesday_candy_everyone_else_gets_candy",
    },

    "act1_tuesday_candy_everyone_else_gets_candy": {
        "type": "NARRATION",
        "act": 1,
        "text": "He pulls a small bag from his drawer and begins handing out candy down the rows. Laughter ripples through the room as wrappers crinkle. The girl without homework watches, a little embarrassed, as he skips her desk and moves on.",
        "next": "act1_tuesday_after_school_walk_home_maya",
    },

    "act1_tuesday_after_school_walk_home_maya": {
        "type": "NARRATION",
        "act": 1,
        "text": "Classes finally end. You and Maya leave the gates together, the sky melting into shades of orange and pink.",
        "next": "act1_tuesday_after_school_talk_finn",
    },

    "act1_tuesday_after_school_talk_finn": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "maya",
        "portrait": "suspicious",
        "text": "So\u2026 what do you think about Finn now? He looked like he wanted to throw that kid out the window.",
        "next": "act1_tuesday_after_school_player_reply_finn",
    },

    "act1_tuesday_after_school_player_reply_finn": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "suspicious",
        "text": "It\u2019s the same line as yesterday. Call me crazy, but I can\u2019t shake the feeling something\u2019s wrong.",
        "next": "act1_tuesday_evening_bedroom_intro",
    },

    "act1_tuesday_evening_bedroom_intro": {
        "type": "NARRATION",
        "act": 1,
        "text": "Later that evening, you\u2019re back in your room, half\u2011focused on your phone when a soft knock sounds at the door.",
        "next": "act1_tuesday_evening_mom_brings_food",
    },

    "act1_tuesday_evening_mom_brings_food": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "mom",
        "portrait": "happy",
        "text": "Here\u2019s your food. You must be starving after school.",
        "next": "act1_tuesday_evening_player_food_reply",
    },

    "act1_tuesday_evening_player_food_reply": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "neutral",
        "text": "Thanks, mom. It smells great.",
        "next": "act1_tuesday_evening_mom_news",
    },

    "act1_tuesday_evening_mom_news": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "mom",
        "portrait": "nervous",
        "text": "By the way\u2026 have you seen the news? There was a kidnapping of a kid from your school. Westwood School.",
        "next": "act1_tuesday_evening_player_reacts_news",
    },

    "act1_tuesday_evening_player_reacts_news": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "player",
        "portrait": "shocked",
        "text": "A kidnapping? From my school? That can\u2019t be a coincidence\u2026",
        "next": "act1_tuesday_night_bed_intro",
    },

    "act1_tuesday_night_bed_intro": {
        "type": "NARRATION",
        "act": 1,
        "text": "That night, you lie in bed staring at the ceiling. Every creak of the house sounds like a footstep in the dark.",
        "next": "act1_tuesday_nightmare_start",
    },

    "act1_tuesday_nightmare_start": {
        "type": "NARRATION",
        "act": 1,
        "text": "Sleep finally drags you under. In your dream, the world is soaked in dark red. Voices whisper from every direction.",
        "next": "act1_tuesday_nightmare_voice_line",
    },

    "act1_tuesday_nightmare_voice_line": {
        "type": "DIALOGUE",
        "act": 1,
        "speaker": "narrator",
        "portrait": "none",
        "text": "Shadows crowd around you. A distorted voice booms from nowhere: \u201cNo distinction for you!\u201d",
        "next": "act1_end_of_act1",
    },

    "act1_end_of_act1": {
        "type": "ENDING",
        "act": 1,
        "speaker": "narrator",
        "portrait": "none",
        "text": "You jolt awake, heart racing, the words still echoing in your ears.",
        "ending_type": "act_end",
        "next_act": 2,
        "next": "act2_wed_morning_news_intro",
    },
}

# =========================================================
#  Quick sanity check — run this file directly to verify
#  every non-ending node's "next" key resolves to a key
#  that exists in this dict (cross-act links excluded).
# =========================================================
if __name__ == "__main__":
    cross_act_entry = "act2_wed_morning_news_intro"
    errors = []
    for node_id, node in ACT1_NODES.items():
        if node["type"] == "CHOICE":
            for choice in node["choices"]:
                target = choice["next"]
                if target not in ACT1_NODES:
                    errors.append(f"CHOICE '{node_id}' -> '{target}' NOT FOUND")
        elif node["type"] in ("ENDING",):
            # endings may point to cross-act nodes or have no next — both are fine
            pass
        else:
            target = node.get("next")
            if target and target not in ACT1_NODES and target != cross_act_entry:
                errors.append(f"NODE '{node_id}' -> '{target}' NOT FOUND")

    if errors:
        print("ERRORS FOUND:")
        for e in errors:
            print(" ", e)
    else:
        print(f"All {len(ACT1_NODES)} Act 1 nodes verified OK.")
