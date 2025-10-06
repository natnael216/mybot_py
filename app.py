from flask import Flask, request, render_template_string
from flask_cors import CORS
import hmac
import hashlib
import base64
import json

app = Flask(__name__)
CORS(app)

# Replace with your bot token from BotFather
BOT_TOKEN = "8339914644:AAFmp5_nsV3Cnpmy1rt-IR31CAMG0Ou74G0"  # e.g., "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
ALLOWED_CHANNEL_USERNAME = "grade9_biology"  # Your channel username without @

# Function to validate initData
def validate_init_data(init_data_str, bot_token):
    if not init_data_str:
        return False
    params = dict(param.split('=') for param in init_data_str.split('&'))
    if 'hash' not in params:
        return False
    
    check_hash = params.pop('hash')
    data_check_string = '\n'.join(f'{k}={v}' for k, v in sorted(params.items()))
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return calculated_hash == check_hash

# Function to get chat info
def get_chat_info(init_data):
    try:
        data = dict(param.split('=') for param in init_data.split('&'))
        chat_data = json.loads(base64.urlsafe_b64decode(data.get('chat_instance', '').encode() + b'==').decode())
        return chat_data.get('chat', {}).get('username')
    except Exception:
        return None

# Topic data
topics = {
    "ab1": {
        "title": "Unit 1: Introduction to Biology – 1.1 The Meaning and Importance of Biology",
        "content": """Biology is the scientific study of life or living things.
ባዮሎጂ ህይወት ወይም የህይወት ያላቸው ነገሮች ሳይንሳዊ ጥናት ነው።
What does it mean to be “alive”?
"ህይወት ያለው" መሆን ማለት ምን ማለት ነው?
It seems very difficult to objectively define life in a simple sentence. But, we recognize life mainly by common characteristics shared by living systems.
ህይወትን በአንድ ቀላል ዓረፍተ ነገር ብቻ መግለፅ በጣም ከባድ ይመስላል። ነገር ግን፣ ህይወትን የምንለየው በዋነኝነት ህይወት ባላቸው ስርዓቶች (living systems) በጋራ በሚታዩ ባህሪያት ነው።
Living things:
- are composed of one or more cells
- በአንድ ወይም ከአንድ በላይ በሆኑ ህዋሳት (cells) የተሠሩ ናቸው።
- are complex and highly ordered
- ውስብስብ እና ከፍተኛ የሆነ ቅደም ተከተል ያላቸው ናቸው።
- can respond to stimuli, grow, reproduce, etc.
- ለአካባቢ ለውጦች (stimuli) ምላሽ መስጠት፣ ማደግ፣ መራባት (reproduce) እና የመሳሰሉትን ማድረግ ይችላሉ።
- transmit genetic information to their offspring
- የዘር መረጃን (genetic information) ወደ ልጆቻቸው ያስተላልፋሉ።
- need the energy to accomplish work
- ሥራ ለማከናወን ኃይል (energy) ያስፈልጋቸዋል።
- can maintain relatively constant internal conditions (homeostasis)
- ውስጣዊ ሁኔታቸውን በአንፃራዊነት ቋሚ አድርገው ማቆየት ይችላሉ (ሆሞስታሲስ - homeostasis)።
- are capable of evolutionary adaptation to the environment
- ለአካባቢያቸው የዝግመተ ለውጥ (evolutionary) መላመድ የመቻል ችሎታ አላቸው።"""
    },
    "ab2": {
        "title": "Unit 1: Introduction to Biology – 1.2 The Methods of Studying Biology",
        "content": """What is a scientific study?
(ሳይንሳዊ ጥናት ማለት ምን ማለት ነው?)
Biologists study living things using a scientific method that involves asking questions, suggesting possible answers, and testing for the validity of the answers through experimentation.
ባዮሎጂስቶች ስለ ህይወት ያላቸው ነገሮች የሚያጠኑት ሳይንሳዊ ስነ-ዘዴን (scientific method) በመጠቀም ሲሆን፣ ይህ ስነ-ዘዴ ጥያቄዎችን መጠየቅ፣ ሊሆኑ የሚችሉ መልሶችን መጠቆም እና መልሶቹ ትክክል መሆናቸውን በሙከራ (experimentation) ማረጋገጥን ያካትታል።
The scientific method includes steps like observation, hypothesis, experimentation, and conclusion.
ሳይንሳዊ ስነ-ዘዴ መመልከቻ (observation)፣ ሀሳብ (hypothesis)፣ ሙከራ (experimentation) እና መደምደሚያ (conclusion) ያሉ እርምጃዎችን ይዟል።"""
    },
    "ab3": {
        "title": "Unit 1: Introduction to Biology – 1.3 The Branches of Biology",
        "content": """What comes to your mind when you hear the word science?
"ሳይንስ" የሚለውን ቃል ሲሰሙ ወደ አእምሮዎ የሚመጣው ምንድን ነው?
Biologists are always curious about why things happen or how things happen. By asking questions and seeking science-based responses known as the scientific method, they come up with new theories to explain new findings.
ባዮሎጂ ባለሙያዎች (Biologists) ነገሮች ለምን እንደሚሆኑ ወይም እንዴት እንደሚከሰቱ ሁል ጊዜ ጉጉት አላቸው። ሳይንሳዊ ስነ-ዘዴ (the scientific method) በመባል የሚታወቀውን፣ ጥያቄዎችን በመጠየቅ እና በሳይንስ ላይ የተመሠረተ ምላሽ በመፈለግ አዲስ ግኝቶችን (new findings) ለማስረዳት አዲስ ቲዎሪዎችን (theories) ይፈጥራሉ።
Branches of biology include botany, zoology, microbiology, and genetics.
ባዮሎጂ መጨረሻዎች (branches) መንገድ፣ የእንስሳት ምህንድ (zoology)፣ ማይክሮባዮሎጂ (microbiology) እና ጄኔቲክስ (genetics) ያካትታሉ።"""
    }
    # Add more topics here, e.g., "ab4": { "title": "New Topic", "content": "Content..." }
}

