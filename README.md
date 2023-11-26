# Autoplan
AI powered automated schedule generator.
My entry into the clockhacks international hackathon

# Inspiration
One of the most recommended and easy ways to defeat, or lessen the effect of procrastination and time management issues is to create a schedule. The schedule not only sorts out your tasks, but also helps to create a good mental image of the tasks ahead. 

However, making this schedule can be both confusing and time consuming, which discourages it's use. Humans tend to prefer what is convenient, so making Schedule creation more convenient and accessible will dramatically improve time management.

# What it does

With this tool we can make the creation of schedules convenient enough to do almost daily. Just input the tasks, and schedule will appear for you. You can set the time of the schedule, use the pomodoro method and change any schedule specification such as length of breaks, meal times, and study methods and patterns.

# How I built it
The project was built using the Django framework. Python was used for the backend, the front end is a single page consisting of html, css, and JS because django for easy debugging. I didn't use any CSS libraries for the front end, and just crafted everything the exact way I wanted it to look.

# Challenges I ran into
There were some api issues, and interacting with the OpenAI's API was slightly annoying due to confusing documentation, but googling helped.

# Accomplishments that I'm proud of

I gathered ideas from my friends and feedback from people I knew, and i'm surprised i managed to complete this project within the time constraints. I can see that I've come a long way as a programmer too.

I believe that this tool is genuinely useful, and I will most likely try to host it on my personal domain when i buy one, the tool has a lot of scaling potential and can benefit lots of people around the world who have similar problems in time management and procrastination.

# What I learned
I learned how debug in more efficient ways, i learned more about how django is set up and how it's used, i learned about openai's api, and I learned about configuring shading in CSS and how it can give depth to elements.

# What's next for Autoplan

I want to buy my own domain someday so I can host the tool on my personal site. This tool will help me in many ways and I will try to expand it even further.

# How to run

Requirements:

pip3 install django

pip3 install openai

to run:

cd scheduler

python3 manage.py runserver
