import numpy as np
import os
import pandas as pd
import pingouin as pg
import sys

from pathlib import Path


QUESTIONNARIE_FILENAME = os.environ.get('QUESTIONNARIE_FILENAME', 'questionnaire.json')
QUESTIONNAIRE_PATH = Path(QUESTIONNARIE_FILENAME)
QUESTIONNAIRE_PATH_RESULT = os.environ.get('QUESTIONNAIRE_PATH_RESULT', 'questionnaire.csv')
SAMPLE_SIZE = os.environ.get('SAMPLE_SIZE', 5)
EXPECTED_THRESHOLD = os.environ.get('EXPECTED_THRESHOLD', 0.8)

def generate_selected_options_for_label(options, sample_size=SAMPLE_SIZE):
    return np.random.randint(0, len(options), size=sample_size)


def main():
    data = pd.read_json(QUESTIONNAIRE_PATH)
    counter = 0
    while True:
        counter += 1
        data['selected_option'] = [generate_selected_options_for_label(options) for options in data['options']]
        result_dataframe = pd.DataFrame()
        for value in data.values:
            result_dataframe[value[0]] = value[len(value) - 1]
        cronbach = pg.cronbach_alpha(data=result_dataframe)
        if(float(cronbach[0]) < EXPECTED_THRESHOLD):
            print(f'Not enough alpha of cronbach after {counter} tries')
            continue
        else:
            print(f'Found one on try {counter}. Alpha of cronbach is: {cronbach[0]}')
            break
    print(result_dataframe.T.columns)
    result_dataframe.T.to_csv(QUESTIONNAIRE_PATH_RESULT)

if __name__ == "__main__":
    main()