from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
from pyvalid import validators 
from email_validator import validate_email
import re


class Applicant(BaseModel):
    applicant_id: int 
    phone_number: str = Field(default=..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя, от 1 до 50 символов")
    last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия, от 1 до 50 символов")
    first_name_fa : str = Field(default=..., min_length=1, max_length=50, description="Отчество, от 1 до 50 символов")
    email: EmailStr = Field(default=..., description="Электронная почта ")
    snils : str = Field(default=..., description="Снилс")
    role_id: int =  Field(default=..., description="Этап")
    
    
    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("snils")
    @classmethod
    def validate_snils(cls, values: str) -> str:
        if validators.snils(values):
            return values
        else:
            raise ValueError('Снилс не соответствует формату')

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if validate_email(value):
            return value
        else:
            raise ValueError('email не соответствует формату')
