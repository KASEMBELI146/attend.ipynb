import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
from registration_form import display_registration_form, user_data
from login_form import display_login_form
from attendance_form import display_attendance_form

# Define home page
def home_page():
    clear_output()
    title = widgets.HTML(value="<h1 style='color: green; text-align: center; font-weight: bold; font-size: 32px;'>CS114: Programming II Attendance Confirmation</h1>")
    subtitle = widgets.HTML(value="<h2 style='color: blue; text-align: center; font-weight: bold; font-size: 28px;'>Module Tutor: Dr. Mostafa Al-Emran<br>Faculty of Engineering & IT, The British University in Dubai</h2>")
    
    registration_link = widgets.Button(description="Go to Registration", button_style='', layout=widgets.Layout(width='auto', height='auto'))
    registration_link.style.button_color = 'purple'
    registration_link.style.font_size = '20px'
    registration_link.on_click(lambda b: display_registration_form(home_page))
    
    login_link = widgets.Button(description="Go to Login", button_style='', layout=widgets.Layout(width='auto', height='auto'))
    login_link.style.button_color = 'purple'
    login_link.style.font_size = '20px'
    login_link.on_click(lambda b: display_login_form(home_page, display_attendance_form))
    
    display(title, subtitle, widgets.HTML("<br><br>"), registration_link, login_link)

# Function to display student table
def display_student_table():
    data = {
        'Name': [user['name'] for user in user_data.values()],
        'ID': [user['id'] for user in user_data.values()],
        'Attendance Status': ['Present' if user['attendance'] else 'Absent' for user in user_data.values()]
    }
    df = pd.DataFrame(data)
    
    clear_output()
    display(df)

    home_link = widgets.Button(description="Back to Home", button_style='', layout=widgets.Layout(width='auto', height='auto'))
    home_link.style.button_color = 'purple'
    home_link.style.font_size = '20px'
    home_link.on_click(lambda b: home_page())
    display(home_link)

home_page()
