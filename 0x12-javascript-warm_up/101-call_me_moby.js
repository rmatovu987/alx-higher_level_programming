#!/usr/bin/node

function callMeMoby (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
}
module.exports = {
  callMeMoby: callMeMoby
};
