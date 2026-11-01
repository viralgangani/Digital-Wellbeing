import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Digital Well-being AI", page_icon="📱", layout="wide")

# ========================= MODEL LOADING — UNCHANGED =========================
wellbeing=pickle.load(open('screan_time-wellbeing.sav', 'rb'))
wellle=pickle.load(open('screan_time-wellbeing(le).sav', "rb"))
soc_cmp=pickle.load(open('screan_time-social_comparison.sav','rb'))
self_est=pickle.load(open('screan_time-self_esteem.sav', "rb"))
men_health=pickle.load(open('screan_time-mental_health.sav', "rb"))
men_hel_le=pickle.load(open('screan_time-mental_health(le).sav', "rb"))
low_mood=pickle.load(open('screan_time-low_mood.sav', "rb"))
lonly=pickle.load(open('screan_time-loneliness.sav', "rb"))
setis=pickle.load(open('screan_time-life_satisfaction.sav', "rb"))
fomo=pickle.load(open('screan_time-fomo.sav', "rb"))
label_encoder = LabelEncoder()

st.markdown(r'''<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
*{font-family:Inter,sans-serif} .stApp{background:#f7f9fc;color:#172554}
.main .block-container{max-width:1500px;padding:1.2rem 2rem 3rem}
#MainMenu,footer,header{visibility:hidden}
.top{background:white;border:1px solid #e6ebf2;border-radius:18px;padding:13px 18px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 8px 25px #1e40af0d;margin-bottom:18px}
.brand{display:flex;align-items:center;gap:11px}.logo{width:43px;height:43px;border-radius:13px;background:linear-gradient(135deg,#2563eb,#7c3aed);color:#fff;display:grid;place-items:center;font-size:22px}.bn{font-weight:800;color:#172554}.bs{font-size:11px;color:#64748b}.badge{color:#2563eb;background:#f3f7ff;border:1px solid #dbeafe;border-radius:99px;padding:8px 13px;font-size:11px;font-weight:700}
.panel{background:#fff;border:1px solid #e5eaf1;border-radius:22px;box-shadow:0 10px 35px #0f172a0b;overflow:hidden}.head{padding:26px 28px 20px;border-bottom:1px solid #edf0f5}.title{font-size:32px;line-height:1.12;font-weight:800;letter-spacing:-1.3px;color:#10204b}.sub{font-size:12px;color:#64748b;margin-top:8px}.line{width:52px;height:4px;border-radius:99px;background:linear-gradient(90deg,#2563eb,#7c3aed);margin-top:15px}
.body{padding:22px 25px}.card{background:#fff;border:1px solid #e5eaf1;border-radius:16px;padding:17px;box-shadow:0 4px 15px #0f172a07;margin-bottom:14px}.ct{font-size:14px;font-weight:800;color:#172554}.cs{font-size:10px;color:#94a3b8;margin:3px 0 13px}.ci{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:9px;background:#eef5ff;color:#2563eb;margin-right:7px}
label{color:#334155!important;font-size:11px!important;font-weight:650!important}div[data-baseweb="select"]>div,div[data-testid="stNumberInput"] input{background:#fff!important;border:1px solid #dce3ed!important;border-radius:9px!important;color:#172554!important}div[data-baseweb="select"] span{color:#172554!important}
.anxiety{height:8px;border-radius:99px;background:linear-gradient(90deg,#22c55e 0 20%,#f59e0b 20% 60%,#ef4444 60%);position:relative;margin-top:3px}.marker{position:absolute;left:calc(var(--s)*10%);top:-5px;width:7px;height:18px;background:#fff;border:1px solid #cbd5e1;border-radius:5px;box-shadow:0 2px 7px #0002}.ticks{display:flex;justify-content:space-between;color:#94a3b8;font-size:9px;margin-top:4px}.as{text-align:center;font-size:10px;color:#475569;margin-top:4px}
div.stButton>button{width:100%;height:50px;border:0!important;border-radius:11px!important;color:white!important;font-weight:750!important;background:linear-gradient(90deg,#2563eb,#7c3aed)!important;box-shadow:0 9px 22px #2563eb33}
.report-head{padding:22px 25px 15px;border-bottom:1px solid #edf0f5;display:flex;justify-content:space-between}.rt{font-size:16px;font-weight:800;color:#172554}.time{font-size:10px;color:#94a3b8}.overall{margin:17px;padding:18px;border:1px solid #e6eaf2;border-radius:17px;display:flex;align-items:center;gap:20px;background:linear-gradient(135deg,#fff,#f8fbff)}.ring{width:120px;height:120px;border-radius:50%;display:grid;place-items:center;flex-shrink:0;position:relative}.ring:before{content:"";position:absolute;width:91px;height:91px;border-radius:50%;background:white}.rn{position:relative;font-size:28px;font-weight:850;color:#172554}.rn small{font-size:9px;color:#94a3b8}.status{font-size:21px;font-weight:850}.good{color:#16a34a}.moderate{color:#d97706}.risk{color:#dc2626}.desc{font-size:11px;line-height:1.5;color:#64748b;margin-top:5px}.tip{margin-top:9px;padding:9px 11px;border-radius:10px;background:#fff8ef;border:1px solid #fde7c3;color:#8a5a14;font-size:10px}
.section{font-size:14px;font-weight:800;color:#172554;margin:20px 19px 10px}.metric{border:1px solid #e7ebf2;border-radius:14px;padding:14px;min-height:125px;margin-bottom:11px;background:#fff}.mn{font-size:10px;font-weight:700;color:#334155}.mv{font-size:24px;font-weight:850;color:#172554;margin-top:10px}.bar{height:6px;border-radius:99px;background:#e9edf3;overflow:hidden;margin-top:8px}.fill{height:100%;border-radius:99px}.ms{font-size:9px;font-weight:700;margin-top:5px}.bottom{padding:15px;border:1px solid #e7ebf2;border-radius:15px;min-height:210px;background:#fff}.bt{font-size:12px;font-weight:800;color:#172554;margin-bottom:13px}.fl{font-size:9px;color:#64748b;margin-bottom:4px}.fv{font-size:11px;font-weight:750}.fbar{height:6px;background:#edf0f4;border-radius:99px;margin:6px 0 14px;overflow:hidden}.sug{display:flex;gap:7px;padding:5px 0;font-size:9px;line-height:1.4;color:#475569}.sn{min-width:21px;height:21px;border-radius:50%;display:grid;place-items:center;background:#eff6ff;color:#2563eb;font-size:8px;font-weight:800}.enc{margin:17px;padding:14px;border-radius:14px;background:linear-gradient(90deg,#f3f7ff,#fbf7ff);border:1px solid #dbeafe;color:#294477;font-size:10px}.empty{text-align:center;margin:17px;padding:55px 20px;border:1px dashed #d9e1ee;border-radius:17px;background:#fbfcff}.empty-icon{font-size:42px}.empty-title{font-size:16px;font-weight:800;color:#172554;margin-top:8px}.empty-sub{font-size:10px;color:#94a3b8;line-height:1.5;margin-top:7px}.privacy{text-align:center;color:#94a3b8;font-size:9px;margin-top:7px}
@media(max-width:900px){.main .block-container{padding:1rem}.title{font-size:25px}.overall{flex-direction:column;text-align:center}}
.report-gap{height:24px}\n</style>''', unsafe_allow_html=True)

