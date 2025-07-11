# Housing Price Prediction

A machine learning web application that predicts house prices based on various property features using Linear Regression. This project provides an interactive web interface for users to input property details and receive price predictions.

## 🏠 Project Overview

This application uses a trained Linear Regression model to predict housing prices based on key property characteristics. The model was trained on a dataset containing various housing features and their corresponding prices.

## ✨ Features

- **Interactive Web Interface**: User-friendly Bootstrap-based web application
- **Real-time Predictions**: Instant price predictions based on input parameters
- **Multiple Input Features**: 
  - Area (in square feet)
  - Number of bedrooms
  - Number of bathrooms
  - Air conditioning availability
  - Furnishing status
- **Responsive Design**: Works on desktop and mobile devices
- **Simple Deployment**: Easy to run locally with Flask

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Pickle

## 📊 Dataset

The model is trained on a housing dataset with the following features:
- **price**: Target variable (house price)
- **area**: Property area in square feet
- **bedrooms**: Number of bedrooms
- **bathrooms**: Number of bathrooms
- **airconditioning**: Air conditioning availability (yes/no)
- **furnishingstatus**: Furnishing level (furnished/semi-furnished/unfurnished)

## 🚀 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Housing_price_prediction
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

3. **Train the model** (if needed):
   ```bash
   python model.py
   ```

## 🎯 Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Enter property details**:
   - **Area**: Property area in square feet (e.g., 5000)
   - **Bedrooms**: Number of bedrooms (e.g., 3)
   - **Bathrooms**: Number of bathrooms (e.g., 2)
   - **Air Conditioning**: Enter 0 for NO, 1 for YES
   - **Furnishing Status**: 
     - 0 for unfurnished
     - 0.5 for semi-furnished
     - 1 for furnished

4. **Click "Predict"** to get the estimated house price

## 📁 Project Structure

```
Housing_price_prediction/
├── app.py                 # Flask web application
├── model.py              # Model training script
├── model.pkl             # Trained model file
├── Housing.csv           # Dataset
├── templates/
│   ├── index.html        # Input form page
│   └── index1.html       # Results page
└── README.md            # This file
```

## 🔧 Model Details

- **Algorithm**: Linear Regression
- **Training Data**: 90% of the dataset
- **Test Data**: 10% of the dataset
- **Features**: 5 numerical features
- **Model Persistence**: Saved using pickle for easy deployment

## 📈 Model Features

The model considers the following features for price prediction:

1. **Area**: Property size in square feet
2. **Bedrooms**: Number of bedrooms
3. **Bathrooms**: Number of bathrooms
4. **Air Conditioning**: Binary feature (0/1)
5. **Furnishing Status**: Categorical feature encoded as:
   - 0: Unfurnished
   - 0.5: Semi-furnished
   - 1: Furnished

## 🎨 Web Interface

The application features a clean, responsive web interface with:
- Bootstrap 5 styling
- Form validation
- Clear input instructions
- Professional result display
- Mobile-friendly design

## 🔄 API Endpoints

- `GET /`: Main page with input form
- `POST /home`: Prediction endpoint that processes form data and returns results

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:
- Gunicorn or uWSGI as WSGI server
- Nginx as reverse proxy
- Environment variables for configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For questions or issues, please open an issue in the repository or contact the development team.

---

**Note**: This is a demonstration project for educational purposes. For real-world applications, consider using more sophisticated models and additional data validation.
