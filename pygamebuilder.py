import streamlit as st
import google.generativeai as genai
import pygame
import sys
import os
import tempfile
import subprocess
import threading
import time
import traceback

st.set_page_config(page_title="PyGame Code Generator", layout="wide")

# Initialize session state
if "api_keys" not in st.session_state:
    st.session_state.api_keys = {
        "gemini": ""
    }

# Streamlit sidebar for API keys
with st.sidebar:
    st.title("API Keys Configuration")
    st.session_state.api_keys["gemini"] = st.text_input(
        "Gemini API Key",
        type="password",
        value=st.session_state.api_keys["gemini"]
    )
    
    st.markdown("---")
    st.info("""
    📝 How to use:
    1. Enter your Gemini API key above
    2. Write your PyGame visualization query
    3. Click 'Generate Code' to get the code
    4. Click 'Run Visualization' to:
       - Run the game in a new window
       - Control the game with your keyboard/mouse
       - Close the window when done
    """)

# Main UI
st.title("🎮 AI PyGame Visualizer with Gemini")
example_query = "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
query = st.text_area(
    "Enter your PyGame query:",
    height=70,
    placeholder=f"e.g.: {example_query}"
)

# Split the buttons into columns
col1, col2 = st.columns(2)
generate_code_btn = col1.button("Generate Code")
run_vis_btn = col2.button("Run Visualization")

