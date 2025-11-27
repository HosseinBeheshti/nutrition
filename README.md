# 🍽️ Nutrition Calculator - Interactive Meal Nutrition Analysis

A Google Colab-ready nutrition calculator with an interactive web-based GUI built using Gradio. Calculate the complete nutritional breakdown of your meals instantly!

## ✨ Features

- **Interactive Web Interface**: Easy-to-use Gradio GUI that runs directly in your browser
- **Comprehensive Nutrition Database**: 19 common ingredients with complete nutritional data
- **15 Nutritional Values Tracked**:
  - Calories, Carbohydrates, Fat, Protein
  - Saturated Fat, Trans Fat, Cholesterol
  - Sodium, Potassium, Dietary Fiber, Sugar
  - Vitamins A & C, Calcium, Iron
- **Real-time Calculations**: Instant total nutritional breakdown as you enter quantities
- **Shareable**: Generate public links to share with others
- **No Installation Required**: Runs instantly in Google Colab

## 🚀 Quick Start (Google Colab)

### Option 1: Direct Upload
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Upload notebook**
3. Upload `nutrition_calculator.ipynb` from this repository
4. Click **Runtime → Run all**
5. Click the Gradio link that appears
6. Start calculating!

### Option 2: From GitHub
1. Open [Google Colab](https://colab.research.google.com/)
2. Click **File → Open notebook → GitHub**
3. Enter: `HosseinBeheshti/nutrition`
4. Select `nutrition_calculator.ipynb`
5. Click **Runtime → Run all**

## 📊 Available Ingredients

The calculator includes these ingredients (with their standard units):

| Category | Ingredients |
|----------|-------------|
| **Grains** | Raw Rice (100g), Macaroni (100g), Flour/Sugar (100g) |
| **Proteins** | Meat (100g), Chicken/Turkey (100g), Salmon (100g), Shrimp (100g), Sausage (100g) |
| **Legumes** | Split Peas (100g), Lentils (100g), Beans/Chickpeas (100g) |
| **Dairy** | Egg (1 unit), Cheese (100g) |
| **Vegetables** | Onion (100g), Potato (100g), Herbs/Veg (10g) |
| **Others** | Oil (1 tbsp), Paste/Tomato (1 tbsp), Nuts (100g) |

## 💡 How to Use

1. **Run the notebook** - Execute all cells in Google Colab
2. **Open the GUI** - Click the generated Gradio link
3. **Enter quantities** - Input how much of each ingredient you used
   - Use whole numbers for units (e.g., `2` for 2×100g of rice)
   - Use decimals for partial amounts (e.g., `0.5` for half a tablespoon of oil)
4. **View results** - See instant nutritional breakdown in the output table

### Example Meals

**Simple Rice & Chicken:**
- Raw Rice: `1.5` (150g)
- Chicken/Turkey: `2` (200g)
- Oil: `2` (2 tbsp)
- Onion: `0.5` (50g)
- Herbs/Veg: `1` (10g)

**Pasta with Cheese:**
- Macaroni: `2` (200g)
- Cheese: `0.5` (50g)
- Oil: `1` (1 tbsp)
- Paste/Tomato: `1` (1 tbsp)

## 🛠️ Local Development

If you want to run this locally instead of in Colab:

```bash
# Clone the repository
git clone https://github.com/HosseinBeheshti/nutrition.git
cd nutrition

# Install dependencies
pip install -r requirements.txt

# Run as a Python script (optional - can also use Jupyter)
python -c "$(cat nutrition_calculator.ipynb | jq -r '.cells[].source | join("")')"
```

## 📦 Dependencies

- `gradio` - Web-based GUI framework
- `pandas` - Data manipulation and calculations
- `numpy` - Numerical operations

All dependencies are automatically installed when you run the notebook in Colab.

## 🎯 Technical Details

- **Calculation Method**: Vectorized matrix multiplication for efficiency
- **Data Structure**: Pandas DataFrame for easy manipulation
- **GUI Framework**: Gradio for instant web interface deployment
- **Precision**: All values rounded to 1 decimal place
- **Input Validation**: Negative values automatically reset to 0

## 📝 Notes

- All nutritional values are per standard unit (100g, 1 tbsp, 1 unit, etc.)
- Vitamin and mineral percentages are based on Daily Values (DV)
- The database can be easily extended by adding more ingredients to the `NUTRITION_DATA` dictionary
- Fractional quantities are supported for precise measurements

## 🤝 Contributing

Feel free to:
- Add more ingredients to the database
- Suggest additional nutritional values to track
- Improve the UI/UX
- Report issues or bugs

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Acknowledgments

Nutritional data compiled from standard USDA food composition databases and common food labels.

---

**Made with ❤️ for healthy eating and meal planning**