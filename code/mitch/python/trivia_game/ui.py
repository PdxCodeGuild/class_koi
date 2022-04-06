import dearpygui.dearpygui as dpg
    
dpg.create_context()

width, height, channels, data = dpg.load_image("code/mitch/python/trivia_game/trivia_logo.jpeg")

item_list = ["Black", "Blue", "Red", "Orange"]

with dpg.texture_registry():
    texture_id = dpg.add_static_texture(width, height, data)

with dpg.window(tag="Primary Window"):
    dpg.add_image(texture_id)
    dpg.add_spacing(count=8)
    dpg.add_text("Wecome to Trivia!", color=(249,217,154))
    dpg.add_radio_button(items=item_list, )
    dpg.add_button(label="Submit Answer")
    

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (247, 191, 80), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvInputInt):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (120, 93, 38), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)


dpg.bind_theme(global_theme)
dpg.set_global_font_scale(2)
dpg.create_viewport(title='Trivia Game', width=1230, height=800) # Creates the viewport.
dpg.setup_dearpygui() # Assigns the viewport.
dpg.show_viewport() # Shows the Viewport.
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui() # This completely handles the render loop.
dpg.destroy_context()





#Primary yellow = #F7BF50 (247,191,80)
#Primary brown = #785D26 (120,93,38)
#Light brown = #F9D99A (249,217,154)