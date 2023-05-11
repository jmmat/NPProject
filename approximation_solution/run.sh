#!/bin/bash

# change to the directory containing the tests
cd ./test_cases

# iterate over each Python file in the directory
for file in *.txt
do
  # execute the Python file in the background
  cat "$file" | python3 "../cs412_mingraphcolor_approx.py" &
done

# wait for all background processes to finish
wait
