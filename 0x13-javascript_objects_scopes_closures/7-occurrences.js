#!/usr/bin/node
function nbOccurences (list, searchElement) {
  let totalNum = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      totalNum += 1;
    }
  }

  return totalNum;
}

exports.nbOccurences = nbOccurences;
