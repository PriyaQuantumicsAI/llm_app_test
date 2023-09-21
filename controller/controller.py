# Author: Priyadharshini Devarajan
# Date: September 21, 2023
# Description: Controller page for api jarvis_ai_process_text.


import openai

# Creating a class for the controller
class AppController:

    def __init__(self, main_logger, config):
        self._logger = main_logger
        self._app_config = config

    def jarvis_gen_ai_process_text(self, json_data):
        res_dic = {}
        user_prompt = json_data.get('prompt')
        result = user_prompt + 'Success'
        print(result)
        return result
        

               

        
