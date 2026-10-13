import streamlit as st
import pandas as pd
import pydeck as pdk
from datetime import datetime

st.set_page_config(page_title="WildAlert | Field Intelligence", page_icon="🐾", layout="wide")

# Product-style visual treatment
st.markdown("""
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 2rem; max-width: 1500px;}
[data-testid="stMetric"] {background: #f4f7f5; border: 1px solid #e0e8e2; padding: 14px 16px; border-radius: 14px;}
.hero {padding: 22px 24px; border-radius: 18px; background: linear-gradient(115deg,#102f2b,#245c4e); color: white; margin-bottom: 18px;}
.hero h1 {color:white; margin:0; font-size:2.1rem;}
.hero p {color:#dcebe4; margin:7px 0 0 0; font-size:1rem;}
.small-note {color:#68746f; font-size:0.85rem;}
.alert-card {padding: 14px 16px; border: 1px solid #ead8a7; background:#fff9e9; border-radius:12px; margin-bottom:8px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🐾 WildAlert</h1>
  <p>Field intelligence for safer human–wildlife coexistence in Botswana</p>
</div>
""", unsafe_allow_html=True)

st.warning("PROTOTYPE MODE · The incidents and map points supplied with this demo are illustrative, not live reports. Risk categories are transparent demonstration rules, not validated AI predictions. Do not use this app for real emergency decisions.")

columns = ["id","reported_at","district","community","species","incident_type","severity","status","lat","lon","description"]
sample = [
    ["WA-001","2026-10-10 06:40","Chobe","Demo area North","Elephant","Crop damage","Moderate","Reviewed",-17.80,25.15,"Illustrative sample: crop damage reported near fields."],
    ["WA-002","2026-10-11 19:15","North-West","Demo area Delta","Hippo","Animal near settlement","High","Needs review",-19.35,22.85,"Illustrative sample: animal reported near a settlement."],
    ["WA-003","2026-10-12 05:55","Central","Demo area East","Elephant","Livestock threatened","High","Reviewed",-21.15,26.45,"Illustrative sample: livestock owner reports a wildlife encounter."],
    ["WA-004","2026-10-12 16:20","Chobe","Demo area River","Buffalo","Animal sighting","Low","Reviewed",-17.95,24.95,"Illustrative sample: sighting reported from a safe distance."],
    ["WA-005","2026-10-13 07:10","North-West","Demo area West","Lion","Livestock threatened","High","Needs review",-19.85,22.15,"Illustrative sample: livestock risk report awaiting verification."],
    ["WA-006","2026-10-13 11:25","Central","Demo area South","Unknown","Animal near settlement","Moderate","New",-21.65,25.90,"Illustrative sample: species not confirmed."],
]
if "incidents" not in st.session_state:
    st.session_state.incidents = pd.DataFrame(sample, columns=columns)

def assess(row):
    """Illustrative explainable scoring logic; not a validated predictive model."""
    score = {"Low": 1, "Moderate": 2, "High": 3}.get(str(row["severity"]), 1)
    reasons = [f"Reported severity: {row['severity']}"]
    if row["incident_type"] in ["Animal near settlement", "Attack or injury", "Livestock threatened"]:
        score += 2
        reasons.append("Incident type involves potential proximity to people or livestock")
    elif row["incident_type"] in ["Crop damage", "Property damage"]:
        score += 1
        reasons.append("Reported damage indicates a livelihood impact")
    if row["species"] in ["Elephant", "Lion", "Buffalo", "Hippo", "Unknown"]:
        score += 1
        reasons.append("Species is included in the demo's elevated-caution list")
    if row["status"] == "Needs review" or row["status"] == "New":
        reasons.append("Report still needs review; treat details as unconfirmed")
        score = max(1, score - 1)
    level = "HIGH" if score >= 5 else ("MODERATE" if score >= 3 else "LOW")
    return pd.Series([level, "; ".join(reasons)])

df = st.session_state.incidents.copy()
df[["demo_assessment","assessment_basis"]] = df.apply(assess, axis=1)

# Sidebar controls
with st.sidebar:
    st.header("Explore reports")
    district_options = ["All districts"] + sorted(df["district"].dropna().unique().tolist())
    chosen_district = st.selectbox("District", district_options)
    species_options = ["All species"] + sorted(df["species"].dropna().unique().tolist())
    chosen_species = st.selectbox("Species", species_options)
    status_options = ["All statuses"] + sorted(df["status"].dropna().unique().tolist())
    chosen_status = st.selectbox("Review status", status_options)
    st.divider()
    st.caption("Demo controls filter illustrative records only.")
    st.markdown("**Prototype scope**")
    st.caption("Report intake · Review status · Map view · Explainable risk rules · Export")

view = df.copy()
if chosen_district != "All districts":
    view = view[view["district"] == chosen_district]
if chosen_species != "All species":
    view = view[view["species"] == chosen_species]
if chosen_status != "All statuses":
    view = view[view["status"] == chosen_status]

high_count = int((view["demo_assessment"] == "HIGH").sum())
pending_count = int(view["status"].isin(["New", "Needs review"]).sum())
district_count = int(view["district"].nunique())

m1,m2,m3,m4 = st.columns(4)
m1.metric("Reports in view", len(view))
m2.metric("Elevated-caution flags", high_count)
m3.metric("Awaiting review", pending_count)
m4.metric("Areas represented", district_count)

