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
                <p>${viagem.avaliacao_media} <em>(123)</em></p>
            </div>
            <h3>${viagem.nome}</h3>
            <div>
                <span class="material-symbols-outlined">
                    schedule
                    </span>
                <p>${viagem.qtd_dias} dias e ${viagem.qtd_noites} noites</p>
            </div>
            <p>R$ ${viagem.preco}</p>
        </div>
        <button>Reservar</button>
    </article>
    `
}

const carregarCards = async () => {
    const viagens = await getViagens()

    for (let viagem of viagens) {
        criarCards(viagem)
    }
}

const menuResponsivo = async () => {
    const btnOpen = document.querySelector('.open-menu')
    const btnClose = document.querySelector('.close-menu')
    const menu = document.querySelector('.nav-header-resp')

    //fecha o header quando clicar em alguma rota dele
    document.querySelectorAll('.nav-header-resp ul li a').forEach(a => {
        a.addEventListener('click', () => {
            menu.style.display = 'none'
            btnOpen.style.display = 'block'
            btnClose.style.display = 'none'
        })
    })

    btnOpen.addEventListener('click', () => {
        menu.style.display = 'block'
        btnOpen.style.display = 'none'
        btnClose.style.display = 'block'
    })

    btnClose.addEventListener('click', () => {
        menu.style.display = 'none'
        btnOpen.style.display = 'block'
        btnClose.style.display = 'none'
    })
}
await carregarCards()
menuResponsivo()