from django.http import JsonResponse
from django.shortcuts import render
from openai import OpenAI
import time

client = OpenAI(
    api_key = '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',
)

instruction_set = """
"You are to only reply the schedule of a user with minimal elaboration, 
the user will input a list of tasks and specifications, 
you are to take those tasks and make a very well planned schedule including breaks and eating. "
"""


def ask_openai(message):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instruction_set},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    #usage = response.usage.total_tokens
    return answer

def schebot(request):
    print("[system / views.py]: Request made")
    if request.method == 'POST':
        print("[system / views.py]: Post request made")
        message = request.POST.get('message')  
        print("[system / views.py] - request made: ",message)
        if len(message) < 1:
            time.sleep(3) #artificial delay
            return JsonResponse({'message': message, 'response': "Please input some tasks"})
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'main.html')
