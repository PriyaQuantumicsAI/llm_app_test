# Author: Priyadharshini Devarajan
# Date: September 21, 2023
# Description: GPT model IO

import openai


class GptModel:

    def __init__(self, main_logger, config):
        self._logger = main_logger
        self._app_config = config
        openai.api_key = config.openapi_key

    def process_prompt(self, model_type, user_prompt):
        # use openapi model to parse user prompt to sql or cql
        response = openai.Completion.create(
            model=model_type,
            prompt=user_prompt,
            temperature=0,
            max_tokens=1500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=['#', ';']
        )
        self._logger.info(f"code-davinci-002 Response  :  {response}")
        prog_query = response['choices'][0]['text']
        prog_query_cleaned = prog_query.replace('`', '')
        self._logger.info(f"TEXT TO SQL or CQL:  :  {prog_query_cleaned}")
        return prog_query_cleaned
