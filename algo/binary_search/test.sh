TESTS=("basic" "arc109_b" "aggrcow" "srm230_sortestimate" "srm258_autoloan" "srm277_unionofintervals")

CODE_F="code"
INPUT_F="test_files/input"
OUTPUT_F="test_files/output"
for file in "${TESTS[@]}"; do
    DIFF=$(diff <(cat $OUTPUT_F/output_$file.txt) <(./$CODE_F/$file.py < $INPUT_F/input_$file.txt))
    if [ "$DIFF" != "" ]; then
        echo "$file test failed"
    fi
done