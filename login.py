import customtkinter as ctk
    
class LoginScreen(ctk.CTkFrame):
    """
    A class representing the login screen of the application.
    """
    def __init__(self, master=None):
        """
        Initializes the LoginScreen object.

        Args:
            master: The master widget.
        """
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the login screen.
        """
        # Create a label for email
        email_label = ctk.CTkLabel(master=self, text="Email:")
        email_label.pack(pady=10)  # Add padding between label and entry

        # Create an email entry
        email_entry = ctk.CTkEntry(master=self)
        email_entry.pack()

        # Create a label for password
        password_label = ctk.CTkLabel(master=self, text="Password:")
        password_label.pack(pady=10)  # Add padding between label and entry

        # Create a password entry
        password_entry = ctk.CTkEntry(master=self, show="*")
        password_entry.pack()

        # Create a frame for buttons
        button_frame = ctk.CTkFrame(master=self)
        button_frame.pack(pady=10)  # Add padding between password entry and buttons

        # Create a register button
        register_button = ctk.CTkButton(master=button_frame, text="Register", command=self.register)
        register_button.pack(side=ctk.LEFT, padx=5)  # Add padding on the left side

        # Create a login button
        login_button = ctk.CTkButton(master=button_frame, text="Login", command=self.login)
        login_button.pack(side=ctk.LEFT, padx=5)  # Add padding on the left side

    def register(self):
        """
        Performs the register operation.
        """
        print("Register")

    def login(self):
        """
        Performs the login operation.
        """
        print("Login")