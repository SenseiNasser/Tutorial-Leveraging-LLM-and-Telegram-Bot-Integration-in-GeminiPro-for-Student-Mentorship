# Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship


# Description
This project is a step-by-step tutorial designed for students seeking mentorship with their textbooks. 
Leveraging GeminiPro, it integrates a Large Language Model (LLM) and Telegram bot to provide personalized assistance.
Tailored for student needs, it offers intuitive guidance, explanations, and resources, revolutionizing textbook learning.


# Brief
As a fellow senior student in Computer Science and owner of study groups on Telegram, I understand the challenges students face in grasping complex material.
Recognizing the need for personalized assistance, I created this tutorial.
Tailored for students seeking a personal LLM bot assistant, this project offers customization options for textbooks or PowerPoint slides.
It aims to revolutionize learning by providing intuitive guidance, explanations, resources, and even the ability to 
generate Multiple Choice Questions (MCQs) or explanations on specific topics from the materials, enhancing comprehension and reinforcing key concepts for students
– all from the material set for exams.

# Tools used in this project

[![My Skills](https://skillicons.dev/icons?i=py,vscode,powershell&perline=1)](https://skillicons.dev)


# Instructions
## Step 1: Creating telegram bot API token
A.**Open Telegram**

B.**Search for BotFather**

C.**Start BotFather**

D.**Create a New Bot**

E.**Choose a Username**

F.**Copy API Token**

<img width="716" alt="Screenshot 2024-04-25 211618" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/35b861ed-b04f-4dc0-81f0-65317bf68396">


## Step 2: Setting Environment in VS Code and Use Terminal
A. **Make a folder**

> Make folder for the project, pick any location you want for example: Desktop.

B. **Open The folder in vs code**: 
> Open VS Code and click on "File" > "Open Folder". Select the folder you created in the previous step.


C.Open Terminal in VS Code
> In VS Code, you can open the terminal by clicking on "View" > "Terminal"


## Step 3: Create Virtual Environment and install requirement packages.
> **Note:** Virtual environments are important because they allow you to isolate Python dependencies for each project, preventing conflicts and ensuring that your project runs smoothly regardless of changes to your system-wide Python setup.

A.**Create a Virtual Environment**
> In the terminal, run the following command to create a virtual environment in your project folder:

```
python -m venv venv
```
B.**Activate the Virtual Environment**
>To activate the virtual environment, run the following command:

* On Windows:
  
```
.\venv\Scripts\activate
```

* On macOS/Linux:

```
source venv/bin/activate
```
>You should see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.
<img width="501" alt="Screenshot 2024-04-25 234752" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/a7b59334-6def-40d2-b887-29172864a798">

<br>

C.**Install Packages**
>Now that your virtual environment is active, you can install the required packages using pip:
```
pip install pyTelegramBotAPI google-generativeai
```


## Step 3: Sign-in Google Ai Studio & train your model
> In this section we will upload the Material we need such as textbook or powerpoints files and give instructions to the model to follow for example:
> we may train the model not to answer any pormpt or messages witout a unique word or train him to focus on certain tasks.

A. **Visit Google Ai Studio** https://aistudio.google.com/

B. **Sign-in with your google account**

C. **Create new >> chat prompt**

<img width="207" alt="Screenshot 2024-04-26 001843" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/1fd4411b-c661-412c-81eb-a656e8c236b3">

<img width="1090" alt="V" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/167ff025-e8eb-40f5-b3f8-83c0f03decd9">

> In Green area you upload your material such as textbook, In blue area you write your instructions to the model, In yellow area you must train him to make sure follow what you need note that instructions above might not follow it 100% so confirm it to the model to follow it in yellow area advice to train him here with, the more train the model the more accuracy 

D.**When you done training the model, click get code**

<img width="213" alt="Screenshot 2024-04-26 005055" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/dc2ac32a-0039-4b97-97a6-eb316f425f65">

E.**Copy the python code**

<img width="628" alt="Screenshot 2024-04-26 005117" src="https://github.com/SenseiNasser/Tutorial-Leveraging-LLM-and-Telegram-Bot-Integration-in-GeminiPro-for-Student-Mentorship/assets/65749356/2a95289d-b8d0-4843-a566-0f14ea24c9fc">



## Step 4: copy the train model code & generate your API Gemini key



C. **Go to get API key**
D. **Create API key**
