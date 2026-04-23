import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Issue 1.1: Fix useEffect mapping
old_use_effect_mapping = """              return Object.entries(categories).flatMap(([type, places]) =>
                (places || []).map(p => ({
                  city: city.name,
                  name: p.name,
                  category: [type],
                  icon: p.icon || "📍",
                  description: p.short_description || "",
                  long_description: p.long_description || p.short_description || "",
                  famous_for: p.famous_for || [],
                  cost: 0,
                  location: p.location || "",
                }))
              );"""

new_use_effect_mapping = """              return Object.entries(categories).flatMap(([type, places]) =>
                (places || []).map(p => ({
                  city: city.name,
                  name: p.name,
                  category: p.tags || [type],
                  icon: p.icon || "📍",
                  description: p.short_description || "",
                  long_description: p.long_description || p.short_description || "",
                  famous_for: p.famous_for || [],
                  location: p.location || city.name + ", Maharashtra",
                  cost: 0,
                }))
              );"""
content = content.replace(old_use_effect_mapping, new_use_effect_mapping)

# Issue 1.2: Fix toCard in HomeHighlights
old_to_card = '      const toCard = p => ({ name: p.name, description: p.short_description, long_description: p.long_description || p.short_description || "", famous_for: p.famous_for || [], category: p.tags || [], cost: 0, icon: p.icon || "📍", location: p.location || "" });'
new_to_card = """      const toCard = p => ({
        name: p.name,
        description: p.short_description || "",
        long_description: p.long_description || p.short_description || "",
        famous_for: p.famous_for || [],
        category: p.tags || [],
        icon: p.icon || "📍",
        location: p.location || "Maharashtra",
        cost: 0,
        city: "Maharashtra"
      });"""
content = content.replace(old_to_card, new_to_card)

# Issue 2: Famous For section
old_famous_for = """            {place.famous_for && place.famous_for.length > 0 && (
              <div style={{ marginBottom: "30px" }}>
                <h3 style={{ color: "#1e3a5c", fontSize: "1.2rem", marginBottom: "12px" }}>Famous For</h3>
                <div style={{ display: "flex", flexWrap: "wrap" }}>
                  {place.famous_for.map((item, i) => (
                    <span key={i} style={{ background: "#f9b233", color: "white", borderRadius: "20px", padding: "4px 14px", fontWeight: "600", margin: "4px" }}>
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            )}"""
new_famous_for = """            {((place.famous_for && place.famous_for.length > 0) 
              ? place.famous_for 
              : place.category || []
            ).length > 0 && (
              <div style={{ marginBottom: "32px" }}>
                <h3 style={{
                  fontSize: "1.1rem", fontWeight: "800",
                  color: "#1e3a5c", marginBottom: "14px",
                  textTransform: "uppercase", letterSpacing: "1px",
                  display: "flex", alignItems: "center", gap: "8px"
                }}>
                  <span style={{
                    display: "inline-block", width: "4px", height: "18px",
                    background: "#f9b233", borderRadius: "2px"
                  }}/>
                  Famous For
                </h3>
                <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
                  {((place.famous_for && place.famous_for.length > 0) 
                    ? place.famous_for 
                    : place.category || []
                  ).map((item, i) => (
                    <span key={i} style={{
                      background: "linear-gradient(135deg, #f9b233, #e09e1b)",
                      color: "#fff",
                      borderRadius: "20px",
                      padding: "6px 18px",
                      fontWeight: "600",
                      fontSize: "0.88rem",
                      boxShadow: "0 2px 8px rgba(249,178,51,0.3)"
                    }}>{item}</span>
                  ))}
                </div>
              </div>
            )}"""
content = content.replace(old_famous_for, new_famous_for)

# Issue 3: About This Place & Location row
old_about = """            <div>
              <h3 style={{ color: "#1e3a5c", fontSize: "1.3rem", marginBottom: "12px" }}>About This Place</h3>
              <p style={{ color: "#444", lineHeight: "1.8", fontSize: "1rem" }}>
                {place.long_description}
              </p>
            </div>"""
new_about = """            <div>
              <h3 style={{ color: "#1e3a5c", fontSize: "1.3rem", marginBottom: "12px" }}>About This Place</h3>
              <p style={{
                color: "#444",
                fontSize: "1.05rem",
                lineHeight: "1.9",
                margin: 0
              }}>
                {place.long_description && 
                 place.long_description !== place.description
                  ? place.long_description
                  : place.description}
              </p>
            </div>"""
content = content.replace(old_about, new_about)

old_short_desc = """            <div style={{ fontSize: "1.15rem", color: "#555", lineHeight: "1.8", marginBottom: "30px" }}>
              {place.description}
            </div>"""
new_short_desc = """            {place.location && (
              <div style={{
                display: "flex", alignItems: "center", gap: "8px",
                marginBottom: "24px", color: "#888", fontSize: "0.95rem"
              }}>
                <i className="fa fa-map-pin" style={{ color: "#f9b233" }} />
                {place.location}
              </div>
            )}
            <div style={{ fontSize: "1.15rem", color: "#555", lineHeight: "1.8", marginBottom: "30px" }}>
              {place.description}
            </div>"""
content = content.replace(old_short_desc, new_short_desc)

# Issue 4: Navbar search navigation & Selected Place logic

# Find all occurrences of the old onPlaceClick handler passed to Navbar
old_navbar_click = 'onPlaceClick={(place) => { setSelectedPlace(place); setFromPage("home"); }}'
new_navbar_click = """onPlaceClick={(place) => {
              setSelectedPlace(place);
              setFromPage("home");
              window.scrollTo({ top: 0, behavior: "smooth" });
            }}"""
content = content.replace(old_navbar_click, new_navbar_click)

# Find and replace the if (selectedPlace) return (...)
old_selected_place_check = """      if (selectedPlace) return (
        <PlaceDetailPage place={selectedPlace} onBack={() => setSelectedPlace(null)} />
      );"""
new_selected_place_check = """      if (selectedPlace) return (
        <>
          <Navbar 
            onPlan={scrollToPlanner}
            placesData={placesData}
            onPlaceClick={(p) => { setSelectedPlace(p); window.scrollTo({ top: 0, behavior: "smooth" }); }}
            onCityClick={(city) => { setSelectedCity(city); setPage("details"); }}
          />
          <PlaceDetailPage
            place={selectedPlace}
            onBack={() => { setSelectedPlace(null); window.scrollTo({top:0}); }}
          />
          <Footer />
        </>
      );"""
content = content.replace(old_selected_place_check, new_selected_place_check)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates successful")
