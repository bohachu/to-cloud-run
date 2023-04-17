const githubModule = (() => {
    const getTree = async (token, url) => {
        const formData = new FormData();
        formData.append("token", token);
        formData.append("url", url);
        const tree = await fetch("/api/get_tree", {
            method: "POST",
            body: formData,
        }).then((res) => res.json());
        return tree;
    };

    const readFile = async (token, url, path) => {
        const formData = new FormData();
        formData.append("token", token);
        formData.append("url", url);
        formData.append("path", path);
        const file = await fetch("/api/read_file", {
            method: "POST",
            body: formData,
        }).then((res) => res.json());
        return file;
    };

    const updateFile = async (token, url, path, content, sha) => {
        const formData = new FormData();
        formData.append("token", token);
        formData.append("url", url);
        formData.append("path", path);
        formData.append("content", content);
        formData.append("sha", sha);
        await fetch("/api/update_file", {
            method: "POST",
            body: formData,
        });
    };

    return { getTree, readFile, updateFile };
})();