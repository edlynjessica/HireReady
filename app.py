import streamlit as st
import bcrypt
import pickle
import pandas as pd
model = pickle.load(
    open("model.pkl", "rb")
)
from database import add_user, get_user

st.set_page_config(
    page_title="HireReady",
    page_icon="🚀",
    layout="wide"
)

# Session State

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "name" not in st.session_state:
    st.session_state.name = ""

st.title("HireReady")

# NOT LOGGED IN (show signup and login forms)

if not st.session_state.logged_in:

    st.header("Sign Up")

    with st.form("signup_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        signup = st.form_submit_button("Sign Up")


    if signup:

        if (name == "" or email == "" or password == "" or confirm_password == ""):
            st.error("Please fill all the fields!")

        elif password != confirm_password:
            st.error("Passwords do not match!")

        else:
            hashed = bcrypt.hashpw(
                password.encode(),
                bcrypt.gensalt()
            ).decode()

            success = add_user(name,email,hashed)

            if success:
                st.success("User added successfully!")
            else:
                st.error("Email already exists!")

    st.divider()

    st.header("Login")

    login_email = st.text_input("Login Email")
    login_password = st.text_input("Login Password",type="password")

    login = st.button("Login")


    if login:

        user = get_user(login_email)
        if user:

            if bcrypt.checkpw(
                login_password.encode(),
                user[3].encode()
            ):

                st.session_state.logged_in = True
                st.session_state.name = user[1]
                st.rerun()
            else:
                st.error("Wrong password!")

        else:
            st.error("User not found!")



# LOGGED IN



else:
    st.success(f"Welcome {st.session_state.name}! 🚀")

    st.markdown("## 🎯 HireReady Dashboard")
    st.caption("ML-powered student placement readiness analysis")

    st.divider()

    with st.form("assessment_form"):

        st.subheader("📌 Academic Profile")

        cgpa = st.number_input("CGPA", 0.0, 10.0, 0.01)

        st.subheader("💻 DSA Profile")

        col1, col2, col3 = st.columns(3)

        with col1:
            lc_easy = st.number_input("Easy", min_value=0)

        with col2:
            lc_medium = st.number_input("Medium", min_value=0)

        with col3:
            lc_hard = st.number_input("Hard", min_value=0)

        contest_rating = st.number_input("Contest Rating", min_value=0)

        st.subheader("🏗️ Experience")

        col4, col5 = st.columns(2)
        with col4:
            projects = st.number_input("Projects", min_value=0)

        with col5:
            internships = st.number_input("Internships", min_value=0)

        st.subheader("🧠 Soft Skills")

        communication = st.slider("Communication Skills", 1, 10)

        submit_assessment = st.form_submit_button("🚀 Analyze Profile")
        input_data = pd.DataFrame([{
            "cgpa": cgpa,
            "lc_easy": lc_easy,
            "lc_medium": lc_medium,
            "lc_hard": lc_hard,
            "contest_rating": contest_rating,
            "projects": projects,
            "internships": internships,
            "communication": communication
        }])


    if submit_assessment:

        st.subheader("Assessment Summary")

        st.write("CGPA:", cgpa)

        st.write("LeetCode Easy:", lc_easy)
        st.write("LeetCode Medium:", lc_medium)
        st.write("LeetCode Hard:", lc_hard)
        st.write("Contest Rating:", contest_rating)
        st.write("Projects:", projects)
        st.write("Internships:", internships)
        st.write("Communication:", communication)

        prediction = model.predict(input_data)
        score = round(prediction[0],2)

        dsa_score = (lc_easy + lc_medium*2 + lc_hard*3)

        if dsa_score > 300:
            dsa_level = "Strong"
        elif dsa_score > 150:
            dsa_level = "Good"
        else:
            dsa_level = "Weak"


        if projects >= 4:
            project_level = "Strong"
        elif projects >= 2:
            project_level = "Good"
        else:
            project_level = "Weak"
        

        if internships >= 2:
            internship_level = "Strong"
        elif internships == 1:
            internship_level = "Good"
        else:
            internship_level = "Weak"


        if communication >= 8:
            comm_level = "Strong"
        elif communication >= 5:
            comm_level = "Good"
        else:
            comm_level = "Weak"
        


        st.markdown("---")

        st.markdown("## 🎯 HireReady Score")

        st.progress(score / 100)

        st.metric("Score", f"{score}/100")

        if score >= 80:
            st.success("Excellent Profile! 🚀")

        elif score >= 65:
            st.success("Strong Profile! 💪")

        elif score >= 50:
            st.info("Good Profile! 👍")

        elif score >= 35:
            st.warning("Developing Profile! 🌱")

        else:
            st.error("Needs Improvement! 📚")




        strengths = []
        if project_level == "Strong":
            strengths.append("Strong project experience")

        if internship_level == "Strong":
            strengths.append("Good internship exposure")

        if dsa_level == "Strong":
            strengths.append("Strong DSA profile")
        


        weaknesses = []
        if dsa_level == "Weak":
            weaknesses.append("Improve DSA consistency")

        if project_level == "Weak":
            weaknesses.append("Build more real-world projects")

        if internship_level == "Weak":
            weaknesses.append("Gain internship experience")





        st.markdown("## ⚡Profile Insights")
        st.divider()

        st.markdown("###  DSA Profile")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 🟢 Easy")
            st.metric(label="Solved", value=lc_easy)

        with col2:
            st.markdown("### 🟡 Medium")
            st.metric(label="Solved", value=lc_medium)

        with col3:
            st.markdown("### 🔴 Hard")
            st.metric(label="Solved", value=lc_hard)


            
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💪 Strengths")
            if strengths:
                for s in strengths:
                    st.success("✅ " + s)
            else:
                st.info("No strong areas yet")

        with col2:
            st.markdown("### 📌 Improvement Areas")
            if weaknesses:
                for w in weaknesses:
                    st.warning("⚠️ " + w)
            else:
                st.success("No major issues 🎉")
            



        st.markdown("## 🚀 Action Plan")

        if dsa_level != "Strong":
            st.info("👉 Solve 2–3 LeetCode problems daily")

        if project_level != "Strong":
            st.info("👉 Build 1 strong full-stack project (deploy it)")

        if internship_level != "Strong":
            st.info("👉 Apply to startups + LinkedIn internships")

        if communication != "Strong":
            st.info("👉 Practice mock interviews weekly")




        

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.name = ""
        st.rerun()