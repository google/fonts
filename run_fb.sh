#!/bin/sh
# Run only the most crucial Fontbakery checks. Check fonts render on 

fonts=`curl -v -H "Authorization: token $GH_TOKEN" "https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST/files" | jq '.[] | select(.filename | contains(".ttf")) | .filename' | tr '\n' ' ' | tr '"' ' '`
fontbakery check-googlefonts \
    -c com.google.fonts/check/001 \
    -c com.google.fonts/check/002 \
    -c com.google.fonts/check/004 \
    -c com.google.fonts/check/005 \
    -c com.google.fonts/check/006 \
    -c com.google.fonts/check/006 \
    -c com.google.fonts/check/014 \
    -c com.google.fonts/check/016 \
    -c com.google.fonts/check/020 \
    -c com.google.fonts/check/036 \
    -c com.google.fonts/check/040 \
    -c com.google.fonts/check/045 \
    -c com.google.fonts/check/067 \
    -c com.google.fonts/check/071 \
    -c com.google.fonts/check/083 \
    -c com.google.fonts/check/084 \
    -c com.google.fonts/check/085 \
    -c com.google.fonts/check/086 \
    -c com.google.fonts/check/088 \
    -c com.google.fonts/check/089 \
    -c com.google.fonts/check/090 \
    -c com.google.fonts/check/092 \
    -c com.google.fonts/check/093 \
    -c com.google.fonts/check/094 \
    -c com.google.fonts/check/095 \
    -c com.google.fonts/check/096 \
    -c com.google.fonts/check/097 \
    -c com.google.fonts/check/098 \
    -c com.google.fonts/check/099 \
    -c com.google.fonts/check/100 \
    -c com.google.fonts/check/101 \
    -c com.google.fonts/check/129 \
    -c com.google.fonts/check/130 \
    -c com.google.fonts/check/131 \
    -c com.google.fonts/check/157 \
    -c com.google.fonts/check/158 \
    -c com.google.fonts/check/159 \
    -c com.google.fonts/check/160 \
    -c com.google.fonts/check/161 \
    -c com.google.fonts/check/162 \
    -c com.google.fonts/check/165 \
    -c com.google.fonts/check/vttclean \
    $fonts -l FAIL -n
