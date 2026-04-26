# Installation Guide

Installation Guide - The Last Invader 

Version: 1.0

Authors: Samuel Florez Garcia & Kimora Robinson

Last Updated: April 2026

---
 
Table of Contents

1. Requirements	

2. Installing on macOS	

3. Installing on Windows	

4. Installing on Linux	

5. Downloading the Game	

6. Running the Game	

7. Troubleshooting	

---
 
1. Requirements

Before installing, make sure your system meets the following requirements:

Requirement	Minimum Version

Python	3.7 or higher

Pygame	2.0 or higher

Operating System	macOS, Windows, or Linux

Storage	~50 MB free space

---
 
2. Installing on macOS

Step 1 - Check if Python is already installed

Open Terminal (search for it in Spotlight with Cmd + Space) and type:

python3 --version

If you see a version number like Python 3.11.0, Python is already installed. Skip to Step 3.

If you see an error, continue to Step 2.

Step 2  - Install Python

1.	Go to https://www.python.org/downloads/

2.	Click "Download Python" (the big yellow button)

3.	Open the downloaded .pkg file and follow the installer instructions

4.	Once installed, verify it worked by running python3 --version in Terminal again

Step 3 - Install Pygame

In Terminal, run:

pip3 install pygame

Wait for it to finish. You should see a success message at the end.

---
 
3. Installing on Windows

Step 1 - Check if Python is already installed

Open Command Prompt (search for "cmd" in the Start menu) and type:

python --version

If you see a version number, Python is installed. Skip to Step 3.

Step 2 - Install Python

1.	Go to https://www.python.org/downloads/

2.	Click "Download Python"

3.	Open the downloaded .exe file

4.	IMPORTANT: On the first screen of the installer, check the box that says "Add Python to PATH" before clicking Install. This step is critical, if you skip it, Python will not work from the command line.

5.	Click "Install Now" and wait for it to finish

6.	Verify by opening Command Prompt and running python --version

Step 3 - Install Pygame

In Command Prompt, run:

pip install pygame

Wait for it to finish. You should see a success message at the end.

---
 
4. Installing on Linux

Step 1 - Check if Python is already installed

Open your Terminal and type:

python3 --version

Most Linux distributions come with Python pre-installed. If you see a version number, skip to Step 2.

If not, install Python with:

sudo apt update

sudo apt install python3 python3-pip

Step 2 - Install Pygame

In Terminal, run:

pip3 install pygame
 
---

5. Downloading the Game

You have two options to get the game files onto your computer:

Option A - Download as ZIP (easiest, no Git required)

1.	Go to the repository: https://github.com/ImVidd/the-last-invader

2.	Click the green "Code" button

3.	Click "Download ZIP"

4.	Once downloaded, unzip the folder to a location you can easily find (like your Desktop)

Option B - Clone with Git

If you have Git installed, open your terminal and run:

git clone https://github.com/ImVidd/the-last-invader.git

This will create a folder called the-last-invader in your current directory.

---
 
6. Running the Game

1.	Open your terminal (Terminal on Mac/Linux, Command Prompt on Windows)

2.	Navigate to the game folder. For example:

cd Desktop/the-last-invader

3.	Run the game:

macOS / Linux:

python3 main.py

Windows:

python main.py

The game window should open and you will see the main menu. You are ready to play!

---
 
7. Troubleshooting

"python3: command not found" or "python is not recognized"

Python is not installed or not added to PATH. Go back to Step 2 for your operating system and make sure to check "Add to PATH" during the Windows installer.

"No module named pygame"

Pygame is not installed. Run pip3 install pygame (Mac/Linux) or pip install pygame (Windows) and try again.

"No module named pygame" even after installing

You may have multiple Python versions installed. Try:

python3 -m pip install pygame

The game window opens but there is no sound

Make sure your system volume is turned up. The game uses .mp3 files for sound. If you are on Linux, you may need to install additional audio libraries:

sudo apt install python3-pygame

Images are missing or the game crashes immediately

Make sure you are running main.py from inside the the-last-invader folder, not from a parent directory. The game looks for its asset files relative to where you run it from.

The game runs slowly or lags

Close other applications running in the background. The game runs at 60 FPS and requires minimal resources, but other programs may interfere.

