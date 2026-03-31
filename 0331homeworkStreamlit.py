import tkinter as tk
from tkinter import messagebox

def on_submit():
    name = entry_name.get()
    age = entry_age.get()
    agreed = var_agree.get()
    
    # 하단 텍스트 업데이트
    label_result.config(text=f"이름: {name}, 나이: {age}")
    
    if agreed:
        label_status.config(text="약관에 동의했습니다.", fg="#2e7d32", bg="#e8f5e9")
    else:
        label_status.config(text="약관에 동의하지 않았습니다.", fg="#c62828", bg="#ffebee")

# 메인 창 설정
root = tk.Tk()
root.title("사용자 입력 폼")
root.geometry("400x450")
root.configure(bg="white")

# 제목
tk.Label(root, text="사용자 입력 폼 🔗", font=("NanumGothic", 16, "bold"), bg="white").pack(pady=10, anchor="w", padx=20)

# 이름 입력 창
tk.Label(root, text="이름", bg="white").pack(anchor="w", padx=20)
entry_name = tk.Entry(root, bg="#f0f2f6", relief="flat")
entry_name.insert(0, "")
entry_name.pack(fill="x", padx=20, pady=5, ipady=8)

# 나이 입력 창 (간단하게 Entry로 구현)
tk.Label(root, text="나이", bg="white").pack(anchor="w", padx=20, pady=(10, 0))
entry_age = tk.Entry(root, bg="#f0f2f6", relief="flat")
entry_age.insert(0, "")
entry_age.pack(fill="x", padx=20, pady=5, ipady=8)

# 약관 동의 체크박스
var_agree = tk.BooleanVar(value=True)
chk_agree = tk.Checkbutton(root, text="약관에 동의합니다", variable=var_agree, bg="white", activebackground="white")
chk_agree.pack(anchor="w", padx=20, pady=10)

# 제출 버튼
btn_submit = tk.Button(root, text="제출", command=on_submit, fg="#d32f2f", bg="white", relief="groove", padx=10)
btn_submit.pack(anchor="w", padx=20, pady=10)

# 하단 결과 표시 영역
tk.Frame(root, height=1, bg="#dddddd").pack(fill="x", padx=20, pady=10)

label_result = tk.Label(root, text="이름: 이혜정, 나이: 24", bg="white", font=("NanumGothic", 10))
label_result.pack(anchor="w", padx=20)

label_status = tk.Label(root, text="약관에 동의했습니다.", fg="#2e7d32", bg="#e8f5e9", padx=10, pady=10)
label_status.pack(fill="x", padx=20, pady=10)

root.mainloop()
