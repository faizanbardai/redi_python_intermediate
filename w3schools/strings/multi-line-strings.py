multi_line_strings = """hello
this is new
something"""
print(multi_line_strings)

print(multi_line_strings[0])

for a in multi_line_strings:
    print(a)

print(len(multi_line_strings))

print('this' in multi_line_strings)
print('thisthis' in multi_line_strings)
print('thisthis' not in multi_line_strings)
