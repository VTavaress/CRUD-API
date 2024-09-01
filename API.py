from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
import sqlalchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1728@localhost/db_api'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apelido = db.Column(db.String(80), unique=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    stack = db.Column(db.JSON)

    def __repr__(self):
        return '<Pessoa %r>' % self.nome
    
    def to_dict(self):
        return {
            'id': self.id,
            'apelido': self.apelido,
            'nome': self.nome,
            'nascimento': self.nascimento.isoformat(),
            'stack': self.stack
        }

@app.route("/pessoas", methods=["POST"])
def cria_pessoa():
    body = request.get_json()

    try:
        # Verifica se todos os campos obrigatórios estão presentes
        if not all(k in body for k in ['apelido', 'nome', 'nascimento']):
            raise BadRequest('Os campos "apelido", "nome" e "nascimento" são obrigatórios.')

        # Valida o formato da data
        data_nascimento = datetime.strptime(body['nascimento'], '%Y-%m-%d').date()

        # Cria a pessoa
        pessoa = Pessoa(apelido=body['apelido'], nome=body['nome'], nascimento=data_nascimento, stack=body.get('stack'))
        db.session.add(pessoa)
        db.session.commit()
        return jsonify({'message': 'Pessoa criada com sucesso'}), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 422
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'error': 'Apelido já cadastrado.'}), 409
    except Exception as e:
        app.logger.error(f"Erro ao criar pessoa: {e}")
        return jsonify({'error': 'Erro interno do servidor.'}), 500
    
@app.route("/pessoas/<int:pessoa_id>", methods=["GET"])
def busca_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)

    if pessoa:
        return jsonify(pessoa.to_dict()), 200
    else:
        return jsonify({"error": f"Pessoa com ID {pessoa_id} não encontrada."}), 404
    
@app.route("/pessoas?t=:termo", methods=["GET"])
def busca_pessoas_por_termo():
    termo = request.args.get('t')

    if not termo:
        return jsonify({'error': 'O parâmetro "t" é obrigatório.'}), 400
    
    pessoas = Pessoa.query.filter(
        or_(
            Pessoa.apelido.ilike(f'%{termo}%'),
            Pessoa.nome.ilike(f'%{termo}%'),
        )
    ).all()

    return jsonify([pessoa.to_dict() for pessoa in pessoas]), 200

@app.route("/pessoas/<int:pessoa_id>", methods=["PUT"])
def atualiza_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)

    if not pessoa:
        raise NotFound(f"Pessoa com ID {pessoa_id} não encontrada.")

    data = request.get_json()

    try:
        pessoa.apelido = data['apelido']
        pessoa.nome = data['nome']
        pessoa.nascimento = datetime.strptime(data['nascimento'], '%Y-%m-%d').date()
        pessoa.stack = data.get('stack')
        db.session.commit()
        return jsonify({'message': 'Pessoa atualizada com sucesso'}), 200
    except BadRequest as e:
        return jsonify({'error': str(e)}), 422
    except Exception as e:
        app.logger.error(f"Erro ao atualizar pessoa: {e}")
        return jsonify({'error': 'Erro interno do servidor.'}), 500

@app.route("/pessoas/<int:pessoa_id>", methods=["DELETE"])
def deleta_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)

    if not pessoa:
        raise NotFound(f"Pessoa com ID {pessoa_id} não encontrada.")

    db.session.delete(pessoa)
    db.session.commit()

    return jsonify({'message': 'Pessoa excluída com sucesso'}), 200

if __name__ == "__main__":
    app.run(debug=True)
