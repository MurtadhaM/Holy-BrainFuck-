




# RUN 10 times and get average


function time_benchmark() {
    for i in {1..10}
    do
        time_command "$@"
        total_time=$(echo "$total_time + $record_time" | bc -l) 1>> /dev/null
    done
    average_time=$(echo "$total_time / 10" | bc -l) 1>> /dev/null 
    echo "Average time taken to execute is $average_time"
  
    

}



funtion time_command(){
    # $1 is the command to be executed
    
    start_time=$(gdate +%s.%N)
    command_to_execute="$@"
echo     eval $command_to_execute 1>> /dev/null
    end_time=$(gdate +%s.%N)
    record_time=$(echo "$end_time - $start_time" | bc -l) 1>> /dev/null
    echo "Time taken to execute is $record_time"
}