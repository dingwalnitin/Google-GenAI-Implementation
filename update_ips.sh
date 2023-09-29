#!/bin/bash
log_file="/var/log/apache2/access.log"
ips_file="unique_ips.txt"

while true; do
    inotifywait -e modify "$log_file"
    awk '{print $1}' "$log_file" | sort -u > "$ips_file"
done
