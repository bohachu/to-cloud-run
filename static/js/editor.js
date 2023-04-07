const editorModule = (() => {
    document.addEventListener('keydown', function(event) {
      if (event.metaKey && event.keyCode === 83) { // metaKey 對應 cmd 鍵
        event.preventDefault(); // 取消預設行為
      }
    });

    const fileEditor = ace.edit("file-editor");
    fileEditor.setTheme("ace/theme/monokai");
    fileEditor.setFontSize(17);

    const codeEditor = ace.edit("ai-code");
    codeEditor.setTheme("ace/theme/monokai");
    codeEditor.setFontSize(17);

    const configureEditors = () => {
        fileEditor.setTheme("ace/theme/monokai");
        fileEditor.setFontSize(17);
        codeEditor.setTheme("ace/theme/monokai");
        codeEditor.setFontSize(17);
    };
    const utf8ToBase64 = (str) => {
        return btoa(unescape(encodeURIComponent(str)));
    };
    const saveFile = () => {
        const token = document.getElementById("github-token").value;
        const url = document.getElementById("github-url").value;

        const path = localStorage.getItem("editorModule_path");
        const sha = localStorage.getItem("editorModule_sha");

        const content = fileEditor.getValue();
        githubModule.updateFile(token, url, path, content, sha);
    };

    fileEditor.commands.addCommand({
        name: "saveFile",
        bindKey: { win: "Ctrl-S", mac: "Command-S" },
        exec: saveFile,
    });

    return { fileEditor, codeEditor, configureEditors, saveFile };
})();