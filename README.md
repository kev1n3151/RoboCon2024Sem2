# RoboCon 2024 Semester 2

## This repository is a continuation/build off of the RosieCon2023 project by Jasper Avice Demay ##

Original Repo can be found [here](https://github.com/JasperAviceDemay/RosieCon2023Sem2) 

Mentor: Dr Ian Peake
Client: Professor James Harland

Authors: 
- Kevin Lam | s3840027
- Michael Khalil | s3944778
- Youngjin Kim | s3892555
- Puran Grewal | s3944779
- Meghana Mirian Anil | s392518

### Front-End
Front-End adapted from the [Chats-With-Rosie project](https://github.com/Chats-With-Rosie/rosie-front-end)


### Playing with the Rosie Character Definition through Oogabooga Text Generation WebUI
Follow the instructions to install and run the Text Generation WebUI found [here](https://github.com/oobabooga/text-generation-webui). Follow the instructions in the linked repository to find and set up a suitable language model from the HuggingFace repository.


Copy the Rosie character files from this repo's `characters` folder into the WebUI's `characters` folder. If you are already running the WebUI, simply refresh the characters and you will be able to load the Rosie character from there.

### Real-time speech to text
Azure real-time recognize [here](https://learn.microsoft.com/en-au/azure/ai-services/speech-service/how-to-recognize-speech?pivots=programming-language-python#use-continuous-recognition).



# How to use

## 1. Set environment variable
### Windows
```
setx SPEECH_KEY your-key
setx SPEECH_REGION your-region
```
If you only need to access the environment variables in the current console, you can set the environment variable with set instead of setx.
After you add the environment variables, you might need to restart any programs that need to read the environment variable, including the console window. For example, if you're using Visual Studio as your editor, restart Visual Studio before you run the example.

### Linux
```
export SPEECH_KEY=your-key
export SPEECH_REGION=your-region
source ~/.bashrc
```
After you add the environment variables, run source ~/.bashrc from your console window to make the changes effective.

### macOS
Bash
Edit your .bash_profile file, and add the environment variables:
```
export SPEECH_KEY=your-key
export SPEECH_REGION=your-region
source ~/.bash_profile
```
After you add the environment variables, run source ~/.bash_profile from your console window to make the changes effective.

## 2. Reopen the console window then git clone
```
git clone https://github.com/JasperAviceDemay/RosieCon2023Sem2.git
cd RosieCon2023Sem2/FrontEnd
pip install -r requirements.txt
```
### 3. run realtime.py
```
python realtime.py
```
