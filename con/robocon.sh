#!/bin/bash

#Run the Python script
python3 ./rosie_activate/startup.py

# Check the exit status of the Python script
if [ $? -eq 0 ]; then
  # If the script returns true, run the Docker command
  
    gnome-terminal -- ./run-docker & gnome-terminal -- bash -c "sudo ./actionmonitor.sh; exec bash"

    

else
  echo "Keyword not detected or process interrupted. Exiting."
fi
