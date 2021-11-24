
OUTPUT_DIRECTORY=data/`hostname`_`date +%F`
mkdir -p $OUTPUT_DIRECTORY
OUTPUT_FILE=$OUTPUT_DIRECTORY/measurements_`date +%R`.txt
OUTPUT_FILE="$( echo -e "$OUTPUT_FILE" | tr ':' '_' )"
OUTPUT_CSV=$OUTPUT_DIRECTORY/measurements_`date +%R`.csv
OUTPUT_CSV="$( echo -e "$OUTPUT_CSV" | tr ':' '_' )"

touch $OUTPUT_FILE
# for i in 100 1000 10000 100000 200000 400000 600000 800000 1000000; do
#     for rep in `seq 1 20`; do
#         echo "Size: $i" >> $OUTPUT_FILE;
#         ./src/parallelQuicksort $i >> $OUTPUT_FILE;
#     done ;
# done
python3 scripts/random_exec.py $OUTPUT_FILE

perl scripts/csv_quicksort_extractor.pl < $OUTPUT_FILE > $OUTPUT_CSV
