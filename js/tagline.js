// Dynamic tagline generator
(function() {
  function getDateSpecificTagline() {
    const today = new Date();
    const month = today.getMonth() + 1; // JavaScript months are 0-indexed
    const day = today.getDate();
    
    if (month === 3 && day === 14) {
      return "Happy Pi Day!";
    } else if (month === 6 && day === 28) {
      return "Happy Tau Day!";
    }
    return null;
  }
  
  function getTagline() {
    // Check for date-specific taglines first
    const dateTagline = getDateSpecificTagline();
    if (dateTagline) {
      return dateTagline;
    }
    
    // Default taglines
    const taglines = [
      "An attempt at a blog by someone who thinks Haskell is cool.",
      "Contains 20% of your daily recommended dose of HTML.",
      "Now with automatic dark mode support!",
      "Functional programming enthusiast since the Mayan calendar ended.",
      "Proudly over-engineering simple solutions.",
      "Monads are just monoids in the category of endofunctors.",
      "Blogging at the speed of Jekyll.",
      "Powered by caffeine and recursion.",
      "No side effects, except for this tagline.",
      "Currying favor with functional programmers.",
      "This blog is referentially transparent.",
      "Warning: May contain traces of category theory.",
      "Immutable content since 2016."
    ];
    
    // Random selection that changes on each page load
    // If you want consistency per page, we can use URL-based selection
    const randomIndex = Math.floor(Math.random() * taglines.length);
    return taglines[randomIndex];
  }
  
  // Update tagline on page load
  document.addEventListener('DOMContentLoaded', function() {
    const taglineElement = document.getElementById('footer-text');
    if (taglineElement) {
      taglineElement.textContent = getTagline();
    }
  });
})();
