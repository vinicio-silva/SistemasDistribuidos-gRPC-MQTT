# SistemasDistribuidos-gRPC-MQTT
Trabalho realizado na disciplina de Sistemas Distribuídos <br>
Link para referência https://paulo-coelho.github.io/ds_notes/projeto/#etapa-1-usuariosportais

# Execução
Para executar o trabalho deve-se entrar na pasta Administrador e executar os seguintes comandos:<br>

Terminal 1 - python3 admin_server.py <br>
Digite uma porta para iniciar o servidor do Administrador. <br>
Terminal 2 - python3 admin.py <br>
Digite a mesma porta para iniciar a conexão. <br>

Na pasta Cliente:<br>

Terminal 3 - python3 cliente_server.py <br>
Digite uma porta para iniciar o servidor do Cliente. <br>
Terminal 4 - python3 cliente.py <br>
Digite a mesma porta para iniciar a conexão. <br>

Isso irá iniciar os servidores e os respectivos paineis. <br>

Para realizar os testes, basta usar o menu do admin.py e cliente.py<br>

O mecanismo de comunicação entre o cliente.py e o cliente_server.py foi o GRPC <br>
O mecanismo de comunicação entre o admin.py e o admin_server.py  foi o GRPC <br>
E entre o cliente_server e admin_server foi utilizado o MQTT <br>

### Esquema de dados na tabela

Dicionario cliente tem como chave o clientId e como dados: nome e sobrenome<br>
Dicionario produto tem como chave o productId e como dados: nome, quantidade e preço<br>
Dicionario pedido tem como chave o ordemID e como dados: clientId, produto, quantidade e total<br>