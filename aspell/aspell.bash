#!/usr/bin/env bash

# Get aspell output...
<"$1" aspell pipe list -t --lang=it_IT --personal=./.aspell.ignore |
grep '[a-zA-Z]\+ [0-9]\+ [0-9]\+' -oh | \
grep '[a-zA-Z]\+' -o | \
while read word; do grep -on "\<$word\>" $1; done
