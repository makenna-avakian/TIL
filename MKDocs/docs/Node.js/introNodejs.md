# Introduction

Node.js is a powerful, open-source, server-side runtime environment built on Google Chrome's V8 JavaScript engine. It allows you to run JavaScript/Typescript code outside of a browser, making it possible to build scalable and high-performance applications.

## Node.js Benefits

- Non-blocking I/O: Node.js uses an event-driven, non-blocking I/O model, which makes it lightweight and efficient for building scalable network applications.
- JavaScript Everywhere: With Node.js, you can use JavaScript for both client-side and server-side development.
- Large Ecosystem: Node.js has a huge amount of libraries and modules available through npm (Node Package Manager).

# Getting Started

## 1. Installation
To begin, you need to install Node.js. You can download the installer from the official Node.js website, or for macOS and Linux users, you can also use a package manager.

## 2. Hello World Example
Once Node.js is installed, you can create your first Node.js application.

Create a new directory for your project:

```bash
mkdir my-node-app
cd my-node-app
```

Create a new file named app.js:

```bash
touch app.js
```

Open app.js and add the following code:

```javascript
// app.js
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

Run your application:

```bash
node app.js
```

Open your browser and navigate to http://localhost:3000 to see the message "Hello, World!"


## 3. Node.js Modules
Node.js uses a module system, which are ways to organize and reuse code. There are three types of modules:

- Core Modules: Built-in modules provided by Node.js (e.g., http, fs).
- Third-party Modules: Modules developed by the community and available through npm
- Custom Modules: Modules you create in your application.

Example of using a core module:

```javascript
// Using the 'fs' (File System) core module to read a file
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

4. Creating a RESTful API
Node.js is commonly used to create RESTful APIs. Here is an example using Express:

```javascript
// app.js
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// In-memory database (for simplicity)
const books = [];

// Get all books
app.get('/books', (req, res) => {
  res.json(books);
});

// Add a new book
app.post('/books', (req, res) => {
  const book = req.body;
  books.push(book);
  res.status(201).json(book);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

## 6. File System Operations
Node.js provides a fs module to interact with the file system. Here are some basic operations:

Read a file:

```javascript
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

Write to a file:

```javascript
const fs = require('fs');

const content = 'Hello, Node.js!';

fs.writeFile('example.txt', content, (err) => {
  if (err) throw err;
  console.log('File has been saved!');
});
```

## 7. Error Handling
Proper error handling is crucial in Node.js to prevent crashes and ensure a smooth user experience. Always handle errors in callbacks, promises, and async/await.

Proper examples with callbacks:

```javascript
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log(data);
});
```

Proper example with async/await:

```javascript
const fs = require('fs').promises;

async function readFile() {
  try {
    const data = await fs.readFile('example.txt', 'utf8');
    console.log(data);
  } catch (err) {
    console.error('Error reading file:', err);
  }
}

readFile();
```






