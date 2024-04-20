import json
import re


def vacancy_parsing(vacancy_json):
    if vacancy_json.endswith('.json'):
        with open(vacancy_json, 'r', encoding='utf-8') as r:
            vacancy = json.load(r)

        vacancy_dict = dict()
        # **************************************************************************************************
        vacancy_dict['position_skills'] = re.sub(r'\s+', ' ', f"""
                                          Position: {vacancy['data'].get('position', '')}. 
                                          Skills: {(', ').join(vacancy['skills'])}. """)

        vacancy_dict['mandatory_requirements'] = re.sub(r'\s+', ' ', f"""
                      Requirements: {(' ').join(vacancy['data'].get('mandatoryRequirements', ''))} """)

        try:
            vacancy_dict['additional_requirements'] = re.sub(r'\s+', ' ', f"""
                          Add.Requirements: {(' ').join(vacancy['data']['additionalRequirements'])} """)
        except Exception as ex:
            vacancy_dict['additional_requirements'] = ''

        vacancy_dict['levels'] = f"Levels: {(', ').join(vacancy['data'].get('experienceLevels', ''))}. "

        try:
            vacancy_dict['tasks'] = \
                         re.sub(r'\s+', ' ', f"Tasks: {(' ').join(vacancy['data']['projectTasks'])} ")
        except Exception as ex:
            vacancy_dict['tasks'] = ''

        return vacancy_dict
    return None
