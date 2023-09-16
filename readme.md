# PyeGuard
A Safeguard for photosensitive people to enjoy the web.

# Usage
To use PyeGuard all you have to do is execute the launch.sh in your terminal.

# How does it work?
It constantly takes screenshots, resizes them to 16x16 and applies blur to analyze the percentage of how much colors have changed, if it surpasses the threshold without user interaction (Mouse/Keyboard clicks) it will keep calling `xset dpms force off` until the color changing is below the threshold again.

# Developing // Modifying
In your debugging terminal, do `python3 -m venv .venv` then simply source it with `source .venv/bin/activate`.
Then finally do `pip install -r requirements.txt` to install all necessary packages to use it.

### Made with 💜 by Moonlight Dorkreamer 🌓
