TESTS=("basic" "arc109_b" "aggrcow" "srm258_autoloan")

for file in "${TESTS[@]}"; do
    DIFF=$(diff <(cat output_$file.txt) <(./$file.py < input_$file.txt))
    if [ "$DIFF" != "" ]; then
        echo "$file test failed"
    fi
done