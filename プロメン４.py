import streamlit as st
import pandas as pd
import requests

list_A = []
n = 0

list_kekka = ["得点", "ミス"]
list_syurui = ["DS", "BT", "SS", "PS", "NM", "7MT"]
list_iti = ["右", "左", "中"]
list_kosu = ["右上", "右下", "左上", "左下"]

st.title("スコア分析")

def nyuuryoku():
    global list_A, n
    unique_key = f"sebanngou_{len(list_A)}"
    unique_key_sokkou = f"sokkou_{len(list_A)}"
    unique_key_kekka = f"kekka_{len(list_A)}"
    unique_key_iti = f"iti_{len(list_A)}"
    unique_key_syurui = f"syurui_{len(list_A)}"
    unique_key_kosu = f"kosu_{len(list_A)}"
    unique_key_senntaku = f"senntaku_{len(list_A)}"

    sebanngou = st.number_input("背番号", 1, 100, 1, key=unique_key)

    sokkou = st.radio(label='速攻かどうか',
                      options=("FB", "QS", "なし"),
                      key=unique_key_sokkou)

    kekka = st.radio(label="結果を選択してください",
                           options=("得点", "ミス"),
                           key=unique_key_kekka)

    iti = st.selectbox(label="シュート位置を入力してください",
                         options=list_iti,key=unique_key_iti)

    syurui = st.selectbox(label="シュートの種類を選択してください",
                            options=list_syurui,key=unique_key_syurui)

    kosu = st.selectbox(label="コースを選択してください",
                          options=list_kosu,key=unique_key_kosu)

    senntaku = st.radio(label='入力を続けますか？',
                        options=("終了","続ける"),key=unique_key_senntaku)

    data = [sebanngou, sokkou, kekka, iti, syurui, kosu]
    list_A.append(data)

    if senntaku == "終了":
        n = 2
        st.write(list_A)

while n <1:
    nyuuryoku()
