#!/bin/bash

CONTAINER_NAME="rocroc"
CONTAINER_ID=$(docker inspect --format="{{.Id}}" $(docker ps -aqf "name=$CONTAINER_NAME"))

while [ -z "$CONTAINER_ID" ]; do
  echo "Waiting for container $CONTAINER_NAME to start..."
  sleep 1
  CONTAINER_ID=$(docker inspect --format='{{.Id}}' $(docker ps -aqf "name=$CONTAINER_NAME"))
done

FILE="/var/lib/docker/containers/$CONTAINER_ID/$CONTAINER_ID-json.log"

#sudo chmod +r "$FILE"

# This function listens for the safety word and executes the associated script
execute_action() {
    local action=$1
    echo "Executing line: $line"
   # while true; do
        local safety_word
        echo "Enter safety word for $action:"
        read safety_word
    	echo "$line"
        if [[ "$line" == *"I am going to"* ]]; then
            if [[ "$action" == "tuck" ]]; then
               	 echo "Tuck runs"
		 /home/vxlab/robocon/con/tuck/run-tuck-docker
            elif [[ "$action" == "untuck" ]]; then
		 echo "Untuck runs"
		 echo "Current path: {$pwd}"
                #./untuck/run-untuck-docker
		/home/vxlab/robocon/con/untuck/run-untuck-docker
            fi

            
        else
            echo "Incorrect safety word. Action not executed."
        fi
        
   # done
}

# Monitoring the JSON file and looking for specific phrases
tail -f "$FILE" | while read -r line; do
    if [[ "$line" == *"roll in arms"* ]]; then
        sleep 5
	echo "Close detected"
	execute_action "tuck"
    elif [[ "$line" == *"roll out arms"* ]]; then
	sleep 5
	echo "Open detected"
        execute_action "untuck"
    fi
done
