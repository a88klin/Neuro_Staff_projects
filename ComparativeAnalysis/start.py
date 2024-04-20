from vacancy_processing import vacancy_parsing
from resume_processing import resume_parsing
from chatgpt_processing import get_answers_gpt
from report_processing import create_pdf
from config import settings
import os


directories = [settings.resumes_json_files,
               settings.vacancies_json_files,
               settings.pdf_report_files]
for dir in directories:
    os.makedirs(dir, exist_ok=True)

RESUMES_JSON_FILES = directories[0]
VACANCIES_JSON_FILES = directories[1]
PDF_REPORT_FILES = directories[2]


def main(resume_json: str,
         vacancies_list_json: list,
         main_skill: str=''):

    resume_path = os.path.join(f'{RESUMES_JSON_FILES}', resume_json)
    resume_dict = resume_parsing(resume_path)

    for vacancy_json in vacancies_list_json:
        vacancy_path = os.path.join(f'{VACANCIES_JSON_FILES}', vacancy_json)
        vacancy_dict = vacancy_parsing(vacancy_path)

        answers_gpt = get_answers_gpt(resume_dict, vacancy_dict, main_skill=main_skill)

        try:  # PDF отчет. ************************************************
            pdf_file_name = f"{resume_json[:-5]}_+_{vacancy_json[:-5]}.pdf"
            path = os.path.join(f'{PDF_REPORT_FILES}', pdf_file_name)
            paragraphs = [f"Резюме: {resume_json}",
                          f"Вакансия: {vacancy_json}",
                          f"{answers_gpt['all_skills']}",
                          f"{answers_gpt['main_skill']}"]
            create_pdf(path, paragraphs)
        except Exception as ex:
            print('PDF отчет:', ex)


# **************************************************************************
if __name__ == "__main__":
    # Резюме
    resume_json = 'Будилов_Кирилл-ac4ecc8b-8da8-4441-b4de-a71c0805bdcd.json'
    # Выбранные вакансии
    vacancies_list_json = ['Java_разработчик-2ce1bca2-5a23-4f68-8566-8ff0f7f87e3c.json',
                           'Java_разработчик-6e8ea5e3-47fb-4a15-84fa-6ab618dcbbe0.json',
                           'Java_разработчик-654b79d7-6b07-4705-969d-41a9eef10503.json',
                           'Java_разработчик-f6b48d5d-882e-4afd-8826-3d46b78342c6.json',
                           ]
    # Указать main_skill - какой навык в резюме является ключевым.
    # Если не указано, AI попытается определить самостоятельно
    main(resume_json, vacancies_list_json, main_skill='')
