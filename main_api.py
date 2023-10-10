from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
from flask import Flask, request
import requests
from typing import List


engine = create_engine('postgresql://postgres:password@localhost:5432/mydb')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class MyTable(Base):
    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, nullable=False)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    question_date = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)


app = Flask(__name__)


@app.route('/api/questions', methods=['POST'])
def questions_request():
    questions_num: int = int(request.json['questions_num'])

    while True:
        data: List[dict] = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()
        question_data = session.query(MyTable).filter_by(question_id=data[0]['id']).first()

        if not question_data:
            new_question = MyTable(
                question_id=data[0]['id'],
                question_text=data[0]['question'],
                answer_text=data[0]['answer']
            )
            session.add(new_question)
            session.commit()
            return data


if __name__ == '__main__':
    app.run(debug=True)
