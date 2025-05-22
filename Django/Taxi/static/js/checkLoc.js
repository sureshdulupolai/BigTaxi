window.addEventListener("load", function () {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
          .then((res) => res.json())
          .then((data) => {
            const city = data.address.city || data.address.town || data.address.village || "";
            const state = data.address.state || "";

            // Set form values
            document.getElementById('uCityId').value = city;
            document.getElementById('uStateId').value = state;

            // Show alert message
            document.getElementById('locationAlert').innerText = `By Default Location selected: ${city}, ${state}`;
          });
      },
      function (error) {
        alert("Please allow location access.");
      }
    );
  });