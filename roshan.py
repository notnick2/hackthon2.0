import streamlit as st


from openai import OpenAI

client = OpenAI(api_key = "sk-proj-ijhKEtNHYmVrNPslMemwT3BlbkFJwkaOMTa62mK5kyZW9qbA")

if 'step' not in st.session_state:
    st.session_state.step = 0

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if "appointment" not in st.session_state:
    st.session_state.appointment = ""


def sendToGpt(questionResponse):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "based on the user response give a small comment not more than two lines. then say lets continue with next questions to finish assessment. you are not supposed to ask any questions just give a comment ending with lets continue with next questions to finish assessment. complete response should'nt be more than two lines"
        },
        {
        "role": "user",
        "content": questionResponse
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message.content


def chat(summary_string):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a mental heatlth professional assistant. chat with the user. Assistant: "
            },
            {
                "role": "user",
                "content": summary_string
            }
        ],
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

def assistance():
    if st.session_state.appointment == "No":
        st.write("Thank you for your Co-operation!!")
    else:
        st.title("AI assistant:")
        user_input = st.text_input("You:", "")
        if st.button("Send"):
            if user_input:
                gpt_response = chat(user_input)
                st.write("AI assist:", gpt_response)

def report(summary_string):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
      "role": "system",
      "content": "given is a responses of an mental health assessment give a quick and easily readable report for the assessment.Also give personalized recomendations. personalized recomendation should be title after the report.stramlit's st.write. be descriptive"
        },
        {
        "role": "user",
        "content": summary_string
        }
    ],
    temperature=1,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message.content


        
def summary():
        st.subheader("Mental health status Assessment report")
        summary_string=""
        for question, response in st.session_state.responses.items():
            summary_string += f"{question}\n"
            #st.write(question)
            for key, value in response.items():
                summary_string += f"- {key}: {value}\n"
                #st.write(f"- {key}: {value}")
        st.write(report(summary_string))
        assistance_option = st.radio("Would you like to receive professional assistance?", ["Yes", "No"], index=None)
        st.session_state.appointment = assistance_option

def overall_mood():
    st.title("Overall Mood")
    st.subheader("How are you feeling today, on a scale from 1 to 5?")
    mood_rating = st.slider("Rate your mood", 1, 5)
    st.subheader("Can you briefly describe your mood in a few words?")
    mood_description = st.text_area("Describe your mood")
    if mood_rating and mood_description:
        gptComment = sendToGpt("question: How are you feeling today, on a scale from 1 to 5? answer: "+ str(mood_rating) + "question: Can you briefly describe your mood in a few words?  answer: "+ mood_description)
        st.write(gptComment)
        st.session_state.responses['Overall Mood'] = {'Rating': mood_rating, 'Description': mood_description}
    return mood_rating, mood_description

def stress_levels():
    st.title("Stress Levels")
    st.subheader("How stressed do you feel right now, on a scale from 1 to 5?")
    stress_rating = st.slider("Rate your stress", 1, 5)
    st.subheader("Are there any specific stressors you're dealing with currently?")
    stressors = st.text_area("Describe your stressors")
    if stress_rating and stressors:
        gptComment = sendToGpt("question: How stressed do you feel right now, on a scale from 1 to 5 answer: "+ str(stress_rating) + "question:Are there any specific stressors you're dealing with currently? answer: "+ stressors)
        st.write(gptComment)
        st.session_state.responses['Stress Levels'] = {'Rating': stress_rating, 'Stressors': stressors}
    return stress_rating, stressors

def emotional_state():
    st.title("Emotional State")
    st.subheader("Have you been experiencing any strong emotions lately?")
    emotions = st.text_area("Describe your emotions")
    st.subheader("Is there anything in particular that's been affecting your emotions recently?")
    emotional_factors = st.text_area("Describe emotional factors")
    # Replace sendToGpt with your actual function call
    if emotions and emotional_factors:
        gptComment = sendToGpt("question: Have you been experiencing any strong emotions lately? answer: "+emotions + "question: Is there anything in particular that's been affecting your emotions recently?  answer: "+ emotional_factors)
        st.write(gptComment)
        st.session_state.responses['Emotional State'] = {'Emotions': emotions, 'Factors': emotional_factors}
        return emotions, emotional_factors

def sleep_quality():
    st.title("Sleep Quality")
    st.subheader("How would you rate your sleep quality recently, from poor to excellent?")
    sleep_quality_rating = st.selectbox("Select sleep quality", ["Poor", "Fair", "Good", "Very Good", "Excellent"], index=None)
    st.subheader("Have you noticed any changes in your sleep patterns?")
    sleep_changes = st.text_area("Describe sleep changes", value="")
    # Replace sendToGpt with your actual function call
    if sleep_quality_rating is not None and sleep_changes:
        gptComment = sendToGpt("question: How would you rate your sleep quality recently, from poor to excellent? answer: "+sleep_quality_rating + "question: Have you noticed any changes in your sleep patterns? answer: "+ sleep_changes)
        st.write(gptComment)
        st.session_state.responses['Sleep Quality'] = {'Rating': sleep_quality_rating, 'Changes': sleep_changes}
        return sleep_quality_rating, sleep_changes
