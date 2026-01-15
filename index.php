<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST['email']);
    $emailseguro = escapeshellarg($email);
    $assunto = escapeshellarg(trim($_POST['assunto']));
    $mensagem = escapeshellarg(trim($_POST['mensagem']));

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("E-mail inválido. Volte e tente novamente.");
    }

    $comando = "python3.13.exe main.py $emailseguro $assunto $mensagem 2>&1";
    $saida = shell_exec($comando);
    
    if ($saida === null) {
    echo "Erro ao executar o Python.";
    } else {
    echo "<pre>$saida</pre>";
    }
}
?>
