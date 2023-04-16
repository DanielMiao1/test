const express = require("express");
const path = require("path");

const app = express();
var requests = 0;

app.get("*", function(_, _, next) {
	requests++;
	next();
});

app.get("/", function(_, response) {
	response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("*", function(_, response) {
	response.status(404).end();
});

app.get("/test1", async function(request, response) {
	response.sendFile(path.join(process.cwd(), "test1"));
});

app.get("/test2", async function(request, response) {
	response.sendFile(path.join(process.cwd(), "test2"));
});

app.get("/test3/test3", async function(request, response) {
	response.sendFile(path.join(process.cwd(), "test3"));
});

app.get("/test4--test4/test4/", async function(request, response) {
	response.sendFile(path.join(process.cwd(), "test4"));
});

app.listen(3000);
