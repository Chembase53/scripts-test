import re

def extract_times(pasted_text):
    # Extract time entries using regular expression
    time_entries = re.findall(r'\d+\.\d+', pasted_text)

    # Extract solve times without "DNF" and format with numbering
    formatted_times = []
    for i, time in enumerate(time_entries):
        if "DNF" not in pasted_text.split('\n')[i]:
            formatted_times.append(f"{i+1}. {time}")

    return "\n".join(formatted_times)

# Read text from input.txt
with open('input.txt', 'r') as file:
    pasted_text = file.read()

# Extract and format the times, excluding "DNF" entries
formatted_times = extract_times(pasted_text)

# Print the formatted times
print("\nFormatted Times:\n")
print(formatted_times)
