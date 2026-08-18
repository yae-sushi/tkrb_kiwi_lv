# tkrb_kiwi_lv

## About:

This is a Streamlit app that informs the user what level their sword character will return as from kiwame training in the game [Touken Ranbu ONLINE (aka TKRB)](https://games.dmm.com/detail/tohken/). RIP EN version.

It can be used in two ways:

- through showing how much exp is remaining for characters below max level until their next level, or
- by inputting the cumulative EXP a character currently has (given the game's recent UI changes allowing users to see "extra" EXP, as well as the ability for untrained swords to store "extra" EXP at level 99).

The app can be accessed here: https://share.streamlit.io/yae-sushi/tkrb_kiwi_lv/main/kiwame_return_calc.py. All written for fun.

## Files:

- environment.yml - Tells Streamlit what Conda/Python environment requirements are needed for the app to run.
- kiwame_return_calc.py - The actual calculator and Streamlit application.
- tkrb_exp_scraper.ipynb - (outdated, included for comparison) The code used to initially scrape information from TKRB's wikia. Also includes some data visualizations to satisfy my curiosity.
- tkrb_exp_exploration.ipynb - The code used to clean/reorganize the initial csv file given to me by my friend Crow. Also includes some data visualizations to satisfy my curiosity. Initial CSV file not included.
- tkrb_exp.csv - The clean data, used by the calculator.

## Attributions:

The information required to make this calculator was given to me by my friend Crow, and after cleaning and reorganization is included in .csv form (tkrb_exp.csv) in this repository. Any changes to the game since are not reflected in the data.

## Other:

I also maintain a character ranking sorter for the game at https://tkrbsorter.tumblr.com/, which may be of interest.
