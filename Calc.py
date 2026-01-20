import customtkinter as ctk

ctk.set_appearance_mode("Dark")

class GlassCalc(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Glass Calc Pro")
        self.geometry("380x680") 
        self.resizable(False, False)
        self.configure(fg_color="#0B0E14") 

        self.expression = ""

        # --- Display Panel ---
        self.display_container = ctk.CTkFrame(self, fg_color="transparent")
        self.display_container.pack(pady=(70, 30), padx=30, fill="x")

        self.result_label = ctk.CTkLabel(
            self.display_container,
            text="0",
            font=("Inter", 68, "bold"),
            text_color="#FFFFFF", 
            anchor="e"
        )
        self.result_label.pack(padx=10, fill="x")

        # --- Button Grid ---
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(padx=20, pady=10, expand=True, fill="both")

        for i in range(4):
            self.grid_frame.grid_columnconfigure(i, weight=1)

        self._build_grid()

    def _build_grid(self):
        buttons = [
            ('AC', 0, 0, 'glass_top'),
            ('±', 0, 1, 'glass_top'), 
            ('%', 0, 2, 'glass_top'),
            ('÷', 0, 3, 'glass_op'),
            ('7', 1, 0, 'glass_num'), 
            ('8', 1, 1, 'glass_num'), 
            ('9', 1, 2, 'glass_num'),
            ('×', 1, 3, 'glass_op'),
            ('4', 2, 0, 'glass_num'),
            ('5', 2, 1, 'glass_num'),
            ('6', 2, 2, 'glass_num'), 
            ('-', 2, 3, 'glass_op'),
            ('1', 3, 0, 'glass_num'),
            ('2', 3, 1, 'glass_num'),
            ('3', 3, 2, 'glass_num'),
            ('+', 3, 3, 'glass_op'),
            ('0', 4, 0, 'glass_wide'),                
            ('.', 4, 2, 'glass_num'), 
            ('=', 4, 3, 'glass_eq')
        ]

        colors = {
            'glass_num':  {"bg": "#242830",
                           "hover": "#323842", 
                           "text": "#FFFFFF", 
                           "border": "#404652"},
            'glass_wide': {"bg": "#242830", 
                           "hover": "#323842", 
                           "text": "#FFFFFF",
                           "border": "#404652"},
            'glass_top':  {"bg": "#3D4450",
                           "hover": "#4D5564", 
                           "text": "#FFFFFF",
                           "border": "#5D677A"},
            'glass_op':   {"bg": "#1F4E79",
                           "hover": "#2B6CB0",
                           "text": "#FFFFFF", 
                           "border": "#3182CE"},
            'glass_eq':   {"bg": "#2D3748", 
                           "hover": "#4A5568", 
                           "text": "#63B3ED",
                           "border": "#63B3ED"}
        }

        for (text, r, c, t) in buttons:
            style = colors[t]
            btn_width = 160 if t == 'glass_wide' else 76
            
            btn = ctk.CTkButton(
                self.grid_frame,
                text=text,
                width=btn_width,
                height=76,
                corner_radius=20, 
                font=("Inter", 26, "bold"),
                fg_color=style["bg"],
                hover_color=style["hover"],
                text_color=style["text"],
                border_width=2, 
                border_color=style["border"],
                command=lambda x=text: self._press(x)
            )
            
            if t == 'glass_wide':
                btn.grid(row=4, column=0, columnspan=2, padx=6, pady=8, sticky="nsew")
            else:
                btn.grid(row=r, column=c, padx=6, pady=8, sticky="nsew")

    def _press(self, key):
        if key == "AC":
            self.expression = ""
        elif key == "±":
            if self.expression.startswith("-"): self.expression = self.expression[1:]
            else: self.expression = "-" + self.expression
        elif key == "=":
            try:
                clean = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(clean)
                self.expression = str(int(result) if result % 1 == 0 else round(result, 4))
            except:
                self.expression = "Error"
        else:
            if len(self.expression) < 12:
                self.expression += str(key)
        
        self.result_label.configure(text=self.expression if self.expression else "0")

if __name__ == "__main__":
    app = GlassCalc()

    app.mainloop()


