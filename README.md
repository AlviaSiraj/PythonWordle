<body>

  <h1>🟩 Wordle Game (Python + Tkinter GUI)</h1>

  <p>
    A simple Wordle-style word guessing game built in Python using the
    <code>customtkinter</code> GUI framework. This game gives players 10 attempts to guess a randomly selected word,
    with color-coded feedback for each letter — similar to the original Wordle.
  </p>

  <h2>🎮 Features</h2>
  <ul>
    <li>Random 5-6 letter word selection from a curated list</li>
    <li>Color-coded feedback:</li>
    <ul>
      <li>🟩 Green (<code>#7EBF7A</code>): Correct letter in the correct position</li>
      <li>🟨 Yellow (<code>#E8C97E</code>): Correct letter in the wrong position</li>
      <li>🟥 Pink (<code>#F7DCDA</code>): Incorrect letter</li>
    </ul>
    <li>10 attempts per game</li>
    <li>Basic English dictionary validation (<code>pyenchant</code>)</li>
    <li>Custom-themed GUI with <code>customtkinter</code></li>
    <li>Responsive keyboard input with Enter key binding</li>
  </ul>

  <h2>🛠️ Requirements</h2>
  <ul>
    <li>Python 3.7+</li>
    <li><code>customtkinter</code></li>
    <li><code>pyenchant</code></li>
  </ul>

  <p>Install required packages:</p>
  <pre><code>pip install customtkinter pyenchant</code></pre>

  <blockquote>
    💡 Note: On some systems, <code>pyenchant</code> may require additional setup or dictionaries.
  </blockquote>

  <h2>📂 File Structure</h2>
  <pre><code>wordle/
├── wordle.py          # Contains the core game logic
├── wordleGUI.py       # GUI implementation using customtkinter
├── wordleIcon.ico     # Optional: icon file for the window
└── README.md          # You're here!
</code></pre>

  <h2>🚀 How to Run</h2>
  <ol>
    <li>Clone or download this repository.</li>
    <li>Ensure dependencies are installed (<code>customtkinter</code>, <code>pyenchant</code>).</li>
    <li>Run the GUI:</li>
  </ol>
  <pre><code>python wordleGUI.py</code></pre>

  <h2>🧠 Game Logic Summary</h2>
  <ul>
    <li>The game selects a random 5-letter word from a predefined list.</li>
    <li>The player enters guesses, which are validated against an English dictionary.</li>
    <li>Each guess is checked letter by letter:
      <ul>
        <li>Green: Letter is in the correct position.</li>
        <li>Yellow: Letter exists in the word but in the wrong position.</li>
        <li>Pink: Letter does not exist in the word.</li>
      </ul>
    </li>
    <li>The game ends after 10 attempts or when the word is correctly guessed.</li>
  </ul>

  <h2>🎨 Screenshots</h2>
<img src="/images/screenshot.png" alt="Example Screenshot1" height="300">

  <h2>📝 License</h2>
  <p>This project is open-source and free to use for learning or personal use.</p>

</body>
</html>
