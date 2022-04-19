
import random
import dearpygui.dearpygui as dpg
import time

YELLOW = (247,191,80) #F7BF50 
DARK_BROWN = (39,24,1)  #271801 


class TriviaMaster:

    def __init__(self, question_list:list):
        self.question_number = 1
        self.score = 0
        self.question_list = question_list
        self.current_question = self.question_list[0]
        self.question_text = self.current_question.text
        self.answers = [self.current_question.answer, self.current_question.incorrect_1, self.current_question.incorrect_2, self.current_question.incorrect_3]
        random.shuffle(self.answers)
        

    def are_there_more_questions(self):
        """Returns True if there are more questions left in the quiz and False if there is not."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Uses the current question positon to retrieve the current trivia question from the question list, then tics the question counter. 
        Labels quesion and answers and shuffles answers. Asks for an input from the user, input must be the string of the answer. Calls the check answer func."""
        self.question_number += 1

        self.current_question = self.question_list[self.question_number-1]
        self.question_text = self.current_question.text
        self.answers = [self.current_question.answer, self.current_question.incorrect_1, self.current_question.incorrect_2, self.current_question.incorrect_3]
        random.shuffle(self.answers)



        
    def update_screen(self):
        dpg.set_value(item="question", value=f"Q {self.question_number} of {len(self.question_list)}:  {self.question_text}")
        dpg.set_value(item="ans1", value=self.answers[0])
        dpg.set_value(item="ans2", value=self.answers[1])
        dpg.set_value(item="ans3", value=self.answers[2])
        dpg.set_value(item="ans4", value=self.answers[3])


    def check_answer(self, index):
        """Compares the user answer against the correct answer. Provides appropriate feedback and awards a point if correct."""
        correct_answer = self.current_question.answer

        if self.answers[index].lower() == correct_answer.lower():
            self.score += 1
            dpg.set_value("final_score", "     You got it right!")
        else:
            dpg.set_value("final_score", f"That's wrong.\n\nThe correct answer was '{correct_answer}'")

        time.sleep(4)
        
        dpg.set_value("final_score", "")
        if not self.are_there_more_questions():
            self.end_of_game()
        else:
            self.next_question()
            self.update_screen()
            
    def end_of_game(self):

        dpg.set_value("final_score", f"You've completed the round!!!\n\nYour final score was: {self.score}/{self.question_number}")
        


    def initiate_window(self):

        dpg.create_context()
        dpg.create_viewport(title='Trivia Now', width=1234, height=1234) # Creates the viewport.
        dpg.setup_dearpygui() # Assigns the viewport.

        width, height, _, data = dpg.load_image("code/mitch/python/trivia_now/trivia_logo.jpeg")
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
            dpg.add_text(f"Q {self.question_number} of {len(self.question_list)}:  {self.question_text}", tag="question", color=YELLOW, indent=50, wrap=1100)
            dpg.add_spacing(count=8)
            dpg.add_button(label=" A ", callback=lambda : self.check_answer(index=0), indent=50)
            dpg.add_text(self.answers[0], tag="ans1", color=YELLOW, indent=50, wrap=1100)
            dpg.add_spacing(count=8)
            dpg.add_button(label=" B ", callback=lambda : self.check_answer(index=1), indent=50)
            dpg.add_text(self.answers[1], tag="ans2", color=YELLOW, indent=50, wrap=1100)
            dpg.add_spacing(count=8)
            dpg.add_button(label=" C ", callback=lambda : self.check_answer(index=2), indent=50)
            dpg.add_text(self.answers[2], tag="ans3", color=YELLOW, indent=50, wrap=1100)
            dpg.add_spacing(count=8)
            dpg.add_button(label=" D ", callback=lambda : self.check_answer(index=3), indent=50)
            dpg.add_text(self.answers[3], tag="ans4", color=YELLOW, indent=50, wrap=1100)
            dpg.add_spacing(count=12)
            dpg.add_text("", tag="final_score", color=YELLOW, indent=350, wrap=800)



        dpg.bind_theme(global_theme)
        dpg.set_global_font_scale(2)
        dpg.show_viewport() # Shows the Viewport.
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui() # This completely handles the render loop.
        dpg.destroy_context()

