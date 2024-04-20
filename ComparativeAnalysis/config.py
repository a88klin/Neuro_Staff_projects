# pip install pydantic pydantic-settings
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')
    openai_api_key: SecretStr

    vacancies_json_files: str
    resumes_json_files: str
    pdf_report_files: str


settings = Settings()
