# Aplicativo Imperial Personal Finance
    Aplicativo de Finanças Pessoais desenvolvido em Python 3.12
        utilizando conceitos de Clean Architecture e DDD

# Comentários
    Existem várias formas de se aplicar os conceitos da Clean Architecture e do 
        DDD, visto que eles são linhas de ação e estratégias, e não orientações
        rígidas sobre o "como" fazer.
    A abordagem que utilizo aqui é a minha proposta para a sua utilização,
        usando o Python como ferramenta.
    Longe de pretender ser a melhor, é a minha, é a que eu utilizo.
    Eu acredito que a melhor forma de desenvolver os produtos usando esses
        dois conceitos, e se manter fiel a eles, é começar de dentro para fora.
    Investir mais tempo no núcleo do conceito, que normalmente é também, o 
        que encapsula e resolve as necessidades dos stakeholders e proporciona
        ganho ao negócio.
    E, enquanto avançamos no processo de desenvolvimento, se nos depararmos
        com uma necessidade específica de um recurso que não temos ainda
        disponível, é hora de rever as fronteiras que estabelecemos. 
    Não se pode depender numa camada interna de algo que ainda não temos. 
    Se não temos, ou não usamos ou abstraímos, simples assim.
    Neste simples Sistema de Finanças Pessoais, alguns pontos eu também preciso
        explicar e salientar.
    Um deles é que tentei evitar ao máximo o uso de frameworks. Nada como um
        puro suco de fruta em detrimento de suco de caixinha com imensa 
        quantidade de conservantes e adoçantes que não escolhemos consumir e
        não sabemos o bem, ou principalmente o mal, que poderão nos causar no 
        futuro.
    Mas sem radicalismos. Não se precisa reinventar a roda.
    Outro ponto é que uso UUID's tipo 4 como chaves primárias. Essa escolha 
        tem vantagens e desvantagens.
    A principal vantagem é que quando de uma requisição GET em um browser, 
        corremos o risco de expor a id de um produto/cliente/artigo etc. 
        Muitas empresas não percebem que expondo a id, dão margem à concorrência
        para descobrir algumas informações relevantes. Por exemplo. Se uma
        empresa tem 10 anos de mercado e numa requisição GET eu vejo algo do tipo
        .../cliente_list/10000... seria razoável pensar que ela obtém um
        crescimento médio de 1000 clientes ao ano. Isso pode ser evitado com
        o uso de UUID's como chave primária.
    A desvantagem é que o armazenamento de UUID's (mesmo comprimidas como hexa)
        consome mais recursos que a de um inteiro (tradicionalmente usado nos
        campos auto-incrementos). E as UUID's tipo 4 não tem 100% de garantia
        de unicidade, embora a probabilidade de repetições seja desprezível. 
        E, sendo maior, também consome mais tempo de leitura/escrita. No 
        entanto essas questões pesam mais em grandes volumes de dados. Neste
        sistema que desenvolvi, esses pontos não são tão impactantes no
        todo. Por isso a minha opção em usá-los. Mas, sugiro a seguinte
        avaliação: grandes volumes de dados e de leitura/escrita,
        use auto-incremento tradicional; pequenos volumes aonde pode ser
        interessante ocultar o mínimo de informações, considere o uso de UUIDs.
        Aqui optei pelas UUID's também pela questão didática.
    Outro ponto que devo mencionar é que uso testes. Sei que é chato, é monótono,
        é maçante desenvolver. Afinal, vamos deixar de construir maravilhosos e
        elaborados algoritmos que nos desafiam, para poder usar o tempo para
        inserir centenas de asserts. Mas... Se um dia um cliente te acordar de
        madrugada dizendo que o sistema parou e você tiver de sair correndo para
        tentar descobrir o que houve e depois sofrer as consequências disso, 
        você vai lembrar do que te digo aqui.
    Mas não seja ou Tester Fake. Que cria uma meia dúzia de testes e acha que 
        está implantando TDD. Não faça isso. 
    Confesso que ao longo dos meus 40 anos de desenvolvimento, só recentemente 
        adotei os testes. E como, mea-culpa, tenho uma tendência a ser
        perfeccionista, procuro cobrir 100% do meu código com testes. Você vai
        dizer, "Isso é impossível!". Calma, a princípio eu tenho tendência a 
        concordar com você. Mas... O que eu faço? Eu escrevo testes para cobrir
        o máximo de funcionalidades de código que minha mente pode pensar. Aí,
        usando o pytest, do Python, coloco aquelas três letras mágicas ao final 
        do comando de depuração do código.
            pytest meu_modulo.py -s -v --cov
        Ele me entrega um mapa de cobertura do projeto. Em seguida eu digito:
            coverage html
        E em seguida:
            py coverage_view.py (um arquivo que criei e está na raiz do 
                projeto, que abre o browser com o relatório detalhado 
                da cobertua)
        Posso então trabalhar nos pontos não cobertos. E quando ao final
            desse processo sobram rotinas que não consigo pensar em como 
            testar (por exemplo, erro específico no servidor de banco de dados)
            eu fico feliz. Pois sei que pensei no tratamento desses erros,
            mesmo não tendo, a princípio, como testá-los. Aí é hora de
            colocar ao final da linha, a seguinte string:
                # pragma: no cover
            Ela diz ao pytest para não considerar aquela linha no relatório de
                cobertura de testes (veja a minha configuração de testes e
                coberturas no arquivo .coveragerc na raiz do projeto). E 
                temos os tão sonhados 100% de cobertura. Mais tarde se nossa
                mente conseguir criar uma forma de testar o que não conseguimos
                anteriormente, basta implantar os testes e remover a linha
                com o cometário do pragma e tudo se mantém.

