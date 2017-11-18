import builtins, os, sys
EXECUTABLE = '/anaconda3/bin/python'

# Save original __import__.
orig_import = __import__

# Define a monkeypatch that switches executables.
def new_import(name, globals=None, locals=None, fromlist=(), level=0):
    """Start a different Python interpreter."""
    if hasattr(sys, 'argv'):
        # Replace current process...
        os.execv(EXECUTABLE, ['python'] + sys.argv)
    print('waiting', name, file=sys.stderr)
    return orig_import(name, globals, locals, fromlist, level)

# Install the monkeypatch if we are running a different executable.
if sys.executable != EXECUTABLE:
    builtins.__import__ = new_import
