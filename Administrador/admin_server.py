import ast
from concurrent import futures
import grpc
import admin_pb2
import admin_pb2_grpc
from paho.mqtt import client as mqtt
import json

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Admin Server")
client.connect(mqttBroker)

dicionarioClient = dict()
dicionarioProduct = dict()
clientArray = []
productArray = []

class AdminServicer(admin_pb2_grpc.AdminServicer):  
    def inserirCliente(self, request_iterator, context):
        global dicionarioClient
        print("Inserir Cliente")
        reply = admin_pb2.inserirClienteReply()
        if request_iterator.clientId in dicionarioClient:
            reply.message = 'Cliente já existe!'         
        else: 
            clientArray.append([request_iterator.clientId, request_iterator.dadosCliente])
            dicionarioClient = dict(clientArray)
            client.publish("InserirCliente", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Inserção realizada: " + str(dicionarioClient))
            reply.message = 'Cliente inserido!'

        return reply
    def modificarCliente(self, request_iterator, context):
        global dicionarioClient
        print("Modificar Cliente")      
        reply = admin_pb2.modificarClienteReply()
        
        if request_iterator.clientId not in dicionarioClient:
            reply.message = 'Cliente não existe!'         
        else: 
            novosDados = json.loads(request_iterator.dadosCliente)
            dadosCliente = {"nome": novosDados['nome'], "sobrenome": novosDados['sobrenome']}
            dicionarioClient[request_iterator.clientId] = json.dumps(dadosCliente)
            client.publish("ModificarCliente", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Modificação realizada: " + str(dicionarioClient))
            reply.message = 'Cliente modificado!'

        return reply
    def recuperarCliente(self, request_iterator, context):
        global dicionarioClient
        print("Recuperar Cliente")

        reply = admin_pb2.recuperarClienteReply()
        
        if request_iterator.clientId not in dicionarioClient:
            reply.message = 'Cliente não existe!'         
        else: 
            dadosCliente = json.loads(dicionarioClient[request_iterator.clientId])
            reply.message = f"Cliente recuperado:\nNome - {dadosCliente['nome']}\nSobrenome - {dadosCliente['sobrenome']}"

        return reply
    def apagarCliente(self, request_iterator, context):
        global dicionarioClient
        print("Apagar Cliente")

        reply = admin_pb2.apagarClienteReply()
        
        if request_iterator.clientId not in dicionarioClient:
            reply.message = 'Cliente não existe!'         
        else: 
            dicionarioClient.pop(request_iterator.clientId)
            client.publish("ApagarCliente", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Cliente apagado realizada: " + str(dicionarioClient))
            reply.message = 'Cliente apagado!'

        return reply
    def inserirProduto(self, request_iterator, context):
        global dicionarioProduct
        print("Inserir Produto")
        reply = admin_pb2.inserirProdutoReply()
        if request_iterator.produtoId in dicionarioProduct:
            reply.message = 'Produto já existe!'         
        else: 
            productArray.append([request_iterator.produtoId, request_iterator.dadosProduto])
            dicionarioProduct = dict(productArray)
            client.publish("InserirProduto", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Cadastro realizado: " + str(dicionarioProduct))
            reply.message = 'Produto cadastrado!'

        return reply
    def modificarProduto(self, request_iterator, context):
        global dicionarioProduct
        print("Modificar Produto")      
        reply = admin_pb2.modificarProdutoReply()
        
        if request_iterator.produtoId not in dicionarioProduct:
            reply.message = 'Produto não existe!'         
        else: 
            novosDados = json.loads(request_iterator.dadosProduto)
            dadosProduto = {"nome": novosDados['nome'], "quantidade": novosDados['quantidade'], "preco": novosDados['preco']}
            dicionarioProduct[request_iterator.produtoId] = json.dumps(dadosProduto)
            client.publish("ModificarProduto", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Modificação realizada: " + str(dicionarioProduct))
            reply.message = 'Produto modificado!'

        return reply
    def recuperarProduto(self, request_iterator, context):
        global dicionarioProduct
        print("Recuperar Produto")

        reply = admin_pb2.recuperarProdutoReply()
        
        if request_iterator.produtoId not in dicionarioProduct:
            reply.message = 'Produto não existe!'         
        else: 
            dadosProduto = json.loads(dicionarioProduct[request_iterator.produtoId])
            print("Produto recuperado: " + str(dicionarioProduct))
            reply.message = f"Produto recuperado:\nNome - {dadosProduto['nome']}\nQuantidade - {dadosProduto['quantidade']}"

        return reply
    def apagarProduto(self, request_iterator, context):
        global dicionarioProduct
        print("Apagar Produto")

        reply = admin_pb2.apagarProdutoReply()
        
        if request_iterator.produtoId not in dicionarioProduct:
            reply.message = 'Produto não existe!'         
        else: 
            dicionarioProduct.pop(request_iterator.produtoId)
            client.publish("ApagarProduto", str(dicionarioClient) + '/' + str (dicionarioProduct))
            print("Produto apagado: " + str(dicionarioProduct))
            reply.message = 'Produto apagado!'

        return reply

    def on_message(client, userdata, message):
        print("Produtos cadastrados: ",ast.literal_eval(message.payload.decode("utf-8")))
        global dicionarioProduct
        dicionarioProduct = ast.literal_eval(message.payload.decode("utf-8"))

    client.loop_start()
    client.subscribe("ModificarPedido")
    client.subscribe("ApagarPedido")
    client.on_message = on_message
    
def serve():
    porta = input("Digite uma porta para abrir o servidor: ")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminServicer_to_server(AdminServicer(), server)
    server.add_insecure_port(f"localhost:{porta}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()