#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFileSync(fileName, content, 'utf8');