@app.route('/')
def index():
    init_data = request.args.get('init_data', '')
    topic_key = request.args.get('startapp')

    # Validate init_data
    if not validate_init_data(init_data, BOT_TOKEN):
        return render_template_string(
            html_template,
            title="Access Denied",
            content=f"This content is only available via our official channel: <a href='https://t.me/{ALLOWED_CHANNEL_USERNAME}' style='color: #55acee;'>@{ALLOWED_CHANNEL_USERNAME}</a>"
        )

    # Get chat username
    chat_username = get_chat_info(init_data)
    if chat_username != f"@{ALLOWED_CHANNEL_USERNAME}" and chat_username is not None:
        return render_template_string(
            html_template,
            title="Access Denied",
            content=f"This content is only available via our official channel: <a href='https://t.me/{ALLOWED_CHANNEL_USERNAME}' style='color: #55acee;'>@{ALLOWED_CHANNEL_USERNAME}</a>"
        )

    # Serve content
    topic = topics.get(topic_key)
    if topic:
        return render_template_string(
            html_template,
            title=topic["title"],
            content=topic["content"]
        )
    else:
        available_topics = "<br>".join(
            f'<a href="https://t.me/hkfdd_bot?startapp={key}" style="color: #55acee;">{topics[key]["title"]}</a>'
            for key in topics
        )
        return render_template_string(
            html_template,
            title="Grade 9 Biology Tutorials",
            content=f'Topic not found. Please select a valid topic from <a href="https://t.me/{ALLOWED_CHANNEL_USERNAME}" style="color: #55acee;">@{ALLOWED_CHANNEL_USERNAME}</a>.<br>Available topics:<br>{available_topics}'
        )

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Grade 9 Biology Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background-color: #1e1e2d;
            color: #fff;
            font-family: sans-serif;
            margin: 0;
            padding: 20px;
            user-select: none;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
        }
        ::selection { background: none; }
        html, body { height: 100%; }
        h1 {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 20px;
            color: #55acee;
            text-align: center;
        }
        p {
            white-space: pre-wrap;
            line-height: 1.6;
            margin-top: 20px;
            padding-top: 5px;
            padding-bottom: 5px;
        }
        #content-wrapper {
            max-width: 100%;
            padding: 0;
            margin: 0;
        }
        .error {
            color: #ff5555;
            text-align: center;
            font-size: 1.2rem;
        }
        @media screen {
            body:after {
                content: '';
                display: block;
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                pointer-events: none;
                background: rgba(0, 0, 0, 0);
                z-index: 9999;
            }
        }
    </style>
</head>
<body>
    <div id="content-wrapper">
        <h1>{{ title }}</h1>
        <p>{{ content | safe }}</p>
    </div>
    <script>
        if (window.Telegram && window.Telegram.WebApp) {
            window.Telegram.WebApp.ready();
            window.Telegram.WebApp.expand();
            window.Telegram.WebApp.setBackgroundColor('#1e1e2d');
            window.Telegram.WebApp.setHeaderColor('#1e1e2d');
        }
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
