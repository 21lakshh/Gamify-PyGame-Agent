# Gamify-PyGame-Agent

An interactive web application that generates and runs PyGame visualizations using AI. Create particle systems, games, and interactive simulations with natural language prompts.

## ✨ Features

### 1. AI-Powered Code Generation
- Generate PyGame code using natural language descriptions
- Powered by Google's Gemini AI model
- Real-time code generation and modification
- Intelligent error handling and suggestions

### 2. Interactive Development Environment
- Live code editor with syntax highlighting
- Real-time code testing and validation
- Debug information and error reporting
- Code download functionality

### 3. Game Testing & Debugging
- One-click test run functionality
- Detailed error messages and tracebacks
- Persistent test results display
- Automatic PyGame initialization and cleanup

### 4. User-Friendly Interface
- Clean, modern Streamlit interface
- Sidebar for API configuration
- Expandable code and debug sections
- Clear game instructions and controls

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- PyGame library
- Streamlit
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Gamify
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

### 4. Controls
- **Mouse**: Control particle emission
- **Arrow Keys**: Control wind direction
- **Space**: Pause/Resume simulation
- **R**: Reset simulation
- **ESC**: Quit game

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

## 🐛 Troubleshooting

### Common Issues
1. **API Key Issues**
   - Ensure your Gemini API key is valid
   - Check the key in the sidebar configuration

2. **PyGame Errors**
   - Verify PyGame installation
   - Check for missing dependencies
   - Review error messages in the debug section

3. **Window Not Opening**
   - Ensure no other PyGame windows are running
   - Check system graphics drivers
   - Verify Python environment setup

### Getting Help
- Check the debug information in the application
- Review error messages and tracebacks
- Use the test run feature to identify issues

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 🙏 Acknowledgments

- Google Gemini AI for code generation
- PyGame for game development framework
- Streamlit for web interface
- All contributors and users of the project 