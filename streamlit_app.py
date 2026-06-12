import streamlit as st

# 1. 데이터 정의
symptoms = ['두통', '복통', '감기', '근육통']
medicines = ['타이레놀', '부스코판', '판콜', '파스']

# 증상과 약을 매핑한 딕셔너리 생성
symptom_to_medicine = dict(zip(symptoms, medicines))

# 2. 웹 페이지 제목 및 레이아웃
st.title("💊 맞춤형 약 추천 시스템")
st.markdown("현재 겪고 계신 증상을 선택하시면 알맞은 약을 추천해 드립니다.")
st.divider()

# 3. 입력단 (스트림릿 위젯 활용)
# 사용자가 여러 증상을 동시에 선택할 수 있도록 multiselect 활용
selected_symptoms = st.multiselect(
    "👉 증상을 모두 선택해 주세요 (복수 선택 가능)",
    options=symptoms,
    placeholder="증상을 선택하세요"
)

# 4. 출력단 및 로직 처리
st.subheader("📋 약 추천 목록")

# 추천받기 버튼
if st.button("추천 약 확인하기", type="primary"):
    if selected_symptoms:
        take_list = []
        
        # 선택한 증상에 맞는 약을 리스트에 추가
        for symptom in selected_symptoms:
            medicine = symptom_to_medicine[symptom]
            take_list.append(medicine)
        
        # 결과 출력
        st.success(f"선택하신 증상 [{', '.join(selected_symptoms)}]에 대한 추천 결과입니다.")
        
        # 추천 리스트를 깔끔한 마크다운 문법으로 출력
        for item in take_list:
            st.write(f"✅ **{item}**")
    else:
        # 아무것도 선택하지 않고 버튼을 눌렀을 때
        st.warning("⚠️ 먼저 하나 이상의 증상을 선택해 주세요.")
else:
    st.info("증상을 선택한 후 '추천 약 확인하기' 버튼을 눌러주세요.")