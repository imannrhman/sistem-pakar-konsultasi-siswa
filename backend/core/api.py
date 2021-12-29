from ninja import NinjaAPI
from questions.api import router as question_router

api = NinjaAPI()

api.add_router("/questions/", question_router)
