document.addEventListener('DOMContentLoaded', () => {
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const correctCountElement = document.getElementById('correct-count');
    const incorrectCountElement = document.getElementById('incorrect-count');

    let currentQuestion = null;
    let correctCount = 0;
    let incorrectCount = 0;

    async function fetchQuestion() {
        const response = await fetch('questions.php');
        const data = await response.json();
        currentQuestion = data;
        displayQuestion(data);
    }

    function displayQuestion(question) {
        questionElement.textContent = question.question;
        optionsElement.innerHTML = '';
        const shuffledOptions = shuffleArray(question.options);
        shuffledOptions.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.addEventListener('click', () => checkAnswer(button, option));
            optionsElement.appendChild(button);
        });
    }

    function checkAnswer(button, selectedOption) {
        if (selectedOption === currentQuestion.correct) {
            button.style.backgroundColor = 'green';
            correctCount++;
        } else {
            button.style.backgroundColor = 'red';
            incorrectCount++;
        }
        updateScore();
        disableOptions();
        setTimeout(fetchQuestion, 1500);
    }

    function updateScore() {
        correctCountElement.textContent = correctCount;
        incorrectCountElement.textContent = incorrectCount;
    }

    function disableOptions() {
        const buttons = optionsElement.getElementsByTagName('button');
        for (let button of buttons) {
            button.disabled = true;
        }
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // Fetch the first question when the page loads
    fetchQuestion();
});
