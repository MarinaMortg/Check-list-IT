import streamlit as st
 
st.title("*IT English Level Check*")
 
 
#Answers#
st.subheader("1.Understanding")
understanding_answer = st.radio(
    "", 
    ["Понимает, о чем текст в целом", "Понимает частично/с подсказками", "Не понимает"],
index=1
)
 
st.subheader("2.Details")
details_answer = st.radio(
    "",
    ["Верно отвечает на вопросы по тексту", "Отвечает неточно", "Не может ответить"],
    index=1
)
st.subheader("Confidence")
confidence_answer = st.radio(
    "",
    ["Читает отлично или с небольшими ошибками", "Читает с ошибками", "Сильно теряется"],
    index=1
)
 
#Scores#
Understanding_Scores = {
    "Понимает, о чем текст в целом": 2,
    "Понимает частично/с подсказками": 1,
    "Не понимает": 0,
}
 
Details_Scores = {
    "Верно отвечает на вопросы по тексту": 2,
    "Отвечает неточно": 1,
    "Не может ответить": 0,
}
 
Confidence_Scores = {
    "Читает отлично или с небольшими ошибками": 2,
    "Читает с ошибками": 1,
    "Сильно теряется": 0
}
 
#Scores2#
total_score = (
    Understanding_Scores[understanding_answer] +
    Details_Scores[details_answer] +
    Confidence_Scores[confidence_answer]
)
 
def get_result_by_score(score):
    if score < 3:
        return "❌ Not OK"
    elif score < 6:
        return "⚠️ Partially OK"
    else:
        return "✅ Excellent"
#Result#
if st.button("Показать результат"):
    st.success(get_result_by_score(total_score))
    st.write("Сумма баллов:", total_score)

