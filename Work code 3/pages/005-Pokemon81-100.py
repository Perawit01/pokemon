import streamlit as st

# กำหนดข้อมูล Base Stats ของ Pokemon ในรูปแบบ Dictionary
base_stats = {
    "001Fushigidane": {"HP": 45, "Att": 49, "Def": 49, "S.Att": 64, "S.Def": 65, "Spd": 45},
    "002Fushigisou": {"HP": 60, "Att": 62, "Def": 63, "S.Att": 80, "S.Def": 80, "Spd": 60},
    "003Fushigibana": {"HP": 80, "Att": 82, "Def": 83, "S.Att": 100, "S.Def": 100, "Spd": 80},
    # เพิ่มข้อมูล Pokemon ที่เหลือตามต้องการ
}

# สร้าง layout ของ streamlit ให้เป็น 3 คอลัมน์
col1, col2, col3 = st.columns(3)

# กำหนดข้อมูล Base Stats ของ Pokemon ใน col3
with col3:
    st.header("Base Stats")
    for pokemon, stats in base_stats.items():
        st.write(f"#{pokemon[0:3]} {pokemon[3:]}")
        st.write(f"HP: {stats['HP']}")
        st.write(f"Att: {stats['Att']}")
        st.write(f"Def: {stats['Def']}")
        st.write(f"S.Att: {stats['S.Att']}")
        st.write(f"S.Def: {stats['S.Def']}")
        st.write(f"Spd: {stats['Spd']}")
        st.text("")  # เพิ่มเว้นวรรคเพื่อให้แต่ละข้อมูลห่างจากกัน