left, right = st.columns([1.55, 1], gap="large")
with left:
    st.subheader("Incident overview")
    st.caption("Map points are deliberately approximate demo coordinates, not verified incident locations.")
    if not view.empty:
        # Colors indicate the transparent demo assessment only.
        color_map = {"HIGH":[196,76,59,190],"MODERATE":[224,164,55,190],"LOW":[58,145,105,190]}
        view["point_color"] = view["demo_assessment"].map(color_map)
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=view,
            get_position="[lon, lat]",
            get_fill_color="point_color",
            get_line_color=[255,255,255,220],
            get_radius=9500,
            pickable=True,
            stroked=True,
            line_width_min_pixels=1,
        )
        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=pdk.ViewState(latitude=-21.5, longitude=24.5, zoom=4.2, pitch=0),
            tooltip={"text":"{id} · {district}\\n{species} — {incident_type}\\nDemo assessment: {demo_assessment}\\nStatus: {status}"},
            map_style=None,
        )
        st.pydeck_chart(deck, use_container_width=True)
        st.caption("HIGH / MODERATE / LOW are demo rule outputs, not measured probabilities.")
    else:
        st.info("No reports match the selected filters.")

with right:
    st.subheader("Priority review queue")
    queue = view[view["status"].isin(["New","Needs review"])].sort_values("reported_at", ascending=False)
    if queue.empty:
        st.success("No reports awaiting review in this filtered view.")
    else:
        for _, r in queue.head(4).iterrows():
            st.markdown(
                f"""<div class="alert-card"><b>{r['id']} · {r['district']}</b><br>
                {r['species']} — {r['incident_type']}<br>
                <span class="small-note">Status: {r['status']} · Demo assessment: {r['demo_assessment']}</span></div>""",
                unsafe_allow_html=True
            )
    st.subheader("Report trends")
    if not view.empty:
        by_type = view.groupby("incident_type").size().sort_values(ascending=False).rename("Reports")
        st.bar_chart(by_type)

st.divider()
tab_report, tab_log, tab_method = st.tabs(["＋ Submit a report", "Incident register", "How the demo assessment works"])

with tab_report:
    st.subheader("Capture a new report")
    st.caption("Only record what can be observed safely. Never approach an animal to gather information.")
    with st.form("new_report", clear_on_submit=True):
        c1,c2 = st.columns(2)
        community = c1.text_input("Community / general area", placeholder="e.g. community name; no home address")
        district = c2.selectbox("District", ["Chobe","North-West","Central","Ngamiland","Boteti","Other"])
        species = c1.selectbox("Species", ["Unknown","Elephant","Lion","Buffalo","Hippo","Leopard","Hyena","Other"])
        incident_type = c2.selectbox("Incident type", ["Animal sighting","Animal near settlement","Livestock threatened","Attack or injury","Crop damage","Property damage"])
        severity = c1.selectbox("Reported severity", ["Low","Moderate","High"], index=1)
        status = c2.selectbox("Review status", ["New","Needs review","Reviewed"])
        description = st.text_area("What was observed?", placeholder="Avoid personal details and exact sensitive wildlife locations.")
        submit = st.form_submit_button("Add report to this demo")
    if submit:
        if not community.strip():
            st.error("Enter a general community or area.")
        else:
            # Approximate district-centre coordinates are used for demonstration only.
            coords = {"Chobe":(-17.8,25.1),"North-West":(-19.3,22.8),"Central":(-21.2,26.2),"Ngamiland":(-19.9,22.3),"Boteti":(-21.5,24.5),"Other":(-22.0,25.0)}
            lat, lon = coords[district]
            new_id = f"WA-{len(st.session_state.incidents)+1:03d}"
            new = pd.DataFrame([[new_id,datetime.now().strftime("%Y-%m-%d %H:%M"),district,community.strip(),species,incident_type,severity,status,lat,lon,description.strip()]], columns=columns)
            st.session_state.incidents = pd.concat([st.session_state.incidents,new], ignore_index=True)
            st.success(f"Added {new_id} to this browser session. Its map position is an approximate district-level demo point.")
            st.info("No message was sent to authorities and no real alert was issued. For a real emergency, contact the appropriate local authority.")

with tab_log:
    st.subheader("Incident register")
    st.dataframe(view[["id","reported_at","district","community","species","incident_type","severity","status","demo_assessment"]], use_container_width=True, hide_index=True)
    st.download_button("Export filtered register (CSV)", data=view[columns + ["demo_assessment","assessment_basis"]].to_csv(index=False).encode("utf-8"), file_name="wildalert_demo_register.csv", mime="text/csv")

with tab_method:
    st.subheader("Explainable demonstration rules")
    st.write("This prototype does not use a trained AI model. It applies simple rules so reviewers can inspect why a report is flagged.")
    st.markdown("""
- Starts with the severity entered in the report.
- Adds caution points for certain incident types and species in this illustrative rule set.
- Reduces the score slightly for reports that have not yet been reviewed, while keeping them visibly unconfirmed.
- Converts the score into LOW, MODERATE, or HIGH demo categories.

**This is not a probability of an attack.** The rules are not validated against real incident outcomes and must not be used to direct field operations.

### What is needed for a credible AI version?
1. Permissioned, sufficiently complete historical incident data.
2. Consultation with wildlife authorities and affected communities.
3. Clear outcome labels and a defined prediction task.
4. Evaluation on held-out data, including false alarms and missed incidents.
5. Privacy, safety, and governance review before any live alerting.
""")

st.divider()
st.caption("WildAlert · Concept-stage field-intelligence prototype · Sample data are illustrative · No live alert service connected")
