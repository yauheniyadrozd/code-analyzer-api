from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect('analyzer.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS reviews
                    (
                        id
                        INTEGER
                        PRIMARY
                        KEY,
                        code
                        TEXT,
                        score
                        INTEGER,
                        issues
                        TEXT
                    )''')
    return conn


def check_code(code):
    score = 100
    issues = []

    for i, line in enumerate(code.split('\n'), 1):
        if len(line) > 80:
            issues.append(f"Line {i} too long")
            score -= 5

    if 'TODO' in code:
        issues.append("Has TODO")
        score -= 10

    return max(score, 0), issues


@app.route('/health')
def health():
    return {'status': 'ok'}


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' in request.files:
        code = request.files['file'].read().decode()
    else:
        code = request.json.get('code', '')

    score, issues = check_code(code)

    db = get_db()
    cur = db.cursor()
    cur.execute('INSERT INTO reviews (code, score, issues) VALUES (?, ?, ?)',
                (code, score, str(issues)))
    db.commit()

    return {'score': score, 'issues': issues}


@app.route('/reviews')
def reviews():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT score, issues FROM reviews')
    return {'reviews': [{'score': r[0], 'issues': eval(r[1])} for r in cur.fetchall()]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)