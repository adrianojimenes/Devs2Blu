from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

    @validator('nome')
    def validar_nome(cls, value):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O Nome deve ter nome minimo 3 espacos')

alunos = [
    Aluno(id=1, nome="Adriano Cezar Gonçalves Jimenes", idade=33, email="adriano@email"),
    Aluno(id=2, nome="Marcio de Oliveira Santos", idade=30, email="cezar@email")
]