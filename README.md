
This is code to scrapes website(s) in order to build a database of golf courses


```
mkdir states
mkdir cities
mkdir courses

bash get_state_links.sh

bash get_city_links.sh

cat cities/*.links | 
    while read line; 
        do python scraper.py $line; 
    done
```
