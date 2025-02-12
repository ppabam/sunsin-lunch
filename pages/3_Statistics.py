import streamlit as st
from sunsin_lunch.db import select_table
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

  
st.set_page_config(page_title="STATISTICS", page_icon="🍽️")

st.markdown("# 🍽️ STATISTICS Menu")
st.sidebar.header("STATISTICS Menu")

select_df = select_table()
gdf = select_df.groupby('name')['menu_name'].count().reset_index()

st.subheader("차트")
# https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
try:
    fig, ax = plt.subplots()
    gdf.plot(x="name", y="menu_name", kind="bar", ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다")
    print(f"Exception:{e}")

st.subheader("테이블")
st.dataframe(gdf, use_container_width=True)

st.subheader("차트(한글)")

def load_fonts():
    font_dirs = [os.getcwd() + '/fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
            fm.fontManager.addfont(font_file)
            
plt.rc('font', family='NanumGothic')
kgdf = select_df.groupby('menu_name')['name'].count().reset_index()
try:
    fig, ax = plt.subplots()
    kgdf.plot(x="menu_name", y="name", kind="bar", ax=ax)
    ax.set_xticklabels(kgdf["menu_name"], rotation=45, ha='right')
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다")
    print(f"Exception:{e}")