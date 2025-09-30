async function sendMessage() {
  const inputField = document.getElementById("userInput");
  const message = inputField.value.trim();
  if (!message) return;

  // Add user message
  const chatBox = document.getElementById("chatBox");
  chatBox.innerHTML += `<div class="message user">${message}</div>`;
  inputField.value = "";

  // Call backend
  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message})
  });
  const data = await response.json();

  // Add bot reply
  chatBox.innerHTML += `<div class="message bot">${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}

