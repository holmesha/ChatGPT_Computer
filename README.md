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

8.

Credit to Tom's Hardware for getting me started with the OpanAi script.
