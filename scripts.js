/* comments
 - Variáveis: let
 */

 let botao = document.querySelector(".button-gen")
 let endereco = "https://api.groq.com/openai/v1/chat/completions"
 let inputText = document.querySelector(".text-box");

async function gerarCodigo() {
    let textUser = document.querySelector(".text-box").value;
    let codeBloc = document.querySelector(".code-bloc");
    let codeResult = document.querySelector(".code-result");

    let resposta = await fetch(endereco, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        },
        body: JSON.stringify({
            model: "llama-3.3-70b-versatile",
            messages: [{
                role: "system",
                content: "Você é um gerador de código HTML e CSS. Responda SOMENTE com código puro. NUNCA use crases, markdown ou explicações. Formato: primeiro <style> com o CSS, depois o HTML. Siga EXATAMENTE o que o usuário pedir. Se pedir algo quicando, use translateY no @keyframes. Se pedir algo girando, use rotate."
            },
            {
                role: "user",
                content: textUser
            }]
        })
    })
    
    let dados = await resposta.json()
    let resultado = dados.choices[0].message.content

    codeBloc.textContent = resultado
    codeResult.srcdoc = resultado
 }

 botao.addEventListener("click", gerarCodigo)

    inputText.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            gerarCodigo();
        }
    });
