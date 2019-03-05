"""Print `Hello World` without using the word 'world'
Note: captialization and punctuation are important. "hello world", "Hello World!" and "HELLO WORLD" aren't valid
"""
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    import __hello__  # noqa

f.seek(0)
hw = f.read(11)
del f
print(' '.join(word.capitalize() for word in hw.split()))
