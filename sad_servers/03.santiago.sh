# Scenario: "Santiago": Find the secret combination  --> https://sadservers.com/scenarios

# Level: Easy

# Type: Do

# Description: Alice the spy has hidden a secret number combination, find it using these instructions:

# 1) Find the number of lines where the string Alice occurs in *.txt files in the /home/admin directory
# 2) There's a file where "Alice" appears exactly once. In the line after that ocurrence there's a number.
# Write both numbers consecutively as one (no new line or spaces) to the solution file (eg if the first number from 1) is 11 and the second 22, you can do echo -n 11 > /home/admin/solution; echo 22 >> /home/admin/solution).

# Test: Running md5sum /home/admin/solution returns d80e026d18a57b56bddf1d99a8a491f9(just a way to verify the solution without giving it away.)

# Time to Solve: 15 minutes.

#!/bin/bash

global_count=0
number=null

for file in /home/admin/*.txt; do
        file_count=$(grep "Alice" "$file" | wc -l)
        global_count=$((global_count + file_count))
        if [ $file_count -eq 1 ]; then
            number=$(grep Alice -A 1 "$file" | grep -Eo '[0-9]+')
        fi
done

echo -n $global_count > /home/admin/solution; echo $number >> /home/admin/solution

echo $global_count
echo $number

md5sum /home/admin/solution


# or

global_count=$(cat *.txt | grep -c Alice)
onefile=$(grep -c Alice *.txt | grep ':1$' | cut -d: -f1)
number=$(grep -A1 Alice $onefile | tail -1 | grep -Eo '[0-9]+') (edited) 
