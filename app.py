import streamlit as st
from pathlib import Path

st.set_page_config(page_title='For My Sister ❤️', page_icon='❤️', layout='centered')
ROOT=Path(__file__).parent
PHOTO=ROOT/'assets'/'photo.jpg'
st.markdown('''<style>
.stApp{background:radial-gradient(circle at 15% 8%,rgba(171,78,139,.32),transparent 30%),#100a10;color:white}
.block-container{max-width:650px;padding:35px 20px 55px}.hero{text-align:center;font-family:Georgia,serif;margin-bottom:22px}
.kicker{font:11px Arial,sans-serif;letter-spacing:4px;text-transform:uppercase;opacity:.62}h1{font-size:44px;margin:8px 0 18px}
img{border-radius:24px;box-shadow:0 22px 70px rgba(0,0,0,.48)}
.thoughts{text-align:center;margin-top:30px}.thought{font:19px/1.85 Georgia,serif;margin:0 0 24px;opacity:0;animation:rise .9s ease forwards}
.thought:nth-child(1){animation-delay:.15s}.thought:nth-child(2){animation-delay:.55s}.thought:nth-child(3){animation-delay:.95s}.thought:nth-child(4){animation-delay:1.35s}.thought:nth-child(5){animation-delay:1.75s}.thought:nth-child(6){animation-delay:2.15s}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.divider{width:55px;height:1px;background:rgba(255,255,255,.35);margin:30px auto}.final{text-align:center;font:italic 21px/1.65 Georgia,serif}.heart{text-align:center;font-size:30px;margin-top:12px}
</style>''',unsafe_allow_html=True)
st.markdown("<div class='hero'><div class='kicker'>A little something for you</div><h1>For My Sister ❤️</h1></div>",unsafe_allow_html=True)
st.image(str(PHOTO),use_container_width=True)
st.markdown('''<div class="thoughts">
<p class="thought">Bachpan mein kitni baar lade hain,<br>kitni baar ek dusre ko irritate kiya hai...</p>
<p class="thought">Par shayad yehi toh bhai-behen ka rishta hai. ❤️</p>
<p class="thought">Waqt badlega, hum apni-apni zindagi mein busy ho jayenge,</p>
<p class="thought">lekin ek baat kabhi nahi badlegi —<br>main hamesha tere saath rahunga.</p>
<p class="thought">Tujhe har baar bol nahi pata,<br>par tu mere liye bahut important hai.</p>
<p class="thought"><b>Bas aise hi rehna... meri behan. ❤️</b></p></div>''',unsafe_allow_html=True)
st.markdown('<div class="divider"></div><div class="final">Kuch rishte explain nahi kiye jaate...<br>bas feel kiye jaate hain.<br><br><b>Lucky hoon ki tu meri behan hai.</b></div><div class="heart">❤️</div>',unsafe_allow_html=True)
