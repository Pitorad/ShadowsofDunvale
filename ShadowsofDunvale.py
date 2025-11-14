from os import system
import sys
import time
import random

belief = 0
fear = 0
curiosity = 0
journal = []

def pause():
    input("Press Enter to continue ...")

def clear():
    system("cls||clear")

def adjust_stat(stat_name, amount):
    global belief, fear, curiosity
    if stat_name == "belief":
        belief = max(0, min(10, belief + amount))
    elif stat_name == "fear":
        fear = max(0, min(10, fear + amount))
    elif stat_name == "curiosity":
        curiosity = max(0, min(10, curiosity + amount))

def print_stats():
    print(f"Belief: {belief} | Fear: {fear} | Curiosity: {curiosity}")

def open_journal():
    clear()
    print("--- Journal ---")
    if not journal:
        print("No entries yet.")
        pause()
        return

    for entry in journal:
        print(f"{entry['entry']}. {entry['title']}")
    
    choice = input("\nEnter entry number to read, or press Enter to close: ").strip()
    if choice.isdigit():
        entry_num = int(choice)
        for entry in journal:
            if entry["entry"] == entry_num:
                clear()
                print(f"Entry #{entry['entry']} – {entry['title']}\n")
                print(entry["text"])
                pause()
                break
    else:
        return
    
def add_journal_entry(entry_obj):
    """
    Accepts either:
      - a dict: {"entry": n, "title": "Title", "text": "Base text"}
      - or a plain string (legacy, will be wrapped into a dict)
    Applies mood/tone lines depending on current stats, then appends a dict to journal.
    """
    global belief, fear, curiosity, journal

    # Normalize input: if a string was passed, wrap it
    if isinstance(entry_obj, str):
        base = entry_obj
        entry_dict = {
            "entry": len(journal) + 1,
            "title": f"Entry {len(journal) + 1}",
            "text": base
        }
    elif isinstance(entry_obj, dict):
        # copy to avoid mutating caller's object accidentally
        entry_dict = {
            "entry": entry_obj.get("entry", len(journal) + 1),
            "title": entry_obj.get("title", f"Entry {len(journal) + 1}"),
            "text": entry_obj.get("text", "")
        }
    else:
        raise TypeError("add_journal_entry expects a dict or string")

    base_text = entry_dict["text"]

    # --- Dual-stat hybrids first ---
    if fear >= 7 and curiosity >= 7:
        mood_lines = [
            "Curiosity drags me deeper, even as every step feels like a warning.",
            "I should turn back, but I need to see what’s waiting in the dark.",
            "Terror and fascination—two sides of the same sickness."
        ]
        mood = random.choice(mood_lines)

    elif belief >= 7 and fear >= 7:
        mood_lines = [
            "Fear tests faith, but faith endures.",
            "If I survive this, maybe I’ll finally understand what 'belief' costs.",
            "Whatever’s out there isn’t stronger than my conviction. It can’t be."
        ]
        mood = random.choice(mood_lines)

    elif belief >= 7 and curiosity >= 7:
        mood_lines = [
            "Faith tells me there’s purpose here, but I can’t help dissecting every clue.",
            "Maybe understanding *is* belief—just sharper, colder.",
            "I tell myself I’m uncovering truth, but maybe I’m proving what I already believe."
        ]
        mood = random.choice(mood_lines)

    # --- Single dominant stat moods ---
    elif fear >= 7 and fear > belief and fear > curiosity:
        mood_lines = [
            "Something’s breathing just beyond the trees. I swear it.",
            "I can feel eyes in the mist. Watching. Waiting.",
            "Even the quiet feels alive, like it’s holding its breath for me to break."
        ]
        mood = random.choice(mood_lines)

    elif belief >= 7 and belief > fear and belief > curiosity:
        mood_lines = [
            "I can’t falter now. Truth demands endurance.",
            "Doubt is a luxury I can’t afford when this much is at stake.",
            "I’ve chosen to believe that purpose exists, even in horror."
        ]
        mood = random.choice(mood_lines)

    elif curiosity >= 7 and curiosity > belief and curiosity > fear:
        mood_lines = [
            "Every detail pulls me closer. The puzzle wants to be solved.",
            "The unknown is a siren’s call, and I’m already drowning.",
            "Whatever’s behind this is beautifully precise. Almost deliberate."
        ]
        mood = random.choice(mood_lines)

    # --- Balanced (no extremes) ---
    else:
        mood_lines = [
            "Another note in the margins. Facts first, feelings later.",
            "Need to keep perspective. Details matter more than hunches.",
            "Just a record. Keep it factual, keep it sane."
        ]
        mood = random.choice(mood_lines)

    # Append mood line to the text (with a space to separate). Keep the entry dict intact.
    entry_dict["text"] = base_text + " " + mood

    # Ensure entry number is consistent with the journal length if not provided
    if not entry_obj.get("entry") if isinstance(entry_obj, dict) else True:
        entry_dict["entry"] = len(journal) + 1

    journal.append(entry_dict)

