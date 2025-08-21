from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# DB設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p%40ssw0rd@localhost/sample'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# モデル定義
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String)
    age = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'test_name': self.test_name,
            'age': self.age
        }

# データ取得API
@app.route('/api/test', methods=['GET'])
def get_test_data():
    try:
        data = Test.query.order_by(Test.id).all()
        result = [item.to_dict() for item in data]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)