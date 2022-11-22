# SistemasDistribuidos-gRPC-MQTT
Trabalho realizado na disciplina de Sistemas Distribuídos <br>
Link para referência https://paulo-coelho.github.io/ds_notes/projeto/#etapa-1-usuariosportais

# Execução
Para executar o trabalho deve-se entrar na pasta Administrador e executar os seguintes comandos:<br>

Terminal 1 - python3 admin_server <br>
Digite uma porta para iniciar o servidor do Administrador. <br>
Terminal 2 - python3 admin <br>
Digite a mesma porta para iniciar a conexão. <br>

Na pasta Cliente:<br>

Terminal 3 - python3 cliente_server <br>
Digite uma porta para iniciar o servidor do Cliente. <br>
Terminal 4 - python3 cliente <br>
Digite a mesma porta para iniciar a conexão. <br>

Isso irá iniciar os servidores e os respectivos paineis. <br>

Para realizar os testes, basta usar o menu do admin e cliente<br>

O mecanismo de comunicação entre o cliente e o cliente_server é o GRPC <br>
O mecanismo de comunicação entre o admin e o admin_server  é o GRPC <br>
E entre o cliente_server e admin_server é utilizado o MQTT <br>

### Esquema de dados na tabela

Dicionario cliente tem como chave o clientId e como dados: nome e sobrenome<br>
Dicionario produto tem como chave o productId e como dados: nome, quantidade e preço<br>
Dicionario pedido tem como chave o ordemID e como dados: clientId, produto, quantidade e total<br>