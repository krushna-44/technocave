// --- Carousel Logic ---
let carouselIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
function showCarouselSlide(idx) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === idx);
  });
}
function carouselNext() {
  carouselIndex = (carouselIndex + 1) % slides.length;
  showCarouselSlide(carouselIndex);
}
function carouselPrev() {
  carouselIndex = (carouselIndex - 1 + slides.length) % slides.length;
  showCarouselSlide(carouselIndex);
}
// Auto-slide every 4.5s
setInterval(() => {
  carouselNext();
}, 4500);
// Allow navigation by arrow keys
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowLeft') carouselPrev();
  if (e.key === 'ArrowRight') carouselNext();
});
// On load, ensure first slide is active
showCarouselSlide(carouselIndex);

// app.js - Maharashtra Tourism Planner

// Sample dataset for tourist places in Maharashtra
const placesData = [
  {
    city: "Mumbai",
    name: "Gateway of India",
    category: ["Historical", "Entertainment"],
    image: "images/mumbai.jpg",
    description: "Iconic arch-monument and a must-visit landmark by the Arabian Sea.",
    cost: 0
  },
  {
    city: "Mumbai",
    name: "Marine Drive",
    category: ["Nature", "Entertainment"],
    image: "images/marine_drive.jpg",
    description: "Scenic promenade, perfect for evening walks and sunset views.",
    cost: 0
  },
  {
    city: "Mumbai",
    name: "Elephanta Caves",
    category: ["Historical", "Adventure"],
    image: "images/elephanta.jpg",
    description: "UNESCO World Heritage site with ancient rock-cut temples.",
    cost: 200
  },
  {
    city: "Pune",
    name: "Shaniwar Wada",
    category: ["Historical"],
    image: "images/shaniwarwada.jpg",
    description: "18th-century fortification and palace in Pune.",
    cost: 50
  },
  {
    city: "Pune",
    name: "Sinhagad Fort",
    category: ["Historical", "Adventure", "Nature"],
    image: "images/sinhagad.jpg",
    description: "Hill fortress with panoramic views and trekking opportunities.",
    cost: 30
  },
  {
    city: "Aurangabad",
    name: "Ajanta Caves",
    category: ["Historical", "Religious"],
    image: "images/ajanta.jpg",
    description: "Ancient Buddhist caves with exquisite paintings and sculptures.",
    cost: 40
  },
  {
    city: "Aurangabad",
    name: "Ellora Caves",
    category: ["Historical", "Religious"],
    image: "images/ellora.jpg",
    description: "Rock-cut temples representing Buddhist, Hindu, and Jain faiths.",
    cost: 40
  },
  {
    city: "Nashik",
    name: "Trimbakeshwar Temple",
    category: ["Religious"],
    image: "images/trimbak.jpg",
    description: "One of the twelve Jyotirlingas, a sacred Hindu temple.",
    cost: 0
  },
  {
    city: "Lonavala",
    name: "Tiger Point",
    category: ["Nature", "Adventure"],
    image: "images/tiger_point.jpg",
    description: "Popular viewpoint with stunning valley views and misty weather.",
    cost: 0
  },
  {
    city: "Lonavala",
    name: "Bhushi Dam",
    category: ["Nature", "Entertainment"],
    image: "images/bhushi_dam.jpg",
    description: "Famous dam and picnic spot, especially during monsoon.",
    cost: 0
  },
  {
    city: "Mahabaleshwar",
    name: "Mapro Garden",
    category: ["Nature", "Entertainment"],
    image: "images/mapro.jpg",
    description: "Strawberry farm, food court, and scenic garden.",
    cost: 0
  },
  {
    city: "Mahabaleshwar",
    name: "Arthur Seat",
    category: ["Nature", "Adventure"],
    image: "images/arthur_seat.jpg",
    description: "Famous viewpoint with breathtaking valley views.",
    cost: 0
  },
  {
    city: "Alibaug",
    name: "Alibaug Beach",
    category: ["Beaches", "Nature", "Adventure"],
    image: "images/alibaug.jpg",
    description: "Clean sandy beach, water sports, and sunset views.",
    cost: 0
  },
  {
    city: "Kolhapur",
    name: "Mahalaxmi Temple",
    category: ["Religious"],
    image: "images/mahalaxmi.jpg",
    description: "Ancient temple dedicated to Goddess Mahalaxmi.",
    cost: 0
  },
  {
    city: "Nagpur",
    name: "Ambazari Lake",
    category: ["Nature", "Entertainment"],
    image: "images/ambazari.jpg",
    description: "Largest lake in Nagpur, boating and gardens.",
    cost: 0
  }
];

