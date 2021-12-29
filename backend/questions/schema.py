from .models import Question
from ninja.orm import create_schema


QuestionSchema = create_schema(Question)