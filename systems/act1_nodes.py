# systems/act1_nodes.py - Act 1 story nodes (Monday and Tuesday).
# Author(s): 5752530
# ====================================================

from systems.story_tree import StoryTree, StoryNode, NodeType, Choice
from settings import *


def add_act1_nodes(tree: StoryTree):

    # =========================================================
    # MONDAY
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_bedroom_monday_morning",
        node_type=NodeType.NARRATION,
        text="It's Monday morning. Your alarm cuts through the silence of your room.",
        bg="room_day",
        next_node_id="act1_bedroom_phone_buzz",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_bedroom_phone_buzz",
        node_type=NodeType.NARRATION,
        text="Your phone buzzes on the nightstand with a new message.",
        next_node_id="act1_bedroom_player_reads_maya",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_bedroom_player_reads_maya",
        node_type=NodeType.DIALOGUE,
        text="Maya again. She says she's still sick and won't be in today.",
        speaker="[PLAYER]",
        portrait=("player", "sad"),
        next_node_id="act1_bedroom_player_thinks_maya",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_bedroom_player_thinks_maya",
        node_type=NodeType.DIALOGUE,
        text="It's been days now. I really hope she's okay.",
        speaker="[PLAYER]",
        portrait=("player", "nervous"),
        next_node_id="act1_house_hallway_mom_calls",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_house_hallway_mom_calls",
        node_type=NodeType.NARRATION,
        text="You grab your bag and head for the front door. The smell of toasted bread and peanut butter drifts from the kitchen.",
        bg="kitchen_day",
        next_node_id="act1_house_door_mom_lunch",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_house_door_mom_lunch",
        node_type=NodeType.DIALOGUE,
        text="I packed your favourite today, peanut-butter jelly sandwiches.",
        speaker="mom",
        portrait=("mom", "happy"),
        next_node_id="act1_house_door_player_reply",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_house_door_player_reply",
        node_type=NodeType.DIALOGUE,
        text="Thanks, mom. You're the best.",
        speaker="[PLAYER]",
        portrait=("player", "happy"),
        next_node_id="act1_house_exit_walk_to_school",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_house_exit_walk_to_school",
        node_type=NodeType.NARRATION,
        text="You step out into the cool morning air, lunchbox in hand, and start the walk to school.",
        bg="house_day",
        next_node_id="act1_school_cs_class_intro",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_school_cs_class_intro",
        node_type=NodeType.NARRATION,
        text="The day blurs by until computer science, your last and favourite class of the day.",
        bg="hallway_day",
        next_node_id="act1_school_cs_player_thought",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_school_cs_player_thought",
        node_type=NodeType.DIALOGUE,
        text="I love this class, but as a final period, it always drags.",
        bg="cs_class_sunset",
        speaker="[PLAYER]",
        portrait=("player", "happy"),
        next_node_id="act1_school_cs_look_out_window",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_school_cs_look_out_window",
        node_type=NodeType.NARRATION,
        text="Your attention drifts to the window. Outside, a tall figure leads a younger student in a red jacket toward the side gate.",
        bg="kidnap_scene",
        next_node_id="act1_cutscene_red_hood_kid_frame_1",
        act=ACT_1
    ))

    # HERE, RED HOOD KID AND TALL SILHOULETTE ON THE SIDE - 5744357
    tree.add_node(StoryNode(
        node_id   = "act1_cutscene_red_hood_kid_frame_1",
        node_type = NodeType.CUTSCENE,
        act       = 1,
        text      = "",           # no text needed
        bg        = None, # your bg key
        portrait  = None,
        next_node_id = "act1_cutscene_red_hood_kid_frame_2"
    ))

    # HERE, BOTH OF THEM DISSAPEARED, JUST BACKGROUND - 5744357
    tree.add_node(StoryNode(
        node_id   = "act1_cutscene_red_hood_kid_frame_2",
        node_type = NodeType.CUTSCENE,
        act       = 1,
        text      = "",           # no text needed
        bg        = None, # your bg key
        portrait  = None,
        next_node_id = "act1_school_cs_strange_line"
    ))

    tree.add_node(StoryNode(
        node_id="act1_school_cs_strange_line",
        node_type=NodeType.NARRATION,
        text="You can't hear everything, but one sentence cuts through the noise: \"You need some disciplining.\"",
        bg="hallway_sunset",
        next_node_id="act1_school_cs_player_reacts",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_school_cs_player_reacts",
        node_type=NodeType.DIALOGUE,
        text="Unlucky kid...",
        speaker="[PLAYER]",
        portrait=("player", "suspicious"),
        next_node_id="act1_street_sunset_walk_home",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_street_sunset_walk_home",
        node_type=NodeType.NARRATION,
        text="Classes end. You walk home alone under an orange sunset, the image of the red jacket still stuck in your mind.",
        bg="street_sunset",
        next_node_id="act1_monday_end_fade",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_monday_end_fade",
        node_type=NodeType.NARRATION,
        text="The street grows darker as you turn the last corner toward home.",
        next_node_id="act1_tuesday_morning_house_front",
        act=ACT_1
    ))

    # =========================================================
    # TUESDAY
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_morning_house_front",
        node_type=NodeType.NARRATION,
        text="It's the next morning. You stand by the front door, tying your laces as the sun creeps over the rooftops.",
        bg="room_day",
        next_node_id="act1_tuesday_morning_bye_mom",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_morning_bye_mom",
        node_type=NodeType.DIALOGUE,
        text="Bye, mom! I'm off to school!",
        bg="kitchen_day",
        speaker="[PLAYER]",
        portrait=("player", "happy"),
        next_node_id="act1_tuesday_morning_mom_reply",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_morning_mom_reply",
        node_type=NodeType.DIALOGUE,
        text="Have a good day, sweetie. Text me if you need anything.",
        speaker="mom",
        portrait=("mom", "neutral"),
        next_node_id="act1_tuesday_walk_maya_surprise",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_maya_surprise",
        node_type=NodeType.NARRATION,
        text="You pull the door shut and start down the familiar street. Footsteps rush up behind you.",
        bg="street_day",
        next_node_id="act1_cutscene_maya_returns",
        act=ACT_1
    ))

    # Maya appears Tuesday morning cutscene - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_maya_returns",
        node_type=NodeType.CUTSCENE,
        text="",
        bg=None,
        portrait=None,
        next_node_id="act1_tuesday_walk_maya_appears",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_maya_appears",
        node_type=NodeType.DIALOGUE,
        text="Guess who's finally back from the dead?",
        speaker="maya",
        portrait=("maya", "happy"),
        next_node_id="act1_tuesday_walk_player_reacts",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_player_reacts",
        node_type=NodeType.DIALOGUE,
        text="Maya! You scared me. I thought you were still sick.",
        speaker="[PLAYER]",
        portrait=("player", "happy"),
        next_node_id="act1_tuesday_walk_chat_leads_red_jacket",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_chat_leads_red_jacket",
        node_type=NodeType.NARRATION,
        text="You fall into step together, trading stories about homework, teachers, and how boring the past 3 days were without her.",
        next_node_id="act1_tuesday_walk_player_mentions_yesterday",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_player_mentions_yesterday",
        node_type=NodeType.DIALOGUE,
        text="Actually… something weird did happen yesterday. I saw a kid in a red jacket being led away by some tall teacher near the side gate.",
        speaker="[PLAYER]",
        portrait=("player", "nervous"),
        next_node_id="act1_tuesday_walk_maya_reacts_red_jacket",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_walk_maya_reacts_red_jacket",
        node_type=NodeType.DIALOGUE,
        text="That's creepy. Maybe it was just detention or something? Still, red jacket… kind of stands out.",
        speaker="maya",
        portrait=("maya", "neutral"),
        next_node_id="act1_tuesday_school_corridor_transition",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_school_corridor_transition",
        node_type=NodeType.NARRATION,
        text="The school buildings rise into view. The morning bell shrieks, and the corridor floods with students hurrying to class.",
        bg="hallway_day",
        next_node_id="act1_cutscene_school_corridor_rush",
        act=ACT_1
    ))

    # Crowded school corridor after the bell cutscene - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_school_corridor_rush",
        node_type=NodeType.CUTSCENE,
        text="",
        bg=None,
        portrait=None,
        next_node_id="act1_tuesday_physics_finn_intro",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_physics_finn_intro",
        node_type=NodeType.DIALOGUE,
        text="First up: physics with Dr. Finn. Lucky me.",
        bg="physics_classroom",
        speaker="[PLAYER]",
        portrait=("player", "neutral"),
        next_node_id="act1_tuesday_physics_classroom_scene",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_physics_classroom_scene",
        node_type=NodeType.NARRATION,
        text="You take your seat. Dr. Finn, the stern-looking teacher, scribbles equations across the board while the class half-listens.",
        next_node_id="act1_tuesday_physics_finn_line",
        act=ACT_1
    ))

    # HERE, SHOW A PICTURE OF 2 KIDS LAUGHING IN THE CLASS, WITHOUT THE DIALOGUE BOX - 5744357
    tree.add_node(StoryNode(
        node_id   = "act1_cutscene_kids_laughing_class",
        node_type = NodeType.CUTSCENE,
        act       = 1,
        text      = "",           # no text needed
        bg        = None, # your bg key
        portrait  = None,
        next_node_id = "act1_tuesday_physics_finn_line"
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_physics_finn_line",
        node_type=NodeType.NARRATION,
        text="A student loudly laughed with his friends. Dr. Finn slams the chalk down and snaps, \"You need some disciplining!\"",
        next_node_id="act1_cutscene_finn_pointing_kids",
        act=ACT_1
    ))

    # RIGHT AFTER, SHOW A PICTURE OF FELIX POINTING AT THE KIDS, WITHOUT THE DIALOGUE BOX - 5744357
    tree.add_node(StoryNode(
        node_id   = "act1_cutscene_finn_pointing_kids",
        node_type = NodeType.CUTSCENE,
        act       = 1,
        text      = "",           # no text needed
        bg        = None, # your bg key
        portrait  = None,
        next_node_id = "act1_tuesday_physics_player_ears_prick"
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_physics_player_ears_prick",
        node_type=NodeType.DIALOGUE,
        text="Wait… that's the exact same line from yesterday.",
        speaker="[PLAYER]",
        portrait=("player", "shocked"),
        next_node_id="act1_tuesday_chem_elias_intro",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_chem_elias_intro",
        node_type=NodeType.NARRATION,
        text="Physics drags to an end. Later, in chemistry, the air feels lighter. Dr. Elias smiles as he wipes his hands on his red scarf.",
        bg="chemistry_class_day",
        next_node_id="act1_cutscene_elias_chemistry_intro",
        act=ACT_1
    ))

    # Elias is introduced in the chemistry classroom cutscene - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_elias_chemistry_intro",
        node_type=NodeType.CUTSCENE,
        text="",
        bg=None,
        portrait=None,
        next_node_id="act1_tuesday_chem_elias_no_homework",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_chem_elias_no_homework",
        node_type=NodeType.DIALOGUE,
        text="No homework today, guys. Just make sure you actually listened this time.",
        bg="chemistry_class_sunset", 
        speaker="elias",
        portrait=("elias", "happy"),
        next_node_id="act1_tuesday_chem_player_still_thinking",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_chem_player_still_thinking",
        node_type=NodeType.DIALOGUE,
        text="Everyone else is cheering, but I can't stop thinking about Finn and that red jacket.",
        speaker="[PLAYER]",
        portrait=("player", "nervous"),
        next_node_id="act1_tuesday_chem_overhear_red_jacket",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_chem_overhear_red_jacket",
        node_type=NodeType.NARRATION,
        text="Across the room, a girl whispers to her friends. The words \"red jacket\" and \"yesterday\" drift over the bubbling beakers.",
        next_node_id="act1_tuesday_choice_candy",
        act=ACT_1
    ))

    # =========================================================
    # CHOICE: Speak up or stay quiet
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_choice_candy",
        node_type=NodeType.CHOICE,
        text="",
        choices=[
            Choice(
                text="Speak up about what you saw.",
                next_node_id="act1_tuesday_candy_speak_up",
                choice_to_record="spoke_up_red_jacket"
            ),
            Choice(
                text="Stay quiet and mind your own business.",
                next_node_id="act1_tuesday_candy_stay_quiet",
                choice_to_record="stayed_quiet_red_jacket"
            ),
        ],
        act=ACT_1
    ))

    # =========================================================
    # BRANCH 1: Speak up → BAD ENDING
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_speak_up",
        node_type=NodeType.DIALOGUE,
        text="Hey… about that red jacket. I think I saw someone being led away yesterday near the side gate.",
        speaker="[PLAYER]",
        portrait=("player", "nervous"),
        next_node_id="act1_tuesday_candy_class_reacts",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_class_reacts",
        node_type=NodeType.NARRATION,
        text="The girl you heard whispering goes quiet. Her friends trade uneasy looks, while a few other students turn in their seats to listen.",
        next_node_id="act1_tuesday_candy_elias_reassures",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_elias_reassures",
        node_type=NodeType.DIALOGUE,
        text="Whoa, that sounds serious. But let's not panic, okay? If something's wrong, the school and the police will handle it.",
        speaker="elias",
        portrait=("elias", "cold"),
        next_node_id="act1_tuesday_candy_elias_uses_candy",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_elias_uses_candy",
        node_type=NodeType.DIALOGUE,
        text="You all look exhausted. Here—little sugar never hurt anyone. I brought candy to celebrate finishing the topic.",
        speaker="elias",
        portrait=("elias", "happy"),
        next_node_id="act1_tuesday_candy_distribution",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_distribution",
        node_type=NodeType.NARRATION,
        text="Dr. Elias moves between the rows with an easy smile, placing a bright, wrapped candy on each desk. The girl from before laughs it off and unwraps hers right away.",
        next_node_id="act1_cutscene_candy_distribution",
        act=ACT_1
    ))

    # Elias gives candy to the class cutscene - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_candy_distribution",
        node_type=NodeType.CUTSCENE,
        text="",
        bg=None,
        portrait=None,
        next_node_id="act1_tuesday_candy_player_eats",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_player_eats",
        node_type=NodeType.DIALOGUE,
        text="Guess I could use something sweet.",
        speaker="[PLAYER]",
        portrait=("player", "neutral"),
        next_node_id="act1_tuesday_candy_player_feels_odd",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_player_feels_odd",
        node_type=NodeType.NARRATION,
        text="The candy tastes strangely bitter at the end. A heavy fog settles behind your eyes as the bell rings.",
        next_node_id="act1_tuesday_candy_dizzy_hallway",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_dizzy_hallway",
        node_type=NodeType.NARRATION,
        text="You drift into the hallway, each step heavier than the last. Students pass by in a blur of colour and muffled voices.",
        bg="hallway_sunset",
        next_node_id="ending_bad_candy",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="ending_bad_candy",
        node_type=NodeType.NARRATION,
        text="You reached for answers too soon. The world tilted, the lights went out, and no one was there to see you fall.",
        next_node_id=None,
        act=ACT_1
    ))

    # =========================================================
    # BRANCH 2: Stay quiet → MAIN ROUTE
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_stay_quiet",
        node_type=NodeType.DIALOGUE,
        text="If I say something now and I'm wrong, I'll just sound paranoid. Maybe it's nothing.",
        bg="chemistry_class_sunset",
        speaker="[PLAYER]",
        portrait=("player", "nervous"),
        next_node_id="act1_tuesday_candy_homework_check",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_homework_check",
        node_type=NodeType.NARRATION,
        text="Dr. Elias strolls between the desks, glancing at open notebooks. When he reaches the girl and her group, his smile fades just a little.",
        next_node_id="act1_tuesday_candy_elias_scolds_student",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_elias_scolds_student",
        node_type=NodeType.DIALOGUE,
        text="You didn't do the homework again? Come on, you're smart. You can do better than this. See me after class, alright?",
        speaker="elias",
        portrait=("elias", "neutral"),
        next_node_id="act1_tuesday_candy_elias_softens",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_elias_softens",
        node_type=NodeType.DIALOGUE,
        text="Everyone else, relax. You've worked hard this week.",
        speaker="elias",
        portrait=("elias", "happy"),
        next_node_id="act1_tuesday_candy_everyone_else_gets_candy",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_candy_everyone_else_gets_candy",
        node_type=NodeType.NARRATION,
        text="He pulls a small bag from his drawer and begins handing out candy down the rows. Laughter ripples through the room as wrappers crinkle. The girl without homework watches, a little embarrassed, as he skips her desk and moves on.",
        next_node_id="act1_tuesday_after_school_walk_home_maya",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_after_school_walk_home_maya",
        node_type=NodeType.NARRATION,
        text="Classes finally end. You and Maya leave the gates together, the sky melting into shades of orange and pink.",
        bg="street_sunset",
        next_node_id="act1_tuesday_after_school_talk_finn",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_after_school_talk_finn",
        node_type=NodeType.DIALOGUE,
        text="So… what do you think about Finn now? He looked like he wanted to throw that kid out the window.",
        speaker="maya",
        portrait=("maya", "nervous"),
        next_node_id="act1_tuesday_after_school_player_reply_finn",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_after_school_player_reply_finn",
        node_type=NodeType.DIALOGUE,
        text="It's the same line as yesterday. Call me crazy, but I can't shake the feeling something's wrong.",
        speaker="[PLAYER]",
        portrait=("player", "suspicious"),
        next_node_id="act1_tuesday_evening_bedroom_intro",
        act=ACT_1
    ))

    # =========================================================
    # TUESDAY EVENING
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_evening_bedroom_intro",
        node_type=NodeType.NARRATION,
        text="Later that evening, you're back in your room, half-focused on your phone when a soft knock sounds at the door.",
        bg="room_sunset",
        next_node_id="act1_tuesday_evening_mom_brings_food",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_evening_mom_brings_food",
        node_type=NodeType.DIALOGUE,
        text="Here's your food. You must be starving after school.",
        speaker="mom",
        portrait=("mom", "happy"),
        next_node_id="act1_tuesday_evening_player_food_reply",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_evening_player_food_reply",
        node_type=NodeType.DIALOGUE,
        text="Thanks, mom. It smells great.",
        speaker="[PLAYER]",
        portrait=("player", "neutral"),
        next_node_id="act1_tuesday_evening_mom_news",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_evening_mom_news",
        node_type=NodeType.DIALOGUE,
        text="By the way… have you seen the news? There was a kidnapping of a kid from your school. Westwood School.",
        speaker="mom",
        portrait=("mom", "nervous"),
        next_node_id="act1_cutscene_evening_news_reveal",
        act=ACT_1
    ))

    # TV news cutscene - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_evening_news_reveal",
        node_type=NodeType.CUTSCENE,
        text="",
        bg=None,
        portrait=None,
        next_node_id="act1_tuesday_evening_player_reacts_news",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_evening_player_reacts_news",
        node_type=NodeType.DIALOGUE,
        text="A kidnapping? From my school? That can't be a coincidence…",
        bg="room_sunset",
        speaker="[PLAYER]",
        portrait=("player", "shocked"),
        next_node_id="act1_tuesday_night_bed_intro",
        act=ACT_1
    ))

    # =========================================================
    # TUESDAY NIGHT / NIGHTMARE
    # =========================================================

    tree.add_node(StoryNode(
        node_id="act1_tuesday_night_bed_intro",
        node_type=NodeType.NARRATION,
        text="That night, you lie in bed staring at the ceiling. Every creak of the house sounds like a footstep in the dark.",
        bg="room_sunset",
        next_node_id="act1_tuesday_nightmare_start",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_nightmare_start",
        node_type=NodeType.NARRATION,
        text="Sleep finally drags you under. In your dream, the world is soaked in dark red. Voices whisper from every direction.",
        bg="black_screen",
        next_node_id="act1_cutscene_nightmare_red_world",
        act=ACT_1
    ))

    # Nightmare begins with dark red theme - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_nightmare_red_world",
        node_type=NodeType.CUTSCENE,
        text="",
        bg="finn_nightmare",
        portrait=None,
        next_node_id="act1_cutscene_nightmare_shadows",
        act=ACT_1
    ))

    # Shadow figures appear in the nightmare: NO DISTINCTION - 5744357
    tree.add_node(StoryNode(
        node_id="act1_cutscene_nightmare_shadows",
        node_type=NodeType.CUTSCENE,
        text="",
        bg="finn_nightmare_2",
        portrait=None,
        next_node_id="act1_tuesday_nightmare_voice_line",
        act=ACT_1
    ))

    tree.add_node(StoryNode(
        node_id="act1_tuesday_nightmare_voice_line",
        node_type=NodeType.NARRATION,
        text="Shadows crowd around you. A distorted voice booms from nowhere: \"No distinction for you!\"",
        next_node_id="act1_end_of_act1",
        act=ACT_1
    ))

    # Dark room of player as bg
    tree.add_node(StoryNode(
        node_id="act1_end_of_act1",
        node_type=NodeType.NARRATION,
        text="You jolt awake, heart racing, the words still echoing in your ears.",
        bg="room_sunset",
        next_node_id="act2_wed_morning_news_intro",
        act=ACT_1
    ))