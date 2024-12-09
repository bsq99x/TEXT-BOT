import time
import pyautogui as pys
import random

def type_text_naturally(file_path, wpm):
    # Average delay per character based on words per minute
    avg_word_length = 5  
    avg_delay_per_character = 60 / (wpm * avg_word_length)
    
    
    min_delay = avg_delay_per_character * 0.5
    max_delay = avg_delay_per_character * 1.5

    # Function for random pauses and typos
    def human_typing_delay():
        # Random delay between characters
        delay = random.uniform(min_delay, max_delay)
        

        if random.random() < 0.20:  
            time.sleep(random.uniform(0.2, 0.5))
        
        return delay
    
    # Timer before starting to type
    time.sleep(5)

    
    with open(file_path, "r", encoding="utf-8") as text_file:
        for each_line in text_file:
            for char in each_line:
                pys.typewrite(char)
                # Apply human-like delay
                time.sleep(human_typing_delay())

            
            if random.random() < 0.60:  # percentage of a typo
                # Simulate a typo
                typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                pys.typewrite(typo_char)
                time.sleep(human_typing_delay())
                pys.hotkey('backspace')  

wpm = 150  # Words per minute
type_text_naturally("text.txt", wpm)
