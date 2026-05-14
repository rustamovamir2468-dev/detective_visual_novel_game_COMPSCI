# systems/act2_nodes.py - Act 2 story nodes (Wednesday & Thursday)
# Author(s): 5752530
# ====================================================
from systems.story_tree import StoryTree, StoryNode, NodeType, Choice


def add_act2_nodes(tree: StoryTree):

    # ── WEDNESDAY ──────────────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_news_intro",
        node_type=NodeType.NARRATION,
        act=2,
        text="The second missing-kid headline has everyone on edge. Every TV in town seems stuck on the same news channel.",
        next_node_id="act2_wed_morning_player_leaves_home"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_player_leaves_home",
        node_type=NodeType.NARRATION,
        act=2,
        text="You rush through your morning routine and head out, the reporter's voice still echoing in your mind.",
        next_node_id="act2_wed_morning_school_gate_guard"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_school_gate_guard",
        node_type=NodeType.NARRATION,
        act=2,
        text="At the school gate, a new security guard stands stiffly by the entrance, scanning each student as they walk in.",
        next_node_id="act2_wed_morning_guard_interaction_choice"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_guard_interaction_choice",
        node_type=NodeType.CHOICE,
        act=2,
        text="The guard's eyes land on you.",
        choices=[
            Choice("Give the guard a quick nod.", "act2_wed_morning_guard_smalltalk", choice_to_record="nodded_at_guard"),
            Choice("Keep your head down and walk straight through.", "act2_wed_morning_guard_ignore", choice_to_record="ignored_guard"),
        ]
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_guard_smalltalk",
        node_type=NodeType.NARRATION,
        act=2,
        text="You slow down and give the guard a quick nod. He grunts a greeting back, eyes never leaving the crowd.",
        next_node_id="act2_wed_morning_corridor_transition"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_guard_ignore",
        node_type=NodeType.NARRATION,
        act=2,
        text="You keep your head down and walk straight through. The guard's gaze follows you for a second before moving on.",
        next_node_id="act2_wed_morning_corridor_transition"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_morning_corridor_transition",
        node_type=NodeType.NARRATION,
        act=2,
        text="Inside, the corridor buzzes with nervous chatter about curfews, police patrols, and missing classmates.",
        next_node_id="act2_wed_finn_class_intro"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_class_intro",
        node_type=NodeType.NARRATION,
        act=2,
        text="By the time physics rolls around, the air in Dr. Finn's classroom feels heavier than usual.",
        next_node_id="act2_wed_finn_start_lesson"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_start_lesson",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="finn",
        portrait="angry",
        text="Sit down and take out your notebooks. Just because the news is loud doesn't mean your brains can be quiet.",
        next_node_id="act2_wed_finn_rude_student"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_rude_student",
        node_type=NodeType.NARRATION,
        act=2,
        text="Halfway through the lesson, a boy at the back snickers and mutters something under his breath. A few students laugh.",
        next_node_id="act2_wed_finn_throws_out"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_throws_out",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="finn",
        portrait="angry",
        text="If you think this is a joke, mister, get out of my class. Now.",
        next_node_id="act2_wed_finn_boy_leaves"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_boy_leaves",
        node_type=NodeType.NARRATION,
        act=2,
        text="The boy scoffs, shoves his chair back, and storms out into the corridor, the door slamming behind him.",
        next_node_id="act2_wed_choice_confront_finn"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_choice_confront_finn",
        node_type=NodeType.CHOICE,
        act=2,
        text="What do you do?",
        choices=[
            Choice("Follow them and accuse Finn of the kidnappings.", "act2_wed_confront_finn", choice_to_record="confronted_finn"),
            Choice("Stay seated and say nothing.", "act2_wed_do_nothing", choice_to_record="did_nothing_finn"),
        ]
    ))

    # ── BRANCH A: Confront Finn (bad ending) ──

    tree.add_node(StoryNode(
        node_id="act2_wed_confront_finn",
        node_type=NodeType.NARRATION,
        act=2,
        text="As the rest of the class stares at their notes, you quietly slip out, heart pounding in your ears.",
        next_node_id="act2_wed_corridor_finn_elias_scene"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_corridor_finn_elias_scene",
        node_type=NodeType.NARRATION,
        act=2,
        text="In the corridor, you find Dr. Finn and the boy facing each other while Dr. Elias stands between them, hands raised to calm things down.",
        next_node_id="act2_wed_player_accuses"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_player_accuses",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="suspicious",
        text="Stop pretending. I saw a teacher leading a kid away. Same red jacket, same line — 'you need some disciplining.' It has to be you.",
        next_node_id="act2_wed_finn_reacts"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_reacts",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="finn",
        portrait="shocked",
        text="Are you out of your mind? I've never laid a hand on any of you.",
        next_node_id="act2_wed_elias_reassures"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_elias_reassures",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="elias",
        portrait="nervous",
        text="Hey, hey — let's all breathe. Accusing teachers of kidnapping is serious. Why would you even think that?",
        next_node_id="act2_wed_player_explains"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_player_explains",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="nervous",
        text="I saw someone taken away near the side gate. And now kids are missing. How is that a coincidence?",
        next_node_id="act2_wed_hina_interrupts"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_hina_interrupts",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="hina",
        portrait="angry",
        text="What is all this ruckus? Everyone, back to class. We have enough to worry about without wild rumors.",
        next_node_id="act2_wed_after_school_chem_lab_setup"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_after_school_chem_lab_setup",
        node_type=NodeType.NARRATION,
        act=2,
        text="Hours later, the story still circles in your head. You stay behind in the chemistry lab after school, determined to catch up on notes and prove you're not just causing trouble.",
        next_node_id="ending_bad_chem_lab"
    ))

    tree.add_node(StoryNode(
        node_id="ending_bad_chem_lab",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="narrator",
        portrait="none",
        text="The quiet room grows hazy. A faint hiss whispers from a forgotten burner. By the time you notice the smell, it's already too late.",
        next_node_id=None
    ))

    # ── BRANCH B: Do nothing (main route) ──

    tree.add_node(StoryNode(
        node_id="act2_wed_do_nothing",
        node_type=NodeType.NARRATION,
        act=2,
        text="You grip your pen tighter and stare at the worksheet. Confronting Finn in front of everyone would only make you look crazy.",
        next_node_id="act2_wed_finn_class_resumes"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_finn_class_resumes",
        node_type=NodeType.NARRATION,
        act=2,
        text="Finn returns to the board, voice colder than before. The class falls into an uneasy silence until the bell finally rings.",
        next_node_id="act2_wed_corridor_after_class"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_corridor_after_class",
        node_type=NodeType.NARRATION,
        act=2,
        text="Out in the corridor, students spill toward their next lessons, whispering about the kid who got kicked out and the security guard outside.",
        next_node_id="act2_wed_lunch_with_maya"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_lunch_with_maya",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="nervous",
        text="You looked really tense in physics. Did something happen, or is it just the whole kidnapping thing?",
        next_node_id="act2_wed_player_lunch_reply"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_player_lunch_reply",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="nervous",
        text="It's both. Finn keeps snapping at students, and that red jacket thing won't leave my brain.",
        next_node_id="act2_wed_maya_deflects"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_maya_deflects",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="neutral",
        text="Maybe everyone's just stressed. Let's survive this week first, detective. Then you can solve the mystery.",
        next_node_id="act2_wed_afternoon_classes_montage"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_afternoon_classes_montage",
        node_type=NodeType.NARRATION,
        act=2,
        text="The rest of the day passes in a blur of half-finished notes, whispered theories, and teachers pretending everything is normal.",
        next_node_id="act2_wed_after_school_walk_home"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_after_school_walk_home",
        node_type=NodeType.NARRATION,
        act=2,
        text="After the final bell, you and Maya leave the building together. The sunset paints the pavement gold.",
        next_node_id="act2_wed_after_school_talk_missing_kids"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_after_school_talk_missing_kids",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="scared",
        text="Two kids from our school gone already… Do you think it's someone here? A teacher, maybe?",
        next_node_id="act2_wed_after_school_player_reply"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_after_school_player_reply",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="suspicious",
        text="I don't know yet. But whoever it is, they know this place way too well.",
        next_node_id="act2_wed_go_home_separate"
    ))

    tree.add_node(StoryNode(
        node_id="act2_wed_go_home_separate",
        node_type=NodeType.NARRATION,
        act=2,
        text="At the corner, you and Maya split ways, heading down different streets as the sky fades from orange to deep blue.",
        next_node_id="act2_thu_morning_news_intro"
    ))

    # ── THURSDAY ───────────────────────────────────────────────────────────

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_news_intro",
        node_type=NodeType.NARRATION,
        act=2,
        text="The next morning, the news is already blaring when you reach the kitchen. Your mom stares at the screen, her face pale.",
        next_node_id="act2_thu_morning_tv_report"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_tv_report",
        node_type=NodeType.NARRATION,
        act=2,
        text="On-screen, a reporter stands near the school gates. A small red cloth is taped off behind her, flapping in the wind.",
        next_node_id="act2_thu_morning_player_reacts"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_player_reacts",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="shocked",
        text="That's… our school. And that's the red cloth they found?",
        next_node_id="act2_thu_morning_mom_worried"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_mom_worried",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="mom",
        portrait="scared",
        text="Another student is missing. I don't like this at all. Stay with your friends today, okay? No wandering around alone.",
        next_node_id="act2_thu_morning_player_leave"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_player_leave",
        node_type=NodeType.NARRATION,
        act=2,
        text="You promise you'll be careful, grab your bag, and head out, the image of the red cloth burned into your mind.",
        next_node_id="act2_thu_morning_walk_to_school"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_walk_to_school",
        node_type=NodeType.NARRATION,
        act=2,
        text="The streets to school feel quieter than usual. Fewer kids, more nervous parents watching from doorways.",
        next_node_id="act2_thu_morning_meet_maya"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_meet_maya",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="nervous",
        text="Hey. We need to talk. It's about that red cloth the news keeps showing.",
        next_node_id="act2_thu_morning_player_curious"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_player_curious",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="suspicious",
        text="You know something, don't you? What happened?",
        next_node_id="act2_thu_morning_maya_reveals_cloth"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_maya_reveals_cloth",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="scared",
        text="I found it last night near the alley by school. I took it straight to the police. They say it might belong to the kid who disappeared.",
        next_node_id="act2_thu_morning_three_red_items"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_three_red_items",
        node_type=NodeType.NARRATION,
        act=2,
        text="On the way to school, Maya lowers her voice and starts listing names, like she's building a suspect board in her head.",
        next_node_id="act2_thu_morning_maya_lists_teachers"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_maya_lists_teachers",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="suspicious",
        text="There are only three teachers who always wear red: Dr. Hina's red hijab, Dr. Elias's red scarf, and Dr. Finn's red handkerchief.",
        next_node_id="act2_thu_morning_player_notices_finn"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_player_notices_finn",
        node_type=NodeType.NARRATION,
        act=2,
        text="Later, in the corridor, you spot Dr. Finn at his classroom door. Today, his usual red handkerchief is nowhere to be seen.",
        next_node_id="act2_thu_morning_player_comment"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_player_comment",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="suspicious",
        text="Wait… Finn doesn't have his handkerchief today.",
        next_node_id="act2_thu_morning_maya_suspects_finn"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_maya_suspects_finn",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="nervous",
        text="Exactly. That can't be a coincidence. Look, keep this between us for now, but I don't trust him. We should watch him.",
        next_node_id="act2_thu_morning_tracking_app"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_morning_tracking_app",
        node_type=NodeType.NARRATION,
        act=2,
        text="Between classes, you and Maya huddle over your phones, installing the same tracking app and linking locations 'just in case.'",
        next_node_id="act2_thu_day_montage_wait_for_after_school"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_day_montage_wait_for_after_school",
        node_type=NodeType.NARRATION,
        act=2,
        text="The rest of the school day crawls by. Every bell feels like it's counting down to something only you two know about.",
        next_node_id="act2_thu_after_school_follow_decision"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_after_school_follow_decision",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="suspicious",
        text="Okay. When Finn leaves, we follow his car. No getting too close, no doing anything stupid. We just watch.",
        next_node_id="act2_thu_after_school_wait_parking"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_after_school_wait_parking",
        node_type=NodeType.NARRATION,
        act=2,
        text="After the final bell, you and Maya linger near the parking lot, pretending to scroll your phones while staff cars slowly pull out.",
        next_node_id="act2_thu_after_school_follow_car"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_after_school_follow_car",
        node_type=NodeType.NARRATION,
        act=2,
        text="When Finn's old sedan finally rolls past, you slip into the crowd and trail a safe distance behind, eyes fixed on his rear bumper.",
        next_node_id="act2_thu_drive_outskirts"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_drive_outskirts",
        node_type=NodeType.NARRATION,
        act=2,
        text="The route winds away from school, past familiar shops and into quieter streets lined with worn-down houses.",
        next_node_id="act2_thu_outside_house_listen"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_outside_house_listen",
        node_type=NodeType.NARRATION,
        act=2,
        text="Finn parks outside a small, tired-looking house. You and Maya duck behind a fence as he steps out, shoulders slumped, and goes inside.",
        next_node_id="act2_thu_overhear_finn"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_overhear_finn",
        node_type=NodeType.NARRATION,
        act=2,
        text="A cracked window is slightly open. Voices drift out — Finn's, low and shaky, and another, older and weaker.",
        next_node_id="act2_thu_finn_talking_inside"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_finn_talking_inside",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="finn",
        portrait="sad",
        text="I'm doing my best, mom. The kids hate me, the pay is awful, and the hospital still wants ten thousand. But I'll figure it out.",
        next_node_id="act2_thu_player_realisation"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_player_realisation",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="player",
        portrait="shocked",
        text="He's not some monster… he's just trying to keep his job and pay for her treatment.",
        next_node_id="act2_thu_maya_realisation"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_maya_realisation",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="sad",
        text="And the red handkerchief? He probably left it here with her. Like a reminder he'll come back.",
        next_node_id="act2_thu_finn_innocent_narration"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_finn_innocent_narration",
        node_type=NodeType.NARRATION,
        act=2,
        text="Finn's voice cracks as he laughs weakly about homework and test scores. It doesn't sound like the voice of a kidnapper — just a worn-out teacher clinging to something normal.",
        next_node_id="act2_thu_two_suspects_left"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_two_suspects_left",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="maya",
        portrait="suspicious",
        text="So Finn is off the list. That leaves Dr. Hina with her red hijab… and Dr. Elias with his red scarf.",
        next_node_id="act2_thu_evening_walk_home_separate"
    ))

    tree.add_node(StoryNode(
        node_id="act2_thu_evening_walk_home_separate",
        node_type=NodeType.NARRATION,
        act=2,
        text="By the time you and Maya head back toward town, the sun is dipping low. The tracking app blips quietly in your pocket.",
        next_node_id="act2_end_of_act2"
    ))

    tree.add_node(StoryNode(
        node_id="act2_end_of_act2",
        node_type=NodeType.DIALOGUE,
        act=2,
        speaker="narrator",
        portrait="none",
        text="You say goodbye to Maya at the corner, minds racing with new questions and fewer suspects than before.",
        next_node_id=None
    ))