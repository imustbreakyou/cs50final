// Collapsable content provided by https://www.w3schools.com/howto/howto_js_collapsible.asp

document.addEventListener('DOMContentLoaded', function() {
  var expandButton = document.querySelector('.expand-button-languages');
  var expandablePanel = document.querySelector('.expandable-panel-languages');

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

// JS for Type filter section

document.addEventListener('DOMContentLoaded', function() {
  var expandButton = document.querySelector('.expand-button-types');
  var expandablePanel = document.querySelector('.expandable-panel-types');

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


// JS for Games filter section


//
document.addEventListener('DOMContentLoaded', function() {
  var expandButton = document.querySelector('.expand-button-games');
  var expandablePanel = document.querySelector('.expandable-panel-games');

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