# Material de Estudo da Definição Formal da Clean Architecture e do DDD
    TODO:

# Ciclo de Desenvolvimento
    Como disse acima, sempre de dentro para fora. Sempre do mais independente
        para o menos indenpendente.
    Sendo assim, começemos pela camada de Entidades, após nos preocuparmos com
        os alicerces.

## Preparação dos Alicerces
    Ordem que adoto no desenvolvimento:
        ➡️ Criação da pasta src (padrão de boas práticas no Python)
        ➡️ Criação do ambiente virtual (padrão de bom senso para desenvolvedores
            Python, a não ser os kamikazes)
        ➡️ Utilitários (pasta: src\utils)
            São ferramentas gerais que facilitarão o desenvolvimento e podem
                encapsular funções mais complexas da linguagem. Com o tempo e a
                experiência, construimos um arsenal delas. E quando queremos
                migrar a linguagem, basta reescrever as rotinas na nova linguagem
                e continuar usando as funções que já estamos acostumados no nosso
                código.
        ➡️ Erros (pasta: src\errors)
            É uma prática recomendável que se adote a saída única das funções com
                o resultado perfeito desta. E nos casos de erros ou inconsistências,
                podemos adotar a geração de erros padrão sempre propagando para
                o chamador da função, não importando o nível de profundidade
                aonde o erro ocorreu. Com isso garantimos que qualquer erro é
                canalizado para o funil dos blocos try/except/finally. Se a função
                chega no return, tudo correu bem. E criando erros personalizados,
                temos o controle total sobre eles, inclusive para tradução do 
                sistema para outros idiomas.

