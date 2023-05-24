# Ravens Progressive Matrix Test Application

This application presents a series of visual puzzles that are part of the **Raven's Progressive Matrices** test. The objective of this test is to measure general cognitive ability or intelligence, particularly in the areas of abstract reasoning and problem-solving.

## Getting Started

Please visit https://rpmvisual.streamlit.app/ to play with the application


## Application Overview

The application presents a series of visual puzzles, each consisting of a matrix of geometric shapes with one shape missing. The user is presented with a list of problems from which they can choose one to solve. After selecting a problem, an image of the problem is displayed, and the user can select an answer from the provided options.

The application uses the following main functions:

- `get_problem_set(path=None)`: Retrieves the problem set from the specified path.
- `get_options_for_problem(path)`: Retrieves the options for the selected problem.
- `get_answer(path)`: Reads the answer for the problem from a text file.
- `get_image(selection, current_index, problems)`: Opens the image of the problem.
- `calculate_answer(usr_ans, selection, curr_selection)`: Checks if the selected answer is correct and displays a success or error message.
- `present_question(problems, selection)`: Presents the current question and handles the progression to the next question.
- `move_to_next_question(problems, selection)`: Advances to the next question.
- `clear_current_index()`: Resets the current index in the session state.

## Contributing

We welcome contributions to improve the application. Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the terms of the MIT license.
