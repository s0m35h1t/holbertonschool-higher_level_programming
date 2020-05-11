#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  list.forEach(elm => {
    rev.unshift(elm);
  });
  return rev;
};
