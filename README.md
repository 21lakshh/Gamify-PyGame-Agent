# 🎮 Gamify-PyGame-Agent

**Gamify-PyGame-Agent** is an interactive AI-powered web application that enables users to create and run PyGame visualizations from natural language descriptions. With the help of Google Gemini and a seamless Streamlit interface, anyone can prototype games, simulations, or animations quickly—no advanced coding skills required.

---

## ✨ Key Features

### 🤖 AI-Driven Game Code Generation
- Turn plain English into fully functional PyGame code
- Leverage Google Gemini for accurate and context-aware code generation
- Separates reasoning, explanation, and final code for transparency

### 💡 Interactive Streamlit Interface
- Intuitive sidebar for API setup and user prompts
- Live editable code blocks with syntax highlighting
- Test and debug code before launching the final visualization

### 🧪 Debugging & Error Handling
- Built-in "Test Run" feature to validate code before full execution
- Captures tracebacks and displays meaningful debug messages
- Handles PyGame windows cleanly and gracefully

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/21lakshh/Gamify-PyGame-Agent.git
cd Gamify-PyGame-Agent
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Set up your API key:
   - Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Enter the API key in the application's sidebar

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run pygamebuilder.py
```

2. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

## 🎮 How to Use

### 1. Generating Code
- Describe the visualization or simulation you want.
- Example: "Create a simple bouncing ball simulation with gravity and elastic collision on window borders."
- Click "Generate Code" to create the PyGame implementation
- 🧠 Reasoning: Explanation of how the AI interpreted your prompt
- 🧾 Final Code: The full PyGame implementation

### 2. Editing and Testing
- Review the generated code in the expandable code section
- Edit the code directly in the text area if needed
- Use the "Test Run" button to check for errors
- Fix any issues based on the debug information

### 3. Running the Game
- Click "Run Visualization" to start the game
- A new window will open with your PyGame visualization
- Use the controls as described in the game instructions
- Close the window when done playing


## 🔧 Development

### Project Structure
```
Gamify/
├── pygamebuilder.py    # Main application file
├── README.md          # This documentation
└── requirements.txt   # Project dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request