st.markdown('''<div class="top"><div class="brand"><div class="logo">♡</div><div><div class="bn">Digital Well-being AI</div><div class="bs">Understand • Improve • Thrive</div></div></div><div class="badge">✦ &nbsp; AI Powered &nbsp;•</div></div>''',unsafe_allow_html=True)


st.markdown('<div class="panel"><div class="head"><div class="title">Let’s assess your<br>digital well-being 👋</div><div class="sub">Answer a few questions to get your personalized insights.</div><div class="line"></div></div><div class="body">',unsafe_allow_html=True)
c1,c2=st.columns(2,gap="medium")
with c1:
    st.markdown('<div class="card"><div class="ct"><span class="ci">👤</span>Personal Information</div><div class="cs">Tell us about yourself</div>',unsafe_allow_html=True)
    age=st.number_input("Age",min_value=1,max_value=120,value=18)
    gender=st.selectbox("Gender",["Male","Female"])
    occupation=st.selectbox("Occupation",["Student","Full-time employed","Part-time employed","Self-employed","Unemployed","Retired"])
    st.markdown('</div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="ct"><span class="ci">🧠</span>Lifestyle & Mental Health</div><div class="cs">Your daily routine & emotional well-being</div>',unsafe_allow_html=True)
    avg_sleep_hours=st.number_input("Average Sleep time (in hrs)",min_value=0.0,max_value=24.0,value=8.0,step=0.1,format="%.2f")
    physical_activity_days_per_week=st.number_input("Physical activity days per week",min_value=0,max_value=50)
    anxiety_score_0to27=st.slider("Anxiety score out of 10",min_value=0,max_value=10,value=4,help="a normal human emotion involving fear, tension, or worry about future events")
    st.markdown(f'<div class="anxiety"><div class="marker" style="--s:{anxiety_score_0to27}"></div></div><div class="ticks"><span>0</span><span>5</span><span>10</span></div><div class="as">Score: <b>{anxiety_score_0to27}/10</b></div></div>',unsafe_allow_html=True)
