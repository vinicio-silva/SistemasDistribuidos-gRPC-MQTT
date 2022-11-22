import client_pb2_grpc
import client_pb2
import time
import grpc

def run():
    porta = input("Digite uma porta para se conectar ao servidor: ")
    with grpc.insecure_channel(f'localhost:{porta}') as channel:
        stub = client_pb2_grpc.ClientStub(channel)

        print("1. Criar Pedido")
        print("2. Modificar Pedido")
        print("3. Listar Pedido")
        print("4. Listar Pedidos")
        print("5. Apagar Pedido")
        print("6. Sair")       

        while True:
            rpc_call = input("Selecione um serviço: ")
            if rpc_call == "1":
                clientId = input("Digite o ID fornecido pelo Administrador:")
                request = client_pb2.criarPedidoRequest(clientId = clientId)
                reply = stub.criarPedido(request)
                print(reply.message)
            elif rpc_call == "2":
                clientId = input("Digite o ID fornecido pelo Administrador:")
                ordemId = input("Digite a ordem do seu pedido:")
                produto = input("Digite o nome do produto:")
                quantidade = int(input("Digite a quantidade do produto:"))
                request = client_pb2.modificarPedidoRequest(clientId = clientId, ordemId = ordemId, produto = produto, quantidade = quantidade)
                reply = stub.modificarPedido(request)
                print(reply.message)
            elif rpc_call == "3":
                clientId = input("Digite o ID fornecido pelo Administrador:")
                ordemId = input("Digite a ordem do seu pedido:")
                request = client_pb2.listarPedidoRequest(clientId = clientId, ordemId = ordemId)
                reply = stub.listarPedido(request)
                print(reply.message)
            elif rpc_call == "4":
                clientId = input("Digite o ID fornecido pelo Administrador:")
                request = client_pb2.listarPedidosRequest(clientId = clientId)
                reply = stub.listarPedidos(request)
                print(reply.message)
            elif rpc_call == "5":
                clientId = input("Digite o ID fornecido pelo Administrador:")
                ordemId = input("Digite a ordem do seu pedido:")
                request = client_pb2.apagarPedidoRequest(clientId = clientId, ordemId = ordemId)
                reply = stub.apagarPedido(request)
                print(reply.message)
            elif rpc_call == "6":
                break
            else:
                print("Serviço inválido!")

        

if __name__ == "__main__":
    run()