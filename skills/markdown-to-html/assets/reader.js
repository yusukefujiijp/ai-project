(function () {
  'use strict';
  var toc = document.querySelector('.toc');
  if (toc) toc.open = window.matchMedia('(min-width:801px)').matches;
  document.querySelectorAll('.toc a').forEach(function (link) {
    link.addEventListener('click', function () {
      document.querySelectorAll('.toc a[aria-current]').forEach(function (a) { a.removeAttribute('aria-current'); });
      link.setAttribute('aria-current', 'location');
      if (window.matchMedia('(max-width:800px)').matches) toc.open = false;
    });
  });
  async function renderDiagrams() {
    var figures = Array.from(document.querySelectorAll('.diagram'));
    if (!figures.length || !window.mermaid) return;
    window.mermaid.initialize({
      startOnLoad: false, securityLevel: 'strict', suppressErrorRendering: true,
      theme: 'base', layout: 'dagre', look: 'classic', htmlLabels: false,
      fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
      themeVariables: { primaryColor: '#eaf3ec', primaryTextColor: '#243b36', primaryBorderColor: '#51836c', lineColor: '#60726b', secondaryColor: '#f5f1e6', tertiaryColor: '#fffefa' }
    });
    for (var i = 0; i < figures.length; i += 1) {
      var fig = figures[i], source = fig.querySelector('pre code').textContent, status = fig.querySelector('.diagram-status');
      try {
        var result = await window.mermaid.render('mdhtml-graph-' + i, source);
        fig.querySelector('.diagram-view').innerHTML = result.svg;
        var svg = fig.querySelector('.diagram-view svg');
        if (svg && svg.viewBox.baseVal.width) {
          svg.style.width = svg.viewBox.baseVal.width + 'px';
          svg.style.maxWidth = 'none';
          var fitButton = document.createElement('button');
          fitButton.type = 'button';
          fitButton.className = 'diagram-fit';
          fitButton.textContent = '図全体を表示';
          fitButton.setAttribute('aria-pressed', 'false');
          fitButton.addEventListener('click', (function (target, control) {
            return function () {
              var fit = control.getAttribute('aria-pressed') !== 'true';
              target.style.maxWidth = fit ? '100%' : 'none';
              control.setAttribute('aria-pressed', String(fit));
              control.textContent = fit ? '文字を大きく表示' : '図全体を表示';
            };
          }(svg, fitButton)));
          fig.querySelector('.diagram-status').after(fitButton);
        }
        fig.dataset.rendered = 'true';
        status.textContent = '図 ' + (i + 1) + '：収まらない部分は横にスクロールできます。';
        fig.querySelector('details').open = false;
      } catch (error) {
        fig.dataset.rendered = 'false';
        status.textContent = '図 ' + (i + 1) + '：描画できませんでした。定義を表示しています。';
        fig.querySelector('details').open = true;
      }
    }
    document.documentElement.dataset.diagramsComplete = 'true';
  }
  renderDiagrams();
}());
