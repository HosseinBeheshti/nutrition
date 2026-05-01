"""
Meal Nutrition Calculator — Samsung Health
Standalone Tkinter GUI (no external dependencies beyond numpy)
"""

import tkinter as tk
from tkinter import ttk, font
import numpy as np

# ── Nutrition Database ──────────────────────────────────────────────────────
# Per standard unit. Index order:
# [0=Calories, 1=Carbs, 2=Fat, 3=Protein, 4=SatFat, 5=TransFat,
#  6=Cholesterol, 7=Sodium, 8=Potassium, 9=Fiber, 10=Sugar,
#  11=VitA, 12=VitC, 13=Calcium, 14=Iron]

NUTRITION_DATA = {
    'Raw Rice (x 100g)':        [360, 79.5,  0.6,  7.0,  0.1, 0.0,   0,   1, 110,  1.0,  0.1,  0,  0,  0,  1],
    'Meat (x 100g)':            [250,  0.0, 17.0, 25.0,  6.5, 0.0,  75,  75, 300,  0.0,  0.0,  0,  0,  0, 10],
    'Chk/Turkey (x 100g)':      [165,  0.0,  3.6, 31.0,  1.0, 0.0,  85,  70, 450,  0.0,  0.0,  0,  0,  0,  4],
    'Salmon (x 100g)':          [208,  0.0, 13.0, 22.0,  3.0, 0.0,  60,  60, 490,  0.0,  0.0,  2,  0,  0,  5],
    'Shrimp (x 100g)':          [130,  0.0,  2.5, 25.0,  0.5, 0.0, 200, 100, 200,  0.0,  0.0,  0,  0,  1, 10],
    'Oil (x 1 tbsp)':           [120,  0.0, 13.5,  0.0,  2.0, 0.0,   0,   0,   1,  0.0,  0.0,  0,  0,  0,  0],
    'Split Peas (x 100g)':      [360, 60.3,  1.0, 24.5,  0.2, 0.0,   0,  15, 960, 25.0,  5.0,  0,  0,  1, 40],
    'Lentils (x 100g)':         [350, 60.1,  1.0, 25.0,  0.2, 0.0,   0,   5, 900, 30.0,  2.0,  0,  0,  1, 37],
    'Beans/Chickpeas (x 100g)': [350, 63.0,  6.0, 20.0,  0.6, 0.0,   0,  20, 870, 17.0, 11.0,  0,  0,  1, 37],
    'Egg (x 1 unit)':           [ 70,  0.6,  5.0,  6.0,  1.5, 0.0, 185,  70,  70,  0.0,  0.3,  4,  0,  2,  5],
    'Onion (x 100g)':           [ 40,  9.3,  0.1,  1.1,  0.0, 0.0,   0,   4, 145,  1.7,  4.2,  0, 10,  2,  1],
    'Paste/Tomato (x 1 tbsp)':  [ 20,  4.8,  0.1,  1.0,  0.0, 0.0,   0,  60, 160,  1.0,  3.0,  5, 10,  1,  4],
    'Herbs/Veg (x 100g)':       [ 30,  6.0,  0.5,  3.0,  0.1, 0.0,   0,  25, 300,  3.0,  1.0, 20, 10,  5, 15],
    'Macaroni (x 100g)':        [370, 74.0,  1.5, 13.0,  0.5, 0.0,   0,   5, 150,  3.0,  1.0,  0,  0,  1,  8],
    'Cheese (x 100g)':          [350,  3.1, 29.0, 25.0, 18.0, 0.0, 100, 620,  90,  0.0,  0.5, 10,  0, 72,  1],
    'Nuts (x 100g)':            [650, 21.0, 56.0, 22.0,  4.5, 0.0,   0,   1, 700, 12.0,  4.0,  0,  0,  7, 15],
    'Potato (x 100g)':          [ 75, 17.5,  0.1,  2.0,  0.0, 0.0,   0,   6, 420,  2.0,  0.8,  0, 30,  0,  3],
    'Flour/Sugar (x 100g)':     [400, 83.0,  1.0, 10.0,  0.3, 0.0,   0,   1, 100,  3.0,  0.2,  0,  0,  1, 10],
    'Sausage (x 100g)':         [300,  1.0, 28.0, 12.0, 10.0, 0.0,  60, 800, 200,  0.0,  1.0,  0,  0,  1,  5],
}

