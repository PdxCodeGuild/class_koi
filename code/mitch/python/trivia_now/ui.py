
from distutils.fancy_getopt import wrap_text
from turtle import color
import dearpygui.dearpygui as dpg

YELLOW = (247,191,80) #F7BF50 
DARK_BROWN = (39,24,1)  #271801 
BROWN = (120,93,38) #785D26 
LIGHT_BROWN = (249,217,154) #F9D99A 

item_list = ["Answer #1", "Answer #2", "Answer #3", "Answer #4"]
welcome_message = "Welcome to Trivia Now! Twenty trivia questions are headed your way now!"

dpg.create_context()
dpg.create_viewport(title='Trivia Game', width=1234, height=900) # Creates the viewport.
dpg.setup_dearpygui() # Assigns the viewport.

width, height, channels, data = dpg.load_image("code/mitch/python/trivia_game/trivia_logo.jpeg")
with dpg.texture_registry():
    texture_id = dpg.add_static_texture(width, height, data)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (YELLOW), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (DARK_BROWN))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, YELLOW)



with dpg.window(tag="Primary Window"):
    dpg.add_image(texture_id)
    dpg.add_spacing(count=6)
    dpg.add_text(welcome_message, label="question", color=YELLOW, indent=50, wrap=1100)
    dpg.add_spacing(count=5)
    dpg.add_radio_button(items=item_list, indent=50)
    dpg.add_spacing(count=5)
    dpg.add_button(label="Submit Answer", callback=None, indent=50)
    


dpg.bind_theme(global_theme)
dpg.set_global_font_scale(2)
dpg.show_viewport() # Shows the Viewport.
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui() # This completely handles the render loop.
dpg.destroy_context()


