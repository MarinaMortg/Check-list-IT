import streamlit as st


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="General English Checklist",
    page_icon="💬",
    layout="wide"
)


# --------------------------------------------------
# Styling #
# --------------------------------------------------

st.markdown(
    """
    <style>
        /* Уменьшаем верхние и нижние отступы страницы */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1500px;
        }

        /* Компактный главный заголовок */
        h1 {
            margin-top: 0;
            margin-bottom: 0.4rem;
            font-size: 2rem;
        }

        /* Компактные заголовки параметров */
        h3 {
            margin-top: 0.2rem;
            margin-bottom: 0.1rem;
            font-size: 1.15rem;
        }

        /* Уменьшаем расстояние между вариантами radio */
        div[role="radiogroup"] {
            gap: 0.15rem;
        }

        /* Уменьшаем вертикальные отступы внутри элементов */
        div[data-testid="stRadio"] {
            margin-bottom: 0.35rem;
        }

        div[data-testid="stRadio"] label {
            padding-top: 0;
            padding-bottom: 0;
        }

        /* Компактный разделитель */
        hr {
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("General English Checklist")


# --------------------------------------------------
# ANSWER OPTIONS
# --------------------------------------------------

understanding_options = [
    "Understands simple questions with support",
    "Understands clear, familiar workplace questions",
    "Understands normal workplace communication and follow-ups",
    "Understands detailed and complex workplace communication",
    "Not Demonstrated"
]

functional_communication_options = [
    "Communicates a few basic points",
    "Communicates the main message with some support",
    "Communicates all key points independently",
    "Communicates effectively and adapts to changes",
    "Not Demonstrated"
]

interaction_clarification_options = [
    "Responds to simple questions using basic phrases",
    "Maintains a short exchange and asks for clarification",
    "Asks follow-up questions and resolves misunderstandings",
    "Clarifies ambiguity and develops the exchange effectively",
    "Not Demonstrated"
]

grammar_and_structure_options = [
    "Uses basic sentence patterns with frequent errors",
    "Uses simple structures; the main message is clear",
    "Uses varied structures with reasonable control",
    "Uses complex structures clearly and accurately",
    "Not Demonstrated"
]

vocabulary_options = [
    "Uses a limited range of familiar words",
    "Uses familiar vocabulary for routine tasks",
    "Uses sufficient workplace vocabulary and can paraphrase",
    "Uses broad, precise vocabulary and adapts terminology",
    "Not Demonstrated"
]

pronunciation_and_fluency_options = [
    "Uses familiar phrases with frequent pauses",
    "Produces short, generally understandable speech",
    "Speaks clearly at a workable pace",
    "Speaks fluently and reformulates smoothly",
    "Not Demonstrated"
]


# --------------------------------------------------
# TWO COLUMNS
# --------------------------------------------------

left_column, right_column = st.columns(2, gap="large")


# --------------------------------------------------
# LEFT COLUMN
# --------------------------------------------------

with left_column:

    st.subheader("Understanding")

    understanding_answer = st.radio(
        "Understanding",
        understanding_options,
        index=1,
        key="understanding",
        label_visibility="collapsed"
    )

    st.subheader("Functional Communication")

    functional_communication_answer = st.radio(
        "Functional Communication",
        functional_communication_options,
        index=1,
        key="functional_communication",
        label_visibility="collapsed"
    )

    st.subheader("Interaction and Clarification")

    interaction_clarification_answer = st.radio(
        "Interaction and Clarification",
        interaction_clarification_options,
        index=1,
        key="interaction_clarification",
        label_visibility="collapsed"
    )


# --------------------------------------------------
# RIGHT COLUMN
# --------------------------------------------------

with right_column:

    st.subheader("Grammar and Structure")

    grammar_and_structure_answer = st.radio(
        "Grammar and Structure",
        grammar_and_structure_options,
        index=1,
        key="grammar_and_structure",
        label_visibility="collapsed"
    )

    st.subheader("Vocabulary")

    vocabulary_answer = st.radio(
        "Vocabulary",
        vocabulary_options,
        index=1,
        key="vocabulary",
        label_visibility="collapsed"
    )

    st.subheader("Pronunciation and Fluency")

    pronunciation_and_fluency_answer = st.radio(
        "Pronunciation and Fluency",
        pronunciation_and_fluency_options,
        index=1,
        key="pronunciation_and_fluency",
        label_visibility="collapsed"
    )


# --------------------------------------------------
# SCORE DICTIONARIES
# --------------------------------------------------

understanding_scores = {
    "Understands simple questions with support": 1,
    "Understands clear, familiar workplace questions": 2,
    "Understands normal workplace communication and follow-ups": 3,
    "Understands detailed and complex workplace communication": 4,
    "Not Demonstrated": 0
}

functional_communication_scores = {
    "Communicates a few basic points": 1,
    "Communicates the main message with some support": 2,
    "Communicates all key points independently": 3,
    "Communicates effectively and adapts to changes": 4,
    "Not Demonstrated": 0
}

interaction_clarification_scores = {
    "Responds to simple questions using basic phrases": 1,
    "Maintains a short exchange and asks for clarification": 2,
    "Asks follow-up questions and resolves misunderstandings": 3,
    "Clarifies ambiguity and develops the exchange effectively": 4,
    "Not Demonstrated": 0
}

grammar_and_structure_scores = {
    "Uses basic sentence patterns with frequent errors": 1,
    "Uses simple structures; the main message is clear": 2,
    "Uses varied structures with reasonable control": 3,
    "Uses complex structures clearly and accurately": 4,
    "Not Demonstrated": 0
}

vocabulary_scores = {
    "Uses a limited range of familiar words": 1,
    "Uses familiar vocabulary for routine tasks": 2,
    "Uses sufficient workplace vocabulary and can paraphrase": 3,
    "Uses broad, precise vocabulary and adapts terminology": 4,
    "Not Demonstrated": 0
}

pronunciation_and_fluency_scores = {
    "Uses familiar phrases with frequent pauses": 1,
    "Produces short, generally understandable speech": 2,
    "Speaks clearly at a workable pace": 3,
    "Speaks fluently and reformulates smoothly": 4,
    "Not Demonstrated": 0
}


# --------------------------------------------------
# TOTAL SCORE
# --------------------------------------------------

total_score = (
    understanding_scores[understanding_answer]
    + functional_communication_scores[functional_communication_answer]
    + interaction_clarification_scores[interaction_clarification_answer]
    + grammar_and_structure_scores[grammar_and_structure_answer]
    + vocabulary_scores[vocabulary_answer]
    + pronunciation_and_fluency_scores[pronunciation_and_fluency_answer]
)


# --------------------------------------------------
# LEVEL CALCULATION
# --------------------------------------------------

if total_score <= 6:
    level = "Not Demonstrated"
elif total_score <= 10:
    level = "Level 1 — Basic"
elif total_score <= 15:
    level = "Level 2 — Supported"
elif total_score <= 20:
    level = "Level 3 — Working"
else:
    level = "Level 4 — Independent"
##

st.divider()

result_column_1, result_column_2 = st.columns([1, 3])

with result_column_1:
    st.metric(
        label="Total",
        value=f"{total_score}/24"
    )

with result_column_2:
    st.metric(
        label="Result",
        value=level
    )

