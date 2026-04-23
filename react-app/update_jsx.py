import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. CSS border-radius updates
content = content.replace("border-radius: 25px", "border-radius: 8px")
# In Carousel:
content = content.replace('borderRadius: "30px"', 'borderRadius: "8px"')

# Keyframes
keyframes = """
    @keyframes fadeSlideUp {
      from { opacity: 0; transform: translateY(40px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>"""
content = content.replace("</style>", keyframes)

# 2. Navbar update
old_navbar = """    // ── Navbar ────────────────────────────────────────────────────────────────
    function Navbar({ onPlan }) {
      const [open, setOpen] = useState(false);
      return (
        <nav>
          <div className="logo"><i className="fa fa-map-location-dot" /> RoamGenie</div>
          <div className="nav-right">
            <div className="nav-search">
              <i className="fa fa-magnifying-glass" />
              <input type="text" placeholder="Search places..." />
            </div>
            <button className="plan-btn" onClick={onPlan}><i className="fa fa-route" /> Plan Your Trip</button>
            <button className="nav-icon-btn" title="Email us at roamgenie@gmail.com" onClick={() => window.open("mailto:roamgenie@gmail.com?subject=Inquiry - Maharashtra Tourism", "_blank")}>
              <i className="fa fa-envelope" />
            </button>
            <button className="nav-icon-btn" title="Follow us on Instagram" onClick={() => window.open("https://www.instagram.com/roamgenie/", "_blank")}>
              <i className="fab fa-instagram" />
            </button>
            <div className="dots-wrap">
              <button className="nav-icon-btn" onClick={() => setOpen(o => !o)}>
                <i className="fa fa-ellipsis-vertical" />
              </button>
              {open && (
                <div className="dropdown">
                  <a href="#" onClick={() => setOpen(false)}>About</a>
                  <a href="#" onClick={() => setOpen(false)}>Contact</a>
                  <a href="#" onClick={() => setOpen(false)}>Help</a>
                </div>
              )}
            </div>
          </div>
        </nav>
      );
    }"""

new_navbar = """    // ── Navbar ────────────────────────────────────────────────────────────────
    function Navbar({ onPlan, placesData = [], onPlaceClick, onCityClick }) {
      const [open, setOpen] = useState(false);
      const [query, setQuery] = useState("");
      const [searchResults, setSearchResults] = useState([]);
      const [showResults, setShowResults] = useState(false);

      return (
        <nav>
          <div className="logo"><i className="fa fa-map-location-dot" /> RoamGenie</div>
          <div className="nav-right">
            <div style={{ position: "relative" }}>
              <div className="nav-search">
                <i className="fa fa-magnifying-glass" />
                <input type="text" placeholder="Search places..." value={query}
                  onChange={e => {
                    const val = e.target.value;
                    setQuery(val);
                    if (val.trim().length > 1) {
                      const results = placesData.filter(p =>
                        p.name.toLowerCase().includes(val.toLowerCase()) ||
                        p.city.toLowerCase().includes(val.toLowerCase()) ||
                        (p.description || "").toLowerCase().includes(val.toLowerCase())
                      ).slice(0, 6);
                      setSearchResults(results);
                      setShowResults(true);
                    } else {
                      setShowResults(false);
                      setSearchResults([]);
                    }
                  }}
                  onFocus={() => query.length > 1 && setShowResults(true)}
                  onBlur={() => setTimeout(() => setShowResults(false), 200)}
                />
              </div>
              {showResults && searchResults.length > 0 && (
                <div style={{
                  position: "absolute",
                  top: "calc(100% + 8px)",
                  left: 0,
                  right: 0,
                  background: "#fff",
                  borderRadius: "12px",
                  boxShadow: "0 8px 32px rgba(30,58,92,0.18)",
                  zIndex: 300,
                  overflow: "hidden",
                  minWidth: "280px"
                }}>
                  {searchResults.map((place, i) => (
                    <div key={i}
                      style={{
                        padding: "12px 16px",
                        cursor: "pointer",
                        borderBottom: "1px solid #f0f0f0",
                        display: "flex",
                        alignItems: "center",
                        gap: "12px",
                        transition: "background 0.15s"
                      }}
                      onMouseEnter={e => e.currentTarget.style.background = "#f8f9fc"}
                      onMouseLeave={e => e.currentTarget.style.background = "#fff"}
                      onClick={() => {
                        onPlaceClick(place);
                        setQuery("");
                        setShowResults(false);
                      }}>
                      <span style={{ fontSize: "1.4rem" }}>{place.icon || "📍"}</span>
                      <div>
                        <div style={{
                          fontWeight: "700", fontSize: "0.95rem", color: "#1e3a5c"
                        }}>{place.name}</div>
                        <div style={{
                          fontSize: "0.8rem", color: "#888"
                        }}>{place.city} · {place.category?.[0]}</div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <button className="plan-btn" onClick={onPlan}><i className="fa fa-route" /> Plan Your Trip</button>
            <button className="nav-icon-btn" title="Email us at roamgenie@gmail.com" onClick={() => window.open("mailto:roamgenie@gmail.com?subject=Inquiry - Maharashtra Tourism", "_blank")}>
              <i className="fa fa-envelope" />
            </button>
            <button className="nav-icon-btn" title="Follow us on Instagram" onClick={() => window.open("https://www.instagram.com/roamgenie/", "_blank")}>
              <i className="fab fa-instagram" />
            </button>
            <div className="dots-wrap">
              <button className="nav-icon-btn" onClick={() => setOpen(o => !o)}>
                <i className="fa fa-ellipsis-vertical" />
              </button>
              {open && (
                <div className="dropdown">
                  <a href="#" onClick={() => setOpen(false)}>About</a>
                  <a href="#" onClick={() => setOpen(false)}>Contact</a>
                  <a href="#" onClick={() => setOpen(false)}>Help</a>
                </div>
              )}
            </div>
          </div>
        </nav>
      );
    }"""