## Entidades
    E chegamos ao ponto chave. As Entidades devem ser os núcleos da
        lógica do negócio e o foco de atenção se queremos que o sistema entregue
        valor ao cliente.
    Com isso, devemos tentar protegê-lo de contaminação. Ou seja, garantir que
        o que ele terá de tratar seja puro, perfeito e límpido. As validações
        e sanitizações devem ser feitas antes que os dados cheguem até elas.
    Nesta camada adoto a seguinte ordem de criação:
        ➡️ Enumerators (pasta: src\domain\enums)    
            São meras e simples tabelas de dados que mudarão muito pouco ao longo do
                tempo de vida do sistema (pense numa tabuada por exemplo, ou numa
                tabela de gêneros como Masculino e Feminino, se bem que nos dias
                de hoje, não sei se foi um bom exemplo, mas a tabuada foi).
        ➡️ Value Objects (pasta: src\domain\value_objects)
            São objetos ainda rudimentares e que deveriam ser anêmicos. Mas já estão
                num estágio acima na escala de complexidade. Eles podem usar os
                enums, e normalmente o fazem. São objetos únicos e com "identidade"
                não volátil. Morre a identidade, morre o objeto, e vice-versa.
                O coneito vem do DDD.
        ➡️ Entities (pasta: src\domain\entities)       
            São o coração do negócio e que contém, de forma centralizada uma
                reunião de todos os processos e regras que fazem o negócio do
                cliente girar. Não podemos descuidar delas nunca, ao contrário.
                E, se são tão importantes, precisaremos armazená-las para 
                depois manipulá-las e gerar valor. Serão a base (mas não a
                essência) para o que no futuro será nosso mapeamento em 
                meios físicos (não interessa aqui quais, uma ficha de um paciente
                de um médico pode ser armazenada no pen-drive, num banco de dados,
                num arquivo de segurança num banco ou num cofre, não interessa,
                foque agora na ficha que fala do principal, o paciente).
        ➡️ Interfaces de Repositório (pasta: src\domain\interfaces)   
            Este é um ponto polêmico. Aonde colocá-los. Eu entendo que de nada
                adianta eu ter uma riqueza de informações bem organizadas, se 
                não defino as regras de como eu posso distribuí-las a quem 
                possa se interessar. Não devemos pensar em meios físicos, mas 
                sim nos conceitos que serão necessários para que a informação
                possa ser mantida (as famososas funções CRUD e as opções de
                atualizações e consultas). Seguindo o que disse acima, 
                se preciso agora mas não tenho, abstraio. Aqui ficarão as
                interfaces dos repositórios que usaremos no sistema.

        Veja a figura abaixo para uma representação esquemática.

        TODO: Inserir imagem do Modelo de Entidades

## Casos de Uso
    São os executores das funções que manipulam as Entidades. Eles executam o
        trabalho pesado, muitas vezes manipulando informações de mais de uma
        entidade. Nele já temos lógicas mais complexas de manipulação de dados
        e parte das regras que a aplicação deve obedecer.
    Nesta camada adoto a seguinte ordem de criação:
        ➡️ DTO's (pasta: src\use_cases\dtos)    
            São como um mapa que define a forma como iremos receber os dados e
                encaminharmos ela adiante. Devemos trabalhar para que nelas não
                haja lógica de negócio. Deveriam ser apenas mapas para se chegar
                a um objetivo. Serão como envelopes que transportarão os dados
                entre as camadas do sistema (principalmente no sentido de fora
                para dentro dele).
        ➡️ Validator's (pasta: src\use_cases\validators)   
            São os guardiões dos envelopes. Os agentes de segurança no transporte 
                de valores. São responsáveis por validar e garantir a qualidade
                dos dados transportados pelos DTO's.
        ➡️ Use Cases (pasta: src\use_cases\<ENTIDADE>)
            São as fábricas aonde o trabalho acontece. Manipulam as informações 
                recebidas via DTO's pela Entidades e, através das regras de
                negócio implantadas por eles, orquestram a comunicação entre
                elas para poder produzir a informação desejada ou efetuar o
                processo solicitado. São as fábricas de soluções. Gosto de 
                agrupar os Casos de Uso em subdiretórios sendo um para cada
                Entidade, pois algumas podem ter dezenas de Casos de Uso
                em sistemas complexos.
        ➡️ Repositórios Mockados (pasta: src\use_cases\mocks)
            Eu procuro sempre criar repositórios mockados com dados que desejo
                usar para simular os processos dos Casos de Uso ou até mesmo
                para simular situações reais com dados que não impactem o
                repositório central do sistema. São basicamente usados nos 
                testes de aceitação e integração dos Casos de Uso. E os coloco
                aqui.

        Veja a figura abaixo para uma representação esquemática.

        TODO: Inserir Imagem do Modelo de Casos de Uso
