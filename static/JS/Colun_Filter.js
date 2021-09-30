// Criando e Recebendo valores por requerimento via elementos de um Identificador
button = document.getElementById("btn_enviar")
input_qtd_col = document.getElementById("input_qtd_col")
div_container = document.getElementById("select-container")

qtd_filhos = 0

// Função com o Intuito de Criar e Receber Relatórios de um Filtro
function Teste(){
    // Valor relacionado a quantidade colunas pelo usuário
    for(x = 0;x < qtd_filhos; x++){
        child = document.getElementById(x)
        div_container.removeChild(child)
    }
    num = input_qtd_col.value
    if(num > 100){
        return
    }

    // Criando um for para preencher o número de linhas requisitadas pelo usuário acima
    for(x = 0; x<num; x++){
        select = document.createElement("select")
        select.setAttribute("class", "form-select")
        select.setAttribute("name", x)
        select.setAttribute("id", x)
        select.style = "margin-top: 10px;"

        // Através de um formulário, receber os valores da tabela e adaptar ao tamanho da área selecionada
        option = document.createElement("option")
        option.setAttribute("selected", "selected")
        option.innerHTML = "Escolha Uma Coluna.."

        //
        select.appendChild(option)
        columns.forEach((iten)=> {
            option = document.createElement("option")
            option.setAttribute("value", iten)
            option.innerHTML = iten
            select.appendChild(option)
        })
        // Recebendo os valores de uma classe "filha"
        div_container.insertBefore(select, div_container.firstChild)
    }
    qtd_filhos = num
}

function VerificarValor(){
    if(qtd_filhos == 0 || qtd_filhos == null || qtd_filhos == undefined){
        button.setAttribute("disabled", "disabled")
    }
    else{
        button.removeAttribute("disabled")
    }

}
VerificarValor()

input_qtd_col.addEventListener("change", Teste)
input_qtd_col.addEventListener("change", VerificarValor)
