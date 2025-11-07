

# Career Guidance Expert System for College Students
# -----------------------------------------------

def ask_question(question, options):
    print(f"\n{question}")
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    while True:
        try:
            choice = int(input("Enter your choice (1-" + str(len(options)) + "): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice, please select again.")
        except ValueError:
            print("Please enter a valid number.")

def career_expert_system():
    print("=============================================")
    print("   🎓 Career Guidance Expert System 🎯")
    print("=============================================\n")
    print("Answer the following questions honestly to get personalized career guidance.\n")

    # Step 1: Gather user information
    interest = ask_question(
        "What field are you most interested in?",
        ["Technology", "Business", "Art & Design", "Science & Research", "Teaching", "Social Work"]
    )

    skill = ask_question(
        "Which skill describes you best?",
        ["Logical Thinking", "Creativity", "Communication", "Analytical Thinking", "Empathy", "Leadership"]
    )

    personality = ask_question(
        "How would you describe your personality?",
        ["Introvert", "Extrovert", "Ambivert"]
    )

    environment = ask_question(
        "What kind of work environment do you prefer?",
        ["Office-based", "Outdoor", "Remote/Flexible", "Lab/Research", "Creative Studio"]
    )

    # Step 2: Apply rule-based reasoning (Inference Engine)
    print("\n---------------------------------------------")
    print("Analyzing your answers and matching with careers...")
    print("---------------------------------------------\n")

    # Step 3: Knowledge Base (Rules)
    if interest == "Technology":
        if skill in ["Logical Thinking", "Analytical Thinking"]:
            print("💡 Recommended Career: Software Engineer or Data Analyst")
            print("   ➤ You enjoy logical problem-solving and working with systems.")
        elif skill == "Creativity":
            print("💡 Recommended Career: UI/UX Designer or Game Developer")
            print("   ➤ You blend creativity with technology beautifully!")

    elif interest == "Business":
        if skill == "Communication" or personality == "Extrovert":
            print("💡 Recommended Career: Marketing Manager or HR Specialist")
            print("   ➤ Your communication and leadership skills make you thrive in business environments.")
        elif skill == "Analytical Thinking":
            print("💡 Recommended Career: Business Analyst or Financial Advisor")
            print("   ➤ You have an eye for patterns, data, and smart decision-making.")

    elif interest == "Art & Design":
        if skill == "Creativity":
            print("💡 Recommended Career: Graphic Designer, Animator, or Fashion Designer")
            print("   ➤ You love to express ideas visually and think outside the box.")
        elif skill == "Communication":
            print("💡 Recommended Career: Content Creator or Art Director")
            print("   ➤ You can inspire and guide others through design and storytelling.")

    elif interest == "Science & Research":
        if skill == "Analytical Thinking":
            print("💡 Recommended Career: Scientist, Researcher, or Biotechnologist")
            print("   ➤ You enjoy investigation, experimentation, and discovery.")
        elif skill == "Logical Thinking":
            print("💡 Recommended Career: Data Scientist or AI Researcher")
            print("   ➤ You’re curious about solving complex real-world problems.")

    elif interest == "Teaching":
        if skill == "Communication" and personality in ["Extrovert", "Ambivert"]:
            print("💡 Recommended Career: Teacher or Professor")
            print("   ➤ You’re great at sharing knowledge and inspiring others.")
        elif skill == "Empathy":
            print("💡 Recommended Career: School Counselor or Mentor")
            print("   ➤ You guide and support others with understanding and care.")

    elif interest == "Social Work":
        if skill == "Empathy":
            print("💡 Recommended Career: Social Worker or NGO Coordinator")
            print("   ➤ You care deeply about helping others and making a difference.")
        elif skill == "Leadership":
            print("💡 Recommended Career: Community Project Leader")
            print("   ➤ You have the drive to lead social initiatives and empower people.")

    else:
        print("⚠ Sorry, we couldn’t find a perfect match. Try exploring interdisciplinary fields!")

    # Step 4: Closing message
    print("\n---------------------------------------------")
    print("✨ Thank you for using the Career Guidance Expert System!")
    print("   Remember: The best career combines your interests, skills, and values.")
    print("---------------------------------------------")

# Run the expert system
career_expert_system()
