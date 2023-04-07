// Initialize the application
editorModule.configureEditors();

// Load GitHub Token and URL from localStorage
document.getElementById("github-token").value = localStorage.getItem("github-token") || "";
document.getElementById("github-url").value = localStorage.getItem("github-url") || "";

// Event listeners
document.getElementById("github-connect").addEventListener("click", async () => {
    const token = document.getElementById("github-token").value;
    const url = document.getElementById("github-url").value;

    // Save GitHub Token and URL to localStorage
    localStorage.setItem("github-token", token);
    localStorage.setItem("github-url", url);

    const tree = await githubModule.getTree(token, url);
    treeModule.buildTree(tree);
});

document.getElementById("send-to-ai").addEventListener("click", async () => {
    const input = document.getElementById("ai-input").value;
    const data = await aiModule.sendToAI(input);
    const code = data.code;
    editorModule.codeEditor.setValue(code);
    editorModule.codeEditor.clearSelection();
});