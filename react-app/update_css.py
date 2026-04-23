import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update --bg
content = content.replace('--bg: #f8fafc;', '--bg: #f8f9fc;')

# 2. Navbar Redesign CSS
nav_old = """    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 6vw;
      height: 68px;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 8px rgba(0,0,0,0.06);
    }
    .logo {
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-blue);
      letter-spacing: 1px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .logo i { color: var(--accent); font-size: 1.4rem; }
    .nav-right {
      display: flex;
      align-items: center;
      gap: 8px;
      position: relative;
    }
    .nav-search {
      display: flex;
      align-items: center;
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 7px 14px;
      gap: 8px;
      margin-right: 8px;
    }
    .nav-search input {
      background: none;
      border: none;
      outline: none;
      color: var(--text);
      font-family: var(--font);
      font-size: 0.88rem;
      width: 180px;
    }
    .nav-search input::placeholder { color: var(--muted); }
    .nav-search i { color: var(--muted); font-size: 0.9rem; }
    .plan-btn {
      background: var(--primary-blue);
      color: #fff;
      border: none;
      border-radius: 8px;
      padding: 9px 20px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      letter-spacing: 0.3px;
      transition: background 0.2s, transform 0.15s;
      white-space: nowrap;
      font-family: var(--font);
    }
    .plan-btn:hover {
      background: #1447c0;
      transform: translateY(-1px);
    }"""
nav_new = """    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 6vw;
      height: 70px;
      background: rgba(15, 30, 50, 0.92);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 20px rgba(0,0,0,0.3);
      border-bottom: 1px solid rgba(249,178,51,0.15);
    }
    .logo {
      font-size: 1.4rem;
      font-weight: 800;
      color: #fff;
      letter-spacing: 3px;
      display: flex;
      align-items: center;
      gap: 10px;
      text-transform: uppercase;
    }
    .logo i { color: #f9b233; font-size: 1.3rem; }
    .nav-right {
      display: flex;
      align-items: center;
      gap: 8px;
      position: relative;
    }
    .nav-search {
      display: flex;
      align-items: center;
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 7px 14px;
      gap: 8px;
      margin-right: 8px;
    }
    .nav-search input {
      background: none;
      border: none;
      outline: none;
      color: var(--text);
      font-family: var(--font);
      font-size: 0.88rem;
      width: 180px;
    }
    .nav-search input::placeholder { color: var(--muted); }
    .nav-search i { color: var(--muted); font-size: 0.9rem; }
    .plan-btn {
      background: linear-gradient(135deg, #f9b233, #e09e1b);
      color: #fff;
      border: none;
      border-radius: 25px;
      padding: 10px 26px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      letter-spacing: 0.5px;
      box-shadow: 0 4px 15px rgba(249,178,51,0.4);
      transition: background 0.2s, transform 0.15s;
      white-space: nowrap;
      font-family: var(--font);
    }
    .plan-btn:hover {
      transform: translateY(-1px);
    }"""
content = content.replace(nav_old, nav_new)

# 3. Carousel Hero CSS
carousel_old = """    .carousel-wrap {
      position: relative;
      width: 100%;
      height: 520px;
      overflow: hidden;
      background: #0f172a;
    }
    .carousel-slide {
      position: absolute;
      inset: 0;
      opacity: 0;
      transition: opacity 0.9s cubic-bezier(.4,0,.2,1);
    }
    .carousel-slide.active { opacity: 1; z-index: 2; }
    .carousel-slide img {
      width: 100%;
      height: 520px;
      object-fit: cover;
      filter: brightness(0.55) saturate(1.2);
      display: block;
    }
    .carousel-caption {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: 0 8vw;
      background: linear-gradient(90deg, rgba(0,0,0,0.65) 0%, transparent 100%);
    }
    .carousel-caption h1 {
      font-size: 3rem;
      margin: 0 0 12px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.5px;
      text-shadow: 0 2px 20px rgba(0,0,0,0.4);
      max-width: 600px;
    }
    .carousel-caption p {
      font-size: 1.1rem;
      margin: 0 0 28px;
      color: rgba(255,255,255,0.85);
      max-width: 480px;
    }"""
carousel_new = """    .carousel-wrap {
      position: relative;
      width: 100%;
      height: 100vh;
      min-height: 600px;
      overflow: hidden;
      background: #0f172a;
    }
    .carousel-slide {
      position: absolute;
      inset: 0;
      opacity: 0;
      transition: opacity 0.9s cubic-bezier(.4,0,.2,1);
    }
    .carousel-slide.active { opacity: 1; z-index: 2; }
    .carousel-slide img {
      width: 100%;
      height: 100vh;
      min-height: 600px;
      object-fit: cover;
      filter: brightness(0.5) saturate(1.2);
      display: block;
    }
    .carousel-caption {
      position: absolute;
      left: 8vw;
      bottom: 140px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: 0;
      background: transparent;
      backdrop-filter: none;
      border-radius: 0;
    }
    .carousel-caption h1 {
      font-size: 3.5rem;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 4px 20px rgba(0,0,0,0.5);
      letter-spacing: 2px;
      margin-bottom: 12px;
      max-width: 600px;
    }
    .carousel-caption p {
      font-size: 1.2rem;
      color: rgba(255,255,255,0.85);
      text-shadow: 0 2px 10px rgba(0,0,0,0.4);
      margin: 0 0 28px;
      max-width: 480px;
    }"""
