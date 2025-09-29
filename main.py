import streamlit as st

# -------------------------------
# Quiz Questions and Answers
# -------------------------------
questions = [
    # Part 1
    {
        "q": "Which of the following is NOT a key strength of Tableau?",
        "options": [
            "Speed in analyzing millions of rows",
            "Ease of use without programming skills",
            "Ability to create static, non-interactive dashboards",
            "Direct connection to databases and data warehouses",
        ],
        "answer": 2,
    },
    {
        "q": "In the Tableau Workspace, where would you drag fields to define how data should be shown in a view?",
        "options": [
            "Marks card",
            "Columns and Rows shelves",
            "Filters shelf",
            "Status bar",
        ],
        "answer": 1,
    },
    {
        "q": "Which of the following best describes a Dimension in Tableau?",
        "options": [
            "Fields that contain numbers and can be aggregated",
            "Subsets of data you define",
            "Fields that contain qualitative or categorical information such as text or dates",
            "Dynamic variables that can replace constant values",
        ],
        "answer": 2,
    },
    {
        "q": "When connecting to data, what is the main difference between a Live connection and an Extract?",
        "options": [
            "Live connection supports offline use, Extract does not",
            "Extracts are snapshots optimized for performance, while Live queries data in real-time",
            "Live connection is always faster than Extract",
            "Extract requires database connectivity at all times",
        ],
        "answer": 1,
    },
    {
        "q": "Which of the following is TRUE about Tableau Data Extracts (TDE/Hyper)?",
        "options": [
            "They are row-based databases optimized for transactional queries",
            "They allow offline analysis because the data is embedded in the workbook",
            "They always run slower than live connections",
            "They cannot be saved or shared with other users",
        ],
        "answer": 1,
    },
    {
        "q": "A filter based on Category or Region would be an example of what type of filter?",
        "options": [
            "Measure filter",
            "Dimension filter",
            "Context filter",
            "Extract filter",
        ],
        "answer": 1,
    },
    {
        "q": "In Tableau, what is the quickest way to sort a bar chart in descending order by sales?",
        "options": [
            "Right-click the dimension field and select 'Manual sort'",
            "Use the sort icon that appears when hovering over an axis or header",
            "Rearrange items manually in the legend",
            "Apply a filter and re-order the results",
        ],
        "answer": 1,
    },
    {
        "q": "What is the main purpose of creating a Group in Tableau?",
        "options": [
            "To apply filters across multiple worksheets",
            "To combine related members into a single category for easier analysis",
            "To change a discrete field into a continuous field",
            "To improve extract performance",
        ],
        "answer": 1,
    },
    {
        "q": "In Tableau, when you see a blue field in your view, it indicates:",
        "options": [
            "A discrete field (e.g., date part like Month or categorical data)",
            "A continuous field (e.g., timeline axis)",
            "A calculated field",
            "A measure used on Color",
        ],
        "answer": 0,
    },
    {
        "q": "Which statement correctly differentiates date parts from date values in Tableau?",
        "options": [
            "Date parts create a timeline axis; date values aggregate all periods together",
            "Date parts aggregate by units like Month or Year, while date values show data along a continuous timeline",
            "Both date parts and date values always appear in green",
            "Date values can only be used in filters, not in visualizations",
        ],
        "answer": 1,
    },
    #     # Part 2
    #     {"q": "To create a scatter plot in Tableau, you need at least:", "options": ["One measure on Columns and one dimension on Rows", "One measure on Columns and one measure on Rows", "Two dimensions on Columns and Rows", "A geographic field on Rows and a measure on Columns"], "answer": 1},
    #     {"q": "In Tableau, which shelf or card would you use to break down a scatter plot by Category using color?", "options": ["Columns shelf", "Filters shelf", "Marks card → Color", "Rows shelf"], "answer": 2},
    #     {"q": "A tabular view (cross-tab) in Tableau is created when:", "options": ["A map view is converted into a polygon map", "A measure is dropped on Size", "At least one dimension is placed on Columns and another on Rows", "Two measures are placed on Columns and Rows"], "answer": 2},
    #     {"q": "What is the primary use of a Dual Axis Chart in Tableau?", "options": ["To visualize categorical data with text tables", "To compare two measures that may have different scales", "To filter multiple views at once", "To calculate ratios across fields"], "answer": 1},
    #     {"q": "After creating a dual axis chart with Sales and Profit, what must you do to align the scales?", "options": ["Swap the axes", "Synchronize the axes", "Convert one field to a dimension", "Change both measures to percentages"], "answer": 1},
    #     {"q": "In Tableau, a globe icon next to a field indicates:", "options": ["A calculated field", "A discrete field", "A geographic field", "A parameter"], "answer": 2},
    #     {"q": "Which calculation would correctly compute the overall profit ratio in Tableau?", "options": ["[Profit] / [Sales]", "SUM([Profit]) / SUM([Sales])", "SUM([Profit] / [Sales])", "AVG([Profit]) / [Sales]"], "answer": 1},
    #     {"q": "In Tableau, the plus sign (+) between two string fields does what?", "options": ["Adds the ASCII values of the characters", "Concatenates the strings together", "Converts them to numbers", "Returns an error unless converted with STR()"], "answer": 1},
    #     {"q": "Which of the following is NOT a Quick Table Calculation in Tableau?", "options": ["Running Total", "Percent of Total", "Moving Average", "Correlation Coefficient"], "answer": 3},
    #     {"q": "Which of the following dashboard objects allows navigation to another sheet or dashboard?", "options": ["Image", "Navigation", "Extension", "Blank"], "answer": 1},
]

# -------------------------------
# Streamlit App
# -------------------------------
st.title("📊 Tableau Training Quiz")
st.write("Test your knowledge with this multiple-choice quiz.")

user_answers = []

for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}. {q['q']}")
    user_choice = st.radio("Select your answer:", q["options"], key=f"q{i}")
    user_answers.append(q["options"].index(user_choice))

if st.button("Submit Quiz"):
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
    st.success(f"✅ You scored {score} out of {len(questions)}")

    st.write("---")
    st.write("### 📋 Correct Answers:")
    for i, q in enumerate(questions):
        correct = q["options"][q["answer"]]
        st.write(f"Q{i+1}: {correct}")
