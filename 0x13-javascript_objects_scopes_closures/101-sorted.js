#!/usr/bin/node

const { dict } = require('./101-data');

// Function to compute reverse dictionary
function computeReverseDict (originalDict) {
  const reverseDict = {};

  // Iterate through the original dictionary
  for (const userId in originalDict) {
    const occurrence = originalDict[userId];

    // Check if the occurrence exists as a key in reverseDict
    if (occurrence in reverseDict) {
      reverseDict[occurrence].push(userId);
    } else {
      reverseDict[occurrence] = [userId];
    }
  }

  return reverseDict;
}

// Compute the reverse dictionary
const reverseDict = computeReverseDict(dict);

// Print the reverse dictionary
console.log(reverseDict);
