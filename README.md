# ChatGPT_Computer
Run ChatGPT on a Raspberry Pi 4. Uses voice commands and displays on an OLED screen.

Before you start you have to get your ChatGPT APi code and install some libraries to make speech recognition work.

1. install the OpenAI Python library using the pip package manager.

pip3 install openai

2. Open the bashrc file hidden in your home directory. This file is where we need to set a path, a location where Raspberry Pi OS and Python can look for executable / configuration files.

nano ~/.bashrc

3. When the bashrc file opens, scroll to the bottom of the file and add this line:

export PATH="$HOME/.local/bin:$PATH"

5. Save the file by pressing CTRL + X, then Y and Enter.

6. Reload the bashrc config to finish the configuration. Then close the terminal.

source ~/.bashrc

7. Set up your ChatGPT APi - you have to already have an account to make this work. Log into your OpenAI account, click on the menu and select View API Keys. Click on Create new secret key to generate an API key. Make sure to copy and paste this key somewhere safe, it will not be shown again. Never share your API keys, they are unique to your account, any costs incurred will come from your account.

Next we have to set up speech recognition:

1. Install the Speech Recognition and a couple other Python libraries. 

pip install SpeechRecognition
sudo apt-get install portaudio19-dev
pip install pyaudio
sudo apt-get install flac

2. To make this work I used a USB microphone. We have to find the device index. In my code my device index was 0. If yours isn't 0, replace that number with the correct number. To find the device index use the 'arecord -l' command. If your microphone is plugged in, you should see the corect device number.
3. I had a hard time getting this to work at first, but then I changed the default card to what was listed for my microphone (card 1 in my case). Open the following file and scroll to the section where it lists defaults. Change the card number in the first two default lines to the correct card number. Exit and save the file.

cat /proc/asound/cards

After all of that set up, the code should work for you. Speech recognition is a bit slow, but I found it to be fairly accurate if you speak clearly. The module doesn't have ALL the nice functionality of the full Chat GPT system, but its a fun build nonetheless.

Credit to Tom's Hardware for getting me started with the OpanAi script.
