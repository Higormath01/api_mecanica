@app.route('/atualizar_clientes/<int:id_cliente>', methods=["PUT"])
def atualizar_clientes(id_cliente):
    db_session = local_session()
    try:
        dados = request.get_json()
        print(dados)
        cliente = db_session.execute(select(Cliente).where(Cliente.id_cliente == id_cliente)).first()
        print(Cliente)
        print("xxxxx")
        if not dados["nome"] or not dados["cpf"] or not dados["telefone"] or not dados["endereco"]:
            return jsonify({'error': 'Preencha todos os campos'})
        else:
            Cliente.nome = dados["nome"]
            Cliente.cpf = dados["cpf"]
            Cliente.telefone = dados["telefone"]
            Cliente.endereco = dados["endereco"]


            return jsonify({
                'mensagem': 'Cliente atualizado com sucesso!',
                'nome': cliente.nome,
                'cpf': cliente.cpf,
                'telefone': cliente.telefone,
                'endereco': cliente.endereco,

            })
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        db_session.close()
