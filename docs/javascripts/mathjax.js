window.MathJax = {
    loader: {load: ['[tex]/braket']},
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
      processEnvironments: true,
    packages: {'[+]': ['braket']}
  },
  options: {

  }
};

document$.subscribe(() => {

  MathJax.typesetPromise()
})
