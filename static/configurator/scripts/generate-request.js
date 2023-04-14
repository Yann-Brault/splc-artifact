let btn = document.getElementById("generate");

const action = async () => {
  const response = await fetch(`${getCurrentURL()}generate`, {
    method: "POST",
    body: JSON.stringify({
      config: "hello_world",
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const res = response.json();
  res.then((result) => {
    alert(`${result.message}, notebook has been generated`);
  });
};

btn.addEventListener("click", action);

function getCurrentURL() {
  return window.location.href;
}
