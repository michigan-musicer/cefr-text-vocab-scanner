Short script to fetch C1 / C2 vocabulary from a text file based on the list from [https://github.com/openlanguageprofiles/olp-en-cefrj](https://github.com/openlanguageprofiles/olp-en-cefrj). 

Only requires `pandas` to run.

Possible feature extensions:
- C1 / C2 list is very small (2000 words only), can be supplemented by other lists.
- data should be cleaned so that American / British english is separated.
    - this has been done for the one list but will be necessary for any future lists we add
- counts of C1 / C2 words.
- labeling in output of C1 / C2 words.
- Inclusion of B2 words.
- take in text file as cmdline arg.
