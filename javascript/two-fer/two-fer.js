var TwoFer = function () {};

TwoFer.prototype.twoFer = function (who) {
  return `One for ${((who == undefined) ? "you" : who)}, one for me.`;
};

module.exports = TwoFer;
