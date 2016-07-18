from sys import argv
from methods import *

if len(argv) == 3:
	# Call functions to get sentiment
	if argv[1] == 'text':
		print analyze_text(argv[2])
	elif argv[1] == 'file':
		print analyze_file(argv[2])
	else:
		print """
Usage: python main.py <option> <arguments>
Options: text, file
For text: python main.py text 'some text to analyze'
For file: python main.py file /path/to/file
(Use backward slashes for Windows paths)
"""

else:
	print """
Usage: python main.py <option> <arguments>
Options: text, file
For text: python main.py text 'some text to analyze'
For file: python main.py file /path/to/file
(Use backward slashes for Windows paths)
"""