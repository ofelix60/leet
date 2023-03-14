#!/bin/bash


# # Step 1
# alice_lines=$(grep -rc 'Alice' /home/admin/*.txt | awk -F':' '{sum += $2} END {print sum}')
# echo "Number of lines with 'Alice': $alice_lines"

# # Step 2
# secret_file=$(grep -l -m1 '\bAlice\b' /home/admin/*.txt)
# secret_num=$(sed -n '/Alice/{n;p;q;}' "$secret_file" | grep -oE '[0-9]+')
# echo -n "$alice_lines$secret_num" > /home/admin/solution


# count=0; for file in *.txt; do if [ -f "$file" ]; then count=$(($count + $(grep -o -i "Alice" "$file" | wc -l))); fi; done; echo -n $count > /Users/oscar/Desktop/ss03/home/admin/solution


# global_count=0; for file in *.txt; count=0 do if [ -f "$file" ]; then global_count=$(($global_count + $(grep -o -i "Alice" "$file" | wc -l))); count=$(($count + $(grep -o -i "Alice" "$file" | wc -l))); do if [ count==0 ]; then echo $file; echo $global_count

#!/bin/bash

global_count=0
number=null

for file in /home/admin/*.txt; do
        file_count=$(grep -o -i "Alice" "$file" | wc -l)
        global_count=$((global_count + file_count))
        if [ $file_count -eq 1 ]; then
            number=$(grep Alice -A 1 /home/admin/"$file" | grep -Eo '[0-9]+')
        fi
done

echo -n $global_count > /home/admin/solution; echo $number >> /home/admin/solution
echo md5sum /home/admin/solution

echo $global_count
echo $number
