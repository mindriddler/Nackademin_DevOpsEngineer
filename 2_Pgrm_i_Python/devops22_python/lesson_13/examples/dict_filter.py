my_list = [{"key1": "value1"}, {"key2": "value2"}]

# List comprehension
print([meeting for meeting in my_list if "key1" in meeting.keys()])

# Loop version
result = []
search = "key1"
for meeting in my_list:
    if search in meeting.keys():
        result.append(meeting)
print(result)
