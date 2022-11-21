import admin_pb2_grpc
import admin_pb2
import time
import grpc
import json

def run():
    porta = input("Digite uma porta para se conectar ao servidor: ")
    with grpc.insecure_channel(f'localhost:{porta}') as channel:
        stub = admin_pb2_grpc.AdminStub(channel)

        print("1. Inserir Cliente")
        print("2. Modificar Cliente")
        print("3. Recuperar Cliente")
        print("4. Apagar Cliente")
        print("5. Inserir Produto")
        print("6. Modificar Produto")
        print("7. Recuperar Produto")
        print("8. Apagar Produto")
        print("9. Sair")       

        while True:
            rpc_call = input("Selecione um serviço: ")
            if rpc_call == "1":
                clientId = input("Digite o ID do cliente:")
                nome = input("Digite o nome do cliente:")
                sobrenome = input("Digite o sobrenome do cliente:")
                dadosCliente = {"nome": nome, "sobrenome": sobrenome}

                request = admin_pb2.inserirClienteRequest(clientId = clientId, dadosCliente = json.dumps(dadosCliente))
                reply = stub.inserirCliente(request)
                print(reply.message)
            elif rpc_call == "2":
                clientId = input("Digite o ID do cliente:")
                nome = input("Digite o novo nome do cliente:")
                sobrenome = input("Digite o novo sobrenome do cliente:")
                dadosCliente = {"nome": nome, "sobrenome": sobrenome}

                request = admin_pb2.modificarClienteRequest(clientId = clientId, dadosCliente = json.dumps(dadosCliente))
                reply = stub.modificarCliente(request)
                print(reply.message)
            elif rpc_call == "3":
                clientId = input("Digite o ID do cliente:")
                request = admin_pb2.recuperarClienteRequest(clientId = clientId)
                reply = stub.recuperarCliente(request)
                print(reply.message)
            elif rpc_call == "4":
                clientId = input("Digite o ID do cliente:")
                request = admin_pb2.apagarClienteRequest(clientId = clientId)
                reply = stub.apagarCliente(request)
                print(reply.message)
            elif rpc_call == "5":
                produtoId = input("Digite o ID do produto:")
                nome = input("Digite o nome do produto:")
                quantidade = int(input("Digite a quantidade do produto:"))
                preco = int(input("Digite o preço do produto:"))
                dadosProduto = {"nome": nome, "quantidade": quantidade, "preco": preco}
                request = admin_pb2.inserirProdutoRequest(produtoId = produtoId, dadosProduto = json.dumps(dadosProduto))
                reply = stub.inserirProduto(request)
                print(reply.message)
            elif rpc_call == "6":
                produtoId = input("Digite o ID do produto:")
                nome = input("Digite o nome do produto:")
                quantidade = int(input("Digite a quantidade do produto:"))
                preco = int(input("Digite o preço do produto:"))
                dadosProduto = {"nome": nome, "quantidade": quantidade, "preco": preco}
                request = admin_pb2.modificarProdutoRequest(produtoId = produtoId, dadosProduto = json.dumps(dadosProduto))
                reply = stub.modificarProduto(request)
                print(reply.message)
            elif rpc_call == "7":
                produtoId = input("Digite o ID do produto:")
                request = admin_pb2.recuperarProdutoRequest(produtoId = produtoId)
                reply = stub.recuperarProduto(request)
                print(reply.message)
            elif rpc_call == "8":
                produtoId = input("Digite o ID do produto:")
                request = admin_pb2.apagarProdutoRequest(produtoId = produtoId)
                reply = stub.apagarProduto(request)
                print(reply.message)
            elif rpc_call == "9":
                return
            else:
                print("Serviço inválido!")

        

if __name__ == "__main__":
    run()