// eslint-disable-next-line no-undef
const express = require("express");
// eslint-disable-next-line no-undef
const path = require("path");

const app = express();
var requests = 0;

app.get("*", function(_, __, next) {
  requests++;
  console.log(requests);
  next();
});

app.get("/", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("/aaaaaa-test", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("/test-7666", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("/test-11111111", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("/test-11111112222222222", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("*", function(_, response) {
  response.status(404).end();
});

app.get("/test/asdfgh", function(_, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "index.html"));
});

app.get("/test1", async function(request, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "test1"));
});

app.get("/test2", async function(request, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "test2"));
});

app.get("/test3/test3", async function(request, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "test3"));
});

app.get("/test4--test4/test4/", async function(request, response) {
  // eslint-disable-next-line no-undef
  response.sendFile(path.join(process.cwd(), "test4"));
});

app.listen(3000);
