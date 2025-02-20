#!/bin/bash

echo "Отчет о логе веб-сервера" > report.txt
echo "========================" >> report.txt

awk --posix '$1 ~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/ \
{ count ++ } END { print "Общее количество запросов:    ", count }' access.log >> report.txt

awk --posix '$1 ~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/ { ips[$1]++ } \
END { count=0; for (ip in ips) count++; \
print "Количество уникальных IP-адресов:    ", count }' access.log >> report.txt

echo "" >> report.txt
echo "Количество запросов по методам:" >> report.txt
awk '{gsub(/"/, "", $6); methods[$6]++} \
END { for (method in methods) print methods[method], method }' access.log >> report.txt

echo "" >> report.txt
awk '{urls[$7]++} END { max_url=""; max_count=0; \
for (url in urls) { if (urls[url] > max_count) { max_count = urls[url]; \
max_url = url; }} print "Самый популярный URL:    " max_count, max_url; }' access.log >> report.txt

