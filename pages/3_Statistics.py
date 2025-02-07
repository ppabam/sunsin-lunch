import streamlit as st
from sunsin_lunch.db import select_table

st.set_page_config(page_title="STATISTICS", page_icon="🍽️")

st.markdown("# 🍽️ STATISTICS Menu")
st.sidebar.header("STATISTICS Menu")

select_df = select_table()
gdf = select_df.groupby('ename')['menu'].count().reset_index()
gdf

st.subheader("차트")
# https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
try:
    fig, ax = plt.subplots()
    gdf.plot(x="ename", y="menu", kind="bar", ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다")
    print(f"Exception:{e}")