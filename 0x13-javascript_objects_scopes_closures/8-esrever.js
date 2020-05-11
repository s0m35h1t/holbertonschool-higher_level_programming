#!/usr/bin/node
exports.esrever = (list) => {
  const rev = [];
  list.forEach(elm => {
    rev.unshift(list[elm]);
  });
  return rev;
};
