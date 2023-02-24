import os
from collections import OrderedDict

errors = 0


def error(file, line_number, message, message_type="S", increment_error=True):
	global errors
	print(f"{message_type} {file} line {line_number}:")
	print("\n".join(["\t" + line for line in message.splitlines()]) + "\n")
	if increment_error:
		errors += 1


def processFile(path):
	header = True
	in_brackets = False
	properties = OrderedDict()

	for line_number, line in enumerate(open(path, "r").read().splitlines()):
		if not line.strip():
			continue

		if "}" in line:
			sorted_keys = sorted(properties.keys())
			if sorted_keys != list(properties.keys()):
				error(path, line_number + 1, f"Property keys are not sorted\nExpected properties in order: {sorted_keys}")

			in_brackets = False
			properties = OrderedDict()
			if line != "}":
				return error(path, line_number + 1, "Inline rules or incorrect positioning of closing-braces\nExpected '}' to be the only character in the line")
		elif in_brackets:
			if ":" not in line:
				error(path, line_number + 1, "Possible non-property found in braces\nExpected ': ' to detonate a key-value pair, newline, or a closing-brace", "\033[93mW\033[0m", False)

			if ": " not in line:
				return error(path, line_number + 1, "Expected space after colon")

			if line[-1] != ";":
				return error(path, line_number + 1, "Expected semicolon at the end of the line", "\033[91mE\033[0m")

			properties[line.split(":")[0].strip()] = ":".join(line.split(":")[1:])[:-1]
		else:
			if "{" in line:
				header = False
				in_brackets = True
				if not line.endswith("{"):
					return error(path, line_number + 1, "Inline rules or incorrect positioning of open-braces\nExpected '{' at the end of the line")

				if line[line.index("{") - 1] != " ":
					return error(path, line_number + 1, "Expected whitespace before open-braces")
			elif not header and line.strip():
				return error(path, line_number + 1, "Top-level expression after first rule\nExpected blank line or selector")


def searchDirectory(path="./"):
	for item in os.listdir(path):
		if os.path.isdir(path + item):
			searchDirectory(path + item + "/")
		elif item.endswith(".css"):
			processFile(path + item)


searchDirectory()

print(f"{errors} erroneous files found.")
exit(0 if not errors else 1)
