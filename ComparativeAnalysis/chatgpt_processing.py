from config import settings
import openai
import prompts
import os


os.environ["OPENAI_API_KEY"] = settings.openai_api_key.get_secret_value()
AMOUNT = 0 # Стоимость обработки OpenAI


def print_tokens_count_and_price(completion):
    # https://openai.com/pricing
    # gpt-3.5-turbo-0125 - Input: $0.50 / 1M tokens - Output: $1.50 / 1M tokens
    price = 0.5 * completion.usage.prompt_tokens / 1e6 + \
            1.5 * completion.usage.completion_tokens / 1e6
    print(f'Tokens used: {completion.usage.prompt_tokens} + '
                       f'{completion.usage.completion_tokens} = '
                       f'{completion.usage.total_tokens}. *** $ {round(price, 5)}')
    global AMOUNT
    AMOUNT += price


def answer_gpt(messages, temp=0.3):
    completion = openai.chat.completions.create(
                           model="gpt-3.5-turbo-0125",
                           messages=messages,
                           temperature=temp)
    print_tokens_count_and_price(completion)
    return completion.choices[0].message.content


def get_answers_gpt(resume_dict, vacancy_dict, main_skill):
    answers_gpt = dict()

    # Сравнение Скилов ****************************************************
    content_1 = prompts.question_skills(resume_dict['position_skills'],
                                        vacancy_dict['position_skills'] + vacancy_dict['mandatory_requirements'])
    message_1 = [{"role": "system", "content": prompts.system},
                 {"role": "user", "content": f"{content_1}"}]
    answers_gpt['all_skills'] = answer_gpt(message_1, temp=0)

    # Определение основного Скилла и опыта *********************************
    if not main_skill: # Если основной Скилл не указан
        content_2 = prompts.main_skill_1(resume_dict['position_skills'],
                                         resume_dict['experience'])
    else: # Если основной Скилл указан
        content_2 = prompts.main_skill_2(resume_dict['experience'], main_skill)

    message_2 = [{"role": "system", "content": prompts.system},
                 {"role": "user", "content": f"{content_2}"}]
    answers_gpt['main_skill'] = answer_gpt(message_2, temp=0)

    # ******************************************
    print('Total amount: $', round(AMOUNT, 5))
    return answers_gpt