c1,c2=st.columns(2,gap="medium")
with c1:
    st.markdown('<div class="card"><div class="ct"><span class="ci">📱</span>Social Media Usage</div><div class="cs">How you use social media</div>',unsafe_allow_html=True)
    daily_screen_hours=st.number_input("Average Screen time (in hrs)",min_value=0.0,max_value=24.0,value=6.0,step=0.1,format="%.2f")
    minutes_to_first_check_after_waking=st.number_input("Minutes to first check after waking",min_value=0,max_value=500)
    night_time_use=st.selectbox("Night time use",["Never","Sometimes","Often","Every night"])
    primary_purpose=st.selectbox("Primary purpose of using",["Entertainment","Connection with friends","News/information","Passing time/boredom","Work/career","Content creation"])
    st.markdown('</div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="ct"><span class="ci">🛡️</span>Digital Habits</div><div class="cs">Your digital wellness habits</div>',unsafe_allow_html=True)
    uses_screen_time_limits=st.selectbox("Uses screen time limits",["Yes","No"])
    attempted_digital_detox=st.selectbox("Attempted digital detox",["Yes, failed","Yes, succeeded","No"],help="a planned time when a person stops using phones, computers, and social media to rest their mind and connect with the real world")
    st.markdown('<div style="margin-top:15px;padding:10px;border-radius:10px;background:#f8fbff;border:1px solid #e4edfb;color:#64748b;font-size:10px">🔒 Your answers are used only to generate your digital well-being assessment.</div></div>',unsafe_allow_html=True)
st.markdown('<br>',unsafe_allow_html=True)
predict_clicked=st.button("✨  Predict My Well-being  →")
st.markdown('<div class="privacy">🔒 Your data is private and secure • Used only for analysis</div></div></div>',unsafe_allow_html=True)

st.markdown('<div class="report-gap"></div><div class="panel"><div class="report-head"><div class="rt">▣ &nbsp; Your Digital Well-being Report</div><div class="time">◷ &nbsp; Last updated: just now</div></div>',unsafe_allow_html=True)

