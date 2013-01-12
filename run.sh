#!/bin/sh

mkdir states
mkdir cities
mkdir courses

bash get_state_links.sh

bash get_city_links.sh

cat cities/*.links |
    while read line;
        do python scraper.py "$line";
    done
