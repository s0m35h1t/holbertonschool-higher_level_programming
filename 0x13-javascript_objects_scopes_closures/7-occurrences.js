#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  list.forEach(elm => {
    if (list[elm] === searchElement) count++;
  });
  return count;
};
