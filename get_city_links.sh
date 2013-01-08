

cat states.dat | while read line; do
    echo $line;
    grep golf-courses/city.aspx states/${line}.links | grep ^A | cut -f2 > cities/${line}.links
    wc -l cities/${line}.links;
done


