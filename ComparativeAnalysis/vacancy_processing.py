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
                                          Skills: {(', ').join(vacancy['data'].get('skills', ''))}. """)

        vacancy_dict['mandatory_requirements'] = re.sub(r'\s+', ' ', f"""
                      Requirements: {(' ').join(vacancy['data'].get('mandatoryRequirements', ''))} """)

        vacancy_dict['additional_requirements'] = re.sub(r'\s+', ' ', f"""
                          Add.Requirements: {(' ').join(vacancy['data'].get('additionalRequirements', ''))} """)

        vacancy_dict['levels'] = f"Levels: {(', ').join(vacancy['data'].get('experienceLevels', ''))}. "

        vacancy_dict['tasks'] = \
                    re.sub(r'\s+', ' ', f"Tasks: {(' ').join(vacancy['data'].get('projectTasks'))} ")

        return vacancy_dict
    return None
