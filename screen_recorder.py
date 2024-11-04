import cv2
import numpy as np
from PIL import ImageGrab  # Use PIL instead of pyautogui
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
import threading

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Screen Recorder")
        self.root.geometry("300x150")
        self.recording = False
        self.output_file = None
        
        # Create GUI elements
        self.setup_gui()
        
    def setup_gui(self):
        # Start button
        self.start_button = tk.Button(
            self.root,
            text="Start Recording",
            command=self.start_recording,
            bg="green",
            fg="white",
            height=2,
            width=15
        )
        self.start_button.pack(pady=10)
        
        # Stop button (disabled initially)
        self.stop_button = tk.Button(
            self.root,
            text="Stop Recording",
            command=self.stop_recording,
            bg="red",
            fg="white",
            height=2,
            width=15,
            state="disabled"
        )
        self.stop_button.pack(pady=10)
        
    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Generate output filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_file = f"recording_{timestamp}.avi"
        
        # Start recording in a separate thread
        threading.Thread(target=self.record_screen, daemon=True).start()
        
    def stop_recording(self):
        self.recording = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        messagebox.showinfo("Recording Completed", f"Video saved as {self.output_file}")
        
    def record_screen(self):
        # Get screen size using PIL
        screen = ImageGrab.grab()
        screen_size = screen.size
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(
            self.output_file,
            fourcc,
            20.0,
            screen_size
        )
        
        while self.recording:
            # Capture screen using PIL
            screen = ImageGrab.grab()
            
            # Convert screenshot to numpy array
            frame = np.array(screen)
            
            # Convert from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Write frame
            out.write(frame)
            
            # Small delay to reduce CPU usage
            time.sleep(0.05)
            
        # Release video writer
        out.release()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenRecorder()
    app.run()