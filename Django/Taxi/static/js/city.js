fetch("https://ipapi.co/json/")
  .then((res) => res.json())
  .then((data) => {
    document.getElementById("user-city").value = data.city;
  })
  .catch((err) => console.error("Error fetching city:", err));
