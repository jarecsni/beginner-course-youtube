# Configuration file for jupyter-notebook.

# Allow all IP addresses to connect to the notebook server
c.NotebookApp.ip = '0.0.0.0'

# Set the default directory for notebooks
c.NotebookApp.notebook_dir = './notebooks'

# Automatically open browser when starting
c.NotebookApp.open_browser = True

# Set the port for the notebook server
c.NotebookApp.port = 8888

# Enable autoreload extension for automatic code reloading
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']

# Set matplotlib backend to inline for better notebook integration
c.InteractiveShellApp.matplotlib = 'inline'

# Configure tornado settings for better performance
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

# Enable saving notebooks as .py files automatically
c.NotebookApp.contents_manager_class = 'jupyter_notebook_gist.gist.GistContentsManager'

# Set maximum output length to prevent browser crashes with large outputs
c.NotebookApp.iopub_data_rate_limit = 1000000000
c.NotebookApp.iopub_msg_rate_limit = 3000