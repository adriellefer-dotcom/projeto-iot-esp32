# Projeto IoT com ESP32

Projeto acadêmico de Internet das Coisas (IoT) desenvolvido com ESP32, sensor DHT11, relé e integração com a plataforma ThingSpeak para monitoramento de temperatura e umidade.

## 📌 Sobre o projeto

O projeto foi desenvolvido como atividade acadêmica com o objetivo de aplicar conceitos de Internet das Coisas em um sistema capaz de realizar leituras de sensores, tomar decisões com base nos valores obtidos e enviar informações para uma plataforma de monitoramento.

O ESP32 realiza a leitura de temperatura e umidade utilizando o sensor DHT11. A partir dos valores identificados, o sistema pode acionar um relé quando determinadas condições são atingidas.

Os dados coletados também são enviados para a plataforma ThingSpeak, permitindo o acompanhamento das informações.

## 🚀 Funcionamento

O sistema realiza as seguintes etapas:

1. Conecta o ESP32 à rede Wi-Fi.
2. Realiza a leitura de temperatura e umidade através do sensor DHT11.
3. Analisa os valores obtidos.
4. Aciona o relé quando as condições programadas são atingidas.
5. Envia os dados para a plataforma ThingSpeak.
6. Aguarda um intervalo definido.
7. Realiza uma nova leitura.

## ⚙️ Regras implementadas

O sistema foi configurado para acionar o relé quando:

- A temperatura ultrapassa 31 °C; ou
- A umidade ultrapassa 70%.

As leituras são realizadas periodicamente e enviadas para monitoramento.

## 🛠️ Tecnologias e componentes utilizados

### Hardware

- ESP32
- Sensor DHT11
- Módulo relé

### Software

- MicroPython
- Python
- ThingSpeak
- Comunicação Wi-Fi

## 📂 Organização do projeto

- `iot_esp32.py` — código principal responsável pela execução do projeto
- `wifi_lib.py` — funções utilizadas para conexão do ESP32 à rede Wi-Fi

As credenciais de Wi-Fi e a chave da API do ThingSpeak foram removidas da versão pública do projeto e substituídas por valores de exemplo.

## 🔐 Segurança

Informações sensíveis, como senha da rede Wi-Fi e chave de API, não são disponibilizadas neste repositório público.

Para executar o projeto em um ambiente próprio, essas informações devem ser configuradas localmente.

## 🎓 Contexto acadêmico

Este projeto foi desenvolvido como parte do processo de aprendizagem em Internet das Coisas durante a formação em Análise e Desenvolvimento de Sistemas.

A atividade possibilitou integrar programação, hardware, sensores, comunicação de rede e serviços de monitoramento em uma aplicação prática.

## 📚 Aprendizados

Durante o desenvolvimento foram trabalhados conceitos relacionados a:

- Internet das Coisas
- ESP32
- MicroPython
- Sensores
- Leitura de dados
- Automação
- Comunicação Wi-Fi
- Acionamento de dispositivos
- APIs
- Envio de dados para plataformas de monitoramento
- Integração entre hardware e software

## 🔄 Evolução futura

O projeto poderá receber melhorias como novos sensores, novas regras de automação, aprimoramentos no monitoramento dos dados e expansão das possibilidades de controle do sistema.

---

**Projeto desenvolvido para fins acadêmicos e de aprendizagem.**
