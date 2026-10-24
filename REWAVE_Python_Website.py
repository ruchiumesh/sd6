import streamlit as st

st.set_page_config(page_title="REWAVE | Water Reuse", page_icon="💧", layout="wide")

# ---------- Visual theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root { --cyan:#37e8ff; --blue:#1769ff; --green:#a7ff5a; --yellow:#ffe45c; --ink:#05070d; }
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp {
  background:
    radial-gradient(circle at 8% 8%, #073e78 0%, transparent 28%),
    radial-gradient(circle at 90% 18%, #063d3b 0%, transparent 24%),
    radial-gradient(circle at 65% 78%, #1a1049 0%, transparent 28%),
    #05070d;
  color:#edf8ff;
}
.block-container { max-width: 1450px; padding-top: 1.3rem; padding-bottom: 3rem; }
h1,h2,h3 { color:#f2fbff; }
h2 { text-shadow:0 0 24px #1c8dff35; }
.hero {
  position:relative; overflow:hidden; border:1px solid #1d83a9; border-radius:28px; padding:2.2rem;
  background:linear-gradient(120deg,rgba(0,85,255,.25),rgba(0,238,255,.10),rgba(12,25,38,.90));
  box-shadow:0 0 38px #0066ff20, inset 0 0 36px #20cfff0b;
  animation:heroGlow 6s ease-in-out infinite alternate;
}
.hero:after {
  content:""; position:absolute; width:230px; height:230px; right:-55px; top:-80px; border-radius:50%;
  border:1px solid #4deeff66; box-shadow:0 0 0 22px #24dfff0b,0 0 0 46px #24dfff08;
  animation:orb 10s linear infinite; pointer-events:none;
}
.brand { font-size:clamp(3.5rem,9vw,7rem); line-height:.95; letter-spacing:.08em; font-weight:900; color:#145bff; text-shadow:0 0 15px #087cffb0,0 0 42px #087cff65; }
.kicker { color:var(--green); font-weight:900; letter-spacing:.18em; text-transform:uppercase; font-size:.78rem; }
.sub { color:#d0e7fa; font-size:1.12rem; line-height:1.7; max-width:850px; }
.pill { display:inline-block; border:1px solid #20c9ef; color:#b4f7ff; background:linear-gradient(120deg,#06203a,#0b2551); padding:7px 12px; border-radius:999px; margin:4px 5px 4px 0; font-size:.8rem; box-shadow:0 0 15px #00cfff12; }
.card {
  background:linear-gradient(145deg,rgba(20,40,62,.96),rgba(7,12,23,.98));
  border:1px solid #24577a; border-radius:18px; padding:20px; min-height:130px;
  box-shadow:0 10px 30px #0003; transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;
  animation:riseIn .7s ease both;
}
.card:hover { transform:translateY(-5px); border-color:var(--cyan); box-shadow:0 12px 35px #00cfff20; }
.card h3 { margin:0 0 8px 0; font-size:1.05rem; }
.muted { color:#a9c4da; font-size:.91rem; line-height:1.65; }
.big { font-size:2rem; font-weight:900; color:var(--green); text-shadow:0 0 20px #a7ff5a28; }
.stage { border-left:3px solid var(--cyan); padding:6px 0 6px 15px; margin:10px 0; }
div[data-testid="stMetric"] { background:linear-gradient(145deg,#0d2033,#09101b); border:1px solid #276184; padding:15px; border-radius:15px; }
div[data-testid="stMetricValue"] { color:var(--cyan); }
.stButton>button { border-radius:12px; border:1px solid #2be4ff; background:linear-gradient(100deg,#145bff,#00a9c7,#138c62); color:white; font-weight:800; min-height:44px; transition:transform .2s,filter .2s; }
.stButton>button:hover { transform:translateY(-2px); filter:brightness(1.15); border-color:var(--green); }
[data-testid="stSlider"] [role="slider"] { background:var(--cyan); }
hr { border-color:#24516d; }
@keyframes heroGlow { from { box-shadow:0 0 25px #0066ff15,inset 0 0 25px #20cfff08; } to { box-shadow:0 0 48px #00d9ff25,inset 0 0 45px #20cfff12; } }
@keyframes orb { from { transform:rotate(0deg) scale(1); } to { transform:rotate(360deg) scale(1.08); } }
@keyframes riseIn { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
@media (prefers-reduced-motion: reduce) { *,*::before,*::after { animation:none!important; transition:none!important; } }
</style>
""", unsafe_allow_html=True)

# ---------- Header / navigation ----------
st.markdown('''<div class="kicker">SDG 06 · CLEAN WATER AND SANITATION</div>
<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0 16px;color:#8cefff;font-size:1.35rem">
  <span style="animation:orb 7s linear infinite;display:inline-block">💧</span>
  <span style="color:#a7ff5a;font-size:.78rem;font-weight:800;letter-spacing:.18em">WATER CIRCULARITY · SMART REUSE · LOCAL IMPACT</span>
  <span style="animation:orb 9s linear infinite;display:inline-block">✦</span>
</div>''', unsafe_allow_html=True)
nav = st.columns(6)
for col, label in zip(nav, ["Home", "How it works", "Monitor", "Water savings", "Budget", "Impact"]):
    with col:
        st.markdown(f'<span class="pill">{label}</span>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="brand">REWAVE <span style="color:#39d9ff">💧</span></div>
  <h2>Every Drop Deserves Another Purpose.</h2>
  <p class="sub">Turning lightly used water into a valuable resource through affordable filtration, smart monitoring and local reuse.</p>
  <div style="font-size:1.05rem;font-weight:800;color:#a6f7ff;letter-spacing:.08em">COLLECT&nbsp; → &nbsp;FILTER&nbsp; → &nbsp;CHECK&nbsp; → &nbsp;REUSE</div>
  <br><span class="pill">HOSTELS</span><span class="pill">COLLEGE CAMPUSES</span><span class="pill">LOCAL COMMUNITIES</span>
</div>
""", unsafe_allow_html=True)

st.write("")
m1,m2,m3,m4 = st.columns(4)
for col, num, label in [
    (m1,"33,000 L","Illustrative daily campus supply"),
    (m2,"4 stages","Collect · Filter · Check · Reuse"),
    (m3,"₹30 lakh","Maximum planning budget"),
    (m4,"SDG 6","Responsible water reuse")]:
    with col:
        st.markdown(f'<div class="card"><div class="big">{num}</div><div class="muted">{label}</div></div>', unsafe_allow_html=True)

st.write("")
st.markdown("## The water we can still put to use")
st.markdown('<p class="muted">Washbasin and shower water is often sent directly to drains. With suitable treatment and quality checks, some greywater may be reused for approved non-drinking purposes.</p>', unsafe_allow_html=True)
p1,p2,p3 = st.columns(3)
with p1: st.markdown('<div class="card"><h3>💧 Freshwater pressure</h3><p class="muted">Use less drinking-quality water for tasks that do not need it.</p></div>',unsafe_allow_html=True)
with p2: st.markdown('<div class="card"><h3>🔧 Local maintenance</h3><p class="muted">Modular filters and serviceable parts are designed around campus needs.</p></div>',unsafe_allow_html=True)
with p3: st.markdown('<div class="card"><h3>🌱 Suitable reuse</h3><p class="muted">Consider irrigation, landscaping and approved non-potable uses.</p></div>',unsafe_allow_html=True)

st.divider()
st.markdown("## How REWAVE works")
st.markdown('<p class="muted">A proposed small-scale system inspired by the broader principle of water recovery. Singapore’s NEWater uses advanced reclamation technology; REWAVE is a different, local-scale concept and does not claim drinking-water quality.</p>',unsafe_allow_html=True)
stages = st.columns(4)
stage_data = [
    ("01 · COLLECT","🚿","Separate pipes collect lightly used water from washbasins and showers before it mixes with toilet sewage."),
    ("02 · FILTER","🧰","Mesh screening, coarse media, sand or suitable media, and replaceable cartridges reduce particles."),
    ("03 · CHECK","🟡","A sensor such as a turbidity sensor monitors one parameter; additional testing and treatment may be required."),
    ("04 · REUSE","🌿","Approved water enters a separate non-potable tank for suitable uses, with rejected water diverted.")
]
for col,(title,emoji,desc) in zip(stages,stage_data):
    with col:
        st.markdown(f'<div class="card"><div style="font-size:2rem">{emoji}</div><h3>{title}</h3><p class="muted">{desc}</p></div>',unsafe_allow_html=True)

st.markdown("### System flow")
st.markdown("""
<div class="hero" style="padding:1.2rem;text-align:center">
  <span class="pill">🚿 Washbasins + showers</span>　➜　<span class="pill">🛢️ Collection tank</span>　➜　<span class="pill">🧰 Filter 1 + 2</span>　➜　<span class="pill">🚦 Sensor checks</span>　➜　<span class="pill">🌿 Non-potable tank</span>
</div>
""",unsafe_allow_html=True)

st.divider()
st.markdown("## REWAVE SMART MONITOR")
st.caption("Interactive front-end demonstration only — these are simulated readings, not live sensor data.")
if "sensor_mode" not in st.session_state: st.session_state.sensor_mode = "Good"
b1,b2,b3,b4 = st.columns(4)
with b1:
    if st.button("🟢 Simulate good quality", use_container_width=True): st.session_state.sensor_mode="Good"
with b2:
    if st.button("🟡 Simulate caution", use_container_width=True): st.session_state.sensor_mode="Caution"
with b3:
    if st.button("🔴 Simulate rejected water", use_container_width=True): st.session_state.sensor_mode="Rejected"
with b4:
    if st.button("🧰 Filter replacement", use_container_width=True): st.session_state.sensor_mode="Maintenance"
mode = st.session_state.sensor_mode
status = {"Good":("🟢 GREEN","Within configured demo limit — proceed only after all required checks."),
          "Caution":("🟡 YELLOW","Inspect the filter and perform additional checks before deciding."),
          "Rejected":("🔴 RED","Flow to the reuse tank is stopped in this simulation; divert for further treatment or disposal."),
          "Maintenance":("🧰 MAINTENANCE ALERT","Inspect or replace the filter cartridge before continuing.")}[mode]
a,b,c = st.columns(3)
with a: st.metric("Simulated turbidity", {"Good":"2.1 NTU","Caution":"7.8 NTU","Rejected":"18.4 NTU","Maintenance":"—"}[mode])
with b: st.metric("Collection tank", "68%")
with c: st.metric("Filter cartridge", "Inspect" if mode in ("Caution","Maintenance") else ("Replace / investigate" if mode=="Rejected" else "Normal"))
st.warning(f"{status[0]} — {status[1]}")

st.divider()
st.markdown("## Campus water-saving calculator")
st.caption("All efficiencies are editable assumptions, not measured REWAVE performance.")
c1,c2,c3,c4 = st.columns(4)
with c1: available = st.number_input("Lightly used water available (L/day)", min_value=0, value=33000, step=1000)
with c2: collection = st.slider("Collection efficiency (%)", 0, 100, 70)
with c3: recovery = st.slider("Treatment recovery (%)", 0, 100, 85)
with c4: days = st.number_input("Operating days/year", min_value=1, max_value=366, value=300)
collected = available * collection / 100
daily = collected * recovery / 100
annual = daily * days
r1,r2,r3 = st.columns(3)
r1.metric("Collected water", f"{collected:,.0f} L/day")
r2.metric("Recoverable treated water", f"{daily:,.0f} L/day")
r3.metric("Annual treated water", f"{annual:,.0f} L/year")
st.progress(min(daily / available if available else 0, 1.0))
st.caption(f"Estimated recovery of original available water: {(daily/available*100 if available else 0):.1f}%")

st.markdown("### Allocate recovered water")
x1,x2,x3 = st.columns(3)
with x1: irrigation = st.slider("Irrigation (%)", 0, 100, 40)
with x2: flushing = st.slider("Toilet flushing (%)", 0, 100, 40)
with x3: other = st.slider("Other approved uses (%)", 0, 100, 20)
allocation = irrigation + flushing + other
if allocation > 100:
    st.error(f"Allocation is {allocation}%. Reduce it to 100% or less.")
else:
    q1,q2,q3 = st.columns(3)
    q1.metric("Irrigation", f"{daily*irrigation/100:,.0f} L/day")
    q2.metric("Flushing", f"{daily*flushing/100:,.0f} L/day")
    q3.metric("Other uses", f"{daily*other/100:,.0f} L/day")

st.divider()
st.markdown("## Build your REWAVE campus · Budget planner")
st.caption("Preliminary planning estimates only. Confirm all costs with site inspection, engineering design and supplier quotations.")
items = [
    ("Separate plumbing and collection pipelines",700000),
    ("Filter cartridge 1",15000),
    ("Filter cartridge 2",15000),
    ("Collection and treated-water tanks",250000),
    ("Filter housings and media",120000),
    ("Water-quality and level sensors",100000),
    ("Controller, wiring and electricals",75000),
    ("Additional treatment equipment (if required)",300000),
    ("Installation and commissioning",200000),
    ("Testing and water-quality verification",100000),
    ("Maintenance and spare parts",75000),
    ("Contingency",150000)
]
total = 0
left,right = st.columns([1.5,1])
with left:
    st.markdown('<div class="card"><h3>Editable cost assumptions (₹)</h3><p class="muted">Change quantities and unit costs to explore scenarios.</p></div>',unsafe_allow_html=True)
    for idx,(name,cost) in enumerate(items):
        aa,bb = st.columns([3,2])
        with aa: qty = st.number_input(name, min_value=0, value=1, step=1, key=f"qty{idx}")
        with bb: unit = st.number_input(f"Unit cost · {idx+1}", min_value=0, value=cost, step=5000, key=f"cost{idx}")
        total += qty*unit
with right:
    cap = 3000000
    remaining = cap-total
    st.markdown('<div class="card"><h3>Budget snapshot</h3><p class="muted">Maximum planning budget</p></div>',unsafe_allow_html=True)
    st.metric("Estimated project total", f"₹{total:,.0f}")
    st.metric("Remaining budget", f"₹{remaining:,.0f}" if remaining>=0 else f"₹{remaining:,.0f} over")
    st.progress(min(total/cap,1.0))
    st.caption(f"{total/cap*100:.1f}% of ₹30,00,000 budget used")
    if remaining < 0: st.error(f"Over budget by ₹{abs(remaining):,.0f}.")
    else: st.success("Within the ₹30 lakh planning cap.")
    if st.button("Reset budget inputs"):
        for idx in range(len(items)):
            st.session_state.pop(f"qty{idx}",None)
            st.session_state.pop(f"cost{idx}",None)
        st.rerun()

st.divider()
st.markdown("## From one hostel to a wider impact")
s1,s2,s3,s4 = st.columns(4)
for col, title, desc in [
    (s1,"🏢 One hostel","Pilot and measure real water flow."),
    (s2,"🏫 One campus","Review reliability and maintenance."),
    (s3,"🏙️ Multiple campuses","Adapt to local plumbing and demand."),
    (s4,"🌍 Communities","Scale only after successful testing.")]:
    with col: st.markdown(f'<div class="card"><h3>{title}</h3><p class="muted">{desc}</p></div>',unsafe_allow_html=True)

st.markdown("""
<div class="hero" style="text-align:center;margin-top:24px">
  <div style="font-size:3rem">💧</div>
  <h1 style="color:#4bdfff">Small-Scale Action. Large-Scale Impact.</h1>
  <p class="sub" style="margin:auto">REWAVE is not about inventing water recycling again. It is about bringing practical, maintainable water reuse closer to the places where water is wasted every day.</p>
  <h3 style="color:#82eaff">REWAVE — Every Drop Deserves Another Purpose.</h3>
  <span class="pill">SDG 6 · CLEAN WATER AND SANITATION</span>
</div>
""",unsafe_allow_html=True)

st.caption("Safety note: This prototype is not connected to real sensors. Ordinary mesh, gravel and sand filtration cannot guarantee microbiological safety. Water must be appropriately treated and tested for its intended non-potable use; never connect reuse plumbing to drinking-water lines.")
