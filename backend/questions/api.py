from django.db.models import query
from ninja import Router, Schema
from typing import List
from behaviors.models import Behavior, Problem, Solution
from .models import Question
from .schema import QuestionSchema
from .dfs import calculate_dfs
from django.http import JsonResponse

router = Router()





@router.get('/', response=List[QuestionSchema])
def list_question(request):
        queryset = Question.objects.all()
        return list(queryset)


class Answer(Schema):
    codes = []

@router.post("/result")
def result(request, payload: Answer):
    print(payload.codes)
    results = []
    data = []
    data = calculate_dfs(payload.codes)
    
    for c in data:
        obj = {}
        behaviors = Behavior.objects.filter(code=c);
        for behavior in behaviors:
            id = behavior.id
            problems = Problem.objects.filter(behavior_id=id)
            solutions = Solution.objects.filter(behavior_id=id)

            obj['code'] = behavior.code
            obj['behavior'] = behavior.name
            
            problemsText = [];
            solutionText = [];
            
            for problem in problems:
                problemsText.append({
                    "text": problem.text,
                })
            for solution in solutions:
                solutionText.append({
                    "text": solution.text,
                })

            obj['problems'] = problemsText
            obj['solutions'] = solutionText
            results.append(obj)

    return results
    

