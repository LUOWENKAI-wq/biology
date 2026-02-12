import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# --- 設定檔案名稱 (簡易資料庫) ---
DATA_FILE = "members_data.csv"

# --- 核心功能函數 ---

def get_next_thursday(start_date=None):
    """計算下一個週四的日期"""
    if start_date is None:
        start_date = datetime.now()
    
    # 0=Mon, 3=Thu. 計算距離下個週四還有幾天
    days_ahead = 3 - start_date.weekday()
    if days_ahead <= 0: # 如果今天是週四或週五週六，取下週四
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def load_data():
    """讀取資料，若無檔案則建立空表"""
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["姓名", "剩餘次數", "可參加日期", "最後繳費日"])

def save_data(df):
    """儲存資料"""
    df.to_csv(DATA_FILE, index=False)

# --- App 介面開始 ---
st.title("🏸 週四活動管理系統")

# 側邊欄：新增/繳費
st.sidebar.header("💰 繳費與新增")
name_input = st.sidebar.text_input("人員姓名")
amount_input = st.sidebar.selectbox("繳費金額", [100, 1000])

if st.sidebar.button("確認繳費"):
    if name_input:
        df = load_data()
        
        # 計算次數
        add_times = 10 if amount_input == 1000 else 1
        
        # 處理日期邏輯
        current_dates = []
        # 如果是舊成員，檢查他原本還有沒有剩餘日期
        if name_input in df["姓名"].values:
            user_row = df[df["姓名"] == name_input].iloc[0]
            existing_dates = str(user_row["可參加日期"])
            current_count = user_row["剩餘次數"]
            if existing_dates != "nan" and existing_dates != "":
                current_dates = existing_dates.split(", ")
        else:
            current_count = 0

        # 推算新的日期 (從最後一個有效日期往後推，或是從下週四開始)
        new_dates_list = []
        last_date_obj = datetime.now()
        
        if current_dates:
            # 如果還有剩，從最後一個日期往後推
            try:
                last_date_str = current_dates[-1]
                last_date_obj = datetime.strptime(last_date_str, "%Y-%m-%d")
            except:
                pass # 解析失敗就從今天算

        # 產生新日期
        base_date = last_date_obj
        for _ in range(add_times):
            base_date = get_next_thursday(base_date)
            new_dates_list.append(base_date.strftime("%Y-%m-%d"))
        
        # 更新數據
        final_dates = current_dates + new_dates_list
        new_total = current_count + add_times
        
        # 寫入 DataFrame
        if name_input in df["姓名"].values:
            df.loc[df["姓名"] == name_input, "剩餘次數"] = new_total
            df.loc[df["姓名"] == name_input, "可參加日期"] = ", ".join(final_dates)
            df.loc[df["姓名"] == name_input, "最後繳費日"] = datetime.now().strftime("%Y-%m-%d")
        else:
            new_row = pd.DataFrame({
                "姓名": [name_input],
                "剩餘次數": [new_total],
                "可參加日期": [", ".join(final_dates)],
                "最後繳費日": [datetime.now().strftime("%Y-%m-%d")]
            })
            df = pd.concat([df, new_row], ignore_index=True)
            
        save_data(df)
        st.sidebar.success(f"{name_input} 繳費成功！新增 {add_times} 次。")
    else:
        st.sidebar.error("請輸入姓名")

# --- 主畫面：儀表板 ---
df = load_data()

if not df.empty:
    # 1. 提醒名單 (剩餘次數 <= 2)
    st.subheader("⚠️ 續費提醒名單 (剩餘 <= 2次)")
    alert_list = df[df["剩餘次數"] <= 2]
    
    if not alert_list.empty:
        for index, row in alert_list.iterrows():
            st.error(f"🔴 **{row['姓名']}** 只剩 {row['剩餘次數']} 次！")
    else:
        st.info("目前沒有人需要補費。")

    st.markdown("---")

    # 2. 所有成員列表
    st.subheader("📋 成員詳細資料")
    st.dataframe(df)

    # 3. 查詢特定人日期
    st.markdown("---")
    st.subheader("🔍 查詢可參加日期")
    search_name = st.selectbox("選擇成員", df["姓名"].unique())
    if search_name:
        user_info = df[df["姓名"] == search_name].iloc[0]
        dates = str(user_info["可參加日期"]).split(", ")
        st.write(f"**{search_name}** 的額度還能參加以下日期：")
        st.write(dates)

else:
    st.info("目前資料庫是空的，請從左側新增人員。")
