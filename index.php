<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST['email']);
    $assunto = trim($_POST['assunto']);
    $mensagem = trim($_POST['mensagem']);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("E-mail inválido. Volte e tente novamente.");
    }

    $dados = escapeshellarg(json_encode([
        'email' => $email,
        'assunto' => $assunto,
        'mensagem' => $mensagem
    ]));

    $comando = "python3.13.exe main.py $dados";
    $saida = shell_exec($comando);
    
    if ($saida === null) {
    echo "Erro ao executar o Python.";
    } else {
    echo "<pre>$saida</pre>";
    }
}
?>
