from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# بيانات البوت بتاعك (حط التوكن والـ ID بتوعك هنا)
BOT_TOKEN = "7916694602:AAH9S-I70V8XjN_C7F9I-YV8Q9X"
CHAT_ID = "6164508436"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # التأكد أن هناك ملف تم رفعه
    if 'file' not in request.files:
        return "لم يتم اختيار ملف"
    
    file = request.files['file']
    
    if file.filename == '':
        return "اسم الملف فارغ"

    if file:
        # إرسال الملف إلى تليجرام
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        files = {'document': (file.filename, file.read())}
        data = {'chat_id': CHAT_ID}
        
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            return "✅ تم إرسال الملف بنجاح إلى تليجرام!"
        else:
            return f"❌ فشل الإرسال. خطأ: {response.text}"

if __name__ == '__main__':
    app.run()
