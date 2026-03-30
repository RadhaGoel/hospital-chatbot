const chatContainer = document.getElementById("chat-container");

async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const userText = inputField.value;

    if (!userText) return;

    addMessage(userText, "user");
    inputField.value = "";

    // typing indicator
    const typing = addMessage("Typing...", "bot");

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: userText })
        });

        const data = await response.json();

        typing.remove(); // remove "Typing..."
        addMessage(data.response, "bot");

    } catch (error) {
        typing.remove();
        addMessage("Error connecting to server.", "bot");
    }
}

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;

    chatContainer.appendChild(msg);
    chatContainer.scrollTop = chatContainer.scrollHeight;

    return msg;
}

// Enter key support
document.getElementById("userInput")
.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});