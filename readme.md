# PyeGuard
A Safeguard for photosensitive people to enjoy the web.

# Usage
To use PyeGuard all you have to do is execute the launch.sh in your terminal, or do the same with a pre-built binary from the latest release.

# How does it work?
It constantly takes screenshots, resizes them to 16x16 and applies blur to analyze the percentage of how much colors have changed, if it surpasses the threshold without user interaction (Mouse/Keyboard clicks) it will keep calling `xset dpms force off` until the color changing is below the threshold again.

# Developing // Modifying
Execute the `launch.sh` file in your terminal and wait it set everything up. Then you can close PyeGuard and source into it's virtual environment by using `source .venv/bin/activate`. Afterwards you shall just code away :D.

### Made with 💜 by Moonlight Dorkreamer 🌓