if predict_clicked:
    # ===================== ORIGINAL PREDICTION LOGIC =====================
    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "occupation": [occupation],
        "daily_screen_hours": [daily_screen_hours],
        "night_time_use": [night_time_use],
        "minutes_to_first_check_after_waking": [minutes_to_first_check_after_waking],
        "primary_purpose": [primary_purpose],
        "avg_sleep_hours": [avg_sleep_hours],
        "anxiety_score_0to27": [anxiety_score_0to27],
        "physical_activity_days_per_week": [physical_activity_days_per_week],
        "uses_screen_time_limits": [uses_screen_time_limits],
        "attempted_digital_detox": [attempted_digital_detox]
    })
    wellb = wellbeing.predict(input_data)[0]
    soc_cmpi=soc_cmp.predict(input_data)[0]
    self=self_est.predict(input_data)[0]
    men_hel=men_health.predict(input_data)[0]
    low=low_mood.predict(input_data)[0]
    lonli=lonly.predict(input_data)[0]
    lsetis=setis.predict(input_data)[0]
    fmo=fomo.predict(input_data)[0]
    wellb = wellle.inverse_transform([wellb])[0]
    men_hel=men_hel_le.inverse_transform([men_hel])[0]

    # ===================== ORIGINAL SCALING LOGIC =====================
    lsetis=round(lsetis*10,2); low=round(low*10,2); lonli=round(lonli*10,2)
    soc_cmpi=round(soc_cmpi*10,2); self=round(self*10,2); fmo=round(fmo*10,2)

    # ===================== ORIGINAL SCORE CONDITIONS =====================
    if lsetis<=29: life_note="Low (↑)"; life_color="#dc2626"
    elif lsetis>29 and lsetis<70: life_note="Considerable (=)"; life_color="#16a34a"
    else: life_note="Too good for you (↓)"; life_color="#16a34a"
    if low<=29: low_note="Very Good"; low_color="#16a34a"
    elif low>29 and low<50: low_note="Can improve"; low_color="#d97706"
    else: low_note="Getting worse"; low_color="#dc2626"
    if lonli<=40: lon_note="Very Good"; lon_color="#16a34a"
    elif lonli>40 and lonli<60: lon_note="Can improve"; lon_color="#d97706"
    else: lon_note="High"; lon_color="#dc2626"
    if soc_cmpi<=40: social_note="Good"; social_color="#2563eb"
    elif soc_cmpi>40 and soc_cmpi<60: social_note="Moderate"; social_color="#2563eb"
    else: social_note="High"; social_color="#dc2626"
    if self<=40: self_note="Follow suggestions"; self_color="#d97706"
    elif self>40 and self<60: self_note="Moderate"; self_color="#7c3aed"
    else: self_note="Very Good"; self_color="#16a34a"
    if fmo<=20: fomo_note="No FOMO"; fomo_color="#16a34a"
    elif fmo>20 and fmo<51: fomo_note="Moderate"; fomo_color="#d97706"
    else: fomo_note="High"; fomo_color="#dc2626"

    # The original model outputs a class, not a 0-100 overall score.
    # The number below is only a visual UI indicator and does not alter the model result.
    if wellb=="Good": overall_score=78; status="Good"; status_class="good"; icon="😊"; desc="Your digital habits look generally healthy. Keep maintaining a balanced relationship with technology."
    elif wellb=="Moderate": overall_score=58; status="Moderate"; status_class="moderate"; icon="😐"; desc="Some parts of your digital lifestyle are balanced, while a few habits may need attention."
    else: overall_score=67; status="At-risk"; status_class="risk"; icon="😟"; desc="Your digital habits may be impacting your well-being. Small changes can improve your mental and emotional health."
    deg=int(overall_score*3.6)
    st.markdown(f'<div class="overall"><div class="ring" style="background:conic-gradient(#2563eb 0deg {deg}deg,#e8edf5 {deg}deg 360deg)"><div class="rn">{overall_score}<small>/100</small></div></div><div><div class="status {status_class}">{status} {icon}</div><div class="desc">{desc}</div><div class="tip">💡 <b>Keep going!</b><br>You are aware — that’s the first step toward better digital habits.</div></div></div>',unsafe_allow_html=True)

    st.markdown('<div class="section">Well-being Scores</div>',unsafe_allow_html=True)
    def metric(name,value,note,color):
        return f'<div class="metric"><div class="mn">{name}</div><div class="mv">{value:.1f}%</div><div class="bar"><div class="fill" style="width:{min(max(value,0),100)}%;background:{color}"></div></div><div class="ms" style="color:{color}">{note}</div></div>'
    m1,m2,m3=st.columns(3)
    with m1:
        st.markdown(metric("😊 Life Satisfaction",lsetis,life_note,life_color),unsafe_allow_html=True)
        st.markdown(metric("↗ Social Comparison",soc_cmpi,social_note,social_color),unsafe_allow_html=True)
    with m2:
        st.markdown(metric("🙂 Low Mood",low,low_note,low_color),unsafe_allow_html=True)
        st.markdown(metric("◉ Self Esteem",self,self_note,self_color),unsafe_allow_html=True)
    with m3:
        st.markdown(metric("☹ Loneliness",lonli,lon_note,lon_color),unsafe_allow_html=True)
        st.markdown(metric("◌ FOMO",fmo,fomo_note,fomo_color),unsafe_allow_html=True)

    # ===================== ORIGINAL SUGGESTION LOGIC =====================
    suggestions=[]
    if daily_screen_hours <= 3: suggestions.append("You have well maintained screen time.")
    if daily_screen_hours > 3 and daily_screen_hours < 7: suggestions.append("Reduce daily screen time by 1-2 hours.")
    elif daily_screen_hours >= 7: suggestions.append("Reduce daily screen time by 2-3 hours,")
    if uses_screen_time_limits=="No": suggestions.append("Use screen time limits.")
    if avg_sleep_hours < 7: suggestions.append("Aim for at least 7-8 hours of sleep each night,")
    if night_time_use=="Often" or night_time_use=="Every night": suggestions.append("Avoid night time use before bedtime, this will increas seeping hours.")
    if physical_activity_days_per_week <3: suggestions.append("Increase physical activity: Ateast 3 days per week.")
    if minutes_to_first_check_after_waking < 30: suggestions.append("Not check phone after just wake-up, do exercise in this time.")
    if men_hel == "Considering it": suggestions.append("You should Seek to mental health support.")
    elif men_hel == "No": suggestions.append("No need to seek mental health support.")
    else: suggestions.append("Must consider mental health support.")
    if attempted_digital_detox=="No" and wellb=="At-risk": suggestions.append("Attempt digital detox")
    elif attempted_digital_detox=="No" and wellb=="Moderate": suggestions.append("Attempt digital detox")
    elif attempted_digital_detox=="Yes, failed": suggestions.append("Try digital detox again")

    vals={"Life Satisfaction":lsetis,"Low Mood":low,"Loneliness":lonli,"Social Comparison":soc_cmpi,"Self Esteem":self,"FOMO":fmo}
    high=max(vals,key=vals.get); low_name=min(vals,key=vals.get)
    b1,b2=st.columns(2,gap="medium")
    with b1:
        st.markdown(f'<div class="bottom"><div class="bt">📈 &nbsp; What Stood Out?</div><div class="fl">Highest indicator</div><div class="fv" style="color:#dc2626">{high} ({vals[high]:.1f}%)</div><div class="fbar"><div style="height:100%;width:{vals[high]}%;background:#ef4444;border-radius:99px"></div></div><div class="fl">Lowest indicator</div><div class="fv" style="color:#16a34a">{low_name} ({vals[low_name]:.1f}%)</div><div class="fbar"><div style="height:100%;width:{vals[low_name]}%;background:#22c55e;border-radius:99px"></div></div></div>',unsafe_allow_html=True)
    with b2:
        html='<div class="bottom"><div class="bt">✦ &nbsp; Personalized Suggestions</div>'
        if suggestions:
            for i,s in enumerate(suggestions[:6],1): html+=f'<div class="sug"><div class="sn">{i:02d}</div><div>{s}</div></div>'
        else: html+='<div class="sug"><div class="sn">✓</div><div>Your current habits are looking good. Keep it up!</div></div>'
        html+='</div>'; st.markdown(html,unsafe_allow_html=True)

    if anxiety_score_0to27<=2: anxiety_note="You have no Anxiety (↓)"
    elif anxiety_score_0to27>2 and anxiety_score_0to27<=6: anxiety_note="You have moderate Anxity, need little bit more focus on it (=)"
    else: anxiety_note="You have Anixety also (↑)"
    st.markdown(f'<div style="margin:14px 17px 0;padding:11px 14px;border:1px solid #e7ebf2;border-radius:12px;background:#fff;color:#64748b;font-size:10px"><b style="color:#334155">🧠 Anxiety:</b> {anxiety_score_0to27}/10 • {anxiety_note}</div>',unsafe_allow_html=True)

    if wellb=="Good": final_text="Your responses indicate generally healthy digital habits. Continue maintaining a balanced relationship with technology"
    elif wellb=="Moderate": final_text="Your digital lifestyle appears balanced in some areas, but there are signs that certain habits could negatively impact your well-being over time."
    else: final_text="Your current digital habits suggest that excessive or unhealthy social media usage may be affecting your overall well-being."
    st.markdown(f'<div class="enc">💙 &nbsp; <b>{final_text}</b><br><span style="color:#64748b">Small consistent changes can lead to meaningful results.</span></div>',unsafe_allow_html=True)
else:
    st.markdown('<div class="empty"><div class="empty-icon">📊</div><div class="empty-title">Your report will appear here</div><div class="empty-sub">Complete the assessment above and click <b>Predict My Well-being</b> to generate your personalized report.</div></div>',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

st.markdown('<div style="text-align:center;color:#94a3b8;font-size:9px;margin-top:18px">Digital Well-being Prediction System • AI-powered self-awareness tool</div>',unsafe_allow_html=True)