def open_journal():
    """
    Shows a numbered list of journal entries (title), lets the player type a number
    to read a full entry, or press Enter to close.
    """
    clear()
    print("=== Elias Ward’s Journal ===\n")
    if not journal:
        print("The pages are empty. Not yet written, not yet real.\n")
        input("Press Enter to close...")
        clear()
        return

    for item in journal:
        print(f"{item['entry']}. {item['title']}")

    choice = input("\nEnter entry number to read (or press Enter to close): ").strip()
    if not choice:
        clear()
        return

    if choice.isdigit():
        entry_num = int(choice)
        matched = None
        for item in journal:
            if item["entry"] == entry_num:
                matched = item
                break
        if matched:
            clear()
            print(f"Entry #{matched['entry']} – {matched['title']}\n")
            print(matched["text"])
            input("\nPress Enter to close...")
            clear()
            return
        else:
            print("No such entry.")
            input("\nPress Enter to close...")
            clear()
            return
    else:
        print("Invalid input.")
        input("\nPress Enter to close...")
        clear()
        return
    
def crash():
    clear()
    print("""
The steering wheel jerks.
Headlights catch something pale between the trees — a face, or maybe a reflection.
He blinks. Too late.
Metal screams. Glass explodes. Silence follows.
When the mist clears, the car is empty.
The story ends before it ever begins.
""")
    input("Press Enter to continue ...")
    sys.exit(0)

def death_in_fog():
    clear()
    print("The mist thickens until the road vanishes beneath his feet.")
    print("He turns, but every direction is the same shade of nothing.")
    print("A voice hums behind him — low, familiar — repeating his own words back to him.")
    print("‘You shouldn’t have come here,’ it says. His voice. His breath.")
    print("The lantern light ahead flickers once… then once more… then it’s inside his chest.")
    print("By the time the fog clears, there’s only his notebook, half open in the dirt.")
    print("The last line reads: ‘I saw myself walking away.’")
    print("\n[GAME OVER – CONSUMED BY THE MIST]")
    input("\nPress Enter to return to the main menu...")
    # Here you can later redirect to a menu or restart



# --- STORY START ---
print("""Elias Ward had been driving for hours. The road to Dunvale wound through
endless forest, narrow and wet, bordered by trees that seemed to lean closer the deeper
he went. His hands ached from gripping the wheel, his coffee had gone
cold two hours ago, and his phone signal had died before sunset.
""")
pause(); clear()

print("""This was his first real story. His first chance.
A missing woman. A nameless village. A rumor of
something older hiding in the mist.
""")
pause(); clear()

print("""He whispered the name from the case file like a 
charm: Marla Crane. Twenty-six, schoolteacher,
vanished six months ago. The police report was 
thin — “likely fled town,” they’d said. But Elias 
had read the transcripts. He’d heard the unease 
in the sheriff’s voice. Something wasn’t right.
""")
pause(); clear()

# === CHOICE LOOP WITH JOURNAL ACCESS ===
print("""Choice:
      
      1. Review Marla's file again
      2. Keep driving in silence
""")

while True:
    print("""Choice:
      
1. Review Marla's file again
2. Keep driving in silence
""")
    playerinput = input("Please enter 1 or 2 (or J to open journal): ").strip().lower()
    if playerinput == "j":
        open_journal()
    elif playerinput in ["1", "2"]:
        break
    else:
        crash()

clear()

if playerinput == "1":
    print("""Elias opens the folder on the passenger seat. 
The photo stares back — dark hair, half-smile, 
the kind of expression that doesn’t know it’s 
about to become evidence. Notes clutter the 
margins: last seen near village square; sightings 
unconfirmed; locals uncooperative. 
A headline crosses his mind — “The Village That 
Swallowed a Woman.” He almost smiles.
""")
    adjust_stat("curiosity", 1)
    adjust_stat("belief", -1)
    add_journal_entry({
    "entry": len(journal)+1,
    "title": "On the Road to Dunvale",
    "text": (
        "I opened the file again. Marla Crane — gone six months, last seen near the square. Locals say she left."
        "They always say that. The photograph’s grainy, her eyes almost looking past me."
        "Maybe this story will be the one. Maybe I’ll prove that logic still has teeth in places that pray to older gods."
        "I tell myself I’m chasing the truth. But maybe I just like the chase."
    )
    
})
    pause(); clear()
                      

elif playerinput == "2":
    print("""He doesn’t want to think. The forest is 
whispering something against the glass — 
maybe the wind, maybe not.
""")
    adjust_stat("belief", 1)
    adjust_stat("fear", 1)
    adjust_stat("curiosity", -1)
    add_journal_entry({
    "entry": len(journal)+1,
    "title": "On the Road to Dunvale",
    "text": (
        "I left the file shut. The forest doesn’t like when you dig too deep. It hums when you’re quiet enough to hear it. "
        "Maybe she’s out there — maybe the ground itself remembers her. "
        "I can feel it watching. That’s faith, isn’t it? The kind born of fear."
    )
})
    pause(); clear()
