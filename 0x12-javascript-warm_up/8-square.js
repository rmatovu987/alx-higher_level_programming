#!/usr/bin/node

const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
