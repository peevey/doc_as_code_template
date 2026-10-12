(() => {
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let selected = null;
  try { selected = localStorage.getItem('docs-theme'); } catch (_) {}
  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.hidden = false;
      button.textContent = theme === 'dark' ? '☀ Light Mode' : '☾ Dark Mode';
      button.setAttribute('aria-label', theme === 'dark' ? 'Zum Light Mode wechseln' : 'Zum Dark Mode wechseln');
    }
  }
  apply(selected === 'light' || selected === 'dark' ? selected : system.matches ? 'dark' : 'light');
  document.addEventListener('DOMContentLoaded', () => {
    apply(document.documentElement.dataset.theme);
    document.getElementById('theme-toggle').addEventListener('click', () => {
      selected = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('docs-theme', selected); } catch (_) {}
      apply(selected);
    });
  });
  system.addEventListener('change', () => { if (!selected) apply(system.matches ? 'dark' : 'light'); });
})();
