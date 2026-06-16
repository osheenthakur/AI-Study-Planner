import streamlit as st

st.title("📚 AI Study Planner")

st.write(
    "Generate a smart study plan based on subject difficulty and available study hours."
)

subject1 = st.text_input("Enter Subject 1")

difficulty1 = st.selectbox(
    "Difficulty for Subject 1",
    ["Easy", "Medium", "Hard"]
)

subject2 = st.text_input("Enter Subject 2")

difficulty2 = st.selectbox(
    "Difficulty for Subject 2",
    ["Easy", "Medium", "Hard"],
    key="subject2"
)

subject3 = st.text_input("Enter Subject 3")

difficulty3 = st.selectbox(
    "Difficulty for Subject 3",
    ["Easy", "Medium", "Hard"],
    key="subject3"
)

hours = st.number_input(
    "Available Study Hours",
    min_value=1,
    max_value=12,
    value=6
)

exam_date = st.date_input(
    "Select Exam Date"
)

if st.button("Generate Study Plan"):

    score = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    total_score = (
        score[difficulty1]
        + score[difficulty2]
        + score[difficulty3]
    )

    hours1 = hours * score[difficulty1] / total_score
    hours2 = hours * score[difficulty2] / total_score
    hours3 = hours * score[difficulty3] / total_score

    st.subheader("📅 Today's Study Plan")

    st.write(f"Exam Date: {exam_date}")

    st.write(f"📖 {subject1}: {hours1:.1f} hours")
    st.write(f"📖 {subject2}: {hours2:.1f} hours")
    st.write(f"📖 {subject3}: {hours3:.1f} hours")

    st.subheader("🤖 Smart Study Advice")

    if difficulty1 == "Hard":
        st.write(f"🔥 Give extra attention to {subject1}")

    if difficulty2 == "Hard":
        st.write(f"🔥 Give extra attention to {subject2}")

    if difficulty3 == "Hard":
        st.write(f"🔥 Give extra attention to {subject3}")

    st.write("📚 Revise every day before sleeping.")
    st.write("⏰ Follow the Pomodoro Technique (25 min study + 5 min break).")
    st.write("📝 Practice questions daily.")
    st.write("🎯 Keep the last few days before exams for revision.")

    


