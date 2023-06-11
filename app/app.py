from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/criar-instancias', methods=['POST'])
def criar_instancias():
    # Comandos para criar as instâncias usando Terraform
    comando_terraform = 'terraform init && terraform apply -auto-approve'
    subprocess.run(comando_terraform, shell=True)

    return jsonify({'message': 'Instâncias criadas com sucesso!'})

@app.route('/parar-instancias', methods=['POST'])
def parar_instancias():
    # Comandos para parar as instâncias usando AWS CLI
    comando_parar_instancias = 'aws ec2 stop-instances --instance-ids <ID1> <ID2> <ID3>'
    subprocess.run(comando_parar_instancias, shell=True)

    return jsonify({'message': 'Instâncias paradas com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
