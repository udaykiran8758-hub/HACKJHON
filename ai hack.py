<!DOCTYPE html>
<html>
<head>
    <title>Smart Campus Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; text-align: center; }
        #chatbox { width: 400px; margin: auto; background: white; padding: 20px; border-radius: 10px; }
        .message { margin: 10px 0; }
        .user { color: blue; }
        .bot { color: green; }
    </style>
</head>
<body>
    <h2>Smart Campus Assistant</h2>
    <div id="chatbox"></div>
    <input type="text" id="userInput" placeholder="Ask me anything..." />
    <button onclick="sendMessage()">Send</button>

    <script>
        async function sendMessage() {
            let input = document.getElementById("userInput").value;
            let chatbox = document.getElementById("chatbox");

            chatbox.innerHTML += <div class="message user">You: ${input}</div>;

            let res = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input })
            });

            let data = await res.json();
            chatbox.innerHTML += <div class="message bot">Bot: ${data.reply}</div>;
            document.getElementById("userInput").value = "";
        }
    </script>
</body>
</html>