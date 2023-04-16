import re
import sys

WEBSITE_ADDRESS = "https://example.com"
APPLICATION_PATH = "./index.express.js"
application_contents = open(APPLICATION_PATH, "r").read()

routes = []

express_name = None
app_name = None

for line in application_contents.splitlines():
	if express_name is None:
		if re.match(r"^((const|let|var) )?\w+ ?= ?require\(([\"'])express\3\);?$", line):
			express_name = re.sub(r"(const|let|var) ", "", line[:line.index("=")]).strip()
			continue

	if app_name is None:
		if re.match(rf"^((const|var|let) )?\w+ ?= ?{express_name}+\(\);?$", line):
			app_name = re.sub(r"(const|let|var) ", "", line[:line.index("=")]).strip()
			continue

	route_match = re.match(rf"^{app_name}.get\([\"']/((\w|-|\.|%)/?)*[\"']", line)
	if route_match:
		routes.append(line[:route_match.span()[-1]].replace(f"{app_name}.get(", "").strip()[1:-1])


sitemap_urls = "\n".join(["\t" + line for line in "\n".join([f"""<url>
\t<loc>{WEBSITE_ADDRESS}{route}</loc>
</url>""" for route in routes]).splitlines()])

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
"""

if len(sys.argv) >= 2 and sys.argv[1] == "-c":
	import os

	if not os.path.exists("sitemap.xml"):
		print("UPDATE-REQUIRED")
		exit()

	existing_sitemap = open("sitemap.xml", "r").read()
	if existing_sitemap == sitemap:
		print("NOT-REQUIRED")
	else:
		print("UPDATE-REQUIRED")

	exit()

print(sitemap)
