from pyscript import document
import random

teams = [
    ("Yellow Tigers", "yellow", "🐯"),
    ("Blue Bears",    "blue",   "🐻"),
    ("Red Bulldogs",  "red",    "🐕"),
    ("Green Hornets", "green",  "🐝"),
]

def on_signup(event):
    # Get registration answer
    reg_yes = document.querySelector("#reg-yes")
    reg_no  = document.querySelector("#reg-no")

    # Get medical answer
    med_yes = document.querySelector("#med-yes")
    med_no  = document.querySelector("#med-no")

    # Get grade and section
    grade_input = document.querySelector("#grade-section").value.strip()

    # Get result box
    result_box = document.querySelector("#result-box")

    # Check if answers were selected
    reg_answered = reg_yes.checked or reg_no.checked
    med_answered = med_yes.checked or med_no.checked

    # Validate
    errors = []

    if not reg_answered:
        errors.append("Please answer Question 1 (Online Registration).")
    elif reg_no.checked:
        errors.append("You must complete your online registration first.")

    if not med_answered:
        errors.append("Please answer Question 2 (Medical Clearance).")
    elif med_no.checked:
        errors.append("You must get your medical clearance from the clinic first.")

    if not grade_input:
        errors.append("Please enter your Grade and Section.")

    if errors:
        result_box.className = "error"
        result_box.style.display = "block"
        error_html = "<br>".join(f'<p class="error-msg">⚠️ {e}</p>' for e in errors)
        result_box.innerHTML = error_html
        return

    # All good — pick a random team
    team_name, team_color, team_emoji = random.choice(teams)

    result_box.className = "success"
    result_box.style.display = "block"
    result_box.innerHTML = f"""
        <div class="congrats">🎉 Congratulations!</div>
        <div class="team-message">You have been assigned to...</div>
        <div class="team-name {team_color}">{team_emoji} {team_name}</div>
        <div class="team-message" style="margin-top:10px;">
            Grade &amp; Section: <strong style="color:white;">{grade_input}</strong>
        </div>
    """

# Attach the button click event
btn = document.querySelector("#signup-btn")
btn.addEventListener("click", on_signup)