# Samsung Health "Add Food" field order: (display_label, unit, data_index, is_sub_nutrient)
SAMSUNG_HEALTH_FIELDS = [
    ('Calories',         'kcal',   0, False),
    ('Carbohydrates',    'g',      1, False),
    ('    Dietary Fiber','g',      9, True),
    ('    Sugar',        'g',     10, True),
    ('Fat',              'g',      2, False),
    ('    Saturated Fat','g',      4, True),
    ('    Trans Fat',    'g',      5, True),
    ('Protein',          'g',      3, False),
    ('Cholesterol',      'mg',     6, False),
    ('Sodium',           'mg',     7, False),
    ('Potassium',        'mg',     8, False),
    ('Vitamin A',        '% DV',  11, False),
    ('Vitamin C',        '% DV',  12, False),
    ('Calcium',          '% DV',  13, False),
    ('Iron',             '% DV',  14, False),
]


def calculate_nutrition(quantities: list) -> list:
    data_matrix = np.array(list(NUTRITION_DATA.values()), dtype=float)
    qty_array = np.array(quantities, dtype=float)
    result = data_matrix.T.dot(qty_array)
    result = np.clip(result, 0, None)
    return [round(float(v), 1) for v in result]


class NutritionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meal Nutrition Calculator  —  Samsung Health")
        self.configure(bg="#f0f2f5")
        self.geometry("740x800")
        self.minsize(700, 700)
        self._build_fonts()
        self._build_ui()

    def _build_fonts(self):
        self.font_title   = font.Font(family="Helvetica", size=13, weight="bold")
        self.font_sub_ttl = font.Font(family="Helvetica", size=9)
        self.font_header  = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_normal  = font.Font(family="Helvetica", size=10)
        self.font_small   = font.Font(family="Helvetica", size=9)
        self.font_cal     = font.Font(family="Helvetica", size=15, weight="bold")

    def _build_ui(self):
        # ── Title bar ─────────────────────────────────────────────────────────
        title_bar = tk.Frame(self, bg="#1565c0", pady=10)
        title_bar.pack(fill="x")
        tk.Label(title_bar, text="🍽️  Meal Nutrition Calculator",
                 font=self.font_title, bg="#1565c0", fg="white").pack()
        tk.Label(title_bar, text="Optimized for Samsung Health",
                 font=self.font_sub_ttl, bg="#1565c0", fg="#90caf9").pack()

        # ── Body ──────────────────────────────────────────────────────────────
        body = tk.Frame(self, bg="#f0f2f5")
        body.pack(fill="both", expand=True, padx=12, pady=10)
        body.columnconfigure(0, weight=3)
        body.columnconfigure(1, weight=2)
        body.rowconfigure(0, weight=1)

        # ── Left: scrollable ingredient list ──────────────────────────────────
        left = tk.LabelFrame(body, text=" Ingredients ",
                             font=self.font_header, bg="#f0f2f5",
                             padx=4, pady=4)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        left.rowconfigure(0, weight=1)
        left.columnconfigure(0, weight=1)

        inner = tk.Frame(left, bg="#f0f2f5")
        inner.grid(row=0, column=0, sticky="nsew")

        self._qty_vars = []
        self._qty_divisors = []
        for name in NUTRITION_DATA:
            short    = name.split('(')[0].strip()
            raw_unit = name.split('(')[1].rstrip(')')
            if '100g' in raw_unit:
                disp_unit, divisor = 'g', 100
            elif '10g' in raw_unit:
                disp_unit, divisor = 'g', 10
            elif 'tbsp' in raw_unit:
                disp_unit, divisor = 'tbsp', 1
            else:
                disp_unit, divisor = 'unit', 1

            var = tk.IntVar(value=0)
            self._qty_vars.append(var)
            self._qty_divisors.append(divisor)

            row = tk.Frame(inner, bg="#f0f2f5")
            row.pack(fill="x", padx=4, pady=2)

            tk.Label(row, text=short, font=self.font_normal,
                     bg="#f0f2f5", anchor="w", width=20).pack(side="left")
            tk.Label(row, text=disp_unit, font=self.font_small,
                     bg="#f0f2f5", fg="#777", anchor="w", width=9).pack(side="left")
            ttk.Spinbox(row, from_=0, to=9999, increment=1,
                        textvariable=var, width=6).pack(side="right")

        # ── Right: Nutrition Facts ────────────────────────────────────────────
        right = tk.LabelFrame(body, text=" Nutrition Facts (Samsung Health) ",
                              font=self.font_header, bg="#f0f2f5",
                              padx=10, pady=6)
        right.grid(row=0, column=1, sticky="nsew")

        self._result_vars: dict[int, tk.StringVar] = {}

        for label, unit, idx, is_sub in SAMSUNG_HEALTH_FIELDS:
            row = tk.Frame(right, bg="#f0f2f5")
            row.pack(fill="x", pady=1)

            val_var = tk.StringVar(value="0")

            if label == 'Calories':
                tk.Label(row, text=label, font=self.font_cal,
                         bg="#f0f2f5", anchor="w").pack(side="left")
                tk.Label(row, text=unit, font=self.font_small,
                         bg="#f0f2f5", fg="#777").pack(side="right", padx=(0, 2))
                tk.Label(row, textvariable=val_var, font=self.font_cal,
                         bg="#f0f2f5", fg="#1565c0").pack(side="right", padx=(0, 4))
                ttk.Separator(right, orient="horizontal").pack(fill="x", pady=3)
            else:
                lbl_font = self.font_small  if is_sub else self.font_normal
                lbl_fg   = "#666"           if is_sub else "#222"
                tk.Label(row, text=label, font=lbl_font,
                         bg="#f0f2f5", fg=lbl_fg, anchor="w").pack(side="left")
                tk.Label(row, text=unit, font=self.font_small,
                         bg="#f0f2f5", fg="#999").pack(side="right", padx=(0, 2))
                tk.Label(row, textvariable=val_var, font=lbl_font,
                         bg="#f0f2f5", fg=lbl_fg).pack(side="right", padx=(0, 4))
                if not is_sub:
                    ttk.Separator(right, orient="horizontal").pack(fill="x", pady=2)

            self._result_vars[idx] = val_var

        # ── Button bar ────────────────────────────────────────────────────────
        btn_bar = tk.Frame(self, bg="#f0f2f5")
        btn_bar.pack(fill="x", padx=12, pady=(0, 10))

        ttk.Button(btn_bar, text="  Calculate  ",
                   command=self._calculate).pack(side="left", padx=4)
        ttk.Button(btn_bar, text="  Reset  ",
                   command=self._reset).pack(side="left", padx=4)

    def _calculate(self):
        quantities = []
        for var, divisor in zip(self._qty_vars, self._qty_divisors):
            try:
                quantities.append(max(0.0, var.get()) / divisor)
            except tk.TclError:
                quantities.append(0.0)

        results = calculate_nutrition(quantities)
        for idx, str_var in self._result_vars.items():
            val = results[idx]
            str_var.set(str(int(val)) if idx == 0 else str(val))

    def _reset(self):
        for var in self._qty_vars:
            var.set(0)
        for str_var in self._result_vars.values():
            str_var.set("0")


if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop()