else:
    crash()
# === CONTINUE STORY ===
clear()
print("""Soon, headlights catch a wooden sign almost swallowed by moss:
“Welcome to Dunvale.”
Below it, another smaller sign: Population 137.
Someone’s carved through the number. Now it reads 136.
""")
pause(); clear()

print("The car sputters, coughs, then dies.")
pause(); clear()

print("""Elias exhales, tightens his coat, and steps into the mist.
The silence greets him like an old friend.
""")
pause(); clear()

print("""The gravel crunches under Elias’s boots. 
The headlights die behind him, swallowed by the fog. 
Every sound feels heavier out here — the drip of rain, 
the whisper of leaves, the echo of his own breath.""")

pause(); clear()

print("""A shape emerges from the mist ahead — 
a figure with a lantern, standing too still to be casual. 
The light glows dim and yellow, casting no warmth.""")

pause(); clear()


while True:
    print("""Choice:
      
1. Call out to the figure.
2. Approach quietly.
3. Stay back and observe.
""")
    
    playerinput = input("Enter 1, 2, or 3 (or type 'j' to open the Journal): ").lower().strip()

    if playerinput == "1":
        clear()
        print("""Elias raises a hand. 
“Hey — I’m with the *Dunvale Gazette*,” he lies, voice steady. 
The figure doesn’t move for a moment, then turns slowly. 
It’s an old man, eyes clouded but sharp where they matter. 
“You shouldn’t have come here, Elias” he says. “She still walks after dark.”""")

        belief = min(belief + 1, 10)
        curiosity = min(curiosity + 1, 10)
        add_journal_entry({
            "entry": len(journal) + 1,
            "title": "The Lantern Man",
            "text": (
                "A warning whispered through fog. He spoke of her as if she never left. Maybe she didn’t. "
                "His eyes weren’t afraid of the dark — they belonged to it. The way he said my name made me "
                "feel like I’d been expected, like the forest had already written me into its story. "
                "He carried the light like a burden, not a beacon. I wonder how long he’s been walking out there, "
                "keeping something away — or guiding it toward me."
            )
        })
        Lantern_Mans_Warning = True
        pause(); clear()
        break

    elif playerinput == "2":
        print("""Elias lowers his steps, creeping forward. 
Each crunch feels too loud, but the figure doesn’t react. 
When he’s close enough to see the lantern’s glow, he realizes — 
it’s hanging from a branch. The figure’s gone. 
Only footprints remain, ending mid-trail.""")

        fear = min(fear + 1, 10)
        curiosity = min(curiosity + 1, 10)
        add_journal_entry({
            "entry": len(journal) + 1,
            "title": "Empty Path",
            "text": (
                "I followed the light and found nothing human. But the prints — they stopped like the forest swallowed them whole. "
                "Every sound died when I stepped off the road. Even my breath felt stolen. "
                "The fog pressed in so tight I could almost feel it thinking. "
                "If the man was real, he’s gone. If he wasn’t, then I’ve just been following a memory that never belonged to me."
            )
        })
        pause(); clear()
        break

    elif playerinput == "3":
        print("""He stays low, watching. The lantern flickers once. 
A shape shifts behind it — tall, wrong, and silent. 
When Elias blinks, the mist is empty again.""")

        fear = min(fear + 2, 10)
        belief = min(belief + 1, 10)
        add_journal_entry({
            "entry": len(journal) + 1,
            "title": "The Watcher",
            "text": (
                "Something else stood there. I don’t think it wanted to be seen. "
                "The trees bent the wrong way, as if bowing toward it. "
                "I couldn’t tell if it moved or if the mist was shaping itself around a thought too heavy to hold. "
                "Maybe belief isn’t about trust — maybe it’s about survival. "
                "If I stop believing in what’s out there, I might stop seeing it. "
                "And that, somehow, feels worse."
            )
        })
        pause(); clear()
        break

    elif playerinput == "j":
        open_journal()
        clear()
    else:
        death_in_fog()
        clear()

print("""When the fog begins to thin, Elias finds an old wooden chapel by the road. The sign above the door reads 
“Saint Luthien’s Rest”, but the paint has peeled so much that only “Luth” remains.""")
if Lantern_Mans_Warning:
    pause(); clear()
    print("The Lantern Man's warning echoes in his mind.")
pause(); clear()

while True:
    print("""Choice:
          
1. Enter the chapel.
""")
    

    
# Debugging output for now (remove in final build)
print("=== CURRENT STATS ===")
print_stats()
print("\n=== JOURNAL ===")
for entry in journal:
    print(f"- {entry}")
pause();