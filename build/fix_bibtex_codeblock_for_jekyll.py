import re
import glob

# Get all markdown files in the current directory
file_list = glob.glob('./*.md')

# Pattern that matches bibtex block surrounded by ```
pattern = re.compile(r'```(.*?)```', re.DOTALL)

for filename in file_list:
    with open(filename, 'r') as file:
        content = file.read()
    # Replace matched pattern with {% raw %} and {% endraw %}
    new_content = re.sub(pattern, '```\n{% raw %}\g<1>{% endraw %}\n```', content)
    with open(filename, 'w') as file:
        file.write(new_content)