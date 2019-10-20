<?php

$hostname = "Seu Servidor";
$user = "User do banco";
$passaword = "A senha do banco";
$database = "nome do banco";
$conexao = mysqli_connect($hostname,$user,$passaword,$database);

if(!$conexao){
    print "Falha na conexão com o banco";
}

?>