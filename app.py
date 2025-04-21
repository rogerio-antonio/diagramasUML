from plantuml import PlantUML

# Diagrama de Classes
class_diagram = """
@startuml BlackjackClassDiagram

class Blackjack {
    - cards: List[str]
    + calculate_score(cards: List[str]): int
}

@enduml
"""

# Diagrama de Sequência
sequence_diagram = """
@startuml BlackjackSequenceDiagram

actor Player
participant System
participant Computer

Player -> System: Inicia jogo
activate System
System -> Player: Mostra logo
System -> Player: Distribui 2 cartas
System -> Computer: Distribui 1 carta
System -> Player: Mostra pontuação atual
Player -> System: Decide continuar/parar
alt continuar
    System -> Player: Distribui nova carta
else parar
    System -> Computer: Joga suas cartas
end
System -> Player: Mostra resultado final
deactivate System

@enduml
"""

# Gerar os diagramas
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# Salvar diagrama de classes
with open('blackjack_class_diagram.png', 'wb') as f:
    f.write(plantuml.processes(class_diagram))

# Salvar diagrama de sequência
with open('blackjack_sequence_diagram.png', 'wb') as f:
    f.write(plantuml.processes(sequence_diagram))

print("Diagramas gerados com sucesso!") 