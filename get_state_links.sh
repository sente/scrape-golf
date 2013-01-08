
cat states.dat | while read line; do
    echo $line;
    lwp-request -o links "http://www.golflink.com/golf-courses/state.aspx?state=${line}" > states/${line}.links;
    wc -l states/${line}.links;
done