content = content.replace(old_navbar, new_navbar)

# 3. Add WhyUs, OurTeam, Gallery right before "function App() {"
new_components = """
    // ── Why Us ────────────────────────────────────────────────────────────────
    function WhyUs() {
      const reasons = [
        { icon: "🗺️", title: "Expert Local Guides", desc: "Our guides know every hidden gem and local secret across all of Maharashtra's diverse regions." },
        { icon: "💰", title: "Best Price Guarantee", desc: "We offer the most competitive prices with no hidden charges and flexible budget options." },
        { icon: "🛡️", title: "Safe & Trusted", desc: "Thousands of happy travelers trust us for safe, well-planned, and memorable journeys." },
        { icon: "⚡", title: "Instant Planning", desc: "Get a complete personalized itinerary in seconds using our smart trip planning tool." },
        { icon: "🌟", title: "Curated Experiences", desc: "Every destination is handpicked and verified for quality, authenticity, and uniqueness." },
        { icon: "📞", title: "24/7 Support", desc: "Our dedicated support team is always available to assist you before, during, and after your trip." }
      ];

      return (
        <section style={{
          padding: "90px 8vw",
          background: "linear-gradient(135deg, #0f1e32 60%, #1e3a5c 100%)",
          color: "#fff"
        }}>
          <div style={{ textAlign: "center", marginBottom: "60px" }}>
            <p style={{
              color: "#f9b233", fontWeight: "700", fontSize: "0.9rem",
              letterSpacing: "3px", textTransform: "uppercase", marginBottom: "14px"
            }}>WHY CHOOSE US</p>
            <h2 style={{
              fontSize: "2.6rem", fontWeight: "900", margin: "0 0 16px",
              lineHeight: 1.2
            }}>Travel Smarter with <span style={{ color: "#f9b233" }}>RoamGenie</span></h2>
            <div style={{
              width: "60px", height: "4px",
              background: "linear-gradient(90deg, #f9b233, transparent)",
              borderRadius: "2px", margin: "0 auto"
            }} />
          </div>
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
            gap: "28px",
            maxWidth: "1100px",
            margin: "0 auto"
          }}>
            {reasons.map((r, i) => (
              <div key={i} style={{
                background: "rgba(255,255,255,0.05)",
                border: "1px solid rgba(249,178,51,0.15)",
                borderRadius: "16px",
                padding: "32px 28px",
                transition: "transform 0.25s, background 0.25s, border 0.25s",
                cursor: "default"
              }}
              onMouseEnter={e => {
                e.currentTarget.style.transform = "translateY(-8px)";
                e.currentTarget.style.background = "rgba(249,178,51,0.1)";
                e.currentTarget.style.border = "1px solid rgba(249,178,51,0.4)";
              }}
              onMouseLeave={e => {
                e.currentTarget.style.transform = "translateY(0)";
                e.currentTarget.style.background = "rgba(255,255,255,0.05)";
                e.currentTarget.style.border = "1px solid rgba(249,178,51,0.15)";
              }}>
                <div style={{ fontSize: "2.8rem", marginBottom: "16px" }}>{r.icon}</div>
                <h3 style={{
                  fontSize: "1.15rem", fontWeight: "700",
                  color: "#f9b233", margin: "0 0 10px"
                }}>{r.title}</h3>
                <p style={{
                  color: "rgba(255,255,255,0.7)", fontSize: "0.95rem",
                  lineHeight: "1.7", margin: 0
                }}>{r.desc}</p>
              </div>
            ))}
          </div>
        </section>
      );
    }

    // ── Our Team ──────────────────────────────────────────────────────────────
    function OurTeam() {
      const team = [
        { name: "Ansari Muhammad Saud", role: "Founder & Travel Expert", emoji: "👨💼", color: "#1e3a5c" },
        { name: "Om Suryakant Jadhav", role: "UI/UX Designer", emoji: "🎨", color: "#7b1fa2" },
        { name: "Krushna Rakesh Bhavsar", role: "Backend Developer", emoji: "💻", color: "#1565c0" },
        { name: "Tanmay Pravin Chinchore", role: "Content & Research Lead", emoji: "📝", color: "#2e7d32" }
      ];

      return (
        <section style={{
          padding: "90px 8vw",
          background: "#f8f9fc",
          textAlign: "center"
        }}>
          <p style={{
            color: "#f9b233", fontWeight: "700", fontSize: "0.9rem",
            letterSpacing: "3px", textTransform: "uppercase", marginBottom: "14px"
          }}>THE PEOPLE BEHIND IT</p>
          <h2 style={{
            fontSize: "2.6rem", fontWeight: "900", color: "#1e3a5c",
            margin: "0 0 16px"
          }}>Meet Our Team</h2>
          <div style={{
            width: "60px", height: "4px",
            background: "linear-gradient(90deg, #1e3a5c, #f9b233)",
            borderRadius: "2px", margin: "0 auto 60px"
          }} />
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
            gap: "32px",
            maxWidth: "1000px",
            margin: "0 auto"
          }}>
            {team.map((m, i) => (
              <div key={i} style={{
                background: "#fff",
                borderRadius: "20px",
                padding: "40px 24px 32px",
                boxShadow: "0 4px 24px rgba(30,58,92,0.10)",
                animation: `fadeSlideUp 0.6s ease ${i * 0.15}s both`,
                transition: "transform 0.25s, box-shadow 0.25s"
              }}
              onMouseEnter={e => {
                e.currentTarget.style.transform = "translateY(-10px)";
                e.currentTarget.style.boxShadow = "0 16px 40px rgba(30,58,92,0.18)";
              }}
              onMouseLeave={e => {
                e.currentTarget.style.transform = "translateY(0)";
                e.currentTarget.style.boxShadow = "0 4px 24px rgba(30,58,92,0.10)";
              }}>
                <div style={{
                  width: "90px", height: "90px",
                  borderRadius: "50%",
                  background: `linear-gradient(135deg, ${m.color}, #f9b233)`,
                  display: "flex", alignItems: "center", justifyContent: "center",
                  fontSize: "2.4rem",
                  margin: "0 auto 20px",
                  boxShadow: `0 8px 24px ${m.color}44`
                }}>{m.emoji}</div>
                <h3 style={{
                  fontSize: "1.05rem", fontWeight: "800",
                  color: "#1e3a5c", margin: "0 0 8px", lineHeight: 1.3
                }}>{m.name}</h3>
                <p style={{
                  color: "#f9b233", fontWeight: "600",
                  fontSize: "0.85rem", margin: 0,
                  textTransform: "uppercase", letterSpacing: "1px"
                }}>{m.role}</p>
              </div>
            ))}
          </div>
        </section>
      );
    }

    // ── Gallery ───────────────────────────────────────────────────────────────
    function Gallery() {
      const items = [
        { emoji: "🏛️", label: "Gateway of India", color: "#1e3a5c" },
        { emoji: "🌊", label: "Marine Drive", color: "#01579b" },
        { emoji: "🛕", label: "Trimbakeshwar", color: "#880e4f" },
        { emoji: "⛰️", label: "Kalsubai Peak", color: "#2e7d32" },
        { emoji: "🍇", label: "Sula Vineyards", color: "#6a1b9a" },
        { emoji: "🏖️", label: "Tarkarli Beach", color: "#004d40" },
        { emoji: "🦁", label: "Sanjay Gandhi Park", color: "#e65100" },
        { emoji: "🏰", label: "Raigad Fort", color: "#37474f" },
        { emoji: "🌸", label: "Kaas Plateau", color: "#ad1457" }
      ];

      return (
        <section style={{ padding: "90px 8vw", background: "#fff" }}>
          <div style={{ textAlign: "center", marginBottom: "50px" }}>
            <p style={{
              color: "#f9b233", fontWeight: "700", fontSize: "0.9rem",
              letterSpacing: "3px", textTransform: "uppercase", marginBottom: "14px"
            }}>EXPLORE MAHARASHTRA</p>
            <h2 style={{
              fontSize: "2.6rem", fontWeight: "900",
              color: "#1e3a5c", margin: "0 0 16px"
            }}>Our Gallery</h2>
            <div style={{
              width: "60px", height: "4px",
              background: "linear-gradient(90deg, #f9b233, #1e3a5c)",
              borderRadius: "2px", margin: "0 auto"
            }} />
          </div>
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gridTemplateRows: "auto",
            gap: "16px",
            maxWidth: "1100px",
            margin: "0 auto"
          }}>
            {items.map((item, i) => (
              <div key={i} style={{
                background: `linear-gradient(135deg, ${item.color}, ${item.color}99)`,
                borderRadius: "16px",
                height: i === 0 || i === 4 ? "280px" : "200px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                cursor: "pointer",
                transition: "transform 0.25s, box-shadow 0.25s",
                boxShadow: "0 4px 20px rgba(0,0,0,0.12)",
                gridColumn: i === 0 ? "span 2" : i === 4 ? "span 2" : "span 1"
              }}
              onMouseEnter={e => {
                e.currentTarget.style.transform = "scale(1.03)";
                e.currentTarget.style.boxShadow = "0 12px 36px rgba(0,0,0,0.22)";
              }}
              onMouseLeave={e => {
                e.currentTarget.style.transform = "scale(1)";
                e.currentTarget.style.boxShadow = "0 4px 20px rgba(0,0,0,0.12)";
              }}>
                <div style={{ fontSize: "3.5rem", marginBottom: "12px" }}>{item.emoji}</div>
                <div style={{
                  color: "#fff", fontWeight: "700", fontSize: "1rem",
                  textShadow: "0 2px 8px rgba(0,0,0,0.3)", letterSpacing: "0.5px"
                }}>{item.label}</div>
              </div>
            ))}
          </div>
        </section>
      );
    }

    function App() {"""