if generate_code_btn and query:
    if not st.session_state.api_keys["gemini"]:
        st.error("Please provide your Gemini API key in the sidebar")
        st.stop()

    system_prompt = """You are a Pygame and Python Expert that specializes in making games and visualisation through pygame and python programming. 
    During your reasoning and thinking, include clear, concise, and well-formatted Python code in your reasoning. 
    Always include explanations for the code you provide."""

    try:
        # Initialize Gemini
        genai.configure(api_key=st.session_state.api_keys["gemini"])
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Generate solution
        with st.spinner("Generating solution..."):
            try:
                response = model.generate_content(f"{system_prompt}\n\nUser query: {query}")
                reasoning_content = response.text
            except Exception as api_error:
                st.error(f"Error with Gemini API: {str(api_error)}")
                st.info("Please check your API key and try again.")
                st.stop()

        print("\nReasoning:\n", reasoning_content)
        with st.expander("AI Reasoning"):      
            st.write(reasoning_content)

        # Extract code
        extraction_prompt = f"""Extract ONLY the Python code from the following content which is reasoning of a particular query to make a pygame script. 
        Return nothing but the raw code without any explanations, or markdown backticks:
        {reasoning_content}"""

        with st.spinner("Extracting code..."):
            try:
                code_response = model.generate_content(extraction_prompt)
                extracted_code = code_response.text
                
                # Clean up the extracted code
                # Remove markdown code block markers if present
                extracted_code = extracted_code.replace('```python', '').replace('```', '')
                # Remove any leading/trailing whitespace
                extracted_code = extracted_code.strip()
                
                # If the code is empty or still contains markdown, try regex extraction
                if not extracted_code or '```' in extracted_code:
                    import re
                    code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', reasoning_content, re.DOTALL)
                    if code_blocks:
                        extracted_code = code_blocks[0].strip()
                    else:
                        # If no code blocks found, try to extract any Python-like code
                        code_lines = []
                        in_code_block = False
                        for line in reasoning_content.split('\n'):
                            if line.startswith('```'):
                                in_code_block = not in_code_block
                                continue
                            if in_code_block or (line.strip() and not line.startswith('#')):
                                code_lines.append(line)
                        extracted_code = '\n'.join(code_lines).strip()
                
            except Exception as gemini_error:
                st.error(f"Error with Gemini API: {str(gemini_error)}")
                st.info("Attempting to extract code directly from the reasoning...")
                # Simple fallback: try to extract code between triple backticks
                import re
                code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', reasoning_content, re.DOTALL)
                if code_blocks:
                    extracted_code = code_blocks[0].strip()
                else:
                    extracted_code = reasoning_content.strip()

        # Store the generated code in session state
        st.session_state.generated_code = extracted_code
        
        # Display the code with editing capability
        with st.expander("Generated PyGame Code", expanded=True):
            # Add a text area for editing
            edited_code = st.text_area(
                "Edit the code if needed:",
                value=extracted_code,
                height=400,
                key="code_editor"
            )
            
            # Update the stored code with edited version
            st.session_state.generated_code = edited_code
            
            # Add game instructions section
            st.markdown("### 🎮 How to Play")
            st.markdown("""
            #### Controls:
            - **Mouse**: Move to control particle emission
            - **Arrow Keys**: Control wind direction
            - **Space**: Pause/Resume simulation
            - **R**: Reset simulation
            - **ESC**: Quit game
            
            #### Gameplay Tips:
            - Move your mouse to create particles
            - Use arrow keys to create wind effects
            - Watch how particles interact with wind
            - Try different mouse movements for interesting patterns
            
            #### Features:
            - 100 particles emit from mouse position
            - Wind forces affect particle movement
            - Particles fade out over time
            - Dynamic color changes based on particle speed
            """)
            
            # Add debug information
            st.markdown("### 🐛 Debug Information")
            st.markdown("""
            If you encounter any errors:
            1. Check the error message below
            2. Edit the code above to fix the issues
            3. Common issues to check:
               - Missing pygame initialization
               - Incorrect indentation
               - Missing imports
               - Syntax errors
            """)
            
            # Add a test run button and results section
            col1, col2 = st.columns([1, 3])
            with col1:
                test_run_btn = st.button("Test Run (Check for Errors)")
            
            # Create a container for test results that persists
            test_results = st.container()
            
            if test_run_btn:
                with test_results:
                    with st.spinner("Running code check..."):
                        try:
                            # Create a temporary file with proper error checking
                            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                                # Add necessary imports and error handling
                                test_code = f"""import pygame
import sys
import traceback

def test_game():
    try:
        # Initialize Pygame
        pygame.init()
        
        # Create a small window for testing
        screen = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("Test Window")
        
        # Your game code here
{chr(10).join('        ' + line for line in edited_code.split(chr(10)))}
        
        # Basic event loop to test pygame functionality
        running = True
        clock = pygame.time.Clock()
        for _ in range(10):  # Run for a short time to test
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if not running:
                break
            clock.tick(60)
        
        return True, "No errors found! Code runs successfully."
    except Exception as e:
        return False, f"Error: {{str(e)}}\\n\\nTraceback:\\n{{traceback.format_exc()}}"
    finally:
        pygame.quit()

if __name__ == '__main__':
    success, message = test_game()
    if not success:
        print(message, file=sys.stderr)
        sys.exit(1)
    else:
        print(message, file=sys.stdout)
"""
                                f.write(test_code)
                                temp_file = f.name

                            # Try to run the code with error capture
                            process = subprocess.Popen(
                                [sys.executable, temp_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True
                            )
                            stdout, stderr = process.communicate()

                            # Display results in a persistent container
                            if stderr:
                                st.error("❌ Errors found during test run:")
                                st.code(stderr, language="text")
                                st.info("Please fix the errors in the code editor above.")
                            else:
                                st.success("✅ " + stdout.strip())
                                st.info("Your code is ready to run! Click 'Run Visualization' to play the game.")
                            
                            # Clean up
                            try:
                                os.unlink(temp_file)
                            except:
                                pass
                                
                        except Exception as e:
                            st.error(f"Error during test run: {str(e)}")
                            st.code(traceback.format_exc(), language="text")
            
            # Add a persistent status indicator
            if 'last_test_result' in st.session_state:
                with test_results:
                    if st.session_state.last_test_result.get('success'):
                        st.success("✅ Last test: " + st.session_state.last_test_result.get('message', 'No errors found!'))
                    else:
                        st.error("❌ Last test: " + st.session_state.last_test_result.get('message', 'Errors found!'))

        st.success("Code generated successfully! Click 'Run Visualization' to play the game.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please check your API key and try again.")

elif run_vis_btn:
    if "generated_code" not in st.session_state:
        st.warning("Please generate code first before running visualization")
    else:
        def run_pygame_code(code: str):
            try:
                # Create a temporary file with proper PyGame initialization
                with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                    # Add necessary imports and error handling
                    modified_code = f"""import pygame
import sys

# Initialize Pygame
pygame.init()

try:
{chr(10).join('    ' + line for line in code.split(chr(10)))}
except Exception as e:
    print(f"Error in game: {{e}}")
    traceback.print_exc()
finally:
    pygame.quit()
    sys.exit()
"""
                    f.write(modified_code)
                    temp_file = f.name

                # Run the PyGame script in a separate process
                if sys.platform == 'win32':
                    # On Windows, use pythonw to prevent console window
                    python_exe = os.path.join(os.path.dirname(sys.executable), 'pythonw.exe')
                    if not os.path.exists(python_exe):
                        python_exe = sys.executable
                else:
                    python_exe = sys.executable

                process = subprocess.Popen(
                    [python_exe, temp_file],
                    creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == 'win32' else 0,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                # Wait for the process to complete
                stdout, stderr = process.communicate()
                
                if stderr:
                    st.error("Game encountered an error:")
                    st.code(stderr, language="text")
                    st.info("Please fix the errors in the code editor and try again.")
                
                # Clean up the temporary file
                try:
                    os.unlink(temp_file)
                except:
                    pass
                
            except Exception as e:
                st.error(f"Error running PyGame code: {str(e)}")
                st.info("You can still copy the code above and run it manually.")

        # Run the PyGame code in a separate thread
        thread = threading.Thread(target=run_pygame_code, args=(st.session_state.generated_code,))
        thread.daemon = True  # Make thread daemon so it exits when main program exits
        thread.start()
        
        st.info("Game is running in a new window. Close the window when you're done playing!")
        
        # Add a download button for the code
        st.download_button(
            label="Download Game Code",
            data=st.session_state.generated_code,
            file_name="game.py",
            mime="text/plain"
        )

elif generate_code_btn and not query:
    st.warning("Please enter a query before generating code")