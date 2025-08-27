## Centralização de repositórios

▶ Atualmente, os repositórios [pinakesontology](https://github.com/Riverlance/pinakesontology) (onde era publicado a ontologia oficial), [Pinakes_Ontologia_Documentation](https://github.com/cobib-ibict/Pinakes_Ontologia_Documentation) (onde era publicado a documentação da ontologia) e [ontologiapinakes_webvowl](https://github.com/cobib-ibict/ontologiapinakes_webvowl) (onde era publicado o arquivo para a visualização da ontologia) foram mesclados no repositório [ontologies](https://github.com/cobib-ibict/ontologies).

▶ O repositório foi criado dentro da organização da COBIB do GitHub.
▶ Todos da equipe já estão com acesso.

## Centralização de plataformas

Com a centralização de repositórios, foi possível configurar as plataformas para que utilizem apenas uma única ontologia, disponibilizada em [ontology.rdf](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.rdf), ou seja:

▶ O WebVOWL, a documentação e o _Website_ Pinakes agora utilizam o mesmo arquivo de ontologia.

Isso deixa tudo bem mais organizado e centralizado em um único repositório.
O repositório [ontologies](https://github.com/cobib-ibict/ontologies) será onde ficará o versionamento da ontologia.

## Atualização automática nas plataformas

Ao atualizar qualquer arquivo do repositório [ontologies](https://github.com/cobib-ibict/ontologies), principalmente a ontologia [ontology.rdf](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.rdf), o [WebVOWL](https://cobib-pinakes-ontologia.tcti.ibict.br/webvowl/#iri=https://raw.githubusercontent.com/cobib-ibict/ontologies/refs/heads/main/pinakes/ontology.rdf) (através do TomCat) atualizará a ontologia que está sendo exibida, será realizado o deploy automático para a [documentação](https://cobib-ibict.github.io/ontologies/pinakes/), além de atualizar também a [ontologia](https://pinakes.ibict.br/visualizacao-do-modelo/) e a [documentação](https://pinakes.ibict.br/documentacao-tecnica/) no _Website_ Pinakes.

▶ Isso significa que basta atualizar qualquer arquivo do repositório para ser publicado automaticamente em suas devidas plataformas.

## Suporte à múltiplas ontologias e documentações

▶ Organizamos o repositório [ontologies](https://github.com/cobib-ibict/ontologies) de forma em que possa haver a possibilidade de adicionar múltiplas ontologias e documentações. Não necessariamente sempre para a mesma ontologia Pinakes.

Essa ideia não é minha, mas dos próprios criadores do Protégé.

O Protégé tem algumas IRIs como um conjunto de ontologias:
- http://protege.stanford.edu/ontologies/camera.owl
- http://protege.stanford.edu/ontologies/koala.owl
- http://protege.stanford.edu/ontologies/pizza/pizza.owl
- http://protege.stanford.edu/ontologies/travel.owl

▶ Então, da mesma forma, o repositório [ontologies](https://github.com/cobib-ibict/ontologies) será o "repositório de ontologias da COBIB (Ibict)".

---

## Atualizações na ontologia Pinakes

### Tag `pt-br`

▶ Corrigimos alguns elementos que estavam faltando a tag `pt-br` ou que estavam apenas com `pt` sem ser `pt-br`.

No WebVOWL estava identificando o `en` e `pt-br`, mas também identificava `pt` (porque tinham tags erradas nos elementos) e `Undefined` (porque tinha alguns elementos que estavam faltando a tag `lang`).

### Novos dados e metadados

* ▶ Adicionamos alguns dados novos, como título, versão, autor, etc.
* ▶ A descrição não aparecia na visualização do WebVOWL, mas corrigimos também (trocamos de `rdfs:comment` para `terms:description`, de acordo com a ontologia VIVO).
* ▶ Adicionamos alguns metadados baseado na visualização WebVOWL das ontologias [VIVO](https://cobib-pinakes-ontologia.tcti.ibict.br/webvowl/#iri=https://raw.githubusercontent.com/vivo-ontologies/vivo-ontology/refs/heads/master/vivo.owl) e [Vocab-bio](https://cobib-pinakes-ontologia.tcti.ibict.br/webvowl/#iri=https://raw.githubusercontent.com/iand/vocab-bio/refs/heads/master/schema.rdf).

▶ O resultado final ficou assim:

<img width="423" height="963" alt="Image" src="https://github.com/user-attachments/assets/eaaf0fe0-cc2e-4603-be2b-5f4475cef8bc" />

### ▶ Nova IRI

IRI: `https://cobib-ibict.github.io/ontologies/pinakes`
URL: `https://cobib-ibict.github.io/ontologies/pinakes/ontology.rdf`

▶ A IRI, em uma ontologia, poderia ser qualquer nome escolhido (por exemplo, "Pinakes"), mas, para evitar conflitos e garantir que cada termo seja único no mundo todo, convencionou-se utilizar URLs como identificadores das IRIs, ou seja, como os valores das IRIs.

Isso não significa que a IRI dependa do servidor ou que o arquivo precise realmente estar hospedado naquele endereço URL. Para a IRI, a URL funciona como um identificador único, em vez de um link tradicional da Web.

Idealmente, muitas vezes a IRI é igual à URL do arquivo publicado, porque isso facilita a consulta e o reuso, mas não é uma obrigação.

▶ Também é comum que a IRI aponte para a página de documentação da ontologia, em vez do arquivo bruto, justamente para oferecer uma visualização mais amigável e explicativa. Sendo assim, como a ontologia também possui vários formatos disponíveis, a nova IRI agora aponta para a URL da documentação da ontologia Pinakes.

## Atualizações futuras sugeridas

Resumo do que tem para ser feito:

* Ainda é possível mesclar também o repositório de consultas SPARQL [consultas-OntologiaPinakes](https://github.com/cobib-ibict/consultas-OntologiaPinakes) no repositório [ontologies](https://github.com/cobib-ibict/ontologies), mas não foi realizado ainda.
* Conectar as consultas SPARQL com bancos de dados e até com outros sistemas que não de autoria do Ibict.
* Adaptar a ontologia para o inglês, como linguagem secundária, para globalizar o alcance das ontologias.

> [!note]
  Algumas das atualizações sugeridas foram postas no comentário posterior.

# Sprint

## [As 5 estrelas dos dados abertos](https://5stardata.info/pt-BR/) (Tim Berners-Lee)

Os 5 princípios da Web Semântica propostos por Tim Berners-Lee funcionam como um guia para avaliar se uma ontologia realmente está publicada de forma a ser parte da Web Semântica.

---

* ### 1 estrela

Disponibilizar os dados na Web, de forma que qualquer pessoa possa acessar.

✔ No nosso caso, a ontologia Pinakes está publicada no GitHub Pages, garantindo 1 estrela.

---

* ### 2 estrelas

Disponibilizar em formato estruturado, legível por máquinas.

✔ No nosso caso, a ontologia Pinakes está publicada como [`.rdf`](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.rdf) (já suficiente), mas também em [`.owl`](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.owl), [`.ttl`](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.ttl), [`.jsonld`](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.jsonld) e [`.nt`](https://github.com/cobib-ibict/ontologies/blob/main/pinakes/ontology.nt) (todos legíveis por máquinas), garantindo 2 estrelas, no total.

---

* ### 3 estrelas

Usar formatos abertos e não proprietários (não depender de softwares fechados, como `.xlsx` do `Excel`, para abrir os dados).

✔ No nosso caso, a ontologia Pinakes está publicada em `RDF/XML`, `OWL/XML`, `Turtle`, `JSON-LD` e `N-Triple` (todos formatos baseados em padrões pela W3C para representar dados da Web Semântica), garantindo 3 estrelas, no total.

---

* ### 4 estrelas

Cada recurso (classe, propriedade, atributo) deve ter uma URI única.
Assim, qualquer pessoa ou sistema pode referenciar a mesma coisa na Web.

✔ No nosso caso, a ontologia Pinakes já possui URIs únicas, garantindo 4 estrelas, no total.

Exemplos:
* Classes:
  * https://cobib-ibict.github.io/ontologies/pinakes#Agente
  * https://cobib-ibict.github.io/ontologies/pinakes#AgenteColetivo
  * https://cobib-ibict.github.io/ontologies/pinakes#AssuntoControlado
  * https://cobib-ibict.github.io/ontologies/pinakes#Biblioteca
  * https://cobib-ibict.github.io/ontologies/pinakes#Colecao
* Relacionamentos:
  * https://cobib-ibict.github.io/ontologies/pinakes#assigned
  * https://cobib-ibict.github.io/ontologies/pinakes#createdExpressao
  * https://cobib-ibict.github.io/ontologies/pinakes#createdObra
  * https://cobib-ibict.github.io/ontologies/pinakes#distributes
  * https://cobib-ibict.github.io/ontologies/pinakes#modifies
* Atributos:
  * https://cobib-ibict.github.io/ontologies/pinakes#urlDoCatalogo
  * https://cobib-ibict.github.io/ontologies/pinakes#dataAtualizacaoBiblioteca
  * https://cobib-ibict.github.io/ontologies/pinakes#dataCadastroBiblioteca
  * https://cobib-ibict.github.io/ontologies/pinakes#denominacao
  * https://cobib-ibict.github.io/ontologies/pinakes#paginaWeb

> [!caution]
  A ontologia Pinakes atualmente possui URIs únicas para classes, relacionamentos e atributos, mas, ao inserir dados do CCN, futuramente, como instâncias (indivíduos), se não mantiver o padrão de URIs únicas para as instâncias também, a ontologia perderá essa estrela.

---

Conectar a ontologia com outras ontologias na Web.

❌ No nosso caso, a ontologia Pinakes está isolada e, portanto, não está conectada à Web Semântica global.
Portanto, a ontologia Pinakes mantém-se com 4 estrelas.

Para solucionar isso, precisamos conectar as classes, atributos e relacionamentos (não precisa ser tudo) com outras ontologias (vocabulário semântico), através de `owl:equivalentClass` (para classes) e `owl:equivalentProperty` (para relacionamentos e atributos). Também pode ser uma hierarquia de herança utilizando `rdfs:subClassOf` (para classes) e `rdfs:subPropertyOf` (para relacionamentos e atributos).

▶ Ontologia isolada (semelhante a como está na ontologia Pinakes atualmente):
```xml
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:ex="http://example.org/onto#">

  <!-- Classe -->
  <owl:Class rdf:about="http://example.org/onto#Obra"/>

  <!-- Relacionamento -->
  <owl:ObjectProperty rdf:about="http://example.org/onto#temAutor"/>

  <!-- Atributo -->
  <owl:DatatypeProperty rdf:about="http://example.org/onto#titulo"/>

</rdf:RDF>
```

▶ Com `owl:equivalentClass` e `owl:equivalentProperty`
Para quando a classe/relacionamento/atributo tiver literalmente o mesmo significado da que está na outra ontologia.
Por exemplo, abaixo estamos dizendo que:
1. A classe `Obra` é equivalente à classe `http://purl.org/dc/terms/BibliographicResource`.
2. O relacionamento `temAutor` é equivalente ao relacionamento `http://purl.org/dc/terms/creator`.
3. O atributo `titulo` é equivalente ao atributo `http://purl.org/dc/terms/title`.
```xml
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:ex="http://example.org/onto#"
         xmlns:dc="http://purl.org/dc/terms/"
         xmlns:foaf="http://xmlns.com/foaf/0.1/">

  <!-- Classe -->
  <owl:Class rdf:about="http://example.org/onto#Obra">
    <owl:equivalentClass rdf:resource="http://purl.org/dc/terms/BibliographicResource"/>
  </owl:Class>

  <!-- Relacionamento -->
  <owl:ObjectProperty rdf:about="http://example.org/onto#temAutor">
    <owl:equivalentProperty rdf:resource="http://purl.org/dc/terms/creator"/>
  </owl:ObjectProperty>

  <!-- Atributo -->
  <owl:DatatypeProperty rdf:about="http://example.org/onto#titulo">
    <owl:equivalentProperty rdf:resource="http://purl.org/dc/terms/title"/>
  </owl:DatatypeProperty>

</rdf:RDF>
```

▶ Com `rdfs:subClassOf` e `rdfs:subPropertyOf`
Para quando a classe/relacionamento/atributo é uma especialização (subclasse ou subpropriedade — hierarquia de herança) da que está na outra ontologia.
Por exemplo, abaixo estamos dizendo que:
1. A classe `Obra` é subclasse (herda) de `http://purl.org/dc/terms/BibliographicResource`.
2. O relacionamento `temAutor` é subpropriedade (herda) de `http://purl.org/dc/terms/creator`.
3. O atributo `titulo` é subpropriedade (herda) de `http://purl.org/dc/terms/title`.
```xml
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:ex="http://example.org/onto#"
         xmlns:dc="http://purl.org/dc/terms/">

  <!-- Classe -->
  <owl:Class rdf:about="http://example.org/onto#Obra">
    <rdfs:subClassOf rdf:resource="http://purl.org/dc/terms/BibliographicResource"/>
  </owl:Class>

  <!-- Relacionamento -->
  <owl:ObjectProperty rdf:about="http://example.org/onto#temAutor">
    <rdfs:subPropertyOf rdf:resource="http://purl.org/dc/terms/creator"/>
  </owl:ObjectProperty>

  <!-- Atributo -->
  <owl:DatatypeProperty rdf:about="http://example.org/onto#titulo">
    <rdfs:subPropertyOf rdf:resource="http://purl.org/dc/terms/title"/>
  </owl:DatatypeProperty>

</rdf:RDF>
```

> [!caution]
  Para fazer o que está descrito acima, talvez seja necessário fazer uma correção antes.
  Criamos as classes, relacionamentos e atributos manualmente, mas acredito que deveriam ter sido criados, pelo menos as classes, a partir das ontologias do IFLA LRM e do PRESSoo (que existem):
  • IFLA LRM — IRI: `http://iflastandards.info/ns/lrm/lrmer/`
  • IFLA LRM — Como importar via `RDF/XML`: `xmlns:lrmer="http://iflastandards.info/ns/lrm/lrmer/"`
  • IFLA LRM — Fonte (`.rdf`): [lrmer.zip](https://github.com/user-attachments/files/21979440/lrmer.zip) ou https://www.iflastandards.info/lrm/lrmer.html
  • PRESSoo — IRI: `http://iflastandards.info/ns/fr/frbr/pressoo/`
  • PRESSoo — Como importar via `RDF/XML`: `xmlns:pressoo="http://iflastandards.info/ns/fr/frbr/pressoo/"`
  • PRESSoo — Fonte (`.rdf`): [PRESSoo_v1.0.zip](https://github.com/user-attachments/files/21979445/PRESSoo_v1.0.zip) ou https://cidoc-crm.org/sites/default/files/PRESSoo_v1.0.rdfs
  ▶ **Sugestão importante**: O projeto de ontologia `RDF/XML` do PRESSoo me parece ter sido abandonado, visto que só o encontrei via IA (Inteligência Artificial). Não o encontrei no Website oficial [cidoc-crm.org](https://cidoc-crm.org). Portanto, talvez seja interessante trocá-lo, futuramente, por algum outro dos modelos disponíveis no Website do [IFLA](https://www.iflastandards.info/) (todos os modelos têm suas respectivas ontologias).
  .<img width="350" height="300" alt="Image" src="https://github.com/user-attachments/assets/92cb2ccf-7fd5-45a8-81db-b691b66bb52c" />

> [!important]
  Apenas utilizar o IFLA LRM e PRESSoo na ontologia, não dá a 5ª estrela.
  ▶ Isso será um trabalho necessário, apesar de não afetar a quantidade de estrelas.
  Para isso, é preciso conectar a ontologia com outras ontologias através das equivalências de classes, relacionamentos e atributos (vocabulário semântico).
  Ou seja, utilizar `owl:equivalentClass`, `owl:equivalentProperty`, `rdfs:subClassOf` e `rdfs:subPropertyOf` conectando a ontologia Pinakes com outras ontologias, como já mencionado.

> [!tip]
  Essa 5ª estrela, não exige que a ontologia esteja publicada em catálogos como o LOV ou em qualquer outro catálogo, mas, mesmo assim, publicar em catálogos como o LOV é uma boa prática de visibilidade e de reuso para a ontologia.
  ▶ Isso será um trabalho necessário, apesar de também não afetar a quantidade de estrelas.

## Atualizações futuras sugeridas

Resumo do que tem para ser feito:

* Utilizar classes, relacionamentos e atributos das ontologias IFLA LRM e PRESSoo na ontologia Pinakes. Não apenas conceitualmente como está atualmente, mas utilizando as ontologias IFLA LRM e PRESSoo de fato.
* Como mencionado, o projeto de ontologia `RDF/XML` do PRESSoo parece ter sido abandonado, portanto sugiro, futuramente, trocá-lo por algum outro dos modelos disponíveis no Website do [IFLA](https://www.iflastandards.info/).
* Conectar a ontologia Pinakes com outras ontologias (vocabulário semântico), ou seja utilizar `owl:equivalentClass`, `owl:equivalentProperty`, `rdfs:subClassOf` e `rdfs:subPropertyOf`, para atribuir a 5ª estrela à ontologia Pinakes.
* Indexar a ontologia em catálogos renomados como o LOV, com o objetivo de aumentar a visibilidade da ontologia, facilitar o reuso por outras ontologias, garantir interoperabilidade (integrá-la com outras ontologias e dados ligados — Linked Data) e exibir detalhes formais da ontologia. Isso é importante mesmo mantendo o repositório `ontologies`, que foi criado para o versionamento e publicação das ontologias nas plataformas vigentes (Website Pinakes, documentação das ontologias, visualização WebVOWL e acesso das ontologias via Protégé).
* Inserir dados do CCN como instâncias (indivíduos), mantendo o padrão de URIs únicas para essas instâncias, mantendo a 4ª estrela dos dados abertos.
