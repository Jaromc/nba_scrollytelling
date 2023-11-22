# Scrollytelling of Stephen Curry's 22-23 NBA Season #

Data gathered from NBA API is formatted and saved to a CSV to be used in a scrollytelling analysis of Stephen Curry's 22-23shot efficiency compared to his team.

### Setup and Run ###

* docker build -t nba_viz .
* docker run -it --rm -v /mnt/d/dev/nba_viz:/app nba_viz bash
* python3 build_data.py

* Start a python webserver from this folder using python3 -m http.server 9090
* Access webpage from http://localhost:9090/

### Demo ###
https://github.com/Jaromc/nba_scrollytelling/assets/89912906/fbeaeafa-aef2-4d11-8245-cc1637986ea7

### References ###
* https://github.com/russellsamora/scrollama
* https://github.com/swar/nba_api
* https://www.nba.com/stats
