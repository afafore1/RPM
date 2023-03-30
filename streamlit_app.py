import os
import re
import time

import streamlit as st
from PIL import Image


def get_problem_set(path=None):
    if path is not None:
        dir_path = f'Problems/{path}'
    else:
        dir_path = 'Problems'
    dir_contents = os.listdir(dir_path)

    problems = []
    for p in dir_contents:
        if p.startswith('Basic') or p.startswith('Challenge'):
            problems.append(p)

    return problems


def get_options_for_problem(path):
    dir_contents = os.listdir(path)
    options = ['']

    for content in dir_contents:
        content_title = content.title()
        if content_title[0].isdigit():
            opt = content_title[0: content_title.index('.')]
            options.append(opt)

    return sorted(options)


def get_answer(path):
    with open(f'{path}/ProblemAnswer.txt', 'r') as f:
        content = f.read()
        return re.sub(r'\s+', '', content)


def get_image(selection, current_index, problems):
    curr_selection = problems[current_index]

    return Image.open(f'Problems/{selection}/{curr_selection}/{curr_selection}.PNG')


def get_selection_title(selection):
    return selection.title().replace(" ", "_")


def calculate_answer(usr_ans, selection, curr_selection):
    ans = get_answer(f'Problems/{selection}/{curr_selection}')
    if usr_ans == ans:
        st.success(f'Correct answer selected for {curr_selection}!')
        return True
    else:
        st.error(f'Wrong answer selected for {curr_selection}\nCorrect answer is {ans}')
        st.session_state['missed_questions'].add(curr_selection)
    return False


def disable_selecting():
    st.session_state['ans_disabled'] = True


def present_question(problems, selection):
    if 'current_index' not in st.session_state:
        st.session_state['current_index'] = 0
    if 'missed_questions' not in st.session_state:
        st.session_state['missed_questions'] = set()
    if 'ans_disabled' not in st.session_state:
        st.session_state['ans_disabled'] = False

    img = get_image(selection, st.session_state['current_index'], problems)
    curr_selection = problems[st.session_state['current_index']]
    image_placeholder.image(img, caption=curr_selection)
    usr_ans = answer_placeholder.selectbox(f'Please select an answer for {curr_selection}',
                                           get_options_for_problem(f'Problems/{selection}/{curr_selection}'),
                                           on_change=disable_selecting,
                                           disabled=st.session_state.ans_disabled)

    if len(usr_ans) > 0:
        correct_ans_selected = calculate_answer(usr_ans, selection, curr_selection)
        if correct_ans_selected:
            st.session_state.ans_disabled = False
            move_to_next_question(problems, selection)
        if st.session_state.current_index < len(problems):
            next_qst = st.button('Next Question')
            if next_qst:
                st.session_state['ans_disabled'] = False
                move_to_next_question(problems, selection)


def move_to_next_question(problems, selection):
    st.session_state['current_index'] += 1
    if st.session_state['current_index'] < len(problems):
        present_question(problems, selection)
    else:
        next_question_placeholder.success(f'{selection} completed. Please select another problem set')
        total_score = 100 * (len(selection) - len(st.session_state.missed_questions)) / len(selection)
        clear_placeholders(selection)
        caption_placeholder.caption(f'Your total score was {total_score}%')


def clear_placeholders(selection):
    answer_placeholder.empty()
    caption_placeholder.empty()
    st.session_state[selection] = [0, 0]
    time.sleep(0.01)


def clear_current_index():
    st.session_state.current_index = 0


def main():
    title_placeholder.title('Ravens Progressive Matrix Test')
    caption_placeholder.caption(
        "The objective of **Raven's Progressive Matrices** is to measure general cognitive ability or "
        "intelligence, "
        "particularly in the areas of **abstract reasoning _and_ problem-solving**. The test consists of a series "
        "of **visual puzzles**, with each puzzle consisting of a matrix of geometric shapes with one shape missing.")

    user_selection = st.sidebar.selectbox(
        "Select one of the problems",
        sorted(get_problem_set()),
        on_change=clear_current_index
    )

    if user_selection:
        selection_problems = sorted(get_problem_set(user_selection))
        present_question(selection_problems, user_selection)


title_placeholder = st.empty()
caption_placeholder = st.empty()
image_placeholder = st.empty()
answer_placeholder = st.empty()
next_question_placeholder = st.empty()
missed_question_placeholder = st.empty()

if __name__ == '__main__':
    main()
