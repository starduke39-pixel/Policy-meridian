import os
import datetime
import config

# --- 20 MINUTE DEEP DIVE SCRIPT ---
LONG_SCRIPT = """TITLE: The Fracture: North Carolina, The Definition of Sex, and American Geopolitics

[INTRO]
In the halls of the North Carolina General Assembly in Raleigh, a legislative battle is taking place. It looks like a domestic culture war. It looks like a debate over bathrooms, sports teams, and driver's licenses. But if you zoom out—if you look at this map from the perspective of Washington, Brussels, or Beijing—you see something very different.

You see a crack in the foundation of American Soft Power.

Welcome to The Policy Meridian. Today, we are breaking down how the definition of "Sex" in North Carolina law contradicts the foreign policy doctrine of the United States, and why our geopolitical rivals are watching closely.

[CHAPTER 1: THE LEGISLATION]
Let’s start with the text. The legislative push in North Carolina aims to define "sex" in the state statute as a strictly biological binary. Male and Female. Determined by gametes, chromosomes, and reproductive anatomy. This legislation—often titled the 'Women's Bill of Rights' or similar variations—specifically excludes "gender identity" from the legal definition of sex.

For the state, this provides legal clarity for vital statistics, prisons, and privacy. But for the Federal Government, this is a nightmare.

[CHAPTER 2: THE DOCTRINE OF GENDER MAINSTREAMING]
To understand why, we have to look at the State Department. Since the late 90s, and accelerating under recent administrations, the US has adopted a strategy called "Gender Mainstreaming." This is the integration of gender identity rights into all aspects of foreign policy.

When the US negotiates trade deals with Africa, or security pacts in Eastern Europe, "Human Rights" are a core pillar. And the US definition of Human Rights now explicitly includes Gender Identity. We sanction countries like Uganda. We pressure allies like Hungary or Poland. We tie World Bank loans to ESG scores that require gender inclusivity.

[CHAPTER 3: THE GEOPOLITICAL PARADOX]
This creates a paradox. The "Fractured Sovereign."
Imagine a US Diplomat sitting across from a diplomat from the Global South. The American says, "You must modernize your laws to recognize gender identity."
The foreign diplomat can simply pull up a map of the United States, point to North Carolina—a state with a GDP higher than Sweden—and say, "But your own laws do not recognize this."

This is the weaponization of federalism. Rivals like Russia and China use this disconnect to undermine American moral authority. They tell the world: "The American Empire is not a unified moral force. It is a confused collection of warring tribes."

[CHAPTER 4: THE ECONOMIC FALLOUT]
North Carolina is not just a state; it is a global economy. The Research Triangle Park. The Charlotte Banking Center. These are hubs for multinational capital.
Global banks are bound by European ESG standards. They *must* promote gender mainstreaming to keep their credit ratings in the EU. But they must *obey* state law in North Carolina to keep their business licenses.
The legislature is effectively forcing Capital to choose sides.

[CONCLUSION]
The vote in Raleigh is not just about Raleigh. It is about the coherence of the American message. As we move deeper into this election cycle, the question isn't just "What is a woman?" The question is: "Who is America?"
"""

# --- 60 SECOND SHORT SCRIPT ---
SHORT_SCRIPT = """
Why is the Chinese government watching the North Carolina state legislature?
Because Raleigh just became the battleground for the definition of "Sex."
New legislation in North Carolina aims to define sex strictly as "Male" and "Female" based on biology.
Here is the geopolitical twist.
The US State Department uses "Gender Rights" as a tool for diplomacy abroad. We lecture other nations on their laws.
But when major US states pass laws that contradict US foreign policy, it creates a diplomatic weakness.
Rivals like Russia use this to tell the world that America is divided, hypocritical, and weak.
Local laws have global consequences.
Subscribe to The Policy Meridian for the full geopolitical breakdown.
"""

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    production_dir = os.path.join(config.BASE_DIR, f"Run_News_{timestamp}")
    
    if not os.path.exists(production_dir):
        os.makedirs(production_dir)

    print(f"🚀 Starting Policy Meridian Run: {timestamp}")

    channel_name = "The_Policy_Meridian"
    channel_path = os.path.join(production_dir, channel_name)
    if not os.path.exists(channel_path):
        os.makedirs(channel_path)

    # SAVE LONG FORM
    print(f"   ✍️ Writing Long Form Analysis...")
    with open(os.path.join(channel_path, "1_Long_Form_Analysis.txt"), "w", encoding='utf-8') as f:
        f.write(LONG_SCRIPT)

    # SAVE SHORT FORM
    print(f"   ✍️ Writing Short Form Hook...")
    with open(os.path.join(channel_path, "2_Short_Form_Hook.txt"), "w", encoding='utf-8') as f:
        f.write(SHORT_SCRIPT)

    print(f"\n✅ Scripts generated in '{production_dir}'")

if __name__ == "__main__":
    main()
