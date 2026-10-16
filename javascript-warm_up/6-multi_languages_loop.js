#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const output = [];
let i = 0;

while (i < languages.length) {
  output.push(languages[i]);
  i++;
}

console.log(output.join('\n'));
