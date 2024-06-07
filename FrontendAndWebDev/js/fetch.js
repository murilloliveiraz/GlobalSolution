import { dados } from "./dados.js"

//esse fetch só funciona se estiver rodando o servidor local em python
export const getViagens = async () => {
    const url = `http://127.0.0.1:5000/viagens`
    const response = await fetch(url)
    const data = await response.json()

    return data.data
}

export const getViagensJson = () => {
    return dados.data
}