# Resume Builder

A powerful and easy-to-use web application built with Django that helps users create professional resumes in minutes.

## 🚀 Features

- **Easy Data Entry**: Interactive multi-step form to input Personal Info, Education, Experience, and Skills.
- **Dynamic Forms**: Add multiple education and experience entries dynamically.
- **PDF Generation**: Instantly generate and download your resume as a PDF.
- **Professional Templates**: Choose from professional resume layouts (e.g., Executive, Modern).
- **Responsive Design**: Mobile-friendly interface with a sleek black & white aesthetic.

## 🛠️ Technology Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript
- **PDF Engine**: xhtml2pdf
- **Database**: SQLite (Default)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maneeshsshetty/Resume_Builder.git
   cd resume_builder
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash(use this requirements.txt file only when you have already installed all the dependencies and not working)
   pip install -r requirements.txt 
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 📝 Usage

1. Click on **"Get Started Now"** from the home page.
2. Fill in your personal details, professional summary, education, and work experience.
3. Advance through the steps using the **Next** button.
4. Review your information and click **"Save & Create Resume"**.
5. Select a template design from the options provided.
6. Your resume will be generated and downloaded as a PDF!


## 👤 Author

**Maneesh Shetty**
- [GitHub](https://github.com/maneeshsshetty)
- [LinkedIn](https://www.linkedin.com/in/maneeshsshetty/)
- [Gmail](maneeshsshettyy@gmail.com)
