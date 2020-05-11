#!/usr/bin/node
exports.converter = (base) => {
  function conv (nbr) {
    return nbr.toString(base);
  }
  return conv;
};
