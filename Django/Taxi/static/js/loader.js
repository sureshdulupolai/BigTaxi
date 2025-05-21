window.addEventListener('load', function() {
  const loader = document.getElementById('custom-preloader');

  // Scroll disable while loading
  document.body.style.overflow = 'hidden';

  // Start blur fade-out animation
  loader.classList.add('blur-fadeout');

  // After 4s (animation duration), fade out loader and enable scroll
  setTimeout(() => {
    loader.style.opacity = '0';
    // Disable pointer events so page is clickable after fade out
    loader.style.pointerEvents = 'none';

    // Enable scrolling after fade out
    document.body.style.overflow = 'auto';

    // After opacity transition (0.5s), hide completely
    setTimeout(() => {
      loader.style.display = 'none';
    }, 300);
  }, 3000);
});