// Budget cost mapping (per day, per person)
const budgetMap = {
  Low: 800,
  Medium: 2000,
  High: 4000
};

// Helper: Scroll to planner section
function scrollToPlanner() {
  document.getElementById('trip-planner').scrollIntoView({ behavior: 'smooth' });
}

// Handle form submission
const form = document.getElementById('planner-form');
form.addEventListener('submit', function(e) {
  e.preventDefault();
  const city = document.getElementById('city').value;
  const days = parseInt(document.getElementById('days').value);
  const budget = document.getElementById('budget').value;
  const categories = Array.from(form.querySelectorAll('.checkbox-group input:checked')).map(cb => cb.value);
  showRecommendations(city, categories, days, budget);
});

// Main recommendation logic
function showRecommendations(city, categories, days, budget) {
  // Filter places by city and categories
  let filtered = placesData.filter(p => p.city === city && (categories.length === 0 || p.category.some(cat => categories.includes(cat))));
  // If no category selected, show all for city
  if (filtered.length === 0) filtered = placesData.filter(p => p.city === city);

  // Group by category for display
  const byCategory = {};
  filtered.forEach(place => {
    place.category.forEach(cat => {
      if (!byCategory[cat]) byCategory[cat] = [];
      byCategory[cat].push(place);
    });
  });

  // Generate itinerary (simple: spread places over days)
  const itinerary = [];
  for (let d = 0; d < days; d++) {
    itinerary.push([]);
  }
  filtered.forEach((place, i) => {
    itinerary[i % days].push(place);
  });

  // Cost estimation
  const approxCost = budgetMap[budget] * days;

  // Budget tips
  const tips = {
    Low: [
      "Use local trains/buses for transport.",
      "Try street food and budget eateries.",
      "Look for hostels or budget hotels."
    ],
    Medium: [
      "Book 3-star hotels in advance.",
      "Use app-based cabs for convenience.",
      "Try local restaurants and guided tours."
    ],
    High: [
      "Opt for premium hotels and resorts.",
      "Hire private cabs for sightseeing.",
      "Enjoy fine dining and exclusive experiences."
    ]
  };

  // Render recommendations
  const recDiv = document.getElementById('recommendations');
  recDiv.innerHTML = `
    <div class="recommendation-header">
      <h2>Recommended Places in ${city}</h2>
      <p>Categories: ${categories.length ? categories.join(', ') : 'All'}</p>
    </div>
    <div class="cards">
      ${filtered.map(place => `
        <div class="card">
          <img src="${place.image}" alt="${place.name}">
          <div class="card-content">
            <span class="category">${place.category.join(', ')}</span>
            <h3>${place.name}</h3>
            <p>${place.description}</p>
          </div>
        </div>
      `).join('')}
    </div>
    <div class="itinerary">
      <h3>Day-wise Itinerary</h3>
      ${itinerary.map((day, i) => `
        <div class="itinerary-day">
          <strong>Day ${i+1}:</strong> ${day.length ? day.map(p => p.name).join(', ') : 'Rest/Leisure'}
        </div>
      `).join('')}
    </div>
    <div class="budget-tips">
      <strong>Budget Tips:</strong>
      <ul>${tips[budget].map(t => `<li>${t}</li>`).join('')}</ul>
    </div>
    <div class="cost-estimate">
      Approximate Cost: ₹${approxCost.toLocaleString()} (for ${days} day${days>1?'s':''}, per person)
    </div>
  `;
  recDiv.scrollIntoView({ behavior: 'smooth' });
}

// Optionally, preload images for smoother UX
["mumbai.jpg","ajanta.jpg","mahabaleshwar.jpg","alibaug.jpg","marine_drive.jpg","elephanta.jpg","shaniwarwada.jpg","sinhagad.jpg","ellora.jpg","trimbak.jpg","tiger_point.jpg","bhushi_dam.jpg","mapro.jpg","arthur_seat.jpg","mahalaxmi.jpg","ambazari.jpg"].forEach(img => {
  const i = new Image();
  i.src = `images/${img}`;
});
