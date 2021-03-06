import streamlit as st
import pandas as pd

df = pd.read_csv("./tkrb_exp.csv")

KIWI_REQUIREMENTS = {
    "Tantouwame" : 60,
    "Waki, Yari, Nagiwame" : 65,
    "R3 Uchiwame" : 70,
    "R4 Uchiwame" : 70,
    "Tachiwame" : 75,
    "Ootachiwame" : 80,
}

TYPE_TO_CATEGORY = {
    "Tantou" : "Tantouwame",
    "Wakizashi" : "Waki, Yari, Nagiwame",
    "Uchigatana (Current Rarity 2)" : "R3 Uchiwame",
    "Uchigatana (Current Rarity 3)" : "R4 Uchiwame",
    "Tachi" : "Tachiwame",
    "Ootachi" : "Ootachiwame",
    "Yari" : "Waki, Yari, Nagiwame",
    "Naginata" : "Waki, Yari, Nagiwame",
    "Tsurugi" : "Tsurugiwame",
}

def calc_extra_exp(cur_lv, sword_type, exp_remaining):
    """
    Calculates and returns the overflow EXP a touken danshi has
    past the base kiwame requirement.

    Inputs:
    cur_lv - int - the toudan's current level (1-99)
    sword_type - str - the sword type of the toudan
    exp_remaining - int - the amount of EXP remaining until the toudan's
        next level (-1 if unavailable or no EXP remaining (at max lv 99))

    Returns:
    exp_diff - int - the overflow EXP calculated
    """
    base_lv = KIWI_REQUIREMENTS[sword_type]
    base_exp_needed = df[(df["Type"] == "Regular") &
                         (df["Lv."] == base_lv)]["Cumulative EXP"]
    cur_exp = df[(df["Type"] == "Regular") &
                         (df["Lv."] == cur_lv)]["Cumulative EXP"]
    if exp_remaining != -1:
        cur_exp += df[(df["Type"] == "Regular") &
                      (df["Lv."] == cur_lv)]["EXP until Next Lv."] - exp_remaining
    exp_diff = int(cur_exp) - int(base_exp_needed)
    return exp_diff

def return_level(cur_lv, sword_type, exp_remaining = -1):
    """
    Calculates and prints the level at which a touken danshi will be
    upon return from kiwame training given user inputs.

    Inputs:
    cur_lv - int - the toudan's current level (1-99)
    sword_type - str - the sword type of the toudan
    exp_remaining - int - the amount of EXP remaining until the toudan's
        next level (-1 if unavailable or no EXP remaining (at max lv 99))

    Returns:
    int - level of kiwi toudan expected
    """
    extra_exp = calc_extra_exp(cur_lv, sword_type, exp_remaining)
    if extra_exp == 0:
        return 1
    else:
        kiwi_df = df[(df["Type"] == sword_type) &
                (df["Cumulative EXP"] < extra_exp)]
        return max(kiwi_df["Lv."])

def validate_exp_remaining(exp_remaining):
    """
    Validates user input for remaining EXP until next toudan level.
    Strips commas and whitespace from input.

    Inputs:
    exp_remaining - str - user input for remaining EXP

    Returns:
    None - Nonetype - if user input is invalid.
    -1 - int - if toudan is lv 99 and needs no more EXP.
    exp_remaining - int - user input as int if valid.
    """
    exp_remaining = exp_remaining.replace("," , "")
    exp_remaining = "".join(exp_remaining.split())
    try:
        exp_remaining = int(exp_remaining)
    except:
        return None

    if exp_remaining == 0:
        if cur_lv == 99:
            return -1
        else:
            return None

    if exp_remaining < 0:
        return None

    max_exp_needed = df[(df["Type"] == "Regular") &
                    (df["Lv."] == cur_lv)]["EXP until Next Lv."]

    if exp_remaining > int(max_exp_needed):
        return None
    return exp_remaining

# set title
st.title("What level kiwame will my touken danshi be?")

# write a diff line
st.write("""Let's find out! (The data needed to perform these calculations
was scraped from the TKRB Fandom website at
https://touken-ranbu.fandom.com/)""")

sword_type = TYPE_TO_CATEGORY[st.radio(
    "Sword type?",
    list(TYPE_TO_CATEGORY.keys()))]

if sword_type != "Tsurugiwame":
    start_slider_lv = KIWI_REQUIREMENTS[sword_type]
else:
    start_slider_lv = KIWI_REQUIREMENTS["Tantouwame"]

cur_lv = st.slider("Current toudan level?", 1, 99,
                    start_slider_lv)

get_exp = st.radio("Do you know how much EXP is needed until the next level?",
            ["I don't know.",
            "The toudan is max level (99).",
            "I know."])
if get_exp == "I know.":
    exp_remaining = st.text_input('EXP remaining until next lv?',
                    value = "1")
    original_input = exp_remaining
    exp_remaining = validate_exp_remaining(exp_remaining)
else:
    if get_exp == "The toudan is max level (99).":
        cur_lv = 99
    exp_remaining = -1

# make preds from user input
if exp_remaining == None:
    if original_input == '':
        st.write("No input detected. Please try again.")
    else:
        st.write(f"{original_input} is not a valid answer. Please try again.")
else:
    try:
        prediction = return_level(int(cur_lv), sword_type, int(exp_remaining))
    except:
        prediction = False

    #output pred
    if sword_type == "Tsurugiwame":
        output_text = "No tsurugi currently has a kiwame form. :("
    elif not prediction:
        output_text = f"""Your sword is currently unable to kiwame.
            To do so, he must be level {KIWI_REQUIREMENTS[sword_type]} or
            higher."""
    else:
        output_text = f"Your sword will return as a level {prediction} kiwame."

    st.write(output_text)