content = content.replace(carousel_old, carousel_new)

# 4. Intro CSS
intro_old = """    .intro {
      text-align: center;
      padding: 64px 8vw 32px;
      background: #ffffff;
    }
    .intro h2 {
      font-size: 2rem;
      margin-bottom: 14px;
      color: var(--text);
      font-weight: 800;
      letter-spacing: -0.3px;
    }
    .intro p {
      color: var(--muted);
      font-size: 1rem;
      max-width: 640px;
      margin: 0 auto 10px;
      line-height: 1.75;
    }"""
intro_new = """    .intro {
      text-align: center;
      padding: 80px 8vw 40px;
      background: #fff;
    }
    .intro h2 {
      font-size: 2.6rem;
      color: #1e3a5c;
      font-weight: 800;
      margin-bottom: 16px;
      position: relative;
      display: inline-block;
    }
    .intro p {
      color: #555;
      font-size: 1.1rem;
      max-width: 680px;
      margin: 0 auto;
      line-height: 1.9;
    }"""
content = content.replace(intro_old, intro_new)

# 6. Place Cards CSS
card_old = """    .card {
      background: var(--card-bg);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, box-shadow 0.2s;
      cursor: pointer;
    }
    .card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-hover);
      border-color: #c7d7f5;
    }
    .card-img-placeholder {
      width: 100%;
      height: 160px;
      background: linear-gradient(135deg, #dbeafe, #ede9fe);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.8rem;
    }
    .card img {
      width: 100%;
      height: 180px;
      object-fit: cover;
      background: #eee;
    }
    .card-content { padding: 18px; flex: 1; }
    .card-content h3 {
      margin: 0 0 6px;
      font-size: 1.05rem;
      color: var(--text);
      font-weight: 700;
    }
    .card-content p {
      color: var(--muted);
      font-size: 0.88rem;
      margin: 0 0 14px;
      line-height: 1.6;
    }
    .tag {
      display: inline-block;
      background: #dbeafe;
      color: var(--primary-blue);
      border-radius: 6px;
      font-size: 0.75rem;
      padding: 3px 10px;
      margin: 2px 3px 2px 0;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
    }
    .cost-tag {
      background: #dcfce7;
      color: #15803d;
      border-radius: 6px;
      font-size: 0.78rem;
      padding: 3px 10px;
      font-weight: 700;
    }"""
card_new = """    .card {
      background: #fff;
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(30,58,92,0.08);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.25s, box-shadow 0.25s;
      cursor: pointer;
    }
    .card:hover {
      transform: translateY(-10px);
      box-shadow: 0 16px 40px rgba(30,58,92,0.18);
    }
    .card-img-placeholder {
      width: 100%;
      height: 200px;
      background: linear-gradient(135deg, #1e3a5c15, #f9b23325);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 4rem;
    }
    .card img {
      width: 100%;
      height: 180px;
      object-fit: cover;
      background: #eee;
    }
    .card-content { padding: 18px; flex: 1; }
    .card-content h3 {
      margin: 0 0 8px;
      font-size: 1.1rem;
      color: #1e3a5c;
      font-weight: 700;
    }
    .card-content p {
      color: var(--muted);
      font-size: 0.88rem;
      margin: 0 0 14px;
      line-height: 1.6;
    }
    .tag {
      display: inline-block;
      background: linear-gradient(135deg, #f9b233, #e09e1b);
      color: white;
      border-radius: 20px;
      font-size: 0.78rem;
      padding: 3px 12px;
      margin: 2px 3px 2px 0;
      font-weight: 600;
    }
    .cost-tag {
      background: #dcfce7;
      color: #15803d;
      border-radius: 6px;
      font-size: 0.78rem;
      padding: 3px 10px;
      font-weight: 700;
    }"""
content = content.replace(card_old, card_new)

# 7. Section Headings CSS
header_old = """    .rec-header h2 {
      font-size: 1.8rem;
      color: var(--text);
      margin-bottom: 8px;
      font-weight: 800;
    }"""
header_new = """    .rec-header h2 {
      font-size: 2.2rem;
      color: #1e3a5c;
      margin-bottom: 8px;
      font-weight: 800;
      position: relative;
    }"""
content = content.replace(header_old, header_new)

# 8. Footer CSS
footer_old = """    footer {
      background: #0f172a;
      color: #94a3b8;
      text-align: center;
      padding: 40px 0 24px;
    }
    footer .footer-links {
      display: flex;
      justify-content: center;
      gap: 32px;
      margin-bottom: 20px;
    }
    footer .footer-links a {
      color: #cbd5e1;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s;
    }
    footer .footer-links a:hover { color: var(--accent); }
    footer p {
      margin: 4px 0;
      font-size: 0.88rem;
    }"""
footer_new = """    footer {
      background: linear-gradient(135deg, #0f1e32, #1e3a5c);
      color: #94a3b8;
      text-align: center;
      padding: 48px 8vw 24px;
    }
    footer .footer-links {
      display: flex;
      justify-content: center;
      gap: 32px;
      margin-bottom: 20px;
    }
    footer .footer-links a {
      color: #f9b233;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s;
    }
    footer .footer-links a:hover { color: #fff; }
    footer p {
      margin: 4px 0;
      font-size: 0.88rem;
    }"""
content = content.replace(footer_old, footer_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
