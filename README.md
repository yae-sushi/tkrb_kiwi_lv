# tkrb_kiwi_lv

## About:

This is a Streamlit app that informs the user what level their sword character will return as from kiwame training in the game [Touken Ranbu ONLINE (aka TKRB)](https://www.johren.net/games/tohken-en/play/).

It can be used in two ways:

- through showing how much exp is remaining for characters below level 99 until their next level, or
- by inputting the cumulative EXP an untrained character currently has (given the game's recent UI changes allowing users to see "extra" EXP, as well as the ability for untrained swords to store "extra" EXP at level 99).

The app can be accessed here: https://share.streamlit.io/yae-sushi/tkrb_kiwi_lv/main/kiwame_return_calc.py. All written for fun.

## Files:

- environment.yml - Tells Streamlit what Conda/Python environment requirements are needed for the app to run.
- kiwame_return_calc.py - The actual calculator and Streamlit application.
- tkrb_exp_scraper.ipynb - The code used to initially scrape information from TKRB's wikia. Also includes some data visualizations to satisfy my curiosity.
- tkrb_exp.csv - The cleaned and scraped data produced by the scraper file, used by the calculator.

## Attributions:

The information required to make this calculator was scraped via BeautifulSoup from the Touken Ranbu wikia located at https://touken-ranbu.fandom.com/, and is included in .csv form (tkrb_exp.csv) in this repository. Any changes to the wikia since the scrape are not reflected in the data.

## Other:

I also maintain a character ranking sorter for the game at https://tkrbsorter.tumblr.com/, which may be of interest.
