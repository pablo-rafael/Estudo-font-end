/* comments
 - Variáveis: let
 */

 let botao = document.querySelector(".button-gen")
 let inputText = document.querySelector(".text-box");

async function gerarCodigo() {
    let textUser = document.querySelector(".text-box").value;
    let codeBloc = document.querySelector(".code-bloc");
    let codeResult = document.querySelector(".code-result");

    // Agora chamamos o seu servidor Python local
    let enderecoLocal = "http://127.0.0.1:5000/gerar";

    try {
        let resposta = await fetch(enderecoLocal, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: textUser })
        });
        
        let dados = await resposta.json();
        
        // O Python devolve um objeto com a propriedade "codigo"
        codeBloc.textContent = dados.codigo;
        codeResult.srcdoc = dados.codigo;
    } catch (erro) {
        console.error("Erro ao conectar com o servidor:", erro);
        codeBloc.textContent = "Erro ao gerar código. Verifique se o servidor Python está rodando.";
    }
}

botao.addEventListener("click", gerarCodigo);

inputText.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        gerarCodigo();
    }
});
