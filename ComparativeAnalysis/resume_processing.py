import json
import re


def resume_parsing(resume_json):
    if resume_json.endswith('.json'):
        with open(resume_json, 'r', encoding='utf-8') as r:
            resume = json.load(r)

        resume_dict = dict()
        # ****************************************************
        resume_dict['position_skills'] = re.sub(r'\s+', ' ', f"""
                     Position: {resume['title']} .
                     Skills: {(', ').join(resume['skill_set'])}""")

        if resume['skills'] != None: # Add.skills
            add_skills = f"{resume['skills']}."
        else:
            add_skills = ''
        resume_dict['add_skills'] = add_skills

        experience = ''
        for n, place in enumerate(resume['experience']):
            experience += f""" *** Job experience {n+1}: 
                          Position - {place['position']}.
                          Period (yyyy-mm-dd): from {place['start']} to {place['end']}. 
                          Description of job {n+1}: {place['description']} """
        resume_dict['experience'] = re.sub(r'\s+', ' ', f'{experience}')

        return resume_dict
    return None
