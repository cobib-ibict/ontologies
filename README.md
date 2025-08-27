# Sprint

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
