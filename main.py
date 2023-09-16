import time
from PIL import ImageChops, ImageGrab, ImageFilter
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import threading
import os

# Global variables to track if a mouse click or key press occurred
mouse_event_occurred = False
keyboard_event_occurred = False

# Function to reset event_occurred flags after a delay
def reset_event_flags():
    global mouse_event_occurred, keyboard_event_occurred
    while True:
        time.sleep(1.8)  # Adjust the delay as needed
        mouse_event_occurred = False
        keyboard_event_occurred = False

# Global thread for resetting event_occurred flags
reset_thread = threading.Thread(target=reset_event_flags)
reset_thread.daemon = True  # This will exit the thread when the main program exits
reset_thread.start()

def calculate_rmse(image1, image2):
    diff = ImageChops.difference(image1, image2)
    h = diff.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rmse = (sum_of_squares / float(image1.size[0] * image1.size[1])) ** 0.5
    return rmse

def on_mouse_click(x, y, button, pressed):
    global mouse_event_occurred
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        mouse_event_occurred = True

def on_key_press(key):
    global keyboard_event_occurred
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")
    keyboard_event_occurred = True

def monitor_mouse_and_keyboard_events():
    # Start listening for mouse clicks
    mouse_listener = MouseListener(on_click=on_mouse_click)
    mouse_listener.start()

    # Start listening for keyboard key presses
    keyboard_listener = KeyboardListener(on_press=on_key_press)
    keyboard_listener.start()

    # Join both listeners to ensure they run in separate threads
    mouse_listener.join()
    keyboard_listener.join()

def main():
    global mouse_event_occurred, keyboard_event_occurred
    previous_screenshot = None

    # Start monitoring mouse and keyboard events in a separate thread
    input_thread = threading.Thread(target=monitor_mouse_and_keyboard_events)
    input_thread.daemon = True  # This will exit the thread when the main program exits
    input_thread.start()

    while True:
        current_screenshot = ImageGrab.grab()  # Capture the current screenshot
        current_screenshot = current_screenshot.resize((16, 16))
        current_screenshot = current_screenshot.filter(ImageFilter.BLUR)

        if previous_screenshot:
            rmse = calculate_rmse(previous_screenshot.convert('L'), current_screenshot.convert('L'))
            percentage_change = (rmse / 255.0) * 100  # Calculate percentage change

            if percentage_change > threshold and not (mouse_event_occurred or keyboard_event_occurred):
                os.system("xset dpms force off")
                print(f"[DANGER] Color difference:{percentage_change:.2f}% was hit!\n{threshold - percentage_change:.2f}% over the threshold!")

            print(f"Color difference: {percentage_change:.2f}%")
        
        previous_screenshot = current_screenshot

if __name__ == "__main__":
    threshold = 15  # Adjust the threshold as needed, 15 is sensitive but catches everything tested so far
    main()
