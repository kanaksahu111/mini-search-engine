const themeToggle = document.getElementById("themeToggle");

if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    themeToggle.textContent = "☀️";
}

themeToggle.onclick = () => {
    document.body.classList.toggle("dark");
    const isDark = document.body.classList.contains("dark");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    themeToggle.textContent = isDark ? "☀️" : "🌙";
};

// ================= SEARCH LOGIC =================
async function performSearch() {
    const query = document.getElementById("query").value.trim();
    const resultsDiv = document.getElementById("results");
    const loader = document.getElementById("loader");

    if (!query) {
        resultsDiv.innerHTML = "<p>Please enter a search term</p>";
        return;
    }

    resultsDiv.innerHTML = "";
    loader.classList.remove("hidden");

    try {
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        loader.classList.add("hidden");

        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No results found</p>";
            return;
        }

        data.forEach(item => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <h3>${item.document}</h3>
                <p>${item.sentence}</p>
                <small>Score: ${item.score}</small>
            `;

            resultsDiv.appendChild(card);
        });

    } catch (error) {
        loader.classList.add("hidden");
        resultsDiv.innerHTML = "<p>Error fetching results</p>";
        console.error(error);
    }
}