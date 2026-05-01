# 🍽️ Meal Nutrition Calculator — Samsung Health

A desktop GUI app for calculating the complete nutritional breakdown of your meals, with results displayed in **Samsung Health's field order** so you can quickly log food via the "Add custom food" screen.

## ✨ Features

- **Native Desktop GUI**: Standalone Tkinter window, no browser or internet needed
- **Samsung Health optimized**: Results panel matches Samsung Health's "Add custom food" field order exactly
- **19 ingredients** with complete nutritional data, integer gram inputs
- **15 nutritional values tracked**: Calories, Carbohydrates, Fat, Protein, Saturated Fat, Trans Fat, Cholesterol, Sodium, Potassium, Dietary Fiber, Sugar, Vitamins A & C, Calcium, Iron
- **Zero extra dependencies**: Only `numpy` required (Tkinter is built into Python)

## 🚀 Quick Start

```bash
git clone https://github.com/HosseinBeheshti/nutrition.git
cd nutrition
pip install -r requirements.txt
python3 nutrition_app.py
```

## 💡 How to Use

1. **Enter quantities** — type grams (or count for eggs/oil) for each ingredient you used
2. **Click Calculate** — results update instantly in the right panel
3. **Log to Samsung Health** — open Samsung Health → Food → **+** → "Add custom food" and copy each field from the results panel
4. **Click Reset** to start a new meal

### Example: Rice & Chicken meal

| Ingredient | Amount |
|---|---|
| Raw Rice | 150 g |
| Chk/Turkey | 200 g |
| Oil | 2 tbsp |
| Onion | 50 g |

## 📊 Nutrition Database

All values are per the listed standard unit. Sources: USDA FoodData Central and standard food labels.

| Ingredient | Unit | Cal | Carbs | Fat | Protein | Sat.Fat | Trans Fat | Chol | Na | K | Fiber | Sugar | Vit.A | Vit.C | Ca | Fe |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raw Rice | 100g | 360 | 79.5 | 0.6 | 7.0 | 0.1 | 0 | 0 | 1 | 110 | 1.0 | 0.1 | 0 | 0 | 0 | 1 |
| Meat | 100g | 250 | 0 | 17.0 | 25.0 | 6.5 | 0 | 75 | 75 | 300 | 0 | 0 | 0 | 0 | 0 | 10 |
| Chk/Turkey | 100g | 165 | 0 | 3.6 | 31.0 | 1.0 | 0 | 85 | 70 | 450 | 0 | 0 | 0 | 0 | 0 | 4 |
| Salmon | 100g | 208 | 0 | 13.0 | 22.0 | 3.0 | 0 | 60 | 60 | 490 | 0 | 0 | 2 | 0 | 0 | 5 |
| Shrimp | 100g | 130 | 0 | 2.5 | 25.0 | 0.5 | 0 | 200 | 100 | 200 | 0 | 0 | 0 | 0 | 1 | 10 |
| Oil | 1 tbsp | 120 | 0 | 13.5 | 0 | 2.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Split Peas | 100g | 360 | 60.3 | 1.0 | 24.5 | 0.2 | 0 | 0 | 15 | 960 | 25.0 | 5.0 | 0 | 0 | 1 | 40 |
| Lentils | 100g | 350 | 60.1 | 1.0 | 25.0 | 0.2 | 0 | 0 | 5 | 900 | 30.0 | 2.0 | 0 | 0 | 1 | 37 |
| Beans/Chickpeas | 100g | 350 | 63.0 | 6.0 | 20.0 | 0.6 | 0 | 0 | 20 | 870 | 17.0 | 11.0 | 0 | 0 | 1 | 37 |
| Egg | 1 unit | 70 | 0.6 | 5.0 | 6.0 | 1.5 | 0 | 185 | 70 | 70 | 0 | 0.3 | 4 | 0 | 2 | 5 |
| Onion | 100g | 40 | 9.3 | 0.1 | 1.1 | 0 | 0 | 0 | 4 | 145 | 1.7 | 4.2 | 0 | 10 | 2 | 1 |
| Paste/Tomato | 1 tbsp | 20 | 4.8 | 0.1 | 1.0 | 0 | 0 | 0 | 60 | 160 | 1.0 | 3.0 | 5 | 10 | 1 | 4 |
| Herbs/Veg | 100g | 30 | 6.0 | 0.5 | 3.0 | 0.1 | 0 | 0 | 25 | 300 | 3.0 | 1.0 | 20 | 10 | 5 | 15 |
| Macaroni | 100g | 370 | 74.0 | 1.5 | 13.0 | 0.5 | 0 | 0 | 5 | 150 | 3.0 | 1.0 | 0 | 0 | 1 | 8 |
| Cheese | 100g | 350 | 3.1 | 29.0 | 25.0 | 18.0 | 0 | 100 | 620 | 90 | 0 | 0.5 | 10 | 0 | 72 | 1 |
| Nuts | 100g | 650 | 21.0 | 56.0 | 22.0 | 4.5 | 0 | 0 | 1 | 700 | 12.0 | 4.0 | 0 | 0 | 7 | 15 |
| Potato | 100g | 75 | 17.5 | 0.1 | 2.0 | 0 | 0 | 0 | 6 | 420 | 2.0 | 0.8 | 0 | 30 | 0 | 3 |
| Flour/Sugar | 100g | 400 | 83.0 | 1.0 | 10.0 | 0.3 | 0 | 0 | 1 | 100 | 3.0 | 0.2 | 0 | 0 | 1 | 10 |
| Sausage | 100g | 300 | 1.0 | 28.0 | 12.0 | 10.0 | 0 | 60 | 800 | 200 | 0 | 1.0 | 0 | 0 | 1 | 5 |

> Units: Cal = kcal · Carbs/Fat/Protein/Sat.Fat/Trans.Fat/Fiber/Sugar = g · Chol/Na/K = mg · Vit.A/C/Ca/Fe = % Daily Value

## 📦 Dependencies

- `numpy` — vectorized calculation
- `tkinter` — GUI (built into Python, no install needed)

## 🎯 Technical Details

- **Calculation**: dot product of quantity vector × nutrition matrix (`numpy`)
- **GUI**: Tkinter — no server, no browser, works offline
- **Input**: integer grams for 100g-based items; count for eggs; tablespoons for oil and paste
- **Precision**: calories displayed as integers, all other values rounded to 1 decimal

## 📝 Notes

- Vitamin and mineral values are % Daily Value (DV) per standard unit
- Extend the database by adding rows to `NUTRITION_DATA` in `nutrition_app.py`
- The original Gradio notebook (`nutrition_calculator.ipynb`) is kept as a reference

## 🙏 Acknowledgments

Nutritional data compiled from USDA FoodData Central and standard food labels.

---

**Made with ❤️ for healthy eating and meal planning**