import os
from flask import Flask, render_template, request
import requests

# --- الإعدادات النهائية ---
BOT_TOKEN = "8619445540:AAHiIeDhVVC3P3MNrvk2z4sZpzBz8NmVJBc"
CHAT_ID = "5953366331" 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "❌ لم يتم اختيار ملف", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "❌ اسم الملف فارغ", 400

    # إرسال الملف إلى تليجرام
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    files = {'document': (file.filename, file.stream, file.mimetype)}
    data = {
        'chat_id': CHAT_ID, 
        'caption': f"🚀 مبروك يا عمر! فيه ملف جديد وصل:\n📄 الاسم: {file.filename}"
    }

    try:
        response = requests.post(url, files=files, data=data)
        result = response.json()
        
        if result.get("ok"):
            return "✅ تم إرسال الملف بنجاح! شيك على التليجرام دلوقتي."
        else:
            return f"❌ خطأ من تليجرام: {result.get('description')}"
            
    except Exception as e:
        return f"❌ حدث خطأ فني: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
