# tkrb_kiwi_lv

## About:

This is a Streamlit app that informs the user what level their sword character will return as from kiwame training in the game Touken Ranbu ONLINE (aka TKRB). It is mainly meant for use with characters that have not yet achieved level 99, given the game's recent changes allowing untrained swords to store "extra" EXP (which unfortunately cannot be tracked). The app can be accessed here: https://share.streamlit.io/yae-sushi/tkrb_kiwi_lv/main/kiwame_return_calc.py. All written for fun.

## Files:

- environment.yml - Tells Streamlit what Conda/Python environment requirements are needed for the app to run.
- kiwame_return_calc.py - The actual calculator and Streamlit application.
- tkrb_exp_scraper.ipynb - The code used to initially scrape information from TKRB's wikia. Also includes some data visualizations to satisfy my curiosity.
- tkrb_exp.csv - The cleaned and scraped data produced by the scraper file, used by the calculator.

## Attributions:

The information required to make this calculator was scraped via BeautifulSoup from the Touken Ranbu wikia located at https://touken-ranbu.fandom.com/, and is included in .csv form (tkrb_exp.csv) in this repository.

## Other:

I also maintain a character ranking sorter for the game at https://tkrbsorter.tumblr.com/, which may be of interest. (Although I only have precursory knowledge of HTML/CSS/Javascript. Plus it's built off of other people's code.)
