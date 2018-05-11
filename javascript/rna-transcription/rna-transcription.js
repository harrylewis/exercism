
var DnaTranscriber = function () {};

DnaTranscriber.prototype.toRna = function (sequence) {
  let mapping = {G: "C", C: "G", T: "A", A: "U"};
  var rnaSequence = "";
  let splitSequence = sequence.split("");
  for (var base of splitSequence) {
    if (["G", "C", "A", "T"].includes(base))
      rnaSequence += mapping[base];
    else
      throw new Error("Invalid input");
  }
  return rnaSequence;
};

module.exports = DnaTranscriber;
