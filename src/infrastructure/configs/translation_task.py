from infrastructure.configs.language import LanguageEnum
from typing import Optional, Union
from pydantic.fields import Field
from pydantic.main import BaseModel
from core.types import ExtendedEnum

class TranslationTaskNameEnum(str, ExtendedEnum):

    private_file_translation = 'private_file_translation'
    private_plain_text_translation = 'private_plain_text_translation'

    public_file_translation = 'public_file_translation'
    public_plain_text_translation = 'public_plain_text_translation'

TRANSLATION_PUBLIC_TASKS = [
    TranslationTaskNameEnum.public_file_translation.value,
    TranslationTaskNameEnum.public_plain_text_translation.value
]

TRANSLATION_PRIVATE_TASKS = [
    TranslationTaskNameEnum.private_file_translation.value,
    TranslationTaskNameEnum.private_plain_text_translation.value
]

class TranslationTaskStepEnum(str, ExtendedEnum):
    
    detecting_language = 'detecting_language'
    translating_language = 'translating_language'
    
class TranslationTask_LangUnknownResultFileSchemaV1(BaseModel):

    source_text: str 
    source_lang: Union[LanguageEnum, None] = Field(None, allow_mutation=False)

    target_text: Union[str, None] = Field(None, allow_mutation=False)
    target_lang: LanguageEnum 

    task_name: TranslationTaskNameEnum

    status: str = Field('language_not_yet_detected', allow_mutation=False) 

    schema_version: int = Field(1, allow_mutation=False) 

    class Config:
        use_enum_values = True
        validate_assignment = True

class TranslationTask_NotYetTranslatedResultFileSchemaV1(BaseModel):

    source_text: str
    source_lang: LanguageEnum 

    target_text: Union[str, None] = Field(None, allow_mutation=False)
    target_lang: LanguageEnum 

    task_name: TranslationTaskNameEnum

    status: str = Field('not_yet_translated', allow_mutation=False) 

    schema_version: int = Field(1, allow_mutation=False) 

    class Config:
        use_enum_values = True
        validate_assignment = True

class TranslationTask_TranslationCompletedResultFileSchemaV1(BaseModel):

    source_text: str
    source_lang: LanguageEnum

    target_text: str
    target_lang: LanguageEnum

    task_name: TranslationTaskNameEnum

    status: str = Field('translated', allow_mutation=False) 

    schema_version: int = Field(1, allow_mutation=False)  

    class Config:
        use_enum_values = True
        validate_assignment = True