#!/usr/bin/node
exports.converter = function (base) {
  function conv (nbr) {
    return nbr.toString(base);
  }
  return conv;
};
