#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(elm => {
    if (elm === searchElement) count++;
  });
  return count;
};
