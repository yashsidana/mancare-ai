# Entrypoint for Streamlit Cloud
import os
import sys

# Ensure local modules are discoverable
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Run the main app
import app
