# 🎮 Gamify-PyGame-Agent

**Gamify-PyGame-Agent** is an AI-powered interactive web application that generates, edits, and runs PyGame visualizations from natural language prompts. It enables users to prototype visual simulations using PyGame effortlessly through a Streamlit interface powered by Google Gemini.

---

## ✨ Features

### 🧠 AI-Powered Code Generation
- Convert natural language descriptions into PyGame code
- Real-time intelligent code generation and auto-suggestions
- Smart fallback mechanisms and error-handling logic

### 💻 Interactive Development Environment
- Built-in live code editor with syntax highlighting
- Debug console for error reporting and tracebacks
- One-click download of generated or edited code

### 🧪 Game Testing & Debugging
- Instant test-run button to validate PyGame code
- Persistent display of debug and error information
- Automatic PyGame window handling with graceful cleanup

---

## 🚀 Getting Started

1. **Clone the repository**
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
- Enter your PyGame visualization query in the text area
- Example: "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
- Click "Generate Code" to create the PyGame implementation

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

### Key Components
1. **Code Generation**
   - Uses Gemini AI for natural language to code conversion
   - Handles code extraction and formatting
   - Provides fallback mechanisms for error cases

2. **Game Execution**
   - Manages PyGame initialization and cleanup
   - Handles window creation and event loops
   - Provides error handling and debugging

3. **User Interface**
   - Streamlit-based web interface
   - Real-time code editing and testing
   - Persistent state management

### Getting Help
- Check the debug information in the application
- Review error messages and tracebacks
- Use the test run feature to identify issues

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request