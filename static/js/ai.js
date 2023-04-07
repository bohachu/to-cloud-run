const aiModule = (() => {
    const sendToAI = async (input) => {
        const formData = new FormData();
        formData.append("input", input);
        const data = await fetch("/api/ai", {
            method: "POST",
            body: formData,
        }).then((res) => res.json());
        return data;
    };

    return { sendToAI };
})();