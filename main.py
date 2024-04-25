import telebot
import google.generativeai as genai


# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(
    "HERE YOU PUT YOUR TELEGRAM API KEY", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, "HERE YOU CAN TYPE ANY INTRODUCTION MESSAGE YOU WANT TO SEND TO THE USER")


genai.configure(api_key="HERE YOU PUT YOUR GEMINI API KEY")

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]


system_instruction = "* All text generate from the file\n* don't respond to any prompt that not include #Ask in the prompt\n* if prompt don't contain #Ask keep silence , don't reply , don't answer \n* keep the text non bold format\n* you are mentor can explain and answer questions from the file\n* you also can generate questions from the file especially MCQ\n* you can explain in arabic or english language \n* the file is powerpoint slides you must know the page number you get the answer from\n* always support your answer from the context in the file"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

uploaded_files = []


def upload_if_needed(pathname: str) -> list[str]:
    path = Path(pathname)
    hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
    try:
        existing_file = genai.get_file(name=hash_id)
        return [existing_file.uri]
    except:
        pass
    uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
    return [uploaded_files[-1].uri]


def extract_pdf_pages(pathname: str) -> list[str]:
    parts = [f"--- START OF PDF ${pathname} ---"]
    # Add logic to read the PDF and return a list of pages here.
    pages = []
    for index, page in enumerate(pages):
        parts.append(f"--- PAGE {index} ---")
        parts.append(page)
    return parts


convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": extract_pdf_pages("<path>/document0.pdf")
    },
    {
        "role": "user",
        "parts": ["Alternatives to Traditional Waterfall SDLC are ?"]
    },
    {
        "role": "model",
        "parts": ["#Ask \nAlternatives to Traditional Waterfall SDLC from page 18 are:\n\n*   Prototyping\n*   CASE tools\n*   Joint Application Design (JAD)\n*   Rapid Application Development (RAD)\n*   Agile Methodologies\n*   eXtreme Programming"]
    },
    {
        "role": "user",
        "parts": extract_pdf_pages("<path>/document1.pdf")
    },
    {
        "role": "user",
        "parts": ["Alternatives to Traditional Waterfall SDLC are ?"]
    },
    {
        "role": "model",
        "parts": ["#Ask \nAlternatives to Traditional Waterfall SDLC from page 26 are:\n\n*   Prototyping\n*   CASE tools\n*   Joint Application Design (JAD)\n*   Rapid Application Development (RAD)\n*   Agile Methodologies\n*   eXtreme Programming"]
    },
    {
        "role": "user",
        "parts": ["don't answer without #ask be in the prompt question"]
    },
    {
        "role": "model",
        "parts": ["## Requirements Determination Techniques \n\nSeveral techniques can be employed to effectively gather and analyze system requirements. Let's explore some of the key methods:\n\n**Traditional Techniques:**\n\n* **Interviewing:**\n    * **Individual Interviews:** Conducting one-on-one interviews allows for in-depth exploration of individual perspectives and concerns. \n    * **Group Interviews:**  Gathering stakeholders together facilitates open discussion, identification of conflicting viewpoints, and the potential for synergistic solutions.\n* **Observation:** Directly observing users performing their tasks provides firsthand insights into actual workflows and pain points. \n* **Document Analysis:** Examining existing documents such as procedures, reports, and forms offers valuable information about current processes and data usage.\n\n**Contemporary Techniques:**\n\n* **Joint Application Design (JAD):** This collaborative approach brings stakeholders and analysts together in intensive workshops to define and refine system requirements. \n* **Prototyping:** Creating interactive prototypes enables users to experience and provide feedback on potential system functionalities, leading to more accurate requirements.\n* **CASE Tools:** Computer-Aided Software Engineering tools assist in analyzing existing systems, modeling processes, and managing requirements data. \n\n**Radical Techniques:**\n\n* **Business Process Reengineering (BPR):** This approach focuses on radically redesigning core business processes to achieve significant improvements in efficiency and effectiveness.\n\n**Agile Techniques:**\n\n* **User Stories:** Agile methodologies often utilize user stories, which are brief descriptions of desired system features from the user's perspective.\n* **Backlog Grooming:** Regular backlog grooming sessions ensure that requirements are prioritized and refined based on changing needs and priorities.\n\n**Additional Considerations:**\n\n* **Selecting the appropriate techniques:** The choice of techniques depends on factors such as project scope, stakeholder availability, and the level of detail required. \n* **Combining techniques:** Often, a combination of techniques is employed to gain a comprehensive understanding of system requirements.\n* **Iterative refinement:** Requirements determination is an ongoing process that involves continuous refinement as the project progresses."]
    },
    {
        "role": "user",
        "parts": ["dont reply or answer if i ask you without the word #Ask"]
    },
    {
        "role": "model",
        "parts": ["(silence)"]
    },
    {
        "role": "user",
        "parts": ["Alternatives to Traditional Waterfall SDLC are ?"]
    },
    {
        "role": "model",
        "parts": ["(silence)"]
    },
    {
        "role": "user",
        "parts": ["Four Approaches to Reuse"]
    },
    {
        "role": "model",
        "parts": ["(silence)"]
    },
    {
        "role": "user",
        "parts": ["Four Approaches to Reuse #ask"]
    },
    {
        "role": "model",
        "parts": ["#Ask \n\n## Four Approaches to Reuse (Page 53)\n\nSoftware reuse involves utilizing existing software assets to build new applications, leading to increased productivity and quality. Here are four common approaches to reuse:\n\n**1. Ad Hoc Reuse:**\n\n* This informal approach relies on developers' knowledge and initiative to find and reuse suitable software components.\n* While flexible, it can be inconsistent and may not be well-documented, making it difficult to track and manage reused components.\n\n**2. Facilitated Reuse:**\n\n* This approach provides developers with tools and resources to support reuse, such as component libraries, search engines, and guidelines.\n* It promotes a more systematic approach to reuse but requires investment in infrastructure and training.\n\n**3. Designed Reuse:**\n\n* Software components are explicitly designed for reuse from the outset, considering factors like modularity, generality, and documentation.\n* This approach leads to higher-quality reusable components but requires careful planning and design effort.\n\n**4. Managed Reuse:**\n\n* This comprehensive approach combines designed reuse with organizational support and processes to ensure effective reuse practices.\n* It involves establishing a reuse program with dedicated roles, responsibilities, and metrics to track reuse success. \n\nChoosing the most suitable approach depends on factors such as organizational maturity, available resources, and the desired level of reuse."]
    },
    {
        "role": "user",
        "parts": ["generate 3 MCQ questions #ask"]
    },
    {
        "role": "model",
        "parts": ["#Ask \n\n## MCQ Questions:\n\n**Question 1:**\n\nWhich of the following is NOT a primary enabling technology for software reuse?\n\na) Object-oriented development\nb) Component-based development\nc) Waterfall development methodology \nd) Code generators\n\n**Question 2:**\n\nThe process of assessing the degree to which a proposed system solves business problems or takes advantage of business opportunities is known as:\n\na) Economic feasibility\nb) Technical feasibility\nc) Operational feasibility\nd) Schedule feasibility\n\n**Question 3:**\n\nA use case diagram typically includes:\n\na) Actors and use cases \nb) Data flows and data stores \nc) Processes and decision points\nd) Entity-relationship diagrams"]
    },
    {
        "role": "user",
        "parts": ["what is the answer ? #ask"]
    },
    {
        "role": "model",
        "parts": ["#Ask \n\n## MCQ Answers:\n\n**Question 1:** c) Waterfall development methodology  (Page 48)\n\n**Question 2:** c) Operational feasibility (Page 162) \n\n**Question 3:** a) Actors and use cases (Page 268)"]
    },
    {
        "role": "user",
        "parts": ["generate 5 MCQ"]
    },
    {
        "role": "model",
        "parts": ["#Ask\n\n## 5 MCQ Questions:\n\n**Question 1:**\n\nWhich phase of the SDLC focuses on defining clear, discrete activities and the work needed to complete them?\n\na) Planning\nb) Analysis\nc) Design \nd) Implementation\n\n**Question 2:**\n\nWhat is the primary deliverable from the project initiation and planning phase?\n\na) System prototype\nb) Baseline Project Plan (BPP) \nc) Test cases\nd) User manual\n\n**Question 3:**\n\nA technique that uses optimistic, pessimistic, and realistic time estimates to determine expected task duration is:\n\na) Gantt chart\nb) Critical path method \nc) PERT\nd) Work breakdown structure\n\n**Question 4:**\n\nThe process of assessing potential legal and contractual ramifications due to the construction of a system is known as:\n\na) Operational feasibility\nb) Schedule feasibility\nc) Legal and contractual feasibility \nd) Political feasibility \n\n**Question 5:**\n\nWhich of the following is NOT a benefit of using Joint Application Design (JAD)?\n\na) More effective use of time\nb) Opportunity for synergies among stakeholders \nc) Reduced project costs\nd) Simultaneous collection of system requirements"]
    },
    {
        "role": "user",
        "parts": ["the last prompt don't including #Ask you should not respond without #ask"]
    },
    {
        "role": "model",
        "parts": ["(silence)"]
    },
    {
        "role": "user",
        "parts": ["generate 5 MCQ"]
    },
    {
        "role": "model",
        "parts": ["(silence)"]
    },
    {
        "role": "user",
        "parts": ["generate 5 MCQ #Ask"]
    },
    {
        "role": "model",
        "parts": ["#Ask \n\n## 5 MCQ Questions:\n\n**Question 1:**\n\nWhich of the following is NOT a primary activity in the analysis phase of the SDLC?\n\na) Requirements determination \nb) System design\nc) Requirements structuring\nd) Feasibility analysis\n\n**Question 2:**\n\nA graphical representation of a project that shows each task as a horizontal bar whose length is proportional to its time for completion is called a:\n\na) Network diagram \nb) Gantt chart\nc) PERT chart\nd) Flowchart \n\n**Question 3:**\n\nIn a decision table, a condition whose value does not affect which actions are taken for two or more rules is known as:\n\na) Action stub\nb) Condition stub \nc) Indifferent condition\nd) Rule \n\n**Question 4:**\n\nAn external entity that interacts with a system in a use case model is called a(n):\n\na) Use case\nb) Actor \nc) Association \nd) System boundary\n\n**Question 5:**\n\nThe symbol for a decision point in BPMN is a:\n\na) Circle\nb) Rectangle \nc) Diamond\nd) Arrow"]
    },
    {
        "role": "user",
        "parts": ["summerize Module 2 for me and give me keypoints of the Module 2 #Ask"]
    },
    {
        "role": "model",
        "parts": ["## Module 2 Summary: Foundations of Project Management \n\n**Key Points:**\n\n* **Importance of Project Management:** Effective project management is crucial for ensuring that systems development projects are delivered on time, within budget, and meet customer expectations. \n* **Project Manager Roles and Responsibilities:** A project manager oversees the entire project lifecycle, from initiation and planning to execution and closure. Key skills include leadership, communication, problem-solving, and technical expertise.\n* **Project Management Activities:** Core activities include defining project scope, creating a work breakdown structure, estimating resources, developing schedules and budgets, managing risks, and communicating project status.\n* **Project Management Phases:**\n    * **Initiation:** Assessing project size, scope, and complexity, establishing the project team and procedures. \n    * **Planning:** Defining project activities, estimating resources and timeframes, creating a baseline project plan.\n    * **Execution:** Implementing the project plan, monitoring progress, managing changes, and communicating with stakeholders.\n    * **Closure:** Finalizing deliverables, conducting post-project reviews, and closing out contracts. \n* **Project Planning Tools:** \n    * **Gantt Charts:** Visual representation of project tasks and their durations using horizontal bars. \n    * **Network Diagrams:** Illustrate task dependencies and sequences using nodes and arrows.\n    * **PERT (Program Evaluation and Review Technique):** Estimates task durations based on optimistic, pessimistic, and realistic timeframes.\n    * **Critical Path Method (CPM):** Identifies the sequence of tasks that determines the minimum project duration. \n* **Project Management Software:** Tools like Microsoft Project assist in planning, scheduling, resource allocation, and tracking project progress."]
    },
])


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    convo.send_message(message.text)
    response = (convo.last.text)
    bot.reply_to(message, response)


bot.infinity_polling()
