import customtkinter as ctk
import login

class Application(ctk.CTk):
    """
    A class representing the main application.
    """

    def __init__(self):
        """
        Initializes the Application object.
        """
        super().__init__()
        
        self.geometry("400x250")
        self.resizable(False, False)  # Disable window resizing
        self.create_login_screen()
        self.center_window()  # Center the window on the screen

    def center_window(self):
        """
        Centers the window on the screen.
        """
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_login_screen(self):
        """
        Creates the login screen.
        """
        # Set the appearance mode to dark
        ctk.set_appearance_mode("dark")
        
        # Set the default color theme to blue
        ctk.set_default_color_theme("blue")
        
        # Create an instance of the LoginScreen class
        login_screen = login.LoginScreen(master=self)
        login_screen.master.title("RS3Merch | Login")  # Set the title
        login_screen.pack(fill=ctk.BOTH, expand=True)

app = Application()
app.mainloop()
