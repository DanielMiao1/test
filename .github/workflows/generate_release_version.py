import datetime
import re
import subprocess

tags_process = subprocess.Popen(["git", "for-each-ref", "--sort=creatordate", "--format", "'%(refname) %(taggerdate)'", "refs/tags"], stdout=subprocess.PIPE)
tags = ""

while True:
	data = tags_process.stdout.read(1)
	if not data:
		break

	tags += data.decode("UTF-8")

for tag in reversed(tags.splitlines()):
	tag = tag[1:-2].replace("refs/tags/", "")
	if not tag.startswith("v"):
		continue

	time = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
	tag = re.sub(r"\+\d+", "", tag)
	print(f"{tag}+{time}")
	break
