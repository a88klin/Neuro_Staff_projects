from datetime import datetime
import re


current_date = f"{datetime.now().strftime('%Y-%m')}-01"
system = "Ты профессиональный HR."

def question_skills(resume_skills, vacancy_skills):
    return re.sub(r'\s+', ' ', f"""
    *** You have the position and skills of a candidate from a resume: {resume_skills}. ***
    *** You also have the necessary position and skills listed in the vacancy: {vacancy_skills}. ***    
    Compare the skills of the candidate in the resume and the requirements from the vacancy.    
    * Questions #1: Specify which skills from the RESUME match the skills in the vacancy.
    * Questions #2: Specify which skills are listed on the resume, but not listed in the vacancy.
    * Questions #3: Specify which skills are missing from the resume compared to the required skills 
      from the vacancy.    
    * Questions #4: What is the percentage from 0 to 100 of matching skills in the candidate's resume 
      compared to the necessary skills in the vacancy and why? Answer the question briefly in one sentence. 
      Отвечай на русском языке. Если слова - навыки указаны на английском - выводи навыки на английском.
      В каждый ответ включи саммари вопроса, на который получен ответ. Выдавай только саммари вопроса и ответ.
      После каждого ответа ставь перенос строки: <br/>. При форматировании текста используй HTML теги: 
      <b>Жирный текст</b>, <i>курсив</i>, <u>подчеркивание</u> и другие стили, а также перенос строки <br/>""")


def main_skill_1(resume_skills, resume_experience, current_date=current_date):
    return re.sub(r'\s+', ' ', f"""
    *** You have the position and skills of a candidate from a resume: {resume_skills}. *** 
    *** You have the experience of a candidate from a resume: {resume_experience}. *** 
    Определи, какой один навык (skill) является самым важным и основным навыком для указанной позиции.
    После этого, Пожалуйста, посчитай сумму месяцев временных интервалов работы по основному навыку 
    на основании опыта кандидата, если этот основной навык упомянут в этом интервале.    
    Необходимо учитывать все интервалы работы, где упоминается основной навык.
    Если в интервале работы НЕТ упоминания основного навыка - этот интервал не считать.
    Какой суммарный опыт в месяцах по основному навыку ? Выведи расчет и количество месяцев.
    Даты в резюме указаны в формате: yyyy-mm-dd. Если дата "to None" - используй {current_date}.""")


def main_skill_2(resume_experience, main_skill, current_date=current_date): # Скилл указан
    return re.sub(r'\s+', ' ', f"""
    *** You have the experience of a candidate from a resume: {resume_experience}. ***
    Пожалуйста, посчитайте сумму месяцев временных интервалов работы по ключевому навыку "{main_skill}" 
    на основании опыта кандидата, если этот навык упомянут в этом интервале.    
    Необходимо учитывать все интервалы работы, где упоминается навык "{main_skill}".
    Если в интервале работы НЕТ упоминания навыка "{main_skill}" - этот интервал не считать.
    Какой суммарный опыт в месяцах по ключевому навыку "{main_skill}"? Выведи расчет и количество месяцев.
    Даты в резюме указаны в формате: yyyy-mm-dd. Если дата "to None" - используй {current_date}.""")
