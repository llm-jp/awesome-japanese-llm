#!/bin/bash

# Search all markdown files in the directory
for file in $(find . -name "*.md")
do
  # Replace the original BibTex code block with the one enclosed in {% raw %} and {% endraw %}
  sed -i -e 's/@software{LLM-jp_Overview_of_Japanese_2023,/\
{% raw %}\n@software{LLM-jp_Overview_of_Japanese_2023,/g' -e 's/year = {2023}/\
year = {2023}\n{% endraw %}/g' $file
done