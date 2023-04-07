const treeModule = (() => {
    const buildTree = (treeData) => {
        const data = treeData.tree.map((item) => {
            const parentPath = item.path.split("/").slice(0, -1).join("/");
            return {
                id: item.path,
                parent: parentPath === "" ? "#" : parentPath,
                text: item.path.split("/").pop(),
            };
        });
        $("#github-tree").jstree("destroy");
        $("#github-tree").jstree({ core: { data } });
    };

    $("#github-tree").on("select_node.jstree", async (e, data) => {
        const token = document.getElementById("github-token").value;
        const url = document.getElementById("github-url").value;
        const path = data.selected[0];
        const formData = new FormData();
        formData.append("token", token);
        formData.append("url", url);
        formData.append("path", path);
        const file = await fetch("/api/read_file", {
            method: "POST",
            body: formData,
        }).then((res) => res.json());
        if (file.content) {
            // Decode the Base64 string using TextDecoder
            const base64ToUint8Array = (base64) => {
                const binary_string = atob(base64);
                const len = binary_string.length;
                const bytes = new Uint8Array(len);
                for (let i = 0; i < len; i++) {
                    bytes[i] = binary_string.charCodeAt(i);
                }
                return bytes;
            };
            const utf8ArrayToString = (uintArray) => {
                const decoder = new TextDecoder();
                return decoder.decode(uintArray);
            };
            const content = utf8ArrayToString(base64ToUint8Array(file.content));
            editorModule.codeEditor.setValue(content);
            editorModule.codeEditor.clearSelection();
            editorModule.fileEditor.setValue(content);
            editorModule.fileEditor.clearSelection();
            localStorage.setItem("editorModule_path", path);
            localStorage.setItem("editorModule_sha", file.sha);
        } else {
            console.error("File content not found");
        }
    });

    return { buildTree };
})();