content = content.replace("    function App() {", new_components)

# 4. Navbar calls in App

navbar_home_old = '<Navbar onPlan={scrollToPlanner} />'
navbar_home_new = """<Navbar 
            onPlan={scrollToPlanner} 
            placesData={placesData}
            onPlaceClick={(place) => { setSelectedPlace(place); setFromPage("home"); }}
            onCityClick={(city) => { setSelectedCity(city); setPage("details"); }}
          />"""
content = content.replace(navbar_home_old, navbar_home_new)

navbar_cities_old = '<Navbar onPlan={() => { setPage("home"); setTimeout(scrollToPlanner, 100); }} />'
navbar_cities_new = """<Navbar 
            onPlan={() => { setPage("home"); setTimeout(scrollToPlanner, 100); }}
            placesData={placesData}
            onPlaceClick={(place) => { setSelectedPlace(place); setFromPage("home"); }}
            onCityClick={(city) => { setSelectedCity(city); setPage("details"); }}
          />"""
content = content.replace(navbar_cities_old, navbar_cities_new)

# 5. Adding WhyUs, OurTeam, Gallery to App Main
main_old = """          <main>
            <Intro />
            <HomeHighlights data={jsonData} onPlaceClick={setSelectedPlace} />
            <TripPlanner plannerRef={plannerRef} onResults={handleResults} placesData={placesData} />"""
main_new = """          <main>
            <Intro />
            <HomeHighlights data={jsonData} onPlaceClick={setSelectedPlace} />
            <WhyUs />
            <OurTeam />
            <Gallery />
            <TripPlanner plannerRef={plannerRef} onResults={handleResults} placesData={placesData} />"""
content = content.replace(main_old, main_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
