document.addEventListener('DOMContentLoaded', function() {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    const activeTab = tabs[0];
    chrome.scripting.executeScript({
      target: {tabId: activeTab.id},
      function: getSelectedText
    });
  });
});

function getSelectedText() {
  const selection = window.getSelection().toString();
  const textarea = document.getElementById('contentTextbox');
  textarea.value = selection;
}
