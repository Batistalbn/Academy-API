from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from app.configs.database import db
from app.exception.type_error_exc import TypeNotAccepted


@dataclass
class TreinoModel(db.Model):
    id: int
    nome: str
    dia: str

    __tablename__ = 'treino'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    dia = Column(String, nullable=False)

    personal_id = db.Column(
      db.Integer, 
      db.ForeignKey('personal.id')
    )

    aluno_id = db.Column(
      db.Integer, 
      db.ForeignKey('aluno.id')
    )

    @validates("nome", "dia")
    def validate(self, key, value):
      if type(value) != str:
        raise TypeNotAccepted("As chaves passadas devem ser strings")