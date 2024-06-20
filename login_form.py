import ipywidgets as widgets
from IPython.display import display, clear_output
from registration_form import user_data  # Import the shared user_data dictionary

def display_login_form(home_page_callback, attendance_form_callback):
    clear_output()
    login_output = widgets.Output()

    def login_user(b):
        login_output.clear_output()
        with login_output:
            if login_username.value in user_data and user_data[login_username.value]['password'] == login_password.value:
                print(f"Welcome, {login_username.value}!")
                attendance_form_callback()
            else:
                print("Invalid username or password")

    login_username = widgets.Text(description="Username:")
    login_password = widgets.Password(description="Password:")
    login_button = widgets.Button(description="Login")

    home_link = widgets.Button(description="Back to Home", button_style='', layout=widgets.Layout(width='auto', height='auto'))
    home_link.style.button_color = 'purple'
    home_link.style.font_size = '20px'
    home_link.on_click(lambda b: home_page_callback())

    login_button.on_click(login_user)
    display(login_username, login_password, login_button, login_output, home_link)
