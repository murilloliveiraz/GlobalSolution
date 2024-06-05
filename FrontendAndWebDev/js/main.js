'use strict'

import { getViagens } from "./fetch.js"

const criarCards = (viagem) => {
    const containerViagens = document.getElementById('cardsCarousel')

    containerViagens.innerHTML += `
    <article class="card">
        <img src=${viagem.imagem} alt="Destino 1">
        <div class="card-text">
            <div class="rating">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#FFFF55"><path d="m354-287 126-76 126 77-33-144 111-96-146-13-58-136-58 135-146 13 111 97-33 143ZM233-120l65-281L80-590l288-25 112-265 112 265 288 25-218 189 65 281-247-149-247 149Zm247-350Z"/></svg>
                <p>5 <em>(123)</em></p>
            </div>
            <h3>${viagem.nome}</h3>
            <div>
                <span class="material-symbols-outlined">
                    schedule
                    </span>
                <p>${viagem.qtd_dias} dias e ${viagem.qtd_noites} noites</p>
            </div>
            <p>R$ 899.00</p>
        </div>
        <button>Reservar</button>
    </article>
    `
}

const carregarCards = async () => {
    const viagens = await getViagens()

    for (let viagem of viagens){
        criarCards(viagem)
    }
}

await carregarCards()