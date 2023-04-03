#!/bin/bash

print_message() {
	echo "Total: $total"
	echo "2xx: $num_of_2xx_codes ($percent_2xx%)"
	echo "5xx: $num_of_5xx_codes ($percent_5xx%)"
}

maths_python() {
	total=$((left_over_codes + num_of_5xx_codes + num_of_2xx_codes))
	percent_2xx=$(python -c "print('{:.2f}'.format($num_of_2xx_codes * 100 / $total))")
	percent_5xx=$(python -c "print('{:.2f}'.format($num_of_5xx_codes * 100 / $total))")
	#echo "$percent_2xx"
	#echo "$percent_5xx"
}

maths_bc() {
	total=$((left_over_codes + num_of_5xx_codes + num_of_2xx_codes))

	percent_2xx=$(echo "scale=2; $num_of_2xx_codes * 100 / $total" | bc)
	percent_5xx=$(echo "scale=2; $num_of_5xx_codes * 100 / $total" | bc)
	#echo "$percent_2xx"
	#echo "$percent_5xx"
}

convert_bytes() {
	local bytes=$1
	local k=$((bytes / 1024))
	local m=$((k / 1024))
	local g=$((m / 1024))
	local result

	if ((bytes < 1024)); then
		result="${bytes} bytes"
	elif ((k < 1024)); then
		result="${k}."
		printf -v result '%s%02d KB' "$result" "$(((bytes % 1024) * 100 / 1024))"
	elif ((m < 1024)); then
		result="${m}."
		printf -v result '%s%02d MB' "$result" "$(((k % 1024) * 100 / 1024))"
	elif ((g < 1024)); then
		result="${g}."
		printf -v result '%s%02d GB' "$result" "$(((m % 1024) * 100 / 1024))"
	fi
	echo "$result"
}

maths_without_external_libs() {
	factor=10
	total=$((left_over_codes + num_of_5xx_codes + num_of_2xx_codes))

	percent_2xx=$((factor * num_of_2xx_codes * 100 / total))
	percent_2xx_decimal=$((percent_2xx % factor))
	percent_2xx_integer=$((percent_2xx / factor))
	printf -v percent_2xx "%.2f" "$percent_2xx_integer.$percent_2xx_decimal"

	percent_5xx=$((factor * num_of_5xx_codes * 100 / total))
	percent_5xx_decimal=$((percent_5xx % factor))
	percent_5xx_integer=$((percent_5xx / factor))
	printf -v percent_5xx "%.2f" "$percent_5xx_integer.$percent_5xx_decimal"
}

if [[ $1 =~ "gzip" && ($2 == "code" || $2 == "url" || $2 == "downloaded") ]]; then
	while [[ $# -gt 0 ]]; do
		case $1 in
		code)
			num_of_2xx_codes=0
			num_of_5xx_codes=0
			left_over_codes=0
			while read line; do
				status_code=$(echo "$line" | cut -d ' ' -f9)
				if [[ $status_code =~ ^2[0-9]{2}$ ]]; then
					((num_of_2xx_codes += 1))
				elif [[ $status_code =~ ^5[0-9]{2}$ ]]; then
					((num_of_5xx_codes += 1))
				else
					((left_over_codes += 1))
				fi
			done <~/logs.gzip
			#maths_bc
			#maths_python
			maths_without_external_libs
			print_message
			;;
		url)
			rm ~/.urls.txt
			while read line; do
				echo "$line" | cut -d ' ' -f7 >> ~/.urls.txt
			done <~/logs.gzip
			top_urls=$(cat ~/.urls.txt | sort | uniq -c | sort -r | head -n5)
			echo "Top URLS: "
			echo "$top_urls"
			;;
		downloaded)
			total_bytes=0
			while read line; do
				bytes=$(echo "$line" | cut -d ' ' -f10)
				bytes_in_int=$(expr $bytes + 0)
				total_bytes=$(($total_bytes + $bytes_in_int))
			done <~/logs.gzip
			#echo "$total_bytes"
			converted=$(convert_bytes $total_bytes)
			echo "Downloaded:"
			echo $converted
			;;
		esac
		shift
	done
else
	echo "Usage: $0 [FILE] [code|url|downloaded]"
fi
