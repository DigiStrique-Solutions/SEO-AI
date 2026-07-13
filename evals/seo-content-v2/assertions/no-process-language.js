module.exports = (output) => {
  const patterns = [
    /system prompt/i,
    /agent instructions/i,
    /authenticity log/i,
    /tool (?:call|output|use)/i,
    /the source used for this article/i,
  ];
  const match = patterns.find((pattern) => pattern.test(output));
  return match
    ? { pass: false, score: 0, reason: `Internal process language matched ${match}` }
    : { pass: true, score: 1, reason: "No internal process language found" };
};