def social_support():
    st.title("Social Support")
    st.subheader("Do you feel supported by friends or family?")
    support_feeling = st.radio("Select your feeling of support", ["Yes", "No", "Somewhat"], index=None)
    st.subheader("How connected do you feel to others in your life?")
    connection_level = st.slider("Rate your connection level", 1, 5, value=None)
    # Replace sendToGpt with your actual function call
    if support_feeling is not None and connection_level is not None:
        gptComment = sendToGpt("question:Do you feel supported by friends or family? answer: "+support_feeling + "question: How connected do you feel to others in your life? answer: "+ str(connection_level))
        st.write(gptComment)
        st.session_state.responses['Social Support'] = {'Feeling Supported': support_feeling, 'Connection Level': connection_level}
        return support_feeling, connection_level

def coping_mechanisms():
    st.title("Coping Mechanisms")
    st.subheader("What do you usually do to cope with stress or difficult emotions?")
    coping_strategies = st.text_area("Describe your coping strategies")
    st.subheader("Have these coping strategies been effective for you lately?")
    effectiveness = st.radio("Select effectiveness", ["Yes", "No", "Somewhat"])
    # Replace sendToGpt with your actual function call
    if coping_strategies and effectiveness:
        gptComment = sendToGpt("question: What do you usually do to cope with stress or difficult emotions? answer: "+coping_strategies + "question: Have these coping strategies been effective for you lately? answer: "+ effectiveness)
        st.write(gptComment)
        st.session_state.responses['Coping Mechanisms'] = {'Strategies': coping_strategies, 'Effectiveness': effectiveness}
        return coping_strategies, effectiveness

def physical_wellbeing():
    st.title("Physical Well-being")
    st.subheader("How would you describe your energy levels lately?")
    energy_levels = st.radio("Select energy levels", ["Low", "Medium", "High"], index=None)
    st.subheader("Have you been taking care of your physical health?")
    health_care = st.radio("Select your physical health care", ["Yes", "No", "Somewhat"], index=None)
    # Replace sendToGpt with your actual function call
    if energy_levels is not None and health_care is not None:
        gptComment = sendToGpt("question:How would you describe your energy levels lately? answer: "+energy_levels + "question: Have you been taking care of your physical health? answer: "+ health_care)
        st.write(gptComment)
        st.session_state.responses['Physical Well-being'] = {'Energy Levels': energy_levels, 'Health Care': health_care}
        return energy_levels, health_care

def thought_patterns():
    st.title("Thought Patterns")
    st.subheader("Do you find yourself having negative thoughts often?")
    negative_thoughts = st.radio("Select your thoughts", ["Yes", "No", "Sometimes"], index=None)
    st.subheader("How would you describe your ability to focus and concentrate?")
    concentration_ability = st.radio("Select your concentration ability", ["Poor", "Fair", "Good", "Excellent"], index=None)
    # Replace sendToGpt with your actual function call
    if negative_thoughts is not None and concentration_ability is not None:
        gptComment = sendToGpt("question: Do you find yourself having negative thoughts often? answer: "+negative_thoughts + "question:How would you describe your ability to focus and concentrate? answer: "+ concentration_ability)
        st.write(gptComment)
        st.session_state.responses['Thought Patterns'] = {'Negative Thoughts': negative_thoughts, 'Concentration Ability': concentration_ability}
    return negative_thoughts, concentration_ability

def support_system():
    st.title("Support System")
    st.subheader("Is there someone you feel comfortable talking to about your feelings?")
    support_person = st.radio("Select support person", ["Yes", "No"], index=None)
    st.subheader("Would you consider seeking professional help if needed?")
    professional_help = st.radio("Select professional help", ["Yes", "No", "Maybe"], index=None)
    # Replace sendToGpt with your actual function call
    if support_person is not None and professional_help is not None:
        gptComment = sendToGpt("question: Is there someone you feel comfortable talking to about your feelings? answer: "+support_person + "question:Would you consider seeking professional help if needed? answer: "+ professional_help)
        st.write(gptComment)
        st.session_state.responses['Support System'] = {'Support Person': support_person, 'Professional Help': professional_help}
        return support_person, professional_help

def future_outlook():
    st.title("Future Outlook")
    st.subheader("Are you optimistic about the future?")
    optimism = st.radio("Select your optimism", ["Yes", "No", "Somewhat"], index=None)
    st.subheader("Enter any goals or plans that you're excited about?")
    goals_plans = st.text_area("Describe your goals or plans", value="")
    # Replace sendToGpt with your actual function call
    if optimism is not None and goals_plans:
        gptComment = sendToGpt("question:Are you optimistic about the future? answer: "+optimism + "question: Do you have any goals or plans that you're excited about? answer: "+ goals_plans)
        st.write(gptComment)
        st.session_state.responses['Future Outlook'] = {'Optimism': optimism, 'Goals/Plans': goals_plans}
    return optimism, goals_plans

def main():
    # Initialize session state variables
    if 'step' not in st.session_state:
        st.session_state.step = 0

    # Define step-wise function calls
    steps = [
        overall_mood,
        stress_levels,
        emotional_state,
        sleep_quality,
        social_support,
        coping_mechanisms,
        physical_wellbeing,
        thought_patterns,
        support_system,
        future_outlook,
        summary,
        assistance
    ]

    # Execute the current step function
    current_step = st.session_state.step
    if current_step < len(steps):
        step_func = steps[current_step]
        step_func()
        if step_func =="appointment" or step_func == "assistance":
            pass
        # Proceed to the next step when the user clicks the "Next" button
        else:
            if st.button("Next"):
                st.session_state.step += 1
                st.experimental_rerun()
if _name_ == "_main_":
    main()