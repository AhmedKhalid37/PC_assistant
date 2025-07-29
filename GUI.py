import tkinter as tk
from tkinter import scrolledtext


# Gui: Orabi 
class User_Interface : 
    def __init__(self):
        # Create the main application window إنشاء نافذة التطبيق الرئيسية
        self.root = tk.Tk()
        self.root.title("Smart Desktop Assistant")  # Window Title عنوان النافذة
        self.root.geometry("600x500")  # Window Size حجم النافذة

        # Input label - تسمية حقل الإدخال
        self.input_label = tk.Label(self.root, text="Enter your command:")
        self.input_label.pack(pady=(10, 0))  # مسافة من الأعلى

        # Input Text Box - صندوق الإدخال
        self.input_box = tk.Entry(self.root, font=("Arial", 14))
        self.input_box.pack(fill="x", padx=10, pady=5)

        # Output label - تسمية حقل المخرجات
        self.output_label = tk.Label(self.root, text="Assistant Response:")
        self.output_label.pack(pady=(10, 0))

        # Output display - uneditable by the user (غير قابل للتعديل من قبل المستخدم)
        # Results from the LLM منطقة عرض النتائج (LLM نظام)
        self.output_area = scrolledtext.ScrolledText(self.root, height=5, font=("Arial", 12))
        self.output_area.pack(fill="both", padx=10, pady=5)
        self.output_area.config(state="disabled")  # for review only نجعلها للعرض فقط

        # Log/Status label
        self.log_label = tk.Label(self.root, text="Log / Status:")
        self.log_label.pack(pady=(10, 0))

        # Log/Status area - منطقة تسجيل العمليات
        self.log_area = scrolledtext.ScrolledText(self.root, height=8, font=("Courier", 10))
        self.log_area.pack(fill="both", padx=10, pady=5)
        self.log_area.config(state="disabled")

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.handle_command)
        self.submit_button.pack(pady=10)

        # Bind Enter key to the same handler ربط زر الإدخال Enter بنفس الدالة
        self.root.bind('<Return>', lambda event: self.handle_command())

    # Temporary intent handler stub function
    # NOTE: This part should be edited ---> results from LLM or System are shown here
    # وظيفة مؤقتة فقط لعرض الاستجابة
    def handle_command(self):
        command = self.input_box.get()  # الحصول على الأمر من المستخدم

        # نعرضه في خانة الـ output
        self.output_area.config(state="normal")
        self.output_area.delete(1.0, "end")
        self.output_area.insert("end", f"You said: {command}\n(This will be processed soon)")
        self.output_area.config(state="disabled")

        # تسجيل في السجل
        self.log_area.config(state="normal")
        self.log_area.insert("end", f"[LOG] Received command: {command}\n")
        self.log_area.config(state="disabled")

        self.input_box.delete(0, "end")  # تفريغ خانة الإدخال

    # Start the Tkinter main loop بدء تشغيل واجهة التطبيق
    def run(self):
        self.root.mainloop()

