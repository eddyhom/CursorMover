import tkinter as tk
import pyautogui
import math

class CursorMover:
    def __init__(self, root):
         # Create the main window
        self.root = root
        self.root.title("Cursor Mover")

        # Set the window size
        self.root.geometry("400x300")
        
        # Automatic cursos movement flag
        self.auto_move = False

        # Create a label with some text
        self.label_text = "Move the cursor with the arrows or.\n\nYou can press A to enabled automatic movement.\n\nAutomatic Movement "
        self.label = tk.Label(root, text=self.label_text + str(self.auto_move), justify="center", font=("Helvetica", 12, "bold"))

        # Place the label in the middle of the window
        self.label.pack(pady=50)

        # Initial cursor position
        self.cursor_x = 50
        self.cursor_y = 50
        self.curr_angle = 0
        self.speed = 1

        # Call this function
        self.auto_activated()
        self.display_info()

        # Bind arrow key events
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # Bind letter key event
        self.root.bind("a", self.key_a_pressed)
        self.root.bind("x", self.key_x_pressed)


    def key_a_pressed(self, event):
        self.auto_move = not self.auto_move

    def key_x_pressed(self, event):
        self.speed = self.speed * 2

        if self.speed > 16:
            self.speed = 1

    def auto_activated(self):
        if self.auto_move:
            self.draw_circle()

        self.root.after(int(100/self.speed), self.auto_activated)  # Schedule the function to be called again after 100 milliseconds

    def draw_circle(self):
        radius = 20

        # Draw the circle
        angle = self.curr_angle
        angle = angle + 5

        if angle > 360:
            angle = angle % 360

        self.curr_angle = angle
        
        theta = math.radians(self.curr_angle)
        x_circle = radius * math.cos(theta)
        y_circle = radius * math.sin(theta)

        pyautogui.move(x_circle, y_circle)

    def display_info(self):
        x,y = pyautogui.position()
        text = "\n\nX: " + str(x) + ", Y: " + str(y) + "\n\nSpeed is " + str(self.speed) + "x"

        self.label.config(text=self.label_text+str(self.auto_move)+text)
        self.root.after(100, self.display_info)  # Schedule the function to be called again after 100 milliseconds


    def move_up(self, event):
        pyautogui.move(0, -10*self.speed)

    def move_down(self, event):
        pyautogui.move(0, 10*self.speed)

    def move_left(self, event):
        pyautogui.move(-10*self.speed, 0)

    def move_right(self, event):
        pyautogui.move(10*self.speed, 0)

if __name__ == "__main__":
    root = tk.Tk()
    cursor_mover = CursorMover(root)
    root.mainloop()
