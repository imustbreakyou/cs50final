// Collapsable content provided by https://www.w3schools.com/howto/howto_js_collapsible.asp

document.addEventListener('DOMContentLoaded', function() {
  var expandButton = document.querySelector('.expand-button');
  var expandablePanel = document.querySelector('.expandable-panel');

  expandButton.addEventListener('click', function() {
    // This toggles the visibility of the panel
    if (expandablePanel.style.display === 'block') {
      expandablePanel.style.display = 'none';
      expandButton.textContent = '▼'; // Change button text/icon to show expandable action
    } else {
      expandablePanel.style.display = 'block';
      expandButton.textContent = '▲'; // Change button text/icon to show collapsible action
    }
  });
});