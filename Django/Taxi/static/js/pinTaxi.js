let userAddressSelectedTo = "";
let userAddressSelectedFrom = "";

// Destination Map
let destMap,
  destMarker,
  destLatLng = null;
const destMapDiv = document.getElementById("map");
const destConfirmBtn = document.getElementById("confirm-btn");

document.getElementById("open-map-btn").addEventListener("click", () => {
  destMapDiv.style.display = "block";
  destConfirmBtn.style.display = "inline-block";

  if (!destMap) {
    destMap = L.map("map").setView([22.5937, 78.9629], 5);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap contributors",
    }).addTo(destMap);

    destMap.on("click", function (e) {
      destLatLng = e.latlng;
      if (destMarker) {
        destMarker.setLatLng(destLatLng);
      } else {
        destMarker = L.marker(destLatLng).addTo(destMap);
      }
    });
  }
});

destConfirmBtn.addEventListener("click", () => {
  if (!destLatLng)
    return alert("Please select destination location on the map.");

  fetch(
    `https://nominatim.openstreetmap.org/reverse?format=json&lat=${destLatLng.lat}&lon=${destLatLng.lng}`
  )
    .then((res) => res.json())
    .then((data) => {
      const address = data.display_name;
      document.getElementById("toLocationInput").value = address;
      userAddressSelectedTo = address;
      // alert('Destination location selected!');
    });
});

// Current Location Map
let currentMap,
  currentMarker,
  currentLatLng = null;
const currentMapDiv = document.getElementById("currentMap");
const currentConfirmBtn = document.getElementById("confirm-current-btn");

document
  .getElementById("open-current-map-btn")
  .addEventListener("click", () => {
    currentMapDiv.style.display = "block";
    currentConfirmBtn.style.display = "inline-block";

    if (!currentMap) {
      currentMap = L.map("currentMap").setView([22.5937, 78.9629], 5);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "&copy; OpenStreetMap contributors",
      }).addTo(currentMap);

      currentMap.on("click", function (e) {
        currentLatLng = e.latlng;
        if (currentMarker) {
          currentMarker.setLatLng(currentLatLng);
        } else {
          currentMarker = L.marker(currentLatLng).addTo(currentMap);
        }
      });
    }
  });

currentConfirmBtn.addEventListener("click", () => {
  if (!currentLatLng)
    return alert("Please select current location on the map.");

  fetch(
    `https://nominatim.openstreetmap.org/reverse?format=json&lat=${currentLatLng.lat}&lon=${currentLatLng.lng}`
  )
    .then((res) => res.json())
    .then((data) => {
      const address = data.display_name;
      const pincode = data.address.postcode || "";
      document.getElementById("currentLocationUser").value = address;
      userAddressSelectedFrom = address;
      if (pincode) {
        console.log("Pin 1");
        document.getElementById("pincodeInput").value = pincode;
        console.log("Pin 2, Completed");
      }
      //   alert("Current location selected!");
    });
});

// Search current address manually
document
  .getElementById("search-current-location-btn")
  .addEventListener("click", () => {
    const address = document.getElementById("currentLocationUser").value.trim();
    if (!address) return alert("Please enter your current address.");

    fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(
        address
      )}`
    )
      .then((res) => res.json())
      .then((results) => {
        if (results && results.length > 0) {
          const { lat, lon } = results[0];
          currentMapDiv.style.display = "block";
          currentConfirmBtn.style.display = "inline-block";

          if (!currentMap) {
            currentMap = L.map("currentMap").setView([lat, lon], 15);
            L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
              attribution: "&copy; OpenStreetMap contributors",
            }).addTo(currentMap);

            currentMap.on("click", function (e) {
              currentLatLng = e.latlng;
              if (currentMarker) {
                currentMarker.setLatLng(currentLatLng);
              } else {
                currentMarker = L.marker(currentLatLng).addTo(currentMap);
              }
            });
          } else {
            currentMap.setView([lat, lon], 15);
            if (currentMarker) {
              currentMarker.setLatLng([lat, lon]);
            } else {
              currentMarker = L.marker([lat, lon]).addTo(currentMap);
            }
            currentLatLng = { lat, lng: lon };
          }
        } else {
          alert("Address not found.");
        }
      });
  });

// Search destination manually

document.getElementById("search-location-btn").addEventListener("click", () => {
  const address = document.getElementById("toLocationInput").value.trim();
  if (!address) return alert("Please enter your destination address.");

  fetch(
    `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(
      address
    )}`
  )
    .then((res) => res.json())
    .then((results) => {
      if (results && results.length > 0) {
        const { lat, lon } = results[0];
        destMapDiv.style.display = "block";
        destConfirmBtn.style.display = "inline-block";

        if (!destMap) {
          destMap = L.map("map").setView([lat, lon], 15);
          L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "&copy; OpenStreetMap contributors",
          }).addTo(destMap);

          destMap.on("click", function (e) {
            destLatLng = e.latlng;
            if (destMarker) {
              destMarker.setLatLng(destLatLng);
            } else {
              destMarker = L.marker(destLatLng).addTo(destMap);
            }
          });
        } else {
          destMap.setView([lat, lon], 15);
          if (destMarker) {
            destMarker.setLatLng([lat, lon]);
          } else {
            destMarker = L.marker([lat, lon]).addTo(destMap);
          }
          destLatLng = { lat, lng: lon };
        }
      } else {
        alert("Destination address not found.");
      }
    });
});

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();
  const form = e.target;

  const formValueFrom = document
    .getElementById("currentLocationUser")
    .value.trim();
  const formValueTo = document.getElementById("toLocationInput").value.trim();

  let resultSaveFrom = userAddressSelectedFrom
    .trim()
    .split(/\s+/)
    .map((w, i) => (i === 0 ? w.toLowerCase() : w))
    .join("");
  let resultSaveTo = userAddressSelectedTo
    .trim()
    .split(/\s+/)
    .map((w, i) => (i === 0 ? w.toLowerCase() : w))
    .join("");
  let resultFrom = formValueFrom
    .trim()
    .split(/\s+/)
    .map((w, i) => (i === 0 ? w.toLowerCase() : w))
    .join("");
  let resultTo = formValueTo
    .trim()
    .split(/\s+/)
    .map((w, i) => (i === 0 ? w.toLowerCase() : w))
    .join("");

  if (userAddressSelectedFrom === "") {
    alert(
      "you have filled but its not select inside map, please select from the map 'current location'"
    );
  } else {
    if (userAddressSelectedTo === "") {
      alert(
        "you have filled but its not select inside map, please select from the map 'last location'"
      );
    } else {
      if (resultSaveFrom === resultFrom) {
        if (resultSaveTo === resultTo) {
          //   console.log("SuccessFull");
          form.submit();
        } else {
          alert(
            "you have change address for 'current location!', now select on map"
          );
        }
      } else {
        alert(
          "you have change address for 'last location!', now select on map"
        );
      }
    }
  }
});
