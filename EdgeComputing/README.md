# Projeto de Controle de Maré

<img src="https://github.com/murilloliveiraz/GlobalSolution/blob/main/EdgeComputing/circuit.png">

Este repositório contém o código-fonte e a documentação para um projeto de controle de maré. O projeto utiliza um sensor ultrassônico para medir a altura da maré, exibe as informações em um display LCD e aciona um buzzer em caso de perigo.

🔗 Circuito no TinkerCad: https://www.tinkercad.com/things/9omg3dVk7dd-global-solution-fiap?sharecode=a2v0QfoG7mpYKrt5R-Qqo7XeN1Uewlqb1aoiegAbvFg

## Funcionalidades

- **Medição da Altura da Maré:** Utiliza um sensor ultrassônico para medir a altura da maré em tempo real.
- **Exibição de Dados:** Mostra a altura da maré em um display LCD para fácil visualização.
- **Alerta de Perigo:** Aciona um buzzer se a altura da maré ultrapassar um nível seguro pré-definido.

## Componentes Utilizados

- **Arduino Uno:** Microcontrolador principal do projeto.
- **Sensor Ultrassônico HC-SR04:** Para medir a altura da maré.
- **Display LCD 16x2:** Para exibir a altura da maré.
- **Buzzer:** Para alertar sobre condições de perigo.
- **Protoboard e Fios Jumpers:** Para montar e testar o circuito.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/murilloliveiraz/GlobalSolution/tree/main/EdgeComputing
   ```
2. Instale as bibliotecas necessárias no Arduino IDE:
   - LiquidCrystal

3. Carregue o código no Arduino Uno através do Arduino IDE.

## Utilização

1. Conecte os componentes aos pinos correspondentes no Arduino conforme indicado no arquivo `circuit.png`.
2. Carregue o código e abra o monitor serial no Arduino IDE para visualizar os dados em tempo real.
3. Observe a exibição da altura da maré no display LCD.
4. Se a altura da maré ultrapassar o nível de segurança, o buzzer será acionado automaticamente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para sugestões de melhorias ou para enviar pull requests.

---

Este projeto é uma ferramenta importante para monitorar a altura da maré, proporcionando segurança e informações em tempo real. Seja bem-vindo a explorar, utilizar e melhorar este projeto!

---

## Integrantes:

- David Murillo de Oliveira Soares (RM 559078)
- Yasmin Gonçalves Coelho (RM 559147)
