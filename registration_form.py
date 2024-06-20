import ipywidgets as widgets
from IPython.display import display, clear_output

# Dictionary to store user data
user_data = {}

def display_registration_form(home_page_callback):
    clear_output()
    name = widgets.Text(description="Full Name:")
    dob = widgets.DatePicker(description="Date of Birth:")
    student_id = widgets.Text(description="ID:")
    phone = widgets.Text(description="Phone Number:")
    username = widgets.Text(description="Username:")
    password = widgets.Password(description="Password:")
    register_button = widgets.Button(description="Register")
    output = widgets.Output()

    def register_user(b):
        user_data[username.value] = {
            'name': name.value,
            'date_of_birth': dob.value,
            'id': student_id.value,
            'phone': phone.value,
            'password': password.value,
            'attendance': {}
        }
        output.clear_output()
        with output:
            print(f"User {username.value} registered successfully!")

    register_button.on_click(register_user)

    home_link = widgets.Button(description="Back to Home", button_style='', layout=widgets.Layout(width='auto', height='auto'))
    home_link.style.button_color = 'purple'
    home_link.style.font_size = '20px'
    home_link.on_click(lambda b: home_page_callback())

    display(name, dob, student_id, phone, username, password, register_button, output, home_link)
