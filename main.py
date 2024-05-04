import streamlit as st

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state.responses = {}

def overall_mood():
    st.title("Overall Mood")
    st.subheader("How are you feeling today, on a scale from 1 to 5?")
    mood_rating = st.slider("Rate your mood", 1, 5)
    st.subheader("Can you briefly describe your mood in a few words?")
    mood_description = st.text_area("Describe your mood")
    return mood_rating, mood_description

def stress_levels():
    st.title("Stress Levels")
    st.subheader("How stressed do you feel right now, on a scale from 1 to 5?")
    stress_rating = st.slider("Rate your stress", 1, 5)
    st.subheader("Are there any specific stressors you're dealing with currently?")
    stressors = st.text_area("Describe your stressors")
    return stress_rating, stressors

def emotional_state():
    st.title("Emotional State")
    st.subheader("Have you been experiencing any strong emotions lately?")
    emotions = st.text_area("Describe your emotions")
    st.subheader("Is there anything in particular that's been affecting your emotions recently?")
    emotional_factors = st.text_area("Describe emotional factors")
    return emotions, emotional_factors

def sleep_quality():
    st.title("Sleep Quality")
    st.subheader("How would you rate your sleep quality recently, from poor to excellent?")
    sleep_quality_rating = st.selectbox("Select sleep quality", ["Poor", "Fair", "Good", "Very Good", "Excellent"])
    st.subheader("Have you noticed any changes in your sleep patterns?")
    sleep_changes = st.text_area("Describe sleep changes")
    return sleep_quality_rating, sleep_changes

def social_support():
    st.title("Social Support")
    st.subheader("Do you feel supported by friends or family?")
    support_feeling = st.radio("Select your feeling of support", ["Yes", "No", "Somewhat"])
    st.subheader("How connected do you feel to others in your life?")
    connection_level = st.slider("Rate your connection level", 1, 5)
    return support_feeling, connection_level

def coping_mechanisms():
    st.title("Coping Mechanisms")
    st.subheader("What do you usually do to cope with stress or difficult emotions?")
    coping_strategies = st.text_area("Describe your coping strategies")
    st.subheader("Have these coping strategies been effective for you lately?")
    effectiveness = st.radio("Select effectiveness", ["Yes", "No", "Somewhat"])
    return coping_strategies, effectiveness

def physical_wellbeing():
    st.title("Physical Well-being")
    st.subheader("How would you describe your energy levels lately?")
    energy_levels = st.radio("Select energy levels", ["Low", "Medium", "High"])
    st.subheader("Have you been taking care of your physical health?")
    health_care = st.radio("Select your physical health care", ["Yes", "No", "Somewhat"])
    return energy_levels, health_care

def thought_patterns():
    st.title("Thought Patterns")
    st.subheader("Do you find yourself having negative thoughts often?")
    negative_thoughts = st.radio("Select your thoughts", ["Yes", "No", "Sometimes"])
    st.subheader("How would you describe your ability to focus and concentrate?")
    concentration_ability = st.radio("Select your concentration ability", ["Poor", "Fair", "Good", "Excellent"])
    return negative_thoughts, concentration_ability

def support_system():
    st.title("Support System")
    st.subheader("Is there someone you feel comfortable talking to about your feelings?")
    support_person = st.radio("Select support person", ["Yes", "No"])
    st.subheader("Would you consider seeking professional help if needed?")
    professional_help = st.radio("Select professional help", ["Yes", "No", "Maybe"])
    return support_person, professional_help

def future_outlook():
    st.title("Future Outlook")
    st.subheader("Are you optimistic about the future?")
    optimism = st.radio("Select your optimism", ["Yes", "No", "Somewhat"])
    st.subheader("Do you have any goals or plans that you're excited about?")
    goals_plans = st.text_area("Describe your goals or plans")
    return optimism, goals_plans

def main():
    st.header("Well-being Assessment")

    # Display step based on current step
    if st.session_state.step == 1:
        mood_rating, mood_description = overall_mood()
        if mood_rating and mood_description:
            st.session_state.responses['Overall Mood'] = {'Rating': mood_rating, 'Description': mood_description}
            st.session_state.step += 1
    elif st.session_state.step == 2:
        stress_rating, stressors = stress_levels()
        if stress_rating and stressors:
            st.session_state.responses['Stress Levels'] = {'Rating': stress_rating, 'Stressors': stressors}
            st.session_state.step += 1
    elif st.session_state.step == 3:
        emotions, emotional_factors = emotional_state()
        if emotions and emotional_factors:
            st.session_state.responses['Emotional State'] = {'Emotions': emotions, 'Factors': emotional_factors}
            st.session_state.step += 1
    elif st.session_state.step == 4:
        sleep_quality_rating, sleep_changes = sleep_quality()
        if sleep_quality_rating and sleep_changes:
            st.session_state.responses['Sleep Quality'] = {'Rating': sleep_quality_rating, 'Changes': sleep_changes}
            st.session_state.step += 1
    elif st.session_state.step == 5:
        support_feeling, connection_level = social_support()
        if support_feeling and connection_level:
            st.session_state.responses['Social Support'] = {'Feeling Supported': support_feeling, 'Connection Level': connection_level}
            st.session_state.step += 1
    elif st.session_state.step == 6:
        coping_strategies, effectiveness = coping_mechanisms()
        if coping_strategies and effectiveness:
            st.session_state.responses['Coping Mechanisms'] = {'Strategies': coping_strategies, 'Effectiveness': effectiveness}
            st.session_state.step += 1
    elif st.session_state.step == 7:
        energy_levels, health_care = physical_wellbeing()
        if energy_levels and health_care:
            st.session_state.responses['Physical Well-being'] = {'Energy Levels': energy_levels, 'Health Care': health_care}
            st.session_state.step += 1
    elif st.session_state.step == 8:
        negative_thoughts, concentration_ability = thought_patterns()
        if negative_thoughts and concentration_ability:
            st.session_state.responses['Thought Patterns'] = {'Negative Thoughts': negative_thoughts, 'Concentration Ability': concentration_ability}
            st.session_state.step += 1
    elif st.session_state.step == 9:
        support_person, professional_help = support_system()
        if support_person and professional_help:
            st.session_state.responses['Support System'] = {'Support Person': support_person, 'Professional Help': professional_help}
            st.session_state.step += 1
    elif st.session_state.step == 10:
        optimism, goals_plans = future_outlook()
        if optimism and goals_plans:
            st.session_state.responses['Future Outlook'] = {'Optimism': optimism, 'Goals/Plans': goals_plans}
            st.session_state.step += 1

    # Submit the form when all steps are completed
    if st.session_state.step == 11:
        st.subheader("Summary of Responses:")
        for question, response in st.session_state.responses.items():
            st.write(question)
            for key, value in response.items():
                st.write(f"- {key}: {value}")

if __name__ == "__main__":
    main()
