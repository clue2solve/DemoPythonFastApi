from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


WELCOME_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>You shipped on Clue2App!</title>
  <style>
    :root {
      --c1: #EA580C;
      --c2: #F97316;
      --c3: #FB923C;
      --ink: #1f2937;
      --ink-soft: #4b5563;
      --muted: #6b7280;
      --bg: #fff7ed;
      --card: #ffffff;
      --line: rgba(234, 88, 12, 0.12);
      --shadow: 0 10px 30px rgba(234, 88, 12, 0.08), 0 2px 6px rgba(17, 24, 39, 0.04);
    }
    * { box-sizing: border-box; }
    html, body {
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(1200px 600px at 80% -10%, rgba(251, 146, 60, 0.25), transparent 60%),
        radial-gradient(900px 500px at -10% 10%, rgba(234, 88, 12, 0.18), transparent 60%),
        linear-gradient(180deg, #fffaf5 0%, #fff7ed 100%);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }
    .wrap {
      max-width: 1080px;
      margin: 0 auto;
      padding: 56px 24px 80px;
    }
    .hero {
      text-align: center;
      padding: 56px 24px 32px;
    }
    .rocket {
      font-size: 88px;
      line-height: 1;
      display: inline-block;
      filter: drop-shadow(0 6px 18px rgba(234, 88, 12, 0.35));
      animation: float 3.6s ease-in-out infinite;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0) rotate(-8deg); }
      50%      { transform: translateY(-10px) rotate(-4deg); }
    }
    h1 {
      font-size: clamp(36px, 6vw, 64px);
      line-height: 1.05;
      margin: 20px 0 14px;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, var(--c1), var(--c2) 50%, var(--c3));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }
    .sub {
      font-size: clamp(16px, 2vw, 20px);
      color: var(--ink-soft);
      max-width: 720px;
      margin: 0 auto;
    }
    .stack-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-top: 22px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(234, 88, 12, 0.08);
      color: var(--c1);
      font-weight: 600;
      font-size: 13px;
      letter-spacing: 0.02em;
      border: 1px solid var(--line);
    }
    .stack-pill .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--c1), var(--c3));
      box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.15);
    }
    section {
      margin-top: 56px;
    }
    .section-title {
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--c1);
      margin: 0 0 18px;
      text-align: center;
    }
    .section-lede {
      text-align: center;
      color: var(--muted);
      margin: 0 0 28px;
      font-size: 15px;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }
    @media (max-width: 820px) {
      .grid { grid-template-columns: 1fr; }
    }
    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 22px 22px 20px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      transition: transform 160ms ease, box-shadow 160ms ease;
    }
    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 16px 40px rgba(234, 88, 12, 0.12), 0 4px 10px rgba(17, 24, 39, 0.06);
    }
    .card .step {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--c1), var(--c3));
      color: white;
      font-weight: 700;
      font-size: 14px;
      margin-bottom: 14px;
      box-shadow: 0 6px 14px rgba(234, 88, 12, 0.3);
    }
    .card h3 {
      margin: 0 0 6px;
      font-size: 17px;
      letter-spacing: -0.01em;
    }
    .card p {
      margin: 0;
      color: var(--ink-soft);
      font-size: 14px;
      line-height: 1.5;
    }
    .card code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;
      background: rgba(234, 88, 12, 0.08);
      color: var(--c1);
      padding: 2px 6px;
      border-radius: 6px;
      font-size: 13px;
    }
    .cta {
      display: flex;
      flex-direction: column;
      height: 100%;
    }
    .cta .body { flex: 1; }
    .cta a.btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 16px;
      padding: 9px 14px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--c1), var(--c2));
      color: white;
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      box-shadow: 0 6px 14px rgba(234, 88, 12, 0.28);
      transition: transform 120ms ease, box-shadow 120ms ease;
      align-self: flex-start;
    }
    .cta a.btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 10px 22px rgba(234, 88, 12, 0.34);
    }
    .cta a.btn.ghost {
      background: white;
      color: var(--c1);
      border: 1px solid var(--line);
      box-shadow: var(--shadow);
    }
    .icon {
      font-size: 22px;
      margin-bottom: 12px;
      display: inline-block;
    }
    footer {
      margin-top: 72px;
      padding: 28px 0 8px;
      text-align: center;
      color: var(--muted);
      font-size: 14px;
      border-top: 1px solid var(--line);
    }
    footer a {
      color: var(--c1);
      text-decoration: none;
      font-weight: 600;
    }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <main class="wrap">
    <div class="hero">
      <div class="rocket" aria-hidden="true">&#128640;</div>
      <h1>You shipped on Clue2App!</h1>
      <p class="sub">Your Python 3 / FastAPI / Uvicorn app is live and serving at this URL.</p>
      <div class="stack-pill"><span class="dot"></span> Python 3 &middot; FastAPI &middot; Uvicorn</div>
    </div>

    <section>
      <p class="section-title">What just happened</p>
      <p class="section-lede">Three things had to go right. They all did.</p>
      <div class="grid">
        <div class="card">
          <div class="step">1</div>
          <h3>Code pushed to git</h3>
          <p><code>clue2solve/DemoPythonFastApi</code></p>
        </div>
        <div class="card">
          <div class="step">2</div>
          <h3>Built by Clue2App</h3>
          <p>Buildpacks auto-detected your stack &mdash; no Dockerfile needed.</p>
        </div>
        <div class="card">
          <div class="step">3</div>
          <h3>Deployed live</h3>
          <p>Knative serves your app and auto-scales it.</p>
        </div>
      </div>
    </section>

    <section>
      <p class="section-title">What's next</p>
      <p class="section-lede">Make it yours.</p>
      <div class="grid">
        <div class="card cta">
          <div class="body">
            <div class="icon" aria-hidden="true">&#9999;&#65039;</div>
            <h3>Edit this page</h3>
            <p>Open <code>app.py</code> to make this yours.</p>
          </div>
        </div>
        <div class="card cta">
          <div class="body">
            <div class="icon" aria-hidden="true">&#127760;</div>
            <h3>Add a custom domain</h3>
            <p>Point your own hostname at this app from the console.</p>
          </div>
          <a class="btn" href="https://console.clue2.app" target="_blank" rel="noopener">Open console &rarr;</a>
        </div>
        <div class="card cta">
          <div class="body">
            <div class="icon" aria-hidden="true">&#128202;</div>
            <h3>View build logs / metrics</h3>
            <p>Watch builds, inspect runtime logs, track CCU usage.</p>
          </div>
          <a class="btn ghost" href="https://console.clue2.app" target="_blank" rel="noopener">Open console &rarr;</a>
        </div>
      </div>
    </section>

    <footer>
      Clue2App &mdash; push code, get apps &middot;
      <a href="https://clue2app.ai" target="_blank" rel="noopener">clue2app.ai</a>
    </footer>
  </main>
</body>
</html>
"""


@app.get('/', response_class=HTMLResponse)
def root():
    return HTMLResponse(content=WELCOME_HTML, status_code=200)


@app.get('/api/v1/health')
def get():
    return "OK"


@app.get('/api/v1/health/version')
def getVersion():
    return '1.0.